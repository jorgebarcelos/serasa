from datetime import datetime
from typing import Optional
from pydantic import BaseModel as SchemaBaseModel


class UserSchema(SchemaBaseModel):
    id: Optional[int]
    name: str
    cpf: str
    email: str
    phone_number: str
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
