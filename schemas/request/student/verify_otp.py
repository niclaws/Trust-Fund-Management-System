from pydantic import BaseModel, EmailStr


class VerifyOtp(BaseModel):
    email: EmailStr
    verification_code: str
