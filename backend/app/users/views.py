from fastapi import APIRouter

from . import crud
from .schemas import CreateUser

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/users/")
def create_usere(user: CreateUser):
    return crud.create_user(user_in=user)
