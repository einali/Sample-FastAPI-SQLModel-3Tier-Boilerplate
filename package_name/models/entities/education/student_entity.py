from sqlmodel import SQLModel

from package_name.models.entities.base_entity import BaseEntity




class StudentEntity( BaseEntity, table=True):
    __tablename__ = "boilerplate_student"

    first_name: str
    last_name: str
    password: str | None = None

