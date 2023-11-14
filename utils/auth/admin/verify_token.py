from typing import Optional

import jwt
from decouple import config
from fastapi import status, HTTPException, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


class AdminAuthToken(HTTPBearer):
    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        res = await super().__call__(request)

        try:
            payload = jwt.decode(
                res.credentials, config("ADMIN_JWT_SECRET"), algorithms=["HS256"]
            )
            request.state.user = payload
            return payload
        except jwt.ExpiredSignatureError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is expired"
            )
        except jwt.InvalidTokenError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token"
            )


admin_oauth2_scheme = AdminAuthToken()
