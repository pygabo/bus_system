# Core Django rest_framework imports
from rest_framework.serializers import ModelSerializer, SerializerMethodField

# Imports from my apps
from bus_system.apps.trip.models import DestinationModel, TravelModel, TripModel
from bus_system.apps.bus.serializer import BusSerializer
from django.db.models import Sum
from django.db.models import Avg
from django.shortcuts import get_list_or_404, get_object_or_404


class TravelSerializer(ModelSerializer):
    class Meta:
        model = TravelModel
        fields = (
            'id',
            'trip',
            'bus',
            'departure_time',
            'price'
        )
        read_only_fields = (
            'id',
        )


class DestinationSerializer(ModelSerializer):
    class Meta:
        model = DestinationModel
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'id',
        )


class TripSerializer(ModelSerializer):
    departure = DestinationSerializer(many=False)
    arrival = DestinationSerializer(many=False)
    assigned_buses = BusSerializer(many=True)

    class Meta:
        model = TripModel
        fields = (
            'id',
            'departure',
            'arrival',
            'assigned_buses',
        )
        read_only_fields = (
            'id',
        )


class TripCreateSerializer(ModelSerializer):
    class Meta:
        model = TripModel
        fields = (
            'id',
            'departure',
            'arrival',
            'assigned_buses',
        )
        read_only_fields = (
            'id',
        )


class TripAverageSerializer(ModelSerializer):
    average = SerializerMethodField()
    departure = DestinationSerializer(many=False)
    arrival = DestinationSerializer(many=False)
    assigned_buses = BusSerializer(many=True)

    class Meta:
        model = TripModel
        fields = (
            'id',
            'departure',
            'arrival',
            'assigned_buses',
            'average'
        )
        read_only_fields = (
            'id',
        )

    def get_average(self, obj):
        return obj.travel_trip_set.filter(ticket_travel_set__is_pay=True,
                                          ticket_travel_set__passenger__isnull=False).count()
