# Research: Lecture 9 — Docker + PostgreSQL + SQLAlchemy: Real Persistence

**Feature**: 014-lecture9-content
**Date**: 2026-04-02

## Research Tasks

### R1: SQLAlchemy Session Pattern for FastAPI

**Task**: Determine the best pattern for managing SQLAlchemy sessions in FastAPI endpoints.

**Decision**: Use FastAPI dependency injection with `yield` for session lifecycle.

**Rationale**: The `Depends(get_db)` pattern is the standard FastAPI approach. It creates a session per request, yields it, and closes/rolls back after the request completes. This is simpler than async sessions and matches the synchronous teaching approach.

```python
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

**Alternatives considered**:
- Async sessions (asyncpg + async SQLAlchemy) — too complex for first DB lecture, save for advanced course
- Global session — thread-safety issues, bad practice
- Manual session management in each endpoint — duplicated boilerplate

### R2: PostgreSQL Tags Column Type

**Task**: Determine how to store note tags (list of strings) in PostgreSQL.

**Decision**: Use `ARRAY(String)` — PostgreSQL native array type.

**Rationale**: PostgreSQL has native array support. `ARRAY(String)` is simple, queryable with `any()` operator, and maps directly to Python `list[str]`. Students already know tags as `list[str]` from the Pydantic schema — minimal cognitive jump.

**Alternatives considered**:
- JSON column — more flexible but harder to query, overkill for simple string lists
- Separate tags table with many-to-many — correct relational design but too complex for L9 (save for L10 relationships)
- Comma-separated string — anti-pattern, not queryable

### R3: Docker Compose Configuration

**Task**: Determine minimal docker-compose.yml for FastAPI + PostgreSQL.

**Decision**: Two services (db + app), shared network, named volume for data persistence.

```yaml
services:
  db:
    image: postgres:16
    environment:
      POSTGRES_USER: notes
      POSTGRES_PASSWORD: notes
      POSTGRES_DB: notes_db
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U notes"]
      interval: 5s
      timeout: 5s
      retries: 5

  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://notes:notes@db:5432/notes_db
    depends_on:
      db:
        condition: service_healthy

volumes:
  postgres_data:
```

**Rationale**: Minimal config that works. Healthcheck ensures the app doesn't start before Postgres is ready. Named volume preserves data across restarts. Port 5432 exposed for direct debugging with psql.

### R4: Dockerfile for FastAPI App

**Task**: Determine minimal Dockerfile for the notes-api.

**Decision**: Multi-stage not needed for educational context. Single stage with uv.

```dockerfile
FROM python:3.13-slim
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install uv && uv sync --frozen
COPY . .
CMD ["uv", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

**Rationale**: Students use `uv` for dependency management (introduced in L6). Keeping the same tool in Docker reduces confusion. `--host 0.0.0.0` is needed inside containers.

**Alternatives considered**:
- pip install from requirements.txt — students don't use pip in this course, they use uv
- Multi-stage build — unnecessary complexity for educational project
- Poetry — not used in this course

### R5: Test Database Strategy

**Task**: Determine how to test database-backed endpoints without polluting the main DB.

**Decision**: Use a separate test database created/dropped by pytest fixtures in conftest.py.

**Rationale**: Students already know pytest fixtures from L7. A test database is realistic (mirrors production setup) and avoids mocking the entire DB layer. The conftest.py creates a test engine, runs create_all, yields a session, then drops tables.

```python
# tests/conftest.py
@pytest.fixture
def db_session():
    engine = create_engine("sqlite:///./test.db")
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()
    Base.metadata.drop_all(bind=engine)
```

Using SQLite for tests is simpler than spinning up a test Postgres container. Students learn the concept of test isolation; production uses Postgres.

**Alternatives considered**:
- Test Postgres container — correct but slow and complex for students
- Mock all DB calls — loses the value of integration testing (taught in L7)
- Shared Postgres with transaction rollback — too advanced for first exposure

### R6: Repository vs Direct Session Usage

**Task**: Determine how much layering to introduce.

**Decision**: Thin repository (functions, not classes) + simple service module.

**Rationale**: Students need to see separation but shouldn't be overwhelmed by abstraction. Repository as plain functions (not a class with generics) is the simplest entry point. Service module is optional glue — it can start as a passthrough and grow later.

```python
# app/repositories/notes.py
def create_note(db: Session, note_data: NoteCreate) -> NoteModel:
    note = NoteModel(**note_data.model_dump())
    db.add(note)
    db.commit()
    db.refresh(note)
    return note
```

**Alternatives considered**:
- Repository class with generic CRUD — overengineered for first exposure
- No repository, SQL in routers — works but teaches bad habits
- Full clean architecture with interfaces — way too much abstraction

## Summary of Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Session management | FastAPI `Depends(get_db)` with yield | Standard pattern, request-scoped |
| Tags storage | PostgreSQL `ARRAY(String)` | Native, queryable, maps to Python list |
| Docker setup | Two services + healthcheck + named volume | Minimal, reliable, persistent |
| Dockerfile | Single stage with uv | Matches course tooling |
| Test strategy | SQLite test DB in conftest.py | Simple, fast, teaches fixtures |
| Layering | Functions-based repository + thin service | Minimal but teaches separation |
