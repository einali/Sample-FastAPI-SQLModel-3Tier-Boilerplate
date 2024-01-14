
from fastapi.routing import APIRouter

from controller.v1.education import course_controller
from controller.v1.personnel import teacher_controller
from package_name.controller.v1.education import student_controller

api_router = APIRouter()

api_router.include_router(student_controller.router, prefix="/students")
api_router.include_router(course_controller.router, prefix="/courses")
api_router.include_router(teacher_controller.router, prefix="/teachers")
