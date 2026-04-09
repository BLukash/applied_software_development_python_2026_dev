from __future__ import annotations

from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload

from app.models.note import NoteModel
from app.models.tag import TagModel
from app.schemas.notes import NoteCreate


def create_note(db: Session, note_data: NoteCreate) -> NoteModel:
    note = NoteModel(
        title=note_data.title,
        content=note_data.content,
    )
    for tag_name in note_data.tags:
        note.tags.append(TagModel(name=tag_name))
    db.add(note)
    db.commit()
    db.refresh(note)
    return note


def get_note_by_id(db: Session, note_id: str) -> NoteModel | None:
    stmt = (
        select(NoteModel)
        .options(selectinload(NoteModel.tags))
        .where(NoteModel.id == note_id)
    )
    return db.scalars(stmt).first()


def search_notes(
    db: Session,
    query: str = "",
    tags: list[str] | None = None,
    limit: int = 10,
) -> list[NoteModel]:
    stmt = select(NoteModel).options(selectinload(NoteModel.tags))

    if query:
        stmt = stmt.where(
            NoteModel.title.ilike(f"%{query}%") | NoteModel.content.ilike(f"%{query}%")
        )

    if tags:
        stmt = stmt.join(NoteModel.tags).where(TagModel.name.in_(tags))

    stmt = stmt.distinct().limit(limit)
    return list(db.scalars(stmt).all())


def delete_note(db: Session, note_id: str) -> bool:
    note = db.get(NoteModel, note_id)
    if note is None:
        return False
    db.delete(note)
    db.commit()
    return True
