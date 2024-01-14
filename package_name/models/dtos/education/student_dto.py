from enum import Enum

from sqlmodel import SQLModel

from models.enums.personnel.nationality_type import NationalityType
from package_name.models.dtos.base_dto import BasicDTO


class StudentDTOCreate(SQLModel):
    first_name: str
    last_name: str
    nationality_type: str

