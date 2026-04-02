from __future__ import annotations

from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.notes import (
    NoteCreate,
    NoteResponse,
    NoteSearchQuery,
    NoteSearchResult,
)
from app.services import notes as notes_service

router = APIRouter()


@router.post(
    "/notes/create", response_model=NoteResponse, status_code=status.HTTP_201_CREATED
)
def create_note(note: NoteCreate, db: Session = Depends(get_db)) -> NoteResponse:
    return notes_service.create_note(db, note)


@router.get("/notes/{note_id}", response_model=NoteResponse)
def get_note(note_id: str, db: Session = Depends(get_db)) -> NoteResponse:
    return notes_service.get_note(db, note_id)


@router.post("/notes/search", response_model=NoteSearchResult)
def search_notes(
    query: NoteSearchQuery, db: Session = Depends(get_db)
) -> NoteSearchResult:
    return notes_service.search_notes(db, query)


@router.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_note(note_id: str, db: Session = Depends(get_db)) -> Response:
    notes_service.delete_note(db, note_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
