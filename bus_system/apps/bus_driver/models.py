from django.db.models import ImageField, BooleanField

from bus_system.utils.models import StakeholderBaseModel
from bus_system.utils.models import BaseModel


class BusDriverModel(BaseModel, StakeholderBaseModel):
    """
    Bus Driver Model
    """
    avatar = ImageField()
    is_available = BooleanField(default=True)

    class Meta:
        db_table = "bus_driver"
