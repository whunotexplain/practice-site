from fastapi import HTTPException, status
from passlib.context import CryptContext
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from ..models.user_demo_model import Users
from ..users.schemas import CreateUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user_in_db(db: AsyncSession, user_data: CreateUser):
    """Создать пользователя в базе данных"""

    # Проверяем, существует ли пользователь
    existing_user = await get_user_by_login(db, user_data.login)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким логином уже существует",
        )

    # Хешируем пароль
    hashed_password = pwd_context.hash(user_data.password)

    # Создаем объект пользователя для БД
    new_user = Users(
        login=user_data.login,
        phone_number=user_data.phone_number,
        password=hashed_password,
    )

    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    return {
        "id": new_user.id,
        "login": new_user.login,
        "phone_number": new_user.phone_number,
        "message": "Пользователь успешно создан",
    }


def create_user(user_in: Users) -> dict:
    user = user_in.model_dump()
    return {
        "success": True,
        "user": user,
    }


def get_user_by_id(id_user: int) -> dict:
    return {
        "success": True,
        "user": {
            "id": id_user,
            "login": f"user_{id_user}",
            "password": f"password_{id_user}",
        },
    }


async def get_user_by_login(db: AsyncSession, login: str):
    """Получить пользователя по username"""
    result = await db.execute(select(Users).where(Users.login == login))
    return result.scalar_one_or_none()
