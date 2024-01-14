from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

from package_name.logic.education.student_logic import StudentLogic
from package_name.models.dtos.education.student_dto import StudentDTOCreate
from package_name.models.entities.education.student_entity import StudentEntity

router = APIRouter()


@router.get("/", response_model=list[StudentEntity])
def get_all_students(offset: int = 0, limit: int = Query(default=10, le=10),logic: StudentLogic = Depends(StudentLogic)) -> list[StudentEntity]:
    """
    Sends students back to user.


    :returns: student list.
    """

    return logic.get_list(offset,limit)



@router.post("/", response_model=StudentEntity)
def create_student(student:StudentDTOCreate,logic: StudentLogic = Depends(StudentLogic)) -> StudentEntity:
    """
    Sends students back to user.


    :returns: student list.
    """

    return logic.create(student)



