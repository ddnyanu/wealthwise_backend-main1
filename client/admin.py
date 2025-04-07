from django.contrib import admin
from .models import Client

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'on_boarding_manager', 'inv_amt', 'risk_tolerance')
