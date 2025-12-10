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
            <style>h1{
    margin: 15px 10px 74px 10px;
    font: 24px;
    font-family: Arial, Helvetica, sans-serif;
}
article{
    margin: 0 auto;
    text-align: center;
}
.enter_button{
    color: aliceblue;
    background-color: rgba(18, 83, 140, 1);
    width: 160px;
    height: 41px;
    border-radius: 17px;
}

.authorization input{
    margin: 30px;
    text-align: left;
    width: 245px;
    height: 52px;
    border-radius: 17px;
            
    font-family: 'Times New Roman', Times, serif;
    font-weight: normal;
    font-style: normal;
            
}

input,
input::placeholder {
    font: 14px sans-serif;
}

.button-link {
display: inline-block;
padding: 10px 20px;
background-color: #4CAF50;
color: white;
text-decoration: none;
border-radius: 17px;
font-family: Arial, sans-serif;
font-size: 16px;
}
        </style>

        </head>
        <body>
            <article class="authorization">
                <img src="frontend/assets/images/logo.png" alt="logo" width="200">
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
