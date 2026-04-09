# Data Model: Lecture 10 — Migrations, Relationships & Data Integrity

**Feature**: 015-lecture10-content
**Date**: 2026-04-02

## Entities

### Note (Modified from L9)

| Column | Type | Constraints | Change |
|--------|------|-------------|--------|
| id | String(36) | PRIMARY KEY, default=uuid4 | Unchanged |
| title | String(200) | NOT NULL | Unchanged |
| content | Text | NOT NULL | Unchanged |
| ~~tags~~ | ~~JSON~~ | ~~DEFAULT=[]~~ | **REMOVED** (moved to Tag table) |
| created_at | DateTime(tz) | NOT NULL, default=now | Unchanged |

**New relationship**: `tags = relationship("TagModel", back_populates="note", cascade="all, delete-orphan")`

### Tag (New)

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| id | Integer | PRIMARY KEY, autoincrement | Simple integer PK |
| name | String(50) | NOT NULL | Tag label |
| note_id | String(36) | FOREIGN KEY → notes.id, NOT NULL | One-to-many |

**Relationship**: `note = relationship("NoteModel", back_populates="tags")`

### Pydantic Schema Updates

| Schema | Change |
|--------|--------|
| NoteCreate | `tags: list[str]` stays (API accepts tag names as strings) |
| NoteResponse | `tags: list[str]` stays (API returns tag names) — service converts TagModel → string list |
| TagResponse | NEW: `id: int`, `name: str` (optional, for detailed API responses) |

## Notebook Section Map

| # | Section | Content |
|---|---------|---------|
| 0 | Header + Prerequisites | L9 (Docker, PostgreSQL, SQLAlchemy, repository) |
| 1 | Learning Objectives | 5 outcomes |
| 2 | Вступ: навіщо міграції? | The problem: model changed but DB has data. create_all vs migrations |
| 3 | Alembic: крок за кроком | init → revision --autogenerate → upgrade head → downgrade. Show once, explain each step |
| 4 | Вправа 1 | Students run initial migration for existing Note model |
| 5 | Зв'язки між таблицями | One-to-many: Tag → Note. ER diagram. ForeignKey, relationship(), cascade |
| 6 | Міграція для нового зв'язку | Generate and apply migration for Tag table |
| 7 | Оновлення коду | Updated model, repository, service, schemas. Show diffs |
| 8 | Вправа 2 | Students add a constraint or index to improve query performance |
| 9 | Принципи проєктування БД | Indexes, constraints, "think about queries first" |
| 10 | Тестування з базою даних | Updated conftest.py, test relationship queries |
| 11 | psql: швидка діагностика | Connect to container, \dt, \d notes, \d tags, SELECT with JOIN |
| 12 | Підсумок | Key takeaways + meme |
| 13 | Що далі? | L11: pandas analytics from DB exports |
| 14 | Джерела | Alembic docs, SQLAlchemy relationships, PostgreSQL indexes |

## Migration Plan

| Migration | What it does |
|-----------|-------------|
| 001_initial.py | Creates `notes` table from NoteModel (without JSON tags column — clean start) |
| 002_add_tags.py | Creates `tags` table with FK to notes, drops `tags` JSON column from notes if it exists |

## File Change Map

| File | Action | What Changes |
|------|--------|-------------|
| `pyproject.toml` | MODIFY | Add alembic dependency |
| `alembic.ini` | CREATE | Alembic configuration |
| `alembic/env.py` | CREATE | DB URL from env, import Base + models |
| `alembic/script.py.mako` | CREATE | Migration template |
| `alembic/versions/001_initial.py` | CREATE | Notes table |
| `alembic/versions/002_add_tags.py` | CREATE | Tags table + FK |
| `app/main.py` | MODIFY | Remove create_all from lifespan |
| `app/models/__init__.py` | MODIFY | Import note and tag models |
| `app/models/note.py` | MODIFY | Remove JSON tags, add relationship |
| `app/models/tag.py` | CREATE | TagModel |
| `app/repositories/notes.py` | MODIFY | Handle tags as related objects |
| `app/services/notes.py` | MODIFY | Convert TagModel ↔ string list |
| `app/schemas/notes.py` | MODIFY | Keep tags as list[str] in API |
| `tests/conftest.py` | MODIFY | Ensure create_all includes Tag |
| `tests/test_notes.py` | MODIFY | Test tags through relationship |
| `lectures/10-migrations-relationships/lecture-10.ipynb` | CREATE | Notebook |
