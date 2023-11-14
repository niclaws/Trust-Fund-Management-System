from typing import List

from fastapi import APIRouter, status, Depends, Request

from managers.application import ApplicationManager
from managers.student import StudentManager
from schemas.request.application.submit_application import SubmitApplication
from schemas.request.student.login_student import LoginStudent
from schemas.request.student.register_student import RegisterStudent
from schemas.request.student.send_otp import SendOtp
from schemas.request.student.verify_otp import VerifyOtp
from schemas.response.application.load_application import LoadApplication
from schemas.response.student.load_student import LoadStudent
from utils.auth.student.verify_token import student_oauth2_scheme

router = APIRouter(prefix="/student", tags=["STUDENT APIS"])


@router.post(
    "/register",
    summary="Register as Student",
    status_code=status.HTTP_201_CREATED,
)
async def register_student(student: RegisterStudent):
    student = student.dict()
    await StudentManager.register_student(data=student)
    return {"message": "Your account has been created !"}


@router.post(
    "/verify/send-otp",
    summary="Send Verification Code to Email",
    status_code=status.HTTP_201_CREATED,
)
async def send_otp(data: SendOtp):
    data = data.dict()
    await StudentManager.send_otp(email=data["email"])
    return {"message": "A verification code is sent to your email."}


@router.post(
    "/verify/check-otp",
    summary="Check Verification Code",
    status_code=status.HTTP_201_CREATED,
)
async def verify_otp(data: VerifyOtp):
    data = data.dict()
    await StudentManager.verify_otp(
        email=data["email"], verification_code=data["verification_code"]
    )
    return {"message": "Your account is verified now."}


@router.post("/login", summary="Login as Student", status_code=status.HTTP_201_CREATED)
async def login_student(student: LoginStudent):
    student = student.dict()
    token = await StudentManager.login_student(data=student)
    return {"message": "You have logged in successfully !", "token": token}


@router.get(
    "/load-details",
    summary="Load Student Details",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(student_oauth2_scheme)],
    response_model=LoadStudent,
)
async def load_details(request: Request):
    id_ = request.state.user["id"]
    student_details = await StudentManager.get_student_by_id(id_=id_)
    return student_details


@router.post(
    "/submit-application",
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(student_oauth2_scheme)],
    summary="Submit Application Form",
)
async def submit_application(data: SubmitApplication, request: Request):
    id_ = request.state.user["id"]
    data = data.dict()
    data["student_id"] = id_
    await ApplicationManager.create_application(data=data)
    return {"message": "Your application is submitted successfully !"}


@router.get(
    "/load-applications",
    status_code=status.HTTP_200_OK,
    summary="Load Submitted Applications",
    dependencies=[Depends(student_oauth2_scheme)],
    response_model=List[LoadApplication],
)
async def load_applications(request: Request):
    id_ = request.state.user["id"]
    return await ApplicationManager.get_applications_from_student(student_id=id_)
