from django.db.models import ForeignKey, PROTECT, SET_NULL, BooleanField, SmallIntegerField
from bus_system.utils.models import BaseModel
from bus_system.apps.trip.models import TravelModel
from bus_system.apps.passenger.models import PassengerModel


class TicketModel(BaseModel):
    travel = ForeignKey(TravelModel, on_delete=PROTECT)
    passenger = ForeignKey(PassengerModel, on_delete=SET_NULL, null=True)
    is_pay = BooleanField(default=False)
    chair_number = SmallIntegerField()

    class Meta:
        db_table = "ticket"
