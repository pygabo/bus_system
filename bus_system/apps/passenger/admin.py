# Core Django  imports
from django.contrib import admin

# Imports from my apps
from bus_system.apps.passenger.models import PassengerModel


@admin.register(PassengerModel)
class AuthorAdmin(admin.ModelAdmin):
    pass
