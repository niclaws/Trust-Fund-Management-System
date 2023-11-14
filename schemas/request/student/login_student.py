from pydantic import BaseModel, EmailStr


class LoginStudent(BaseModel):
    email: EmailStr
    password: str
