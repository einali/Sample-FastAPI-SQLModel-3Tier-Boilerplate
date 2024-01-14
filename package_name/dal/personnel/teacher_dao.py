from models.entities.personnel.teacher_entity import TeacherEntity
from package_name.dal.base_dao import BaseDAO
from package_name.models.entities.education.student_entity import   StudentEntity


class TeacherDAO(BaseDAO):
    __model_type__: TeacherEntity = TeacherEntity

