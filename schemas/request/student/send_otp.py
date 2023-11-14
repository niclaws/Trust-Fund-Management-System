from pydantic import BaseModel, EmailStr


class SendOtp(BaseModel):
    email: EmailStr
