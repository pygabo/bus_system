from rest_framework.viewsets import ModelViewSet

from bus_system.apps.bus_driver.models import BusDriverModel
from bus_system.apps.bus_driver.serializer import BusDriverSerializer


class BusDriverViewSet(ModelViewSet):
    """
    A viewset for viewing and editing bus driver instances.
    """
    serializer_class = BusDriverSerializer
    queryset = BusDriverModel.objects.all()

