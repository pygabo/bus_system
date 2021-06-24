# Core Django imports
from django.db.models import (
    SET_NULL,
    BooleanField,
    ForeignKey,
    PositiveSmallIntegerField,
)

# Imports from my apps
from bus_system.apps.bus_driver.models import BusDriverModel
from bus_system.utils.models import BaseModel


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
