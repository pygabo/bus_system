from rest_framework.viewsets import ModelViewSet
from bus_system.apps.passenger.models import PassengerModel
from bus_system.apps.passenger.serializer import PassengerSerializer


class PassengerViewSet(ModelViewSet):
    """
    A viewset for viewing and editing passenger instances.
    """
    serializer_class = PassengerSerializer
    queryset = PassengerModel.objects.all()

