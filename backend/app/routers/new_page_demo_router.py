from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/pages", tags=["Frontend"])


BASE_DIR = Path(
    "C:/Users/kozin/OneDrive/Dokumentumok/fastapi-practice/frontend/templates"
)


templates = Jinja2Templates(directory=str(BASE_DIR))


@router.get("/templates/index.html")
async def get_auth_page(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})
