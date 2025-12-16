from typing import List, Union

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Practice api web"
    debug: bool = True
    database_url: str = "postgresql+asyncpg://postgres:12345@localhost/demo_practice"
    cors_origins: Union[List[str], str] = [
        "http://localhost:5173",
        "http://localhost:8080",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:8080",
    ]

    class Config:
        env_file = ".env"


settings = Settings()
