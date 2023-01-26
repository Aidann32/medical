from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'get_role', 'last_login', 'is_staff', 'is_superuser', 'is_active')

    
    def get_role(self, obj):
        if obj.role == 1:
            return 'Доктор'
        elif obj.role == 2:
            return 'Мед. сестра'
    
    get_role.short_description = 'Роль'