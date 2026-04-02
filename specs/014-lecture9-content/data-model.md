# Data Model: Lecture 9 — Docker + PostgreSQL + SQLAlchemy: Real Persistence

**Feature**: 014-lecture9-content
**Date**: 2026-04-02

## Entities

### Note (SQLAlchemy Model)

Maps to PostgreSQL table `notes`.

| Column | Type | Constraints | Notes |
|--------|------|-------------|-------|
| id | UUID | PRIMARY KEY, default=uuid4 | Auto-generated, matches existing Pydantic schema |
| title | String(200) | NOT NULL | 1-200 chars (validated at API layer by Pydantic) |
| content | Text | NOT NULL | Unlimited length |
| tags | ARRAY(String) | DEFAULT=[] | PostgreSQL native array, queryable |
| created_at | DateTime(timezone=True) | NOT NULL, default=now | UTC timestamp |

**Relationships**: None in L9 (relationships introduced in L10).

### Pydantic Schemas (Existing, minor updates)

Already defined in `app/schemas/notes.py` from L6:

| Schema | Purpose | Fields |
|--------|---------|--------|
| NoteCreate | Request body for POST /notes/create | title, content, tags |
| NoteResponse | Response for all note endpoints | id, title, content, tags, created_at |
| NoteSearchQuery | Request body for POST /notes/search | query, tags, limit |
| NoteSearchResult | Response for search | results, total |

**No new schemas needed** — existing ones map cleanly to the SQLAlchemy model.

## Notebook Section Map

**Title**: "Docker + PostgreSQL + SQLAlchemy: Real Persistence"
**Directory**: `lectures/09-docker-postgres-sqlalchemy/`
**Duration**: ~90 minutes

| # | Section | Content |
|---|---------|---------|
| 0 | Header + Prerequisites | L6 (FastAPI), L7 (config, testing), Docker required |
| 1 | Learning Objectives | 5 measurable outcomes |
| 2 | Вступ: від заглушок до реальних даних | Motivation — stubs are fake, time to persist. Show current stub code vs what we'll build |
| 3 | Docker як інструмент | What is a container (1 min), docker-compose.yml walkthrough, `docker compose up`, Dockerfile for notes-api. NOT a Docker deep dive |
| 4 | Підключення до бази даних | DATABASE_URL in .env, pydantic-settings (builds on L7 config), sqlalchemy.create_engine, verify connection. Show app/database.py |
| 5 | SQLAlchemy ORM | ORM concept (class = table), define NoteModel in app/models/note.py, Base.metadata.create_all. Compare with Pydantic schema side-by-side |
| 6 | CRUD з SQLAlchemy | Create (session.add + commit), read (session.get), search (select with filters), delete (session.delete). Show app/repositories/notes.py |
| 7 | Обробка помилок | not found → 404, unique violations → 409, general DB errors. Show updated router |
| 8 | Вправа 1 | Students wire GET /notes/{note_id} through the repository layer |
| 9 | Шари архітектури | "Don't leak ORM models" rule, router → service → repository diagram, before/after refactoring. Show app/services/notes.py |
| 10 | Вправа 2 | Students add a PUT /notes/{note_id} endpoint or add an "updated_at" field |
| 11 | Тестування з базою даних | conftest.py with test DB fixture, updated test_notes.py |
| 12 | Підсумок | Key takeaways |
| 13 | Що далі? | L10: migrations, relationships, data integrity |
| 14 | Джерела | SQLAlchemy docs, Docker docs, FastAPI + SQLAlchemy tutorial |

## File Change Map

| File | Action | What Changes |
|------|--------|-------------|
| `project/notes-api/Dockerfile` | CREATE | App container definition |
| `project/notes-api/docker-compose.yml` | CREATE | Postgres + app services |
| `project/notes-api/.env.example` | MODIFY | Add DATABASE_URL |
| `project/notes-api/app/config.py` | MODIFY | Add database_url field |
| `project/notes-api/app/database.py` | CREATE | Engine, SessionLocal, Base, get_db |
| `project/notes-api/app/main.py` | MODIFY | Add startup event for create_all, include get_db |
| `project/notes-api/app/models/__init__.py` | CREATE | Empty |
| `project/notes-api/app/models/note.py` | CREATE | NoteModel SQLAlchemy class |
| `project/notes-api/app/repositories/__init__.py` | CREATE | Empty |
| `project/notes-api/app/repositories/notes.py` | CREATE | CRUD functions |
| `project/notes-api/app/services/notes.py` | CREATE | Business logic (thin passthrough initially) |
| `project/notes-api/app/routers/notes.py` | MODIFY | Replace stubs with service calls, add GET endpoint |
| `project/notes-api/app/schemas/notes.py` | MODIFY | Add NoteUpdate if needed |
| `project/notes-api/tests/conftest.py` | CREATE | Test DB fixtures |
| `project/notes-api/tests/test_notes.py` | MODIFY | Use test DB fixtures |
| `project/notes-api/pyproject.toml` | MODIFY | Add sqlalchemy, psycopg2-binary |
| `lectures/09-docker-postgres-sqlalchemy/lecture-09.ipynb` | CREATE | Lecture notebook |
