from fastapi import FastAPI, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.config import settings
from .api_auth.views import router as auth_router
from .routers.auth_router import router as auth_page_router
from pathlib import Path

app = FastAPI(
    title = settings.app_name,
    debug = settings.debug,
    docs_url = '/docs',
    redoc_url = '/redoc'
)

STATIC_DIR = Path("C:/Users/kozin/OneDrive/Dokumentumok/fastapi-practice/frontend")

app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(auth_page_router)

app.mount("/css", StaticFiles(directory=str(STATIC_DIR / "css")), name="css")
app.mount("/images", StaticFiles(directory=str(STATIC_DIR / "images")), name="images")

