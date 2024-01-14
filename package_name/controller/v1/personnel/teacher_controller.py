from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

from logic.education.course_logic import CourseLogic
from logic.personnel.teacher_logic import TeacherLogic
from models.entities.education.course_entity import CourseEntity
from models.entities.personnel.teacher_entity import TeacherEntity
from package_name.models.dtos.education.student_dto import StudentDTOCreate
from package_name.models.entities.education.student_entity import StudentEntity

router = APIRouter()


@router.get("/", response_model=list[TeacherEntity])
def get_all(offset: int = 0, limit: int = Query(default=10, le=10),logic: TeacherLogic = Depends(TeacherLogic)) -> list[TeacherEntity]:
    """
    Sends students back to user.


    :returns: student list.
    """

    return logic.get_list(offset,limit)



@router.post("/", response_model=TeacherEntity)
def create_student(student:StudentDTOCreate,logic: CourseLogic = Depends(TeacherLogic)) -> TeacherEntity:
    """
    Sends students back to user.


    :returns: student list.
    """

    return logic.create(student)



