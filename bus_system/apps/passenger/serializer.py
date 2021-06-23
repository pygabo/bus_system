from rest_framework.serializers import ModelSerializer

from bus_system.apps.passenger.models import PassengerModel


class PassengerSerializer(ModelSerializer):
    """
    Passenger serializers.
    """

    class Meta:
        model = PassengerModel
        fields = (
            'id',
            'first_name',
            'surname',
            'identification_number'
        )
        read_only_fields = (
            'id',
        )
