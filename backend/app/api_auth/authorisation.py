import secrets
from typing import Annotated, Literal, Tuple, Union

from app.database.db import get_db
from app.models.admin_model import Administrator
from app.models.volonteur_model import Volonteur
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter(prefix="/demo-auth", tags=["Demo Auth"])

security = HTTPBasic()


async def authenticate_user(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    db: AsyncSession = Depends(get_db),
) -> Tuple[Union[Administrator, Volonteur], Literal["admin", "volonteur"]]:
    """Аутентификация пользователя"""
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


@router.post("/login/")
def login(username: str = Depends(authenticate_user)):
    async def login_redirect(user_and_role=Depends(authenticate_user)):
        """Основной эндпоинт для авторизации с редиректом"""
        user, role = user_and_role

        if role == "admin":
            return RedirectResponse(url="/pages/admin/dashboard")
        elif role == "volonteur":
            return RedirectResponse(url="/pages/volonteur/dashboard")
        else:
            return RedirectResponse(url="/")


@router.post("/test-login/")
async def test_login(
    credentials: HTTPBasicCredentials = Depends(security),
    db: AsyncSession = Depends(get_db),
):
    """Тестовый эндпоинт для проверки аутентификации"""
    try:
        user, role = await authenticate_user(credentials, db)

        return {
            "status": "success",
            "message": "Аутентификация прошла успешно",
            "user": {"id": user.id, "login": user.login, "type": role},
            "authenticated": True,
        }

    except HTTPException as e:
        return {
            "status": "error",
            "message": str(e.detail),
            "authenticated": False,
            "status_code": e.status_code,
        }
