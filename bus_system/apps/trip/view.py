from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# Core Django rest_framework imports
from bus_system.apps.bus.models import BusModel
from bus_system.apps.ticket.serializer import TicketSerializer
# Imports from my apps
from bus_system.apps.trip.models import DestinationModel, TravelModel, TripModel
from bus_system.apps.trip.serializer import (
    DestinationSerializer,
    TravelSerializer,
    TripAverageSerializer,
    TripCreateSerializer,
    TripSerializer,
)


class TravelViewSet(ModelViewSet):
    """
    A viewset for viewing and editing travel instances.
    """
    serializer_class = TravelSerializer
    queryset = TravelModel.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        get_bus_capacity = get_object_or_404(BusModel, id=serializer.data['bus']).capacity
        ticket_data = []
        for chair_number in range(get_bus_capacity):
            chair_number_item = {'chair_number': chair_number, 'travel': serializer.data['id']}
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
    queryset = TripModel.objects.filter(is_available=True)

    def get_serializer_class(self):
        if self.action == 'list':
            return TripSerializer
        if self.action == 'retrieve':
            return TripSerializer
        if self.action == 'create':
            return TripCreateSerializer
        if self.action == 'average':
            return TripAverageSerializer
        return TripSerializer

    @action(detail=False, methods=['GET'])
    def average(self, request, **kwargs):
        queryset = self.get_queryset()
        serializer = TripAverageSerializer(queryset, many=True)
        return Response(serializer.data)


class DestinationViewSet(ModelViewSet):
    """
    A viewset for viewing and editing travel instances.
    """
    serializer_class = DestinationSerializer
    queryset = DestinationModel.objects.all()
