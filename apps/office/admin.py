from django.contrib import admin

from .models import Patient, Diagnosis, XRay, XRayRequest


@admin.register(Diagnosis)
class DiagnosisAdmin(admin.ModelAdmin):
    pass


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('profile', 'first_name', 'last_name', 'iin', 'phone_number', 'email', 'created_at')


@admin.register(XRay)
class XRayAdmin(admin.ModelAdmin):
    list_display = ('patient', 'photo', 'result', 'updated_at', 'created_at')


@admin.register(XRayRequest)
class XRayRequest(admin.ModelAdmin):
    list_display = ('x_ray', 'doctor', 'diagnosis', 'is_answered', 'updated_at', 'created_at') 