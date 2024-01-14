from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

from logic.education.course_logic import CourseLogic
from models.entities.education.course_entity import CourseEntity
from package_name.models.dtos.education.student_dto import StudentDTOCreate
from package_name.models.entities.education.student_entity import StudentEntity

router = APIRouter()


@router.get("/", response_model=list[StudentEntity])
def get_all(offset: int = 0, limit: int = Query(default=10, le=10),logic: CourseLogic = Depends(CourseLogic)) -> list[CourseEntity]:
    """
    Sends students back to user.


    :returns: student list.
    """

    return logic.get_list(offset,limit)



@router.post("/", response_model=StudentEntity)
def create_student(student:StudentDTOCreate,logic: CourseLogic = Depends(CourseLogic)) -> CourseEntity:
    """
    Sends students back to user.


    :returns: student list.
    """

    return logic.create(student)



