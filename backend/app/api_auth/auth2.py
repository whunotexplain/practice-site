# import secrets
# from typing import Annotated

# from app.database.db import get_db
# from app.users.crud import get_user_by_username
# from fastapi import APIRouter, Depends, HTTPException, status
# from fastapi.security import HTTPBasic, HTTPBasicCredentials
# from sqlalchemy.ext.asyncio import AsyncSession

# router = APIRouter(prefix="/demo-auth", tags=["Demo Auth"])

# security = HTTPBasic()


# async def authenticate_user(
#     credentials: Annotated[HTTPBasicCredentials, Depends(security)],
#     db: AsyncSession = Depends(get_db),
# ):
#     """Аутентификация пользователя с данными из БД"""

#     # Получаем пользователя из базы данных
#     user = await get_user_by_username(db, credentials.username)

#     if user is None:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password",
#             headers={"WWW-Authenticate": "Basic"},
#         )

#     # Проверяем пароль
#     # Важно: сравнение должно быть защищено от timing attack
#     # В production используйте hashed_password

#     # Проверяем, есть ли поле 'password' или 'password_hash'
#     user_password = getattr(user, "password", None)
#     if user_password is None:
#         user_password = getattr(user, "password_hash", None)

#     if user_password is None:
#         raise HTTPException(
#             status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
#             detail="User password field not found",
#         )

#     # Безопасное сравнение паролей
#     if not secrets.compare_digest(
#         credentials.password.encode("utf-8"),
#         str(user_password).encode("utf-8"),
#     ):
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Invalid username or password",
#             headers={"WWW-Authenticate": "Basic"},
#         )

#     return credentials.username


# @router.get("/base-auth/")
# async def demo_auth(auth_username: str = Depends(authenticate_user)):
#     return {"Message": f"Hi, {auth_username}!", "username": auth_username}


# @router.post("/login/")
# async def login(username: str = Depends(authenticate_user)):
#     return {"message": "Login successful", "username": username}


# @router.get("/users/me")
# async def get_current_user(
#     db: AsyncSession = Depends(get_db), auth_username: str = Depends(authenticate_user)
# ):
#     """Получить данные текущего пользователя"""
#     user = await get_user_by_username(db, auth_username)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND, detail="User not found"
#         )

#     # Возвращаем данные пользователя (исключая пароль)
#     return {
#         "id": user.id,
#         "username": user.username,
#         "email": user.email,
#         # добавьте другие поля по необходимости
#     }


# @router.get("/users/")
# async def get_users(
#     db: AsyncSession = Depends(get_db), skip: int = 0, limit: int = 100
# ):
#     """Получить список всех пользователей (для админов)"""
#     from app.users.crud import get_all_users

#     users = await get_all_users(db, skip=skip, limit=limit)

#     # Преобразуем в безопасный формат (без паролей)
#     safe_users = []
#     for user in users:
#         safe_users.append(
#             {
#                 "id": user.id,
#                 "username": user.username,
#                 "email": user.email,
#                 # добавьте другие поля по необходимости
#             }
#         )

#     return {"users": safe_users, "count": len(safe_users)}
