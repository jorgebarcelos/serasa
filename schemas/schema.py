import datetime
from typing import Optional
from pydantic import BaseModel as SchemaBaseModel


class UserSchema(SchemaBaseModel):
    id: Optional[int]
    name: str
    cpf: str
    email: str
    phone_number: str
    created_at: datetime.date
    updated_at: datetime.date

    class Config:
        orm_mode = True


class OrderSchema(SchemaBaseModel):
    id: Optional[int]
    user_id: int
    item_description: str
    item_quantity: int
    item_price: float
    total_value: float
    created_at: datetime.date
    updated_at: datetime.date
