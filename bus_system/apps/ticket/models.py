from django.db.models import (
    PROTECT,
    SET_NULL,
    BooleanField,
    ForeignKey,
    SmallIntegerField,
)

from bus_system.apps.passenger.models import PassengerModel
from bus_system.apps.trip.models import TravelModel
from bus_system.utils.models import BaseModel


class TicketModel(BaseModel):
    travel = ForeignKey(TravelModel, on_delete=PROTECT, related_name='ticket_travel_set',
                        related_query_name='ticket_travel_set')
    passenger = ForeignKey(PassengerModel, on_delete=SET_NULL, null=True)
    is_pay = BooleanField(default=False)
    chair_number = SmallIntegerField()

    class Meta:
        db_table = "ticket"
