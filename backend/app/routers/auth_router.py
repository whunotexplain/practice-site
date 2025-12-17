from app.api_auth.test_auth import authenticate_user
from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.get("/login")
async def login(request: Request, user_and_role=Depends(authenticate_user)):
    """Авторизация с редиректом на нужную страницу"""
    user, role = user_and_role

    if role == "admin":
        return RedirectResponse(url="/admin/dashboard")
    else:
        return RedirectResponse(url="/volonteur/dashboard")
