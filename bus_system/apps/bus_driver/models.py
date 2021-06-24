# Core Django imports
from django.db.models import BooleanField, ImageField

# Imports from my apps
from bus_system.utils.models import BaseModel, StakeholderBaseModel


class BusDriverModel(BaseModel, StakeholderBaseModel):
    """
    Bus Driver Model
    """
    avatar = ImageField()
    is_available = BooleanField(default=True)

    class Meta:
        db_table = "bus_driver"
