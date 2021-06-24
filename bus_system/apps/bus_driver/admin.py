# Core Django  imports
from django.contrib import admin

# Imports from my apps
from bus_system.apps.bus_driver.models import BusDriverModel

admin.site.register(BusDriverModel)
