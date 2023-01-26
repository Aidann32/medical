from django.urls import path

from .views import office_menu, create_patient

urlpatterns = [
    path('', office_menu, name='office_menu'),
    path('create_patient/', create_patient, name='create_patient')
]
