from pydantic import BaseModel, Field


class AdminBase(BaseModel):
    login: str = Field(..., min_length=3, max_length=20)
    password: str = Field(..., min_length=3, max_length=20)


class AdminInDB(AdminBase):
    id: int

    class Config:
        from_attributes = True


class AdminLogin(BaseModel):
    login: str
    password: str
