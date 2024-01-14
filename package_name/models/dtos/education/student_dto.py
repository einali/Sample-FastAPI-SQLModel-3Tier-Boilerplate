from package_name.models.dtos.base_dto import BasicDTO


class StudentDTOCreate(BasicDTO):
    first_name: str
    last_name: str
