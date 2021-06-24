# Core Django imports
from django.db.models import (
    PROTECT,
    BooleanField,
    CharField,
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
    plate = CharField(max_length=15)
    is_available = BooleanField(default=True)
    capacity = PositiveSmallIntegerField(default=10)
    driver = ForeignKey(BusDriverModel, on_delete=PROTECT, null=True)

    def __str__(self):
        return str(self.plate)

    class Meta:
        db_table = "bus"
