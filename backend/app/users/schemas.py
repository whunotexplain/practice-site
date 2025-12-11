from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional



class UserBase(BaseModel):
    login: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=3, max_length=20)



class Create_User(BaseModel):
    login: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=3, max_length=20) 
