# Quickstart: Lecture 9 — Docker + PostgreSQL + SQLAlchemy

**Feature**: 014-lecture9-content
**Date**: 2026-04-02

## Prerequisites

- Git repository cloned and on branch `014-lecture9-content`
- Python 3.13+ installed
- Docker and Docker Compose installed
- Jupyter Notebook / JupyterLab installed
- `uv` installed

## Verification Steps

### 1. Verify Lecture Directory

```bash
ls lectures/09-docker-postgres-sqlalchemy/lecture-09.ipynb
```

### 2. Verify Project Files Created

```bash
# New files should exist:
ls project/notes-api/Dockerfile
ls project/notes-api/docker-compose.yml
ls project/notes-api/app/database.py
ls project/notes-api/app/models/note.py
ls project/notes-api/app/repositories/notes.py
ls project/notes-api/app/services/notes.py
ls project/notes-api/tests/conftest.py
```

### 3. Start the Stack

```bash
cd project/notes-api
docker compose up --build -d
```

Both services should be healthy:
```bash
docker compose ps
# db   — healthy
# app  — running, port 8000
```

### 4. Test Endpoints

```bash
# Health check
curl http://localhost:8000/health

# Create a note
curl -X POST http://localhost:8000/notes/create \
  -H "Content-Type: application/json" \
  -d '{"title": "Test Note", "content": "Hello DB!", "tags": ["test"]}'

# Get the note (use ID from create response)
curl http://localhost:8000/notes/{note_id}

# Search notes
curl -X POST http://localhost:8000/notes/search \
  -H "Content-Type: application/json" \
  -d '{"query": "Test", "limit": 10}'

# Delete the note
curl -X DELETE http://localhost:8000/notes/{note_id}
# Should return 204

# Verify deletion
curl http://localhost:8000/notes/{note_id}
# Should return 404
```

### 5. Verify Persistence

```bash
# Restart containers
docker compose restart

# Previously created notes should still be accessible
curl http://localhost:8000/notes/{note_id}
```

### 6. Verify Swagger

Open http://localhost:8000/docs — all endpoints should be documented.

### 7. Run Tests

```bash
cd project/notes-api
make check
# ruff, black, and pytest should all pass
```

### 8. Verify Notebook

```bash
# Open and run all cells:
jupyter nbconvert --to notebook --execute \
  lectures/09-docker-postgres-sqlalchemy/lecture-09.ipynb
```

### 9. Verify Layering

```bash
# Router should NOT import sqlalchemy:
grep -c "sqlalchemy" project/notes-api/app/routers/notes.py
# Should return 0

# Repository should use Session:
grep -c "Session" project/notes-api/app/repositories/notes.py
# Should return > 0
```

### 10. Cleanup

```bash
cd project/notes-api
docker compose down -v  # -v removes the data volume
```

## Notes

- Tests use SQLite (not Postgres) for speed — this is intentional for the educational context
- The repository uses plain functions, not classes — this is the simplest entry point for students
- Tags use PostgreSQL ARRAY(String) type — SQLite tests may need adjustment for this
