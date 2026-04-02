from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.note import NoteModel
from app.schemas.notes import NoteCreate


def create_note(db: Session, note_data: NoteCreate) -> NoteModel:
    note = NoteModel(
        title=note_data.title,
        content=note_data.content,
        tags=note_data.tags,
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def get_note_by_id(db: Session, note_id: str) -> NoteModel | None:
    return db.get(NoteModel, note_id)


def search_notes(
    db: Session,
    query: str = "",
    tags: list[str] | None = None,
    limit: int = 10,
) -> list[NoteModel]:
    stmt = select(NoteModel)

    if query:
        stmt = stmt.where(
            NoteModel.title.ilike(f"%{query}%") | NoteModel.content.ilike(f"%{query}%")
        )

    # Tag filtering: load results and filter in Python for portability
    # (PostgreSQL JSON operators differ from SQLite)

    results = list(db.scalars(stmt).all())

    if tags:
        results = [n for n in results if set(tags) & set(n.tags or [])]

    return results[:limit]


def delete_note(db: Session, note_id: str) -> bool:
    note = db.get(NoteModel, note_id)
    if note is None:
        return False
    db.delete(note)
    db.commit()
    return True
