from fastapi import APIRouter

# from . import crud
# from .schemas import CreateAdmin

router = APIRouter(prefix="/admins", tags=["admins"])


# @router.post("/admins/")
# def create_user(user: CreateAdmin):
#     return crud.create_admin(user_in=user)
