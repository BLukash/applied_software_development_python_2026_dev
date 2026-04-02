# Tasks: Lecture 9 — Docker + PostgreSQL + SQLAlchemy: Real Persistence

**Input**: Design documents from `/specs/014-lecture9-content/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/api.yaml, quickstart.md

**Tests**: Not explicitly requested — no separate test tasks. Test updates included as part of story implementation.

**Organization**: US1 (notebook) and US2 (project) are co-dependent — the notebook teaches the project changes. US3 (layering) can be woven into US2. Execution is sequential: setup → project infrastructure → CRUD implementation → notebook.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Project Infrastructure)

**Purpose**: Add Docker and database infrastructure to the notes-api project before implementing any business logic.

- [x] T001 Add sqlalchemy and psycopg2-binary to dependencies in `project/notes-api/pyproject.toml`
- [x] T002 Create Dockerfile for the notes-api application at `project/notes-api/Dockerfile` — single stage with python:3.13-slim, uv for dependency management, CMD with uvicorn on 0.0.0.0:8000
- [x] T003 Create docker-compose.yml at `project/notes-api/docker-compose.yml` — two services: db (postgres:16 with healthcheck, named volume, port 5432) and app (build from Dockerfile, port 8000, depends_on db healthy, DATABASE_URL env var)
- [x] T004 Update `.env.example` at `project/notes-api/.env.example` — add DATABASE_URL=postgresql://notes:notes@localhost:5432/notes_db
- [x] T005 Extend Settings class in `project/notes-api/app/config.py` — add database_url field (str) loaded from environment
- [x] T006 Create database module at `project/notes-api/app/database.py` — define create_engine from settings.database_url, SessionLocal factory with sessionmaker, Base declarative class, get_db generator function (yield session, close in finally)
- [x] T007 Create lecture directory structure: `lectures/09-docker-postgres-sqlalchemy/` and `lectures/09-docker-postgres-sqlalchemy/assets/memes/`

**Checkpoint**: Docker and database infrastructure files exist. `docker compose up` can start Postgres (app won't work yet — no models).

---

## Phase 2: Foundational (Models & Repository Layer)

**Purpose**: Create the SQLAlchemy model and repository that all endpoints depend on. MUST complete before endpoint implementation.

- [x] T008 [P] Create `project/notes-api/app/models/__init__.py` (empty) and `project/notes-api/app/models/note.py` — define NoteModel class mapped to "notes" table with columns: id (UUID, primary key, default uuid4), title (String 200, not null), content (Text, not null), tags (ARRAY of String, default []), created_at (DateTime with timezone, default utc_now)
- [x] T009 [P] Create `project/notes-api/app/repositories/__init__.py` (empty) and `project/notes-api/app/repositories/notes.py` — implement functions: create_note(db, note_data) → NoteModel, get_note_by_id(db, note_id) → NoteModel | None, search_notes(db, query, tags, limit) → list[NoteModel] with title/content ilike filter and optional tag filter, delete_note(db, note_id) → bool
- [x] T010 Create service layer at `project/notes-api/app/services/__init__.py` (already exists) and `project/notes-api/app/services/notes.py` — thin service wrapping repository functions, converting between Pydantic schemas and SQLAlchemy models. Functions: create_note, get_note, search_notes, delete_note. Each accepts db session + schema input, returns Pydantic response or raises HTTPException
- [x] T011 Update `project/notes-api/app/main.py` — import Base and engine from database module, add lifespan or startup event to run Base.metadata.create_all(bind=engine), register get_db dependency

**Checkpoint**: Model, repository, service, and database lifecycle are ready. Endpoints can now be wired.

---

## Phase 3: User Story 2 — Runnable Project with Real Persistence (Priority: P1)

**Goal**: Replace stub endpoints with real CRUD that persists to PostgreSQL. All endpoints work via docker compose.

**Independent Test**: Run `docker compose up`, POST a note, GET it back, restart containers, GET it again — data persists.

### Implementation for User Story 2

- [x] T012 [US2] Rewrite `project/notes-api/app/routers/notes.py` — replace all stub implementations: POST /notes/create calls service.create_note with Depends(get_db), returns 201. POST /notes/search calls service.search_notes. Add GET /notes/{note_id} calling service.get_note, returns 200 or 404. Wire DELETE /notes/{note_id} calling service.delete_note, returns 204 or 404. Router MUST NOT import sqlalchemy — only service and schemas
- [x] T013 [US2] Update `project/notes-api/app/schemas/notes.py` — verify NoteResponse.model_config has from_attributes=True (needed for ORM → Pydantic conversion). Add NoteUpdate schema if PUT endpoint is planned for exercise
- [x] T014 [US2] Create test fixtures at `project/notes-api/tests/conftest.py` — define test engine (SQLite in-memory or file), create_all/drop_all around session, override get_db dependency with test session, provide client fixture using TestClient with app dependency override
- [x] T015 [US2] Update `project/notes-api/tests/test_notes.py` — rewrite tests to use conftest fixtures: test create returns 201 with persisted data, test get by id returns 200, test get nonexistent returns 404, test search returns matching results, test delete returns 204, test delete nonexistent returns 404, test create with invalid data returns 422
- [x] T016 [US2] Update `project/notes-api/tests/test_health.py` — ensure health test still works with new app setup (may need client fixture from conftest)
- [x] T017 [US2] Run `make check` in `project/notes-api/` — verify ruff, black, and pytest all pass. Fix any issues

**Checkpoint**: All endpoints persist to database. Tests pass. `docker compose up` gives a working stack.

---

## Phase 4: User Story 3 — Repository Layer Understanding (Priority: P2)

**Goal**: Ensure clean separation — routers have no SQLAlchemy imports, repository handles all DB access.

**Independent Test**: grep for "sqlalchemy" in routers/notes.py returns 0. Repository contains all DB operations.

### Implementation for User Story 3

- [x] T018 [US3] Verify layering in `project/notes-api/app/routers/notes.py` — confirm zero sqlalchemy imports, all DB access goes through service layer. If any direct session usage leaked in during T012, refactor it out
- [x] T019 [US3] Verify `project/notes-api/app/services/notes.py` handles model-to-schema conversion — NoteModel instances from repository MUST be converted to NoteResponse before returning from service. Router receives only Pydantic objects

**Checkpoint**: Clean layering verified. Router → Service → Repository → Database.

---

## Phase 5: User Story 1 — Lecture Notebook (Priority: P1)

**Goal**: Create the lecture notebook that teaches everything built in Phases 1-4, using the actual project files as examples.

**Independent Test**: Open notebook in Jupyter, all content is clear, examples reference real project files, 2+ exercises, 2+ memes, 1+ diagram.

**Depends on**: Phases 1-4 (project must be complete so notebook references real, working code).

### Implementation for User Story 1

- [x] T020 [US1] Create notebook skeleton at `lectures/09-docker-postgres-sqlalchemy/lecture-09.ipynb` — header cell (Лекція 9, title, prerequisites referencing L6/L7/Docker), learning objectives cell (5 outcomes: containerized dev, DB connection, ORM, CRUD persistence, layering). Ukrainian text, English technical terms only for specific terms
- [x] T021 [US1] Write Section 1: Вступ — motivation cell showing current stub code from L6 vs what we'll build (real persistence). Show the "before/after" contrast. Include a meme about fake data vs real data. Ukrainian text
- [x] T022 [US1] Write Section 2: Docker як інструмент — what is a container (brief), show the actual docker-compose.yml from the project, explain each field, show Dockerfile, demonstrate `docker compose up`. NOT a Docker deep dive. Show real file contents from `project/notes-api/`. Ukrainian text
- [x] T023 [US1] Write Section 3: Підключення до бази даних — show DATABASE_URL in .env, updated config.py with database_url field, app/database.py (engine, session, Base, get_db). Build on L7's pydantic-settings knowledge. Show real file contents. Ukrainian text
- [x] T024 [US1] Write Section 4: SQLAlchemy ORM — explain ORM concept (class = table), show NoteModel from app/models/note.py side-by-side with NoteCreate Pydantic schema. Highlight differences (SQLAlchemy for DB, Pydantic for API). Show Base.metadata.create_all. Include runnable code example. Ukrainian text
- [x] T025 [US1] Write Section 5: CRUD з SQLAlchemy — show each repository function from app/repositories/notes.py: create (session.add + commit), read (session.get), search (select with filters), delete (session.delete). Runnable code examples. Ukrainian text
- [x] T026 [US1] Write Section 6: Обробка помилок — show not found → 404 pattern, mention unique constraint → 409. Show the updated router code. Ukrainian text
- [x] T027 [US1] Write Exercise 1 — students implement or verify GET /notes/{note_id} endpoint wired through the repository layer. Include starter code and hidden solution. Ukrainian text
- [x] T028 [US1] Write Section 7: Шари архітектури — "don't leak ORM models" rule, show router → service → repository diagram (inline ASCII or image), before/after comparison (stub code vs layered code). Show real app/services/notes.py. Ukrainian text. Include a diagram
- [x] T029 [US1] Write Exercise 2 — students add a PUT /notes/{note_id} endpoint or add an "updated_at" field to the model and see it through all layers. Include starter code and hidden solution. Ukrainian text
- [x] T030 [US1] Write Section 8: Тестування з базою даних — show conftest.py with test DB fixture, show updated test_notes.py. Contrast with L7's in-memory approach. Ukrainian text
- [x] T031 [US1] Write Summary, What's Next, and References sections in `lectures/09-docker-postgres-sqlalchemy/lecture-09.ipynb` — summary (5-6 bullet points), What's Next previewing L10 (migrations, relationships, data integrity), references (SQLAlchemy docs, Docker docs, FastAPI+SQLAlchemy tutorial). Include a meme. Ukrainian text
- [x] T032 [US1] Verify notebook content minimums — at least 5 runnable code examples, 2 exercises with solutions, 2 memes, 1 diagram, no per-section time estimates, Ukrainian text throughout with English only for specific technical terms. Fix any gaps

**Checkpoint**: Notebook is complete, all content references real project files, exercises work, all cells are clear.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final verification and cleanup.

- [x] T033 [P] Verify `docker compose up` works end-to-end in `project/notes-api/` — Postgres starts, app starts, all endpoints return expected responses, data persists across restart
- [x] T034 [P] Verify all cross-references in `lectures/09-docker-postgres-sqlalchemy/lecture-09.ipynb` — prerequisites reference L6/L7 correctly, What's Next references L10 correctly, no broken file path references
- [x] T035 Run full `make check` in `project/notes-api/` — final pass of ruff + black + pytest
- [x] T036 Run quickstart.md validation — execute all 10 verification steps from `specs/014-lecture9-content/quickstart.md`

**Checkpoint**: Everything works end-to-end. Project is clean, tests pass, notebook is complete.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies — start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 (needs dependencies and database module)
- **Phase 3 (US2 - Endpoints)**: Depends on Phase 2 (needs model and repository)
- **Phase 4 (US3 - Layering)**: Depends on Phase 3 (verifies layering from endpoint implementation)
- **Phase 5 (US1 - Notebook)**: Depends on Phases 3-4 (notebook references completed project)
- **Phase 6 (Polish)**: Depends on all previous phases

### Within Each Phase

- Setup: T001-T005 can run in parallel (different files), T006 depends on T005 (config)
- Foundational: T008, T009 parallel (different files), T010 depends on T009, T011 depends on T006
- US2: Sequential — T012 → T013 → T014 → T015 → T016 → T017
- US1: Sequential — sections must be written in order for narrative flow

### Parallel Opportunities

**Phase 1**: T002, T003, T004 can run in parallel
**Phase 2**: T008, T009 can run in parallel
**Phase 6**: T033, T034 can run in parallel

---

## Implementation Strategy

### MVP First (Phase 1-3)

1. Complete Phase 1: Docker + DB infrastructure
2. Complete Phase 2: Model + Repository
3. Complete Phase 3: Wire endpoints + tests
4. **STOP and VALIDATE**: `docker compose up` works, all tests pass
5. This is a working app with persistence — MVP complete

### Full Delivery

1. Phases 1-3: Project infrastructure + CRUD (~2 hours)
2. Phase 4: Verify layering (~15 min)
3. Phase 5: Write notebook (~2-3 hours)
4. Phase 6: Polish + validation (~30 min)

**Estimated total**: ~5-6 hours

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story
- All notebook text MUST be in Ukrainian with English only for specific technical terms
- No per-section time estimates in notebook (constitution v1.5.1 rule)
- Tags use PostgreSQL ARRAY(String) — test fixtures using SQLite may need JSON fallback
- Repository uses plain functions, not classes
- Commit after each phase for clean git history
