import datetime
from core.configs import settings
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship


class UserModel(settings.DBBaseModel):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100))
    cpf: str = Column(String(100))
    email: str = Column(String(100))
    phone_number: str = Column(String(100))
    created_at: datetime = datetime.date
    updated_at: datetime = datetime.date


class OrderModel(settings.DBBaseModel):
    __tablename__ = 'order'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    user_id: int = Column(Integer, ForeignKey('user.id'))
    item_description: str = Column(String(250))
    item_quantity: int = Column(Integer())
    item_price: float = Column(Float())
    total_value: float = Column(Float())
    created_at: datetime = datetime.date
    updated_at: datetime = datetime.date

    user = relationship('user', back_populates='order')
