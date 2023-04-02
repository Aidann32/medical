from django.contrib import admin

from .models import Patient, Diagnosis, XRay, XRayRequest


class DiagnosisInline(admin.TabularInline):
    model = Diagnosis
    extra = 0


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('profile', 'first_name', 'last_name', 'iin', 'phone_number', 'email', 'created_at')
    inlines = (DiagnosisInline, )


@admin.register(XRay)
class XRayAdmin(admin.ModelAdmin):
    list_display = ('patient', 'photo', 'result', 'updated_at', 'created_at')


@admin.register(XRayRequest)
class XRayRequest(admin.ModelAdmin):
    list_display = ('x_ray', 'doctor', 'diagnosis', 'is_answered', 'updated_at', 'created_at') 