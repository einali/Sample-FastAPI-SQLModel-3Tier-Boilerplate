
from sqlmodel import Field, Relationship, SQLModel,Enum


from package_name.models.entities.base_entity import BaseEntity
from package_name.models.enums.personnel.nationality_type import NationalityType


class StudentEntity( BaseEntity, table=True):
    __tablename__ = "boilerplate_student"

    first_name: str
    last_name: str
    password: str | None = None
    nationality_type : NationalityType

