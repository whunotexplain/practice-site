from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database.db import Base


class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True, nullable=False, index=True)
    password = Column(String, nullable=False, index=True)
