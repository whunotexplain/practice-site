import secrets
from typing import Annotated, Literal, Tuple, Union

from app.database.db import get_db
from app.models.admin_model import Administrator
from app.models.volonteur_model import Volonteur
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

security = HTTPBasic()


async def authenticate_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    db: AsyncSession = Depends(get_db),
) -> Tuple[Union[Administrator, Volonteur], Literal["admin", "volonteur"]]:
    """
    Возвращает объект пользователя и его роль
    """

    unauth_exc = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password",
        headers={"WWW-Authenticate": "Basic"},
    )

    # Сначала проверяем админов
    result = await db.execute(
        select(Administrator).where(Administrator.login == credentials.username)
    )
    admin = result.scalar_one_or_none()

    if admin is not None:
        if not secrets.compare_digest(
            credentials.password.encode("utf-8"),
            admin.password.encode("utf-8"),
        ):
            raise unauth_exc
        return admin, "admin"

    # Проверяем волонтеров
    result = await db.execute(
        select(Volonteur).where(Volonteur.login == credentials.username)
    )
    volonteur = result.scalar_one_or_none()

    if volonteur is not None:
        if not secrets.compare_digest(
            credentials.password.encode("utf-8"),
            volonteur.password.encode("utf-8"),
        ):
            raise unauth_exc
        return volonteur, "volonteur"

    raise unauth_exc


# Зависимости для контроля доступа
async def get_current_user(
    user_and_role: Tuple[Union[Administrator, Volonteur], str] = Depends(
        authenticate_user
    ),
):
    """Возвращает пользователя и его роль"""
    return user_and_role


async def require_admin(
    user_and_role: Tuple[Union[Administrator, Volonteur], str] = Depends(
        authenticate_user
    ),
):
    """Только для админов"""
    user, role = user_and_role
    if role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required"
        )
    return user


async def require_volonteur(
    user_and_role: Tuple[Union[Administrator, Volonteur], str] = Depends(
        authenticate_user
    ),
):
    """Только для волонтеров"""
    user, role = user_and_role
    if role != "volonteur":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Volonteur privileges required",
        )
    return user
