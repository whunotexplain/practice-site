import secrets
import uuid
from time import time
from typing import Annotated, Any

from fastapi import APIRouter, Cookie, Depends, Header, HTTPException, Response, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

router = APIRouter(prefix="/demo-auth", tags=["Demo Auth"])

security = HTTPBasic()


def authenticate_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    unauhted_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    correct_password = ClassUser.get(credentials.username)
    if correct_password is None:
        raise unauhted_exc

    if not secrets.compare_digest(
        credentials.password.encode("utf-8"),
        correct_password.encode("utf-8"),
    ):
        raise unauhted_exc

    return credentials.username


@router.get("/base-auth/")
def demo_auth(auth_username: str = Depends(authenticate_user)):
    return {"Message": f"Hi, {auth_username}!", "username": auth_username}


@router.post("/login/")
def login(username: str = Depends(authenticate_user)):
    return {"message": "Login successful", "username": username}
