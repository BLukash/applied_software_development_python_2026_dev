from __future__ import annotations

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Notes API"
    debug: bool = False
    port: int = 8000
    database_url: str = "postgresql://notes:notes@localhost:5432/notes_db"

    model_config = {"env_file": ".env"}


settings = Settings()
