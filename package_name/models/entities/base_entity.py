from datetime import datetime
from typing import Union
from uuid import uuid4, UUID

from pydantic import BaseModel, EmailStr
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional
from typing import List, Optional
# Shared properties
from sqlalchemy import text


class BaseEntity(SQLModel):
    pk_uuid: Optional[UUID] = Field(default_factory=uuid4, primary_key=True)
    created_at: Optional[datetime] = Field(default=None, sa_column_kwargs={
        "server_default": text("current_timestamp(0)")
    })


class LogicalDeleteEntity():
    is_deleted: bool = Field(default=False)



class UpdatedAtBaseEntity():
    updated_at: datetime = Field(default=None,sa_column_kwargs={
            "server_default": text("current_timestamp(0)"),
            "onupdate": text("current_timestamp(0)")
        })


class AdminUser(BaseEntity,LogicalDeleteEntity,UpdatedAtBaseEntity):
    pass





class AdminBaseEntity:
    created_by_uuid : UUID | None = Field(default=None, foreign_key="user.uuid", nullable=False)
    updated_by_uuid : UUID | None = Field(default=None, foreign_key="user.uuid", nullable=False)
    created_by: AdminUser = Relationship()
    updated_by: AdminUser = Relationship()
