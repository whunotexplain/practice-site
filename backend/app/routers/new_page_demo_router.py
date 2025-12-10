from fastapi import FastAPI, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.config import settings
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pathlib import Path

router = APIRouter(prefix="/pages", tags=["Frontend"])


BASE_DIR = Path("C:/Users/kozin/OneDrive/Dokumentumok/fastapi-practice/frontend/templates")


templates = Jinja2Templates(directory=str(BASE_DIR))



@router.get("/templates/index.html")
async def get_auth_page(
    request: Request
):
    return templates.TemplateResponse(name="index.html", context={"request": request})