# Core Django imports
from django.db.models import (
    PROTECT,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    PositiveSmallIntegerField,
)

# Imports from my apps
from bus_system.apps.bus.models import BusModel
from bus_system.apps.bus_driver.models import BusDriverModel
from bus_system.utils.models import BaseModel


class DestinationModel(BaseModel):
    name = CharField(max_length=150)

    class Meta:
        db_table = "destination"


class TripModel(BaseModel):
    departure = ForeignKey(DestinationModel, on_delete=PROTECT, related_name='departure')
    arrival = ForeignKey(DestinationModel, on_delete=PROTECT, related_name='arrival')
    is_available = BooleanField()

    class Meta:
        db_table = "trip"


class TravelModel(BaseModel):
    trip = ForeignKey(TripModel, on_delete=PROTECT)
    driver = ForeignKey(BusDriverModel, on_delete=PROTECT)
    bus = ForeignKey(BusModel, on_delete=PROTECT)
    departure_time = DateTimeField()
    price = PositiveSmallIntegerField()

    class Meta:
        db_table = "travel"
