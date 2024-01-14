from enum import unique, Enum, StrEnum


@unique
class NationalityType(StrEnum):
    IRAN =  "IRAN"
    FOREIGN =  "FOREIGN"


    def get_area(self)->int:
        if self==self.IRAN:
            return 168195
        elif self==self.FOREIGN:
            return 0


if __name__ == '__main__':
    print(NationalityType.IRAN)
    print(NationalityType.IRAN.value)
    print(NationalityType['IRAN'])
