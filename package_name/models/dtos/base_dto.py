from datetime import datetime
from typing import Union
from uuid import uuid4, UUID

from pydantic import BaseModel, EmailStr
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional

# Shared properties



class BasicDTO(SQLModel):
    pk_uuid: UUID
    created_at: datetime


class LogicalDeleteDTO:
    is_deleted: bool



class UpdatedAtDTO:
    updated_at: datetime





