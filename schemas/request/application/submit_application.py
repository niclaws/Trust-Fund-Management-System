from pydantic import BaseModel

from models import Gender


class SubmitApplication(BaseModel):
    ration_card_number: str
    name: str
    dob: str
    gender: Gender
    mobile_number: str
    year: int
    income: str
