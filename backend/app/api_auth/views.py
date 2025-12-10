import uuid
from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from typing import Annotated, Any
from fastapi.security import HTTPBasicCredentials, HTTPBasic
import secrets
from time import time

router = APIRouter(prefix="/authorize", tags=["Authenticate"])

security = HTTPBasic()


@router.get("/authenticate/")
def auth_credentials(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    return {
        "Message":"Hi",
        "username": credentials.username,
        "password": credentials.password,
    }
    
