# Core Django imports
from django.db.models import (
    PROTECT,
    SET_NULL,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    PositiveSmallIntegerField,
    ManyToManyField,
    Manager

)
from django.db.models import Avg, Count, Min, Sum

# Imports from my apps
from bus_system.apps.bus.models import BusModel
from bus_system.apps.bus_driver.models import BusDriverModel
from bus_system.utils.models import BaseModel


class DestinationModel(BaseModel):
    name = CharField(max_length=150)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = "destination"


class TripModel(BaseModel):
    departure = ForeignKey(DestinationModel, on_delete=PROTECT, related_name='departure')
    arrival = ForeignKey(DestinationModel, on_delete=PROTECT, related_name='arrival')
    is_available = BooleanField(default=True)
    assigned_buses = ManyToManyField(BusModel)
    tickets_sold = PositiveSmallIntegerField(default=0)

    def __str__(self):
        return str("{} - {}".format(self.departure, self.arrival))

    class Meta:
        db_table = "trip"


class TravelModel(BaseModel):
    trip = ForeignKey(TripModel, on_delete=PROTECT, related_name='travel_trip_set',
                      related_query_name='travel_trip_set')
    bus = ForeignKey(BusModel, on_delete=PROTECT)
    departure_time = DateTimeField()
    price = PositiveSmallIntegerField()

    @property
    def sales_count(self):
        return self.ticket_travel_set.filter(is_pay=True, passenger__isnull=False).count()

    def __str__(self):
        return str("{} {}".format(self.trip, self.departure_time))

    class Meta:
        db_table = "travel"
