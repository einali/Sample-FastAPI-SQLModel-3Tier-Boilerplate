from sqlmodel import Relationship


class TeacherEntity(table=True):
    __tablename__ = "boilerplate_teacher"
    fullname : str

    courses:list["CourseEntity"] = Relationship(back_populates="teacher")





