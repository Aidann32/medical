from django.urls import path

from .views import office_menu, create_patient, patients_list, patient_details, client_office, client_xray, client_edit_data, xray_result

urlpatterns = [
    path('', office_menu, name='office_menu'),
    path('create_patient/', create_patient, name='create_patient'),
    path('patients_list/', patients_list, name='patients_list'),
    path('patient/<str:iin>/', patient_details, name='patient_details'),

    # Client side
    path('client/', client_office, name='client_office'),
    path('client/xray', client_xray, name='client_xray'),
    path('client/xray/result/<int:xray_pk>', xray_result, name='xray_result'),
    path('client/edit', client_edit_data, name='client_edit_data'),
]
