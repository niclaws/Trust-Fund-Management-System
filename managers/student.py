import sqlalchemy
from fastapi import HTTPException, status

from config.db_connection import database
from models import student
from utils.auth.student.create_token import StudentJWTToken
from utils.bcrypt.password import HashedPassword
from utils.otp_verification.generate_otp import OTPGeneration
from utils.otp_verification.send_email import EmailAutomation


class StudentManager:
    @staticmethod
    async def send_otp(email):
        student_found = await StudentManager.get_student_by_email(email=email)
        if student_found is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The email id is not found in our database !!!",
            )
        verification_code = OTPGeneration.generate_otp()
        await database.execute(
            student.update()
            .values(verification_code=verification_code)
            .where(student.c.email == email)
        )
        subject = "OTP Verification for Trust Fund Management System"
        message = f"""Hey {student_found['name']}!\n\nYou have recently registered for Trust Fund Management System. To complete your registration,\nplease confirm your account.\n\nYou may be asked to enter this confirmation code: {verification_code}\n\nThanks,\nThe Trust Fund Management Team"""
        EmailAutomation.send_email(
            subject=subject, message=message, recipient_email=student_found["email"]
        )

    @staticmethod
    async def verify_otp(email, verification_code):
        student_found = await StudentManager.get_student_by_email(email=email)
        if student_found is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The email id is not found in our database !!!",
            )
        if verification_code != student_found["verification_code"]:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="The Verification Code you have entered is incorrect !",
            )
        await database.execute(student.update().values(is_verified=True))
        subject = "Account Activation for Trust Fund Management System"
        message = f"""Congratulations {student_found['name']}!\n\nYour account is verified for Trust Fund Management System.\nNow You can login to your account and submit your application.\n\nThanks,\nThe Trust Fund Management Team"""
        EmailAutomation.send_email(
            subject=subject, message=message, recipient_email=student_found["email"]
        )

    @staticmethod
    async def get_student_by_email(email):
        return await database.fetch_one(
            student.select().where(student.c.email == email)
        )

    @staticmethod
    async def get_student_by_id(id_):
        return await database.fetch_one(student.select().where(student.c.id == id_))

    @staticmethod
    async def register_student(data):
        student_found = await StudentManager.get_student_by_email(email=data["email"])
        if student_found is not None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="There is already an existing account with this email. Please login to your account.",
            )
        data["password"] = HashedPassword.encode(password=data["password"])
        await database.execute(student.insert().values(data))

    @staticmethod
    async def login_student(data):
        student_found = await StudentManager.get_student_by_email(email=data["email"])
        if student_found is None:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You dont have a registered account yet. Please create an account to login.",
            )

        if student_found["is_verified"] == False:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Your account is not verified !!! Please verify your account using OTP.",
            )

        passwords_matched = HashedPassword.verify(
            entered_password=data["password"], actual_password=student_found["password"]
        )
        if passwords_matched is False:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="The password you have entered is incorrect !!!",
            )
        token = StudentJWTToken.encode_token_with_expiry_time(id=student_found["id"])
        return token

    @staticmethod
    async def get_all_students():
        return await database.fetch_all(student.select())
