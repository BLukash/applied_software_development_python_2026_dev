from __future__ import annotations

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    app_name: str = "Notes API"
    debug: bool = False
    port: int = 8000

    model_config = {"env_file": ".env"}


settings = Settings()
