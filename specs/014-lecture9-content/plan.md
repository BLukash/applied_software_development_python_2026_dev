# Implementation Plan: Lecture 9 — Docker + PostgreSQL + SQLAlchemy: Real Persistence

**Branch**: `014-lecture9-content` | **Date**: 2026-04-02 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/014-lecture9-content/spec.md`

## Summary

Create Lecture 9 notebook and extend the notes-api project with real database persistence. The lecture teaches Docker as a practical tool (not a deep topic), sets up PostgreSQL via docker compose, introduces SQLAlchemy ORM, replaces stub endpoints with real CRUD operations, and adds a repository layer. All examples build on the existing notes-api project. Deliverables: one Jupyter notebook + project extensions (Dockerfile, docker-compose.yml, database module, models, repositories, updated endpoints and tests).

## Technical Context

**Language/Version**: Python 3.13+ (code examples in Jupyter Notebook + FastAPI project)
**Primary Dependencies**: FastAPI, Pydantic, uvicorn, SQLAlchemy 2.0+, psycopg2-binary (PostgreSQL driver), pydantic-settings, pytest, httpx, ruff, black
**Storage**: PostgreSQL (via Docker container), SQLAlchemy ORM for access
**Testing**: pytest + FastAPI TestClient (updated for database-backed endpoints)
**Target Platform**: Jupyter Notebook (lecture delivery), Docker (project runtime)
**Project Type**: Educational content (Jupyter notebook) + web API project (FastAPI + PostgreSQL)
**Performance Goals**: N/A — educational content
**Constraints**: Lecture MUST fit 90 minutes; Docker treated as tool (10 min max)
**Scale/Scope**: 1 notebook, ~10 project files added/modified, 1 docker-compose.yml, 1 Dockerfile

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status | Notes |
|------|--------|-------|
| Learning objectives at start | PASS | L9 objectives: containerized dev, DB connection, ORM, CRUD, layering |
| At least 5 runnable code examples | PASS | SQLAlchemy model, CRUD operations, repository functions, docker commands, config |
| At least 2 exercises with solutions | PASS | Exercise 1: add GET /notes endpoint; Exercise 2: add update endpoint or new field |
| At least 2 memes | PASS | Docker whale meme, "it works on my machine" meme |
| At least 1 diagram | PASS | App ↔ DB architecture diagram, layering diagram |
| Ukrainian text with English terms | PASS | Only specific technical terms get English translation |
| No per-section time estimates | PASS | Constitution v1.5.1 rule — no "(~10 хв)" in notebook |
| Duration 1.5 hours | PASS | Docker (10 min) + Connection (10 min) + SQLAlchemy (15 min) + CRUD (20 min) + Errors (5 min) + Layering (10 min) + Exercises (15 min) + Summary (5 min) = ~90 min |
| Prerequisites section | PASS | References L6 (FastAPI), L7 (config, testing), Docker required |
| Summary + What's Next | PASS | Preview L10: migrations, relationships, data integrity |
| Project uses notes-api | PASS | All examples on existing project files |
| No unnecessary English translations | PASS | Constitution v1.5.1 rule enforced |

**Gate result**: ALL PASS

## Project Structure

### Documentation (this feature)

```text
specs/014-lecture9-content/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── contracts/
│   └── api.yaml         # OpenAPI spec for updated endpoints
├── quickstart.md        # Phase 1 output
└── checklists/
    └── requirements.md  # Spec quality checklist
```

### Source Code (repository root)

```text
lectures/
└── 09-docker-postgres-sqlalchemy/
    ├── lecture-09.ipynb          # NEW — lecture notebook
    └── assets/
        └── memes/

project/notes-api/
├── Dockerfile                   # NEW — app container
├── docker-compose.yml           # NEW — Postgres + app
├── .env.example                 # MODIFIED — add DATABASE_URL
├── app/
│   ├── database.py              # NEW — engine, session, Base
│   ├── config.py                # MODIFIED — add database_url
│   ├── main.py                  # MODIFIED — add DB lifecycle (create_all on startup)
│   ├── models/
│   │   ├── __init__.py          # NEW
│   │   └── note.py              # NEW — SQLAlchemy Note model
│   ├── repositories/
│   │   ├── __init__.py          # NEW
│   │   └── notes.py             # NEW — CRUD functions
│   ├── services/
│   │   ├── __init__.py          # EXISTS (empty)
│   │   └── notes.py             # NEW — business logic layer
│   ├── routers/
│   │   └── notes.py             # MODIFIED — use service layer, add GET /notes/{id}
│   └── schemas/
│       └── notes.py             # MODIFIED — add NoteUpdate if needed
├── tests/
│   ├── conftest.py              # NEW — test DB fixtures
│   ├── test_health.py           # EXISTS — may need minor updates
│   └── test_notes.py            # MODIFIED — test against real DB
├── pyproject.toml               # MODIFIED — add sqlalchemy, psycopg2-binary
└── Makefile                     # EXISTS — no changes needed
```

**Structure Decision**: Extends existing notes-api project. New directories: `app/models/`, `app/repositories/`. New files: `Dockerfile`, `docker-compose.yml`, `app/database.py`. Service layer in `app/services/notes.py` bridges router and repository.

## Complexity Tracking

> No violations detected — section intentionally left empty.
