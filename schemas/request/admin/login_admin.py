from pydantic import BaseModel, EmailStr


class LoginAdmin(BaseModel):
    email: EmailStr
    password: str
