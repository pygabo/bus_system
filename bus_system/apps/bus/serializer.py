# Core Django rest_framework imports
from rest_framework.serializers import ModelSerializer

# Imports from my apps
from bus_system.apps.bus.models import BusModel


class BusSerializer(ModelSerializer):
    """
    Passenger serializers.
    """

    class Meta:
        model = BusModel
        fields = (
            'id',
            'plate',
            'is_available',
            'capacity',
            'driver'
        )
        read_only_fields = (
            'id',
            'capacity'
        )
