from pydantic import BaseModel, EmailStr


class RegisterStudent(BaseModel):
    name: str
    email: EmailStr
    password: str
