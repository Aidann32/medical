from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import PatientModelForm


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
