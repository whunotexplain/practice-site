from app.database.db import get_db
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession

from ..users.schemas import CreateUser

router = APIRouter(prefix="/registration", tags=["Volonteur registartion"])

security = HTTPBasic()

crypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


@router.post("/register")
async def register(user: CreateUser, db: AsyncSession = Depends(get_db)):
    """
    Регистрация нового пользователя
    """
    try:
        db_user = crud.create_user(db, user)
        return db_user
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Ошибка при регистрации пользователя",
        )
