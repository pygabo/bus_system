# Core Django  imports
from django.contrib import admin

# Imports from my apps
from bus_system.apps.trip.models import DestinationModel, TravelModel, TripModel

admin.site.register(DestinationModel)
admin.site.register(TripModel)
admin.site.register(TravelModel)
