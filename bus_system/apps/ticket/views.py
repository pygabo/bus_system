# Core Django rest_framework imports
from django.shortcuts import get_object_or_404
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

# Imports from my apps
from bus_system.apps.ticket.models import TicketModel
from bus_system.apps.ticket.serializer import TicketListSerializer, TicketSerializer
from bus_system.apps.trip.models import TravelModel


class TicketViewSet(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    """
    A viewset for viewing and editing ticket instances.
    """
    serializer_class = TicketSerializer
    queryset = TicketModel.objects.filter(is_pay=False, passenger__isnull=True)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        trip_id = instance.travel.trip
        trip_id.tickets_sold += 1
        trip_id.save()

        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=False, methods=['GET'])
    def available(self, request, **kwargs):
        get_object_travel = get_object_or_404(TravelModel, id=kwargs['travel_id'])
        queryset = TicketModel.objects.filter(travel=get_object_travel)

        serializer = TicketListSerializer(queryset, many=True)
        return Response(serializer.data)
