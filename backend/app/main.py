from fastapi import FastAPI
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
    docs_url = '/api/docs',
    redoc_url = '/api/redoc'
)

# app.mount("/static", StaticFiles(directory="static"), name="static")


# templates = Jinja2Templates(directory="templates")


app.add_middleware(
    CORSMiddleware,
    allow_origins = settings.cors_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)


@app.get('/', response_class=HTMLResponse)
def root():
    html_content = """ 
        <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Авторизация</title>
        <link rel="stylesheet" href="main.css">

    </head>
    <body>
        <article class="authorization">
            <img src="frontend/assets/images/logo.png" alt="" width="200">
            <h1>Авторизация</h1>
            <input type="text" name="login"  placeholder="Логин:" >
            <br>
            <input type="password" name="password" placeholder="Пароль:">
            <br>
            <button class="enter_button" type="submit">Войти</button>
        </article>
    </body>
    </html>
"""
    return HTMLResponse(content=html_content)
@app.get('/health')
def health_check():
    return {'status': 'healthy'}
