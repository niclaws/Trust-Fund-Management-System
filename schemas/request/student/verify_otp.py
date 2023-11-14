from pydantic import BaseModel


class VerifyOtp(BaseModel):
    email: str
    verification_code: str
