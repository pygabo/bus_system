from django.db.models import BooleanField, PositiveSmallIntegerField, ForeignKey, SET_NULL

from bus_system.utils.models import BaseModel
from bus_system.apps.bus_driver.models import BusDriverModel


class BusModel(BaseModel):
    """
    Bus Model
    """
    plate = BooleanField()
    is_available = BooleanField()
    capacity = PositiveSmallIntegerField(default=10)
    driver = ForeignKey(BusDriverModel, on_delete=SET_NULL, null=True)

    class Meta:
        db_table = "bus"
