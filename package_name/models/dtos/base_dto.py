from datetime import datetime
from typing import Union
from uuid import uuid4, UUID

from pydantic import BaseModel, EmailStr
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional

# Shared properties



class BasicDTO(SQLModel):
    pass
class PKDTO():
    pk_uuid: UUID

class CreatedAtDTO:
    created_at: datetime

class LogicalDeleteDTO:
    is_deleted: bool



class UpdatedAtDTO:
    updated_at: datetime
    created_at: datetime





