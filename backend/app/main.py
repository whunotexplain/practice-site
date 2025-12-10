from fastapi import FastAPI, Request, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from app.config import settings
from .api_auth.views import router as auth_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title = settings.app_name,
    debug = settings.debug,
    docs_url = '/docs',
    redoc_url = '/redoc'
)


app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)

router = APIRouter(prefix="/pages", tags=["Frontend"])

templates = Jinja2Templates(directory="frontend/templates")

@router.get("/authorize")
async def get_auth_page(
    request: Request
):
    return templates.TemplateResponse(name="auth_window.html", context={"request": request})



@app.get('/health')
def health_check():
    return {'status': 'healthy'}
