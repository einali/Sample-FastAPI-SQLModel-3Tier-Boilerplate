from enum import unique, StrEnum


@unique
class EducationLevelType(StrEnum):
    UNDERGRADUATE = "UNDERGRADUATE"
    MASTER = "MASTER"
    PHD = "PHD"
