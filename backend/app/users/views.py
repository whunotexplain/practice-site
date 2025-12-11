from .schemas import Create_User
from fastapi import APIRouter
from . import crud


router = APIRouter(prefix="/users", tags=["users"])


@router.post("/users/")
def create_usere(user: Create_User):
    return crud.create_user(user_in=user)