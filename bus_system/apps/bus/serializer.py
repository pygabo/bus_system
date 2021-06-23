from rest_framework.serializers import ModelSerializer
from bus_system.apps.bus.models import BusModel


class BusSerializer(ModelSerializer):
    """
    Passenger serializers.
    """

    class Meta:
        model = BusModel
        fields = (
            'plate',
            'is_available',
            'capacity',
            'driver'
        )
        read_only_fields = (
            'id',
        )
