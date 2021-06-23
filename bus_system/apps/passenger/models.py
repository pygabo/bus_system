from bus_system.utils.models import StakeholderBaseModel
from bus_system.utils.models import BaseModel


class PassengerModel(BaseModel, StakeholderBaseModel):
    """
    Passenger Model
    """

    class Meta:
        db_table = "passenger"
