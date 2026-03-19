from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class NoteCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    content: str = Field(min_length=1)
    tags: list[str] = []


class NoteResponse(BaseModel):
    id: str
    title: str
    content: str
    tags: list[str]
    created_at: datetime


class NoteSearchQuery(BaseModel):
    query: str = ""
    tags: list[str] = []
    limit: int = Field(default=10, ge=1, le=100)


class NoteSearchResult(BaseModel):
    results: list[NoteResponse]
    total: int
