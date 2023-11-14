import sqlalchemy
from fastapi import HTTPException, status
from config.db_connection import database
from models.admin import admin
from utils.auth.admin.create_token import AdminJWTToken
from utils.bcrypt.password import HashedPassword


class AdminManager:
    @staticmethod
    async def get_admin_by_email(email):
        return await database.fetch_one(
            sqlalchemy.select([admin.c.id, admin.c.email, admin.c.password]).where(
                admin.c.email == email
            )
        )

    @staticmethod
    async def create_admin(data):
        admin_found = await AdminManager.get_admin_by_email(email=data["email"])
        if admin_found is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There is already an existing account with this email. Please login to your account.",
            )
        data["password"] = HashedPassword.encode(password=data["password"])
        await database.execute(admin.insert().values(data))

    @staticmethod
    async def login_admin(data):
        admin_found = await AdminManager.get_admin_by_email(email=data["email"])
        if admin_found is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You dont have a registered account yet. Please create an account to login.",
            )
        passwords_matched = HashedPassword.verify(
            entered_password=data["password"], actual_password=admin_found["password"]
        )
        if passwords_matched is False:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The password you have entered is incorrect !!!",
            )
        token = AdminJWTToken.encode_token_with_expiry_time(id=admin_found["id"])
        return token
