from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.forms.models import model_to_dict

from .forms import PatientModelForm
from .models import Patient


@login_required(login_url='/profiles/login/')
def office_menu(request):
    return render(request, 'office/menu.html')


@login_required(login_url='/profiles/login/')
def create_patient(request):
    form = PatientModelForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'Patient created')
        else:
            messages.error(request, 'Patient not created')

    return render(request, 'office/create_patient.html', {'patient_form': form})


@login_required(login_url='/profiles/login/')
def patients_list(request):
    query = request.GET.get('patient_name', '')
    if query:
        if ' ' in query:
            first_name = query.split(' ')[0]
            last_name = query.split(' ')[1]
            patients = Patient.objects.filter(Q(first_name__icontains=first_name) | Q(last_name__icontains=last_name))
        else:
            patients = Patient.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
            
        return render(request, 'office/search_result.html',{'patients': patients})

    patients = Patient.objects.all()

    return render(request, 'office/patients_list.html', {'patients': patients})


@login_required(login_url='/profiles/login/')
def patient_details(request, iin):
    patient = Patient.objects.filter(iin=iin).first()
    birth_date = patient.birth_date.strftime('%d.%m.%Y')

    if not patient:
            Http404()

    if request.method == 'POST':
        form = PatientModelForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.info(request, 'Patient edited')
        else:
            messages.error(request, 'Edition error')
    else:
        form = form = PatientModelForm(instance=patient)
    
    return render(request, 'office/patient_details.html', {'form': form,  'birth_date': birth_date, 'patient': patient })
