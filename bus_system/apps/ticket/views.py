# Core Django rest_framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
# Imports from my apps
from bus_system.apps.ticket.models import TicketModel
from bus_system.apps.ticket.serializer import TicketSerializer


class TicketViewSet(ModelViewSet):
    """
    A viewset for viewing and editing ticket instances.
    """
    serializer_class = TicketSerializer
    queryset = TicketModel.objects.all()
    permission_classes = [AllowAny, ]
