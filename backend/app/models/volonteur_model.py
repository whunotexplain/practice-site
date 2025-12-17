from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Volonteur(Base):
    __tablename__ = "volonteurs"

    id = Column(Integer, primary_key=True, index=True)
    login = Column(String, unique=True)
    password = Column(String)
    phone_number = Column(String)
