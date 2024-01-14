from enum import unique

from package_name.models.enums.base_enum import BaseType

@unique
class EducationLevelType(str,BaseType):
    UNDERGRADUATE = "UNDERGRADUATE"
    MASTER = "MASTER"
    PHD = "PHD"
