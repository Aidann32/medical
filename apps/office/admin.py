from django.contrib import admin

from .models import Patient, Diagnosis


class DiagnosisInline(admin.TabularInline):
    model = Diagnosis
    extra = 0


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'iin', 'phone_number', 'email', 'created_at')
    inlines = (DiagnosisInline, )
