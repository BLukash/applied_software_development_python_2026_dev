# Implementation Plan: Lecture 10 — Migrations, Relationships & Data Integrity

**Branch**: `015-lecture10-content` | **Date**: 2026-04-02 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/015-lecture10-content/spec.md`

## Summary

Create Lecture 10 notebook and extend the notes-api project with Alembic migrations, a Tag entity with one-to-many relationship to Note, and database testing improvements. The lecture teaches schema evolution (why migrations replace create_all), walks through Alembic once end-to-end, adds a Tag model with ForeignKey, covers DB design principles, and introduces psql debugging. Tags move from a JSON column in Note to a separate table — demonstrating exactly why migrations exist.

## Technical Context

**Language/Version**: Python 3.13+ (code examples in Jupyter Notebook + FastAPI project)
**Primary Dependencies**: FastAPI, Pydantic, uvicorn, SQLAlchemy 2.0+, psycopg2-binary, Alembic, pydantic-settings, pytest, httpx, ruff, black
**Storage**: PostgreSQL (via Docker), SQLAlchemy ORM, Alembic for schema migrations
**Testing**: pytest + FastAPI TestClient + SQLite test DB
**Target Platform**: Jupyter Notebook (lecture) + Docker (project runtime)
**Project Type**: Educational content + web API project
**Performance Goals**: N/A — educational content
**Constraints**: Lecture MUST fit 90 minutes; Alembic shown once, not deep-dived
**Scale/Scope**: 1 notebook, ~8 project files added/modified, Alembic init + 2 migrations

## Constitution Check

| Gate | Status | Notes |
|------|--------|-------|
| Learning objectives at start | PASS | 5 outcomes: migrations, relationships, DB design, testing, psql |
| At least 5 runnable code examples | PASS | Alembic commands, Tag model, relationship queries, psql, tests |
| At least 2 exercises with solutions | PASS | Exercise 1: run migration workflow; Exercise 2: add index or constraint |
| At least 2 memes | PASS | Migration meme, "DROP TABLE" meme |
| At least 1 diagram | PASS | ER diagram for Note-Tag relationship |
| Ukrainian text with English terms | PASS | Only specific technical terms |
| No per-section time estimates | PASS | Constitution v1.5.1 |
| Duration 1.5 hours | PASS | ~90 min |
| Prerequisites section | PASS | References L9 |
| Summary + What's Next | PASS | Preview L11: pandas analytics |

**Gate result**: ALL PASS

## Project Structure

### Documentation (this feature)

```text
specs/015-lecture10-content/
├── plan.md
├── research.md
├── data-model.md
├── contracts/
│   └── api.yaml
├── quickstart.md
└── checklists/
    └── requirements.md
```

### Source Code (repository root)

```text
lectures/
└── 10-migrations-relationships/
    ├── lecture-10.ipynb           # NEW
    └── assets/
        └── memes/

project/notes-api/
├── alembic.ini                   # NEW — Alembic config
├── alembic/                      # NEW — migrations directory
│   ├── env.py                    # NEW — configured for project models
│   ├── script.py.mako            # NEW — template
│   └── versions/
│       ├── 001_initial.py        # NEW — initial schema migration
│       └── 002_add_tags.py       # NEW — Tag table + FK
├── app/
│   ├── main.py                   # MODIFIED — remove create_all
│   ├── models/
│   │   ├── __init__.py           # MODIFIED — import all models
│   │   ├── note.py               # MODIFIED — remove JSON tags, add relationship
│   │   └── tag.py                # NEW — TagModel with FK to notes
│   ├── repositories/
│   │   └── notes.py              # MODIFIED — handle tags relationship
│   ├── services/
│   │   └── notes.py              # MODIFIED — handle tags in response
│   ├── routers/
│   │   └── notes.py              # MINOR — adjust for tag changes
│   └── schemas/
│       └── notes.py              # MODIFIED — TagResponse, update NoteResponse
├── tests/
│   ├── conftest.py               # MODIFIED — schema setup for tests
│   └── test_notes.py             # MODIFIED — test tags relationship
└── pyproject.toml                # MODIFIED — add alembic
```

## Complexity Tracking

> No violations detected.
