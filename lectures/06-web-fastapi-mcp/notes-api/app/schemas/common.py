from __future__ import annotations

from pydantic import BaseModel


class HealthStatus(BaseModel):
    status: str
    version: str


class ErrorResponse(BaseModel):
    detail: str
    error_code: str
