from datetime import datetime
from core.configs import settings
from sqlalchemy import Column, Integer, String


class UserModel(settings.DBBaseModel):
    __tablename__ = 'user'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    name: str = Column(String(100))
    cpf: str = Column(String(100))
    email: str = Column(String(100))
    phone_number: str = Column(String(100))
    created_at: datetime = datetime.now()
    updated_at: datetime = datetime.now()
