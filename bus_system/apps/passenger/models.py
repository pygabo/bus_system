# Imports from my apps
from bus_system.utils.models import BaseModel, StakeholderBaseModel


class PassengerModel(BaseModel, StakeholderBaseModel):
    """
    Passenger Model
    """

    def __str__(self):
        return str("{} {} {}".format(self.first_name, self.surname, self.identification_number))

    class Meta:
        db_table = "passenger"
