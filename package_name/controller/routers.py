
from fastapi.routing import APIRouter
from package_name.controller.v1.education import student_controller

api_router = APIRouter()

api_router.include_router(student_controller.router, prefix="/students", tags=["echo"])
