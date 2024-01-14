from package_name.models.enums.base_enum import BaseType


class NationalityType(BaseType):
    IRAN = ("IRAN", 1648195)
    FOREIGN = ("FOREIGN", 0)

    def __init__(self, code: str, area: int):
        super().__init__(code)
        self.area = area


if __name__ == '__main__':
    print(NationalityType.IRAN)
    print(NationalityType.IRAN.value)
    print(NationalityType.IRAN.area)
    print(NationalityType("IRAN"))
