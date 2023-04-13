from django.contrib import admin
from .models import Profile
from django.contrib.auth.admin import UserAdmin

@admin.register(Profile)
class ProfileAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'get_role', 'last_login', 'is_staff', 'is_superuser', 'is_active')
    fieldsets = UserAdmin.fieldsets + (('Офис', {'fields': ('confirmed',)}),)

    
    def get_role(self, obj):
        if obj.role == 1:
            return 'Доктор'
        elif obj.role == 2:
            return 'Клиент'
    
    get_role.short_description = 'Роль'

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.role = 1
            obj.save()
        super().save_model(request, obj, form, change)
