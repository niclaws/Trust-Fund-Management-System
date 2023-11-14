from pydantic import BaseModel


class LoadStudent(BaseModel):
    name: str
    email: str
