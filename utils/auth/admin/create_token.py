from datetime import datetime, timedelta

import jwt
from decouple import config


class AdminJWTToken:
    @staticmethod
    def encode_token_with_expiry_time(id):
        payload = {"id": id, "exp": datetime.utcnow() + timedelta(hours=8)}
        return jwt.encode(payload, config("ADMIN_JWT_SECRET"), algorithm="HS256")
