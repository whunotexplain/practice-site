from sqlalchemy import Column, Integer, String

from ..database.db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, nullable=False, index=True)
    phone_number = Column(String(20), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)
