from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.landing.urls')),
    path('profiles/', include('apps.profiles.urls')),
    path('office/', include('apps.office.urls')),
]
