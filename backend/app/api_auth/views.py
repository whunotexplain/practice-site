import uuid
from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie
from typing import Annotated, Any
from fastapi.security import HTTPBasicCredentials, HTTPBasic
import secrets
from time import time

router = APIRouter(prefix="/authorize/", tags=["Authenticate"])