from sqlmodel import Session, select
from package_name.dal.database import get_session

from fastapi import Depends

from package_name.models.entities.base_entity import BaseEntity


class BaseDAO:
    __model_type__: type[BaseEntity]



    def __init__(self, session: Session = Depends(get_session)):
        super().__init__()
        self.session = session

    def get_list(self, offset: int, limit: int) -> list[BaseEntity]:
        with self.session:

            return self.session.exec(select(self.__model_type__).offset(offset).limit(limit)).all()

    def create(self, dto) -> BaseEntity:
        with self.session as session:
            entity = self.__model_type__.model_validate(dto)

            session.add(entity)
            session.commit()
            session.refresh(entity)

            return entity
