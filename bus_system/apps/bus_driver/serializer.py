from rest_framework.serializers import ModelSerializer

# Imports from your apps
from bus_system.apps.bus_driver.models import BusDriverModel


class BusDriverSerializer(ModelSerializer):
    """
    Bus Driver serializers.
    """

    class Meta:
        model = BusDriverModel
        fields = (
            'id',
            'avatar',
            'is_available',
            'first_name',
            'surname',
            'identification_number'
        )
        read_only_fields = (
            'id',
        )
