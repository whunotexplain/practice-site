from typing import Optional

from pydantic import BaseModel, EmailStr


class AdminBase(BaseModel):
    login: str
    password: str


class AdminCreate(AdminBase):
    password: str


class AdminLogin(BaseModel):
    login: str
    password: str


class Admin(AdminBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
