# import uuid
# from fastapi import APIRouter, Depends, HTTPException, status, Header, Response, Cookie, FastAPI, Request
# from typing import Annotated, Any
# from fastapi.security import HTTPBasicCredentials, HTTPBasic
# import secrets
# from time import time
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates



# templates = Jinja2Templates(directory="templates")

# async def authenticate(request: Request):
#     return templates.TemplateResponse(
#         request=request, name="item.html", context={"id": id}
#     )