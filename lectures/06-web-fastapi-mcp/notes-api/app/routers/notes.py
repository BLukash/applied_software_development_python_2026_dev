from __future__ import annotations

from datetime import UTC, datetime
from uuid import uuid4

from fastapi import APIRouter, status

from app.schemas.notes import (
    NoteCreate,
    NoteResponse,
    NoteSearchQuery,
    NoteSearchResult,
)

router = APIRouter()


@router.post(
    "/notes/create", response_model=NoteResponse, status_code=status.HTTP_201_CREATED
)
async def create_note(note: NoteCreate) -> NoteResponse:
    return NoteResponse(
        id=str(uuid4()),
        title=note.title,
        content=note.content,
        tags=note.tags,
        created_at=datetime.now(UTC),
    )


@router.post("/notes/search", response_model=NoteSearchResult)
async def search_notes(query: NoteSearchQuery) -> NoteSearchResult:
    return NoteSearchResult(results=[], total=0)
