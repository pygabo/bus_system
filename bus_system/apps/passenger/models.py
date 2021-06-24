# Imports from my apps
from bus_system.utils.models import BaseModel, StakeholderBaseModel


class PassengerModel(BaseModel, StakeholderBaseModel):
    """
    Passenger Model
    """

    class Meta:
        db_table = "passenger"
