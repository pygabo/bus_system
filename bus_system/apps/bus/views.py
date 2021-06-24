# Core Django rest_framework imports
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
# Imports from my apps
from bus_system.apps.bus.models import BusModel
from bus_system.apps.bus.serializer import BusSerializer


class BusViewSet(ModelViewSet):
    """
    A viewset for viewing and editing bus instances.
    """
    serializer_class = BusSerializer
    queryset = BusModel.objects.all()
    permission_classes = [AllowAny, ]
