from __future__ import annotations

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.note import NoteModel
from app.repositories import notes as notes_repo
from app.schemas.notes import (
    NoteCreate,
    NoteResponse,
    NoteSearchQuery,
    NoteSearchResult,
)


def _note_to_response(note: NoteModel) -> NoteResponse:
    return NoteResponse(
        id=note.id,
        title=note.title,
        content=note.content,
        tags=[t.name for t in note.tags],
        created_at=note.created_at,
    )


def create_note(db: Session, note_data: NoteCreate) -> NoteResponse:
    note = notes_repo.create_note(db, note_data)
    return _note_to_response(note)


def get_note(db: Session, note_id: str) -> NoteResponse:
    note = notes_repo.get_note_by_id(db, note_id)
    if note is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note {note_id} not found",
        )
    return _note_to_response(note)


def search_notes(db: Session, query: NoteSearchQuery) -> NoteSearchResult:
    notes = notes_repo.search_notes(
        db, query=query.query, tags=query.tags, limit=query.limit
    )
    results = [_note_to_response(n) for n in notes]
    return NoteSearchResult(results=results, total=len(results))


def delete_note(db: Session, note_id: str) -> None:
    deleted = notes_repo.delete_note(db, note_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Note {note_id} not found",
        )
