
from sqlmodel import Session, select

from package_name.dal.base_dao import BaseDAO
from package_name.dal.database import get_session

from fastapi import Depends

from package_name.models.dtos.base_dto import BasicDTO
from package_name.models.entities.base_entity import BaseEntity


class BaseLogic:


    def __init__(self ,session: Session ,dao: BaseDAO):
        super().__init__()
        self.session =session
        self.dao:BaseDAO=dao


    def get_list(self,offset: int , limit: int )->list[BaseEntity]:
       return self.dao.get_list(offset,limit)


    def create(self,dto:BasicDTO)->list[BaseEntity]:
       return self.dao.create(dto)





