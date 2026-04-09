# Quickstart: Lecture 10 — Migrations, Relationships & Data Integrity

**Feature**: 015-lecture10-content
**Date**: 2026-04-02

## Prerequisites

- L9 notes-api project complete (Docker, PostgreSQL, SQLAlchemy, repository)
- Docker and Docker Compose installed
- Python 3.13+, uv, Jupyter

## Verification Steps

### 1. Verify Lecture Directory

```bash
ls lectures/10-migrations-relationships/lecture-10.ipynb
```

### 2. Verify Alembic Setup

```bash
ls project/notes-api/alembic.ini
ls project/notes-api/alembic/env.py
ls project/notes-api/alembic/versions/
```

### 3. Run Migrations

```bash
cd project/notes-api
docker compose up db -d
DATABASE_URL=postgresql://notes:notes@localhost:5432/notes_db \
  uv run alembic upgrade head
```

### 4. Verify Schema

```bash
docker compose exec db psql -U notes -d notes_db -c "\dt"
# Should show: notes, tags, alembic_version

docker compose exec db psql -U notes -d notes_db -c "\d tags"
# Should show: id, name, note_id (FK)
```

### 5. Test API with Tags

```bash
# Create note with tags
curl -X POST http://localhost:8000/notes/create \
  -H "Content-Type: application/json" \
  -d '{"title": "Tagged Note", "content": "Has tags!", "tags": ["important", "test"]}'

# Get note — tags should be in response
curl http://localhost:8000/notes/{note_id}

# Delete note — tags should cascade
curl -X DELETE http://localhost:8000/notes/{note_id}
```

### 6. Run Tests

```bash
cd project/notes-api
make check
```

### 7. Verify create_all Removed

```bash
grep -c "create_all" project/notes-api/app/main.py
# Should return 0
```

### 8. Verify Notebook

```bash
jupyter nbconvert --to notebook --execute \
  lectures/10-migrations-relationships/lecture-10.ipynb
```

### 9. Cleanup

```bash
cd project/notes-api
docker compose down -v
```
