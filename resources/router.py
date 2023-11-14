from fastapi import APIRouter

from resources import student, admin

api_router = APIRouter(prefix="/api")
api_router.include_router(admin.router)
api_router.include_router(student.router)
