# Stdlib imports
from uuid import uuid4

# Core Django imports
from django.db.models import CharField, Model, UUIDField
# Third party imports
from model_utils.models import SoftDeletableModel, TimeStampedModel


class BaseModel(TimeStampedModel, SoftDeletableModel):
    """
    Base Model
    """
    id = UUIDField(primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class StakeholderBaseModel(Model):
    """
    Base Model Stakeholder
    """
    first_name = CharField(max_length=150)
    surname = CharField(max_length=150)
    identification_number = CharField(max_length=150)

    class Meta:
        abstract = True
