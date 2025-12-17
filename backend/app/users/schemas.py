from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class UserBase(BaseModel):
    login: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=3, max_length=20)
    phone_number: str = Field(..., min_length=10, max_length=15)


class CreateUser(UserBase):
    pass


class UserInDB(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserLogin(BaseModel):
    login: str
    password: str
    phone_number: str
