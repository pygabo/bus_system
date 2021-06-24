# Core Django rest_framework imports
from rest_framework.serializers import ModelSerializer

from bus_system.apps.passenger.serializer import PassengerSerializer
# Imports from my apps
from bus_system.apps.ticket.models import TicketModel


class TicketSerializer(ModelSerializer):
    """
    Passenger serializers.
    """

    class Meta:
        model = TicketModel
        fields = (
            'id',
            'travel',
            'chair_number',
            'passenger',
            'is_pay',
        )
        read_only_fields = (
            'id',
        )


class TicketListSerializer(ModelSerializer):
    passenger = PassengerSerializer(many=False)
    """
    Passenger serializers.
    """

    class Meta:
        model = TicketModel
        fields = (
            'id',
            'travel',
            'chair_number',
            'passenger',
            'is_pay',
        )
        read_only_fields = (
            'id',
        )
