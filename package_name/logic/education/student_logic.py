from fastapi import Depends
from sqlmodel import Session

from package_name.dal.database import get_session
from package_name.dal.education.student_dao import StudentDAO
from package_name.logic.base_logic import BaseLogic
from package_name.models.entities.base_entity import BaseEntity


class StudentLogic(BaseLogic):

    def __init__(self, session: Session = Depends(get_session), dao: StudentDAO = Depends(StudentDAO), ):
        super().__init__(session, dao)

    def get_list(self,offset: int, limit: int) -> list[BaseEntity]:
        return super().get_list(offset,limit)
