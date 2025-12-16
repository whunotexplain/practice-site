import secrets
from typing import Annotated

from app.database.db import get_db
from app.models.user_demo_model import Users
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/demo-auth", tags=["Demo Auth"])

security = HTTPBasic()


async def authenticate_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    db: AsyncSession = Depends(get_db),
):
    unauhted_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )

    result = await db.execute(select(Users).where(Users.login == credentials.username))
    user = result.scalar_one_or_none()

    if user is None:
        raise unauhted_exc

    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        user.password.encode("utf-8"),
    ):
        raise unauhted_exc

    return credentials.username


@router.get("/base-auth/")
def demo_auth(auth_username: str = Depends(authenticate_user)):
    return {"Message": f"Hi, {auth_username}!", "username": auth_username}


@router.post("/login/")
def login(username: str = Depends(authenticate_user)):
    return {"message": "Login successful", "username": username}
