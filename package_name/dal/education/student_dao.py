from package_name.dal.base_dao import BaseDAO
from package_name.models.entities.education.student_entity import   StudentEntity


class StudentDAO(BaseDAO):
    __model_type__: StudentEntity = StudentEntity


