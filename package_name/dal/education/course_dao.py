from models.entities.education.course_entity import CourseEntity
from package_name.dal.base_dao import BaseDAO
from package_name.models.entities.education.student_entity import   StudentEntity


class CourseDAO(BaseDAO):
    __model_type__: CourseEntity = CourseEntity

