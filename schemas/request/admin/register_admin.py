from pydantic import EmailStr, BaseModel


class RegisterAdmin(BaseModel):
    email: EmailStr
    name: str
    password: str
