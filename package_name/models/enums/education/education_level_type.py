from enum import unique, StrEnum

from package_name.models.enums.base_enum import BaseType


@unique
class EducationLevelType(StrEnum):
    UNDERGRADUATE = "UNDERGRADUATE"
    MASTER = "MASTER"
    PHD = "PHD"
