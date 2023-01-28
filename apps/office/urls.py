from django.urls import path

from .views import office_menu, create_patient, patients_list, patient_details

urlpatterns = [
    path('', office_menu, name='office_menu'),
    path('create_patient/', create_patient, name='create_patient'),
    path('patients_list/', patients_list, name='patients_list'),
    path('patient/<str:iin>/', patient_details, name='patient_details'),
]
