from __future__ import annotations

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.config import settings
from app.routers import health, notes
from app.schemas.common import ErrorResponse

app = FastAPI(title=settings.app_name, version="0.3.0", debug=settings.debug)

app.include_router(health.router)
app.include_router(notes.router)


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content=ErrorResponse(
            detail=str(exc.detail),
            error_code=f"HTTP_{exc.status_code}",
        ).model_dump(),
    )
