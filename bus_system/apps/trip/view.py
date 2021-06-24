from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
# Core Django rest_framework imports
from rest_framework.viewsets import ModelViewSet

from bus_system.apps.bus.models import BusModel
# Imports from my apps
from bus_system.apps.trip.models import TravelModel, TripModel
from bus_system.apps.trip.serializer import TravelSerializer, TripSerializer
from bus_system.apps.ticket.models import TicketModel
from bus_system.apps.ticket.serializer import TicketSerializer


class TravelViewSet(ModelViewSet):
    """
    A viewset for viewing and editing travel instances.
    """
    serializer_class = TravelSerializer
    queryset = TravelModel.objects.all()
    permission_classes = [AllowAny, ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        get_bus_capacity = get_object_or_404(BusModel, id=serializer.data['bus']).capacity
        ticket_data = []
        for chair_number in range(get_bus_capacity):
            chair_number_item = {}
            chair_number_item['chair_number'] = chair_number
            chair_number_item['travel'] = serializer.data['id']
            ticket_data.append(chair_number_item)
        serializer_tickets = TicketSerializer(data=ticket_data, many=True)
        serializer_tickets.is_valid(raise_exception=True)
        serializer_tickets.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TripViewSet(ModelViewSet):
    """
    A viewset for viewing and editing travel instances.
    """
    serializer_class = TripSerializer
    queryset = TripModel.objects.filter(is_available=False)
    permission_classes = [AllowAny, ]