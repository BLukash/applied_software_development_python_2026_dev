# Research: Lecture 10 — Migrations, Relationships & Data Integrity

**Feature**: 015-lecture10-content
**Date**: 2026-04-02

## Research Tasks

### R1: Alembic Integration with Existing Project

**Decision**: Initialize Alembic with `alembic init alembic`, configure env.py to import project models and use the same DATABASE_URL from settings.

**Rationale**: Standard Alembic setup. The env.py must import `Base` from `app.database` and all models so autogenerate can detect them. The `sqlalchemy.url` in alembic.ini should read from the environment (DATABASE_URL) rather than being hardcoded.

**Alternatives considered**:
- Alembic async mode — unnecessary, project uses sync SQLAlchemy
- Flask-Migrate style — wrong framework

### R2: Tags Migration Strategy (JSON → Separate Table)

**Decision**: Two-step migration approach:
1. First migration: initial schema (Note table as-is from L9)
2. Second migration: add Tag table with FK, drop JSON tags column from Note

**Rationale**: This demonstrates the real-world scenario of schema evolution. Students see that changing how data is stored requires a migration, not just changing the model. The two-step approach shows both "create from scratch" and "alter existing" migration types.

**Alternatives considered**:
- Single migration with data migration (copy JSON tags → rows) — too complex for first exposure
- Keep JSON tags AND add table — confusing, teaches bad practice

### R3: Tag Model Design

**Decision**: Simple Tag model with id, name, note_id (FK). One note has many tags. No many-to-many (too complex for first exposure).

```python
class TagModel(Base):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    note_id: Mapped[str] = mapped_column(ForeignKey("notes.id"), nullable=False)
```

**Rationale**: Simplest possible one-to-many. Integer PK for tags (simpler than UUID). ForeignKey to notes.id. No association table needed.

### R4: Test Strategy with Alembic

**Decision**: Keep using Base.metadata.create_all in tests (SQLite), not Alembic migrations.

**Rationale**: Running Alembic migrations in tests adds complexity and requires Postgres (some migrations may use Postgres-specific features). Tests should be fast and isolated. The create_all approach is fine for tests — migrations are for production schema management.

### R5: Alembic env.py Configuration

**Decision**: Configure env.py to read DATABASE_URL from environment, import Base metadata from app.database.

**Key configuration**:
```python
# alembic/env.py
from app.database import Base
from app.models import note, tag  # ensure models are imported
target_metadata = Base.metadata
config.set_main_option("sqlalchemy.url", os.environ.get("DATABASE_URL", ""))
```

## Summary of Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Migration strategy | 2-step (initial + add tags) | Shows both create and alter migrations |
| Tag model | Simple one-to-many with integer PK | Simplest relationship example |
| Test strategy | Keep create_all in tests | Fast, no Postgres dependency for tests |
| Alembic config | Read DATABASE_URL from env | Consistent with project config pattern |
| JSON tags column | Drop in migration | Demonstrates schema evolution |
