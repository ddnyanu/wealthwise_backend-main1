from django.contrib import admin
from authentication.models import CustomUser
from django.contrib.auth.admin import UserAdmin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'contact_no')
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('dob', 'contact_no', 'address', 'gender', 'profile_photo', 'role')}),
    )