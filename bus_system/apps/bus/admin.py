# Core Django  imports
from django.contrib import admin

# Imports from my apps
from bus_system.apps.bus.models import BusModel

admin.site.register(BusModel)
