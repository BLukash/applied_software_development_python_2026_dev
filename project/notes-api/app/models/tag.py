from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class TagModel(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    note_id: Mapped[str] = mapped_column(
        ForeignKey("notes.id", ondelete="CASCADE"), nullable=False
    )

    note: Mapped["NoteModel"] = relationship(back_populates="tags")  # noqa: F821
