from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from app.config import settings
# from .database import init_db
# from .routes import products_router, cart_router, categories_router

app = FastAPI(
    title = settings.app_name,
    debug = settings.debug,
    docs_url = '/docs',
    redoc_url = '/redoc'
)

