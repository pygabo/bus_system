from django.shortcuts import get_object_or_404

# Core Django rest_framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

# Imports from my apps
from bus_system.apps.trip.models import TravelModel, TripModel
from bus_system.apps.trip.serializer import TravelSerializer, TripSerializer
from bus_system.apps.bus.models import BusModel


class TravelViewSet(ModelViewSet):
    """
    A viewset for viewing and editing travel instances.
    """
    serializer_class = TravelSerializer
    queryset = TravelModel.objects.all()
    permission_classes = [AllowAny, ]


class TripViewSet(ModelViewSet):
    """
    A viewset for viewing and editing travel instances.
    """
    serializer_class = TripSerializer
    queryset = TripModel.objects.filter(is_available=False)
    permission_classes = [AllowAny, ]
