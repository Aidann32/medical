from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.forms.models import model_to_dict
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import PatientModelForm, XRayModelForm
from .models import Patient, XRay
from .decorators import doctor_required, client_required, confirmed_client_required


@login_required(login_url='/profiles/login/')
@doctor_required
def office_menu(request):
    return render(request, 'office/doctor/menu.html')


@login_required(login_url='/profiles/login/')
@doctor_required
def create_patient(request):
    form = PatientModelForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.info(request, 'Patient created')
        else:
            messages.error(request, 'Patient not created')

    return render(request, 'office/doctor/create_patient.html', {'patient_form': form})


@login_required(login_url='/profiles/login/')
@doctor_required
def patients_list(request):
    page_num = request.GET.get('page', 1)
    query = request.GET.get('patient_name', '')
    if query:
        if ' ' in query:
            first_name = query.split(' ')[0]
            last_name = query.split(' ')[1]
            patients = Patient.objects.filter(Q(first_name__icontains=first_name) | Q(last_name__icontains=last_name))
        else:
            patients = Patient.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query))
        
        paginator = Paginator(patients, 1)
        try:
            page_obj = paginator.page(page_num)
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        return render(request, 'office/doctor/search_result.html',{'page_obj': page_obj})

    patients = Patient.objects.all()
    paginator = Paginator(patients, 1)
    try:
        page_obj = paginator.page(page_num)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return render(request, 'office/patients_list.html', {'page_obj': page_obj})


@login_required(login_url='/profiles/login/')
@doctor_required
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
        form = PatientModelForm(instance=patient)
    
    return render(request, 'office/doctor/patient_details.html', {'form': form,  'birth_date': birth_date, 'patient': patient })


# Client side
@login_required(login_url='profiles/login')
@client_required
def client_office(request):
    return render(request, 'office/client/menu.html')


@login_required(login_url='profiles/login')
@client_required
def client_xray(request):
    if request.method == 'POST':
        form = XRayModelForm(files=request.FILES)
        print(form.is_valid())
        if form.is_valid():
            if Patient.objects.filter(profile=request.user).exists():
                patient = Patient.objects.filter(profile=request.user).first()
                xray = form.save(commit=False)
                xray.patient = patient
                xray.save()
                return redirect('xray_result', xray_pk=xray.pk)

            return Http404()
    else:
        form = XRayModelForm()

    return render(request, 'office/client/xray.html', {'form': form})


@login_required(login_url='profiles/login')
@client_required
def xray_result(request, xray_pk):
    if XRay.objects.filter(pk=xray_pk).exists():
        xray = XRay.objects.filter(pk=xray_pk).first()
        return render(request, 'office/client/xray_result.html', {'xray': xray})
    return Http404()

@login_required(login_url='profiles/login')
@client_required
def client_edit_data(request):
    patient = Patient.objects.filter(profile=request.user).first()
    if patient.birth_date:
        birth_date = patient.birth_date.strftime('%d.%m.%Y')
    else:
        birth_date = None

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
    
    return render(request, 'office/client/edit_data.html', {'form': form,  'birth_date': birth_date, 'patient': patient })


