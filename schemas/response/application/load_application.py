from datetime import datetime

from pydantic import BaseModel

from models import Status, Gender


class LoadApplication(BaseModel):
    id: int
    ration_card_number: str
    name: str
    dob: str
    gender: Gender
    mobile_number: str
    year: int
    income: str
    created_at: datetime
    status: Status
