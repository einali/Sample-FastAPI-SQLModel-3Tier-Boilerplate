from sqlmodel import Relationship, Field

from models.entities.personnel.teacher_entity import TeacherEntity
from models.enums.education.education_level_type import EducationLevelType
from package_name.models.entities.base_entity import BaseEntity


class CourseEntity(table=True):
    __tablename__ = "boilerplate_course"
    name : str
    education_level_type :EducationLevelType

    teacher_id: int | None = Field(default=None, foreign_key="teacher.id")
    teacher: TeacherEntity | None = Relationship(back_populates="courses")






