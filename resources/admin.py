from typing import List

from fastapi import APIRouter, status, Depends

from managers.admin import AdminManager
from managers.application import ApplicationManager
from managers.student import StudentManager
from schemas.request.admin.login_admin import LoginAdmin
from schemas.response.application.load_application import LoadApplication
from schemas.response.student.load_student import LoadStudent
from utils.auth.admin.verify_token import admin_oauth2_scheme

router = APIRouter(prefix="/admin", tags=["ADMIN APIS"])


@router.post("/login", summary="Login as Admin", status_code=status.HTTP_201_CREATED)
async def login_admin(data: LoginAdmin):
    data = data.dict()
    token = await AdminManager.login_admin(data=data)
    return {"message": "You have logged in successfully !", "token": token}


@router.get(
    "/load-pending-applications",
    summary="Load Pending Applications",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(admin_oauth2_scheme)],
    response_model=List[LoadApplication],
)
async def load_pending_applications():
    return await ApplicationManager.get_pending_applications()


@router.get(
    "/load-approved-applications",
    summary="Load Approved Applications",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(admin_oauth2_scheme)],
    response_model=List[LoadApplication],
)
async def load_approved_applications():
    return await ApplicationManager.get_approved_applications()


@router.get(
    "/load-rejected-applications",
    summary="Load Rejected Applications",
    status_code=status.HTTP_200_OK,
    dependencies=[Depends(admin_oauth2_scheme)],
    response_model=List[LoadApplication],
)
async def load_rejected_applications():
    return await ApplicationManager.get_rejected_applications()


@router.get(
    "/load-all-students",
    summary="Load All Students",
    status_code=status.HTTP_200_OK,
    response_model=List[LoadStudent],
    dependencies=[Depends(admin_oauth2_scheme)],
)
async def get_all_students():
    all_students = await StudentManager.get_all_students()
    return all_students


@router.put(
    "/approve-application/{application_id}",
    summary="Approve Application",
    dependencies=[Depends(admin_oauth2_scheme)],
)
async def approve_application(application_id: int):
    await ApplicationManager.approve(id_=application_id)
    return {"message": "Application is approved !"}


@router.put(
    "/reject-application/{application_id}",
    summary="Reject Application",
    dependencies=[Depends(admin_oauth2_scheme)],
)
async def reject_application(application_id: int):
    await ApplicationManager.reject(id_=application_id)
    return {"message": "Application is rejected !"}
