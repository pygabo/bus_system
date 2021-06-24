# Core Django rest_framework imports
from rest_framework.serializers import ModelSerializer

# Imports from my apps
from bus_system.apps.trip.models import DestinationModel, TravelModel, TripModel
from bus_system.apps.bus.serializer import BusSerializer


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
