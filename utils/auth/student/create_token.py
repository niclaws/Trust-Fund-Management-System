from datetime import datetime, timedelta

import jwt
from decouple import config


class StudentJWTToken:
    @staticmethod
    def encode_token_with_expiry_time(id):
        payload = {"id": id, "exp": datetime.utcnow() + timedelta(days=7)}
        return jwt.encode(payload, config("STUDENT_JWT_SECRET"), algorithm="HS256")
