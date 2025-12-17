from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from app.config import settings

from .admin.views import router as admin_router
from .api_auth.authorisation import router as auth_router
from .api_auth.registration import router as registration_router
from .routers.admin_page import router as admin_page_router
from .routers.auth_page import router as auth_page_router
from .routers.volonteur_page import router as volonteur_page_router
from .users.views import router as users_router

app = FastAPI(
    title=settings.app_name, debug=settings.debug, docs_url="/docs", redoc_url="/redoc"
)

STATIC_DIR = Path("C:/Users/kozin/OneDrive/Dokumentumok/fastapi-practice/frontend")

app.mount("/css", StaticFiles(directory=str(STATIC_DIR / "css")), name="css")
app.mount("/images", StaticFiles(directory=str(STATIC_DIR / "images")), name="images")
app.mount("/js", StaticFiles(directory=str(STATIC_DIR / "js")), name="js")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# PAGES
app.include_router(admin_page_router)
app.include_router(volonteur_page_router)
app.include_router(auth_page_router)


#
app.include_router(auth_router)
app.include_router(users_router)
app.include_router(admin_router)
app.include_router(registration_router)


@app.get("/")
async def root():
    from fastapi.responses import RedirectResponse

    return RedirectResponse(url="/pages/auth")
