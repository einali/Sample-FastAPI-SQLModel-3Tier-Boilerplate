from enum import unique, Enum, StrEnum


@unique
class NationalityType(Enum):
    IRAN =  1648195
    FOREIGN =  0




if __name__ == '__main__':
    print(NationalityType.IRAN)
    print(NationalityType.IRAN.value)
    print(NationalityType['IRAN'])
