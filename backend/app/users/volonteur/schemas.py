from typing import Optional

from pydantic import BaseModel, EmailStr


class VolonteurBase(BaseModel):
    login: str
    password: str


class VolonteurCreate(VolonteurBase):
    password: str


class VolonteurLogin(BaseModel):
    login: str
    password: str


class Volonteur(VolonteurBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True
