from __future__ import annotations

from fastapi import APIRouter

from app.schemas.common import HealthStatus

router = APIRouter()


@router.get("/health", response_model=HealthStatus)
async def health_check() -> HealthStatus:
    return HealthStatus(status="ok", version="0.1.0")
