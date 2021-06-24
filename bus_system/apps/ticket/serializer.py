# Core Django rest_framework imports
from rest_framework.serializers import ModelSerializer

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
            'chair_number'
        )
        read_only_fields = (
            'id',
        )
