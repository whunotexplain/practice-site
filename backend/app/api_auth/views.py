import uuid
from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from typing import Annotated, Any
from fastapi.security import HTTPBasicCredentials, HTTPBasic
import secrets
from time import time

router = APIRouter(prefix="/authorize", tags=["Authenticate"])

security = HTTPBasic()


usernames_to_passwords = {
    "egor": "egor",
    "admin": "admin"
}


@router.get("/authenticate/")
def auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {
        "Message":"Hi",
        "username": credentials.username,
        "password": credentials.password,
    }

def get_auth_user_username(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    unauhted_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )
    correct_password = usernames_to_passwords.get(credentials.username)
    if correct_password is None:
        raise unauhted_exc

    #secrets
    if not secrets.compare_digest(
        credentials.password.encode('utf-8'),
        correct_password.encode('utf-8'),
    ):
        raise unauhted_exc
    
    return credentials.username



@router.get("/basic-auth-username/")
def demo_auth_some_http_header(
    auth_username: str = Depends(get_auth_user_username)
):
    return {
        "Message": f"Hi, {auth_username}!",
        "username": auth_username
    }
    


 