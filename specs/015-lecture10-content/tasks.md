# Tasks: Lecture 10 — Migrations, Relationships & Data Integrity

**Input**: Design documents from `/specs/015-lecture10-content/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/api.yaml, quickstart.md

**Tests**: Not explicitly requested — test updates included as part of story implementation.

**Organization**: Sequential: setup → Alembic + Tag model → endpoint updates → notebook. Project changes first, notebook second (notebook references real code).

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Dependencies & Alembic Init)

**Purpose**: Add Alembic dependency and initialize migration infrastructure.

- [x] T001 Add alembic to dependencies in `project/notes-api/pyproject.toml` and run `uv sync`
- [x] T002 Create lecture directory structure: `lectures/10-migrations-relationships/` and `lectures/10-migrations-relationships/assets/memes/`

**Checkpoint**: Alembic is installable, lecture directory exists.

---

## Phase 2: Foundational (Alembic Configuration & Initial Migration)

**Purpose**: Configure Alembic and create initial migration for existing Note model. MUST complete before adding relationships.

- [x] T003 Initialize Alembic in `project/notes-api/` — run `alembic init alembic` to create alembic.ini and alembic/ directory
- [x] T004 Configure `project/notes-api/alembic/env.py` — import Base from app.database and all models from app.models, set target_metadata = Base.metadata, read DATABASE_URL from os.environ (fallback to alembic.ini setting)
- [x] T005 Update `project/notes-api/alembic.ini` — set sqlalchemy.url placeholder (actual URL comes from env.py via environment variable)
- [x] T006 Update `project/notes-api/app/models/__init__.py` — import NoteModel so Alembic autogenerate can detect it
- [x] T007 Create initial migration in `project/notes-api/alembic/versions/` — generate migration for existing Note table (with JSON tags column as-is from L9). Use descriptive message like "initial notes table"
- [x] T008 Update `project/notes-api/app/main.py` — remove `Base.metadata.create_all(bind=engine)` from lifespan. Migrations replace create_all

**Checkpoint**: `alembic upgrade head` creates the notes table. create_all is gone from app startup.

---

## Phase 3: User Story 2 — Project Extension with Relationships & Migrations (Priority: P1)

**Goal**: Add Tag model with FK to Note, generate migration, update all layers to handle tags as related entities instead of JSON column.

**Independent Test**: Create a note with tags via API, verify tags are stored in separate table, delete note verifies cascade.

### Implementation for User Story 2

- [x] T009 [P] [US2] Create Tag model at `project/notes-api/app/models/tag.py` — TagModel with columns: id (Integer, PK, autoincrement), name (String 50, not null), note_id (String 36, ForeignKey "notes.id", not null). Add relationship back_populates to NoteModel
- [x] T010 [US2] Update `project/notes-api/app/models/note.py` — remove JSON tags column, add relationship to TagModel: `tags = relationship("TagModel", back_populates="note", cascade="all, delete-orphan")`
- [x] T011 [US2] Update `project/notes-api/app/models/__init__.py` — import TagModel alongside NoteModel
- [x] T012 [US2] Generate migration for Tag table in `project/notes-api/alembic/versions/` — autogenerate migration that creates tags table with FK and drops JSON tags column from notes. Use descriptive message like "add tags table"
- [x] T013 [US2] Update `project/notes-api/app/schemas/notes.py` — keep NoteCreate.tags as `list[str]` (API still accepts tag names as strings). Ensure NoteResponse.tags returns `list[str]`. Add TagResponse schema (id, name) if needed for detailed views
- [x] T014 [US2] Update `project/notes-api/app/repositories/notes.py` — modify create_note to create TagModel instances from tag name strings. Modify search_notes to handle tag filtering via JOIN instead of JSON. Ensure get_note_by_id eagerly loads tags. Delete cascade handled by relationship config
- [x] T015 [US2] Update `project/notes-api/app/services/notes.py` — modify model-to-schema conversion: extract tag names from note.tags relationship (list of TagModel → list of str). Ensure create_note passes tag strings to repository
- [x] T016 [US2] Update `project/notes-api/app/routers/notes.py` — minimal changes if any (router should remain clean, changes are in service/repository)
- [x] T017 [US2] Update `project/notes-api/tests/conftest.py` — ensure Base.metadata.create_all includes TagModel (import app.models.tag). Keep SQLite test DB approach
- [x] T018 [US2] Update `project/notes-api/tests/test_notes.py` — update tests: verify create with tags returns tag names in response, verify get returns tags, verify delete cascades tags, verify search by tag works
- [x] T019 [US2] Run `make check` in `project/notes-api/` — verify ruff, black, and pytest all pass. Fix any issues

**Checkpoint**: Tags stored in separate table via FK. All CRUD works with relationship. Tests pass.

---

## Phase 4: User Story 3 — DB Design & Debugging Skills (Priority: P2)

**Goal**: Content-only — DB design principles and psql commands are taught in the notebook, no project code changes needed.

**Independent Test**: Notebook sections on indexes, constraints, and psql are present and clear.

### Implementation for User Story 3

- [x] T020 [US3] Prepare psql examples — verify that `docker compose exec db psql -U notes -d notes_db` works, document the commands (\dt, \d notes, \d tags, SELECT with JOIN) that will be shown in the notebook

**Checkpoint**: psql commands verified, ready for notebook content.

---

## Phase 5: User Story 1 — Lecture Notebook (Priority: P1)

**Goal**: Create the lecture notebook teaching migrations, relationships, DB design, testing, and psql debugging. All examples reference actual project files.

**Independent Test**: Open notebook, all sections present, examples match real code, 2+ exercises, 2+ memes, 1+ diagram.

**Depends on**: Phases 2-4 (project must be complete so notebook references real code).

### Implementation for User Story 1

- [x] T021 [US1] Create notebook skeleton at `lectures/10-migrations-relationships/lecture-10.ipynb` — header (Лекція 10, title, prerequisites referencing L9), learning objectives (5 outcomes: migrations, relationships, DB design, testing, psql). Ukrainian text
- [x] T022 [US1] Write Section 1: Вступ — why migrations? Show the problem: "you changed your model but the DB has real data — what now?" Show that create_all drops and recreates (data loss!). Motivate Alembic. Ukrainian text
- [x] T023 [US1] Write Section 2: Alembic крок за кроком — show the full workflow: init → revision --autogenerate → upgrade head. Show actual alembic.ini and env.py from project. Explain downgrade briefly. Show migration file contents. Ukrainian text, code cells with actual commands
- [x] T024 [US1] Write Exercise 1 — students verify the initial migration: run `alembic upgrade head`, connect with psql, check table structure with \dt and \d notes. Include starter commands and expected output. Ukrainian text
- [x] T025 [US1] Write Section 3: Зв'язки між таблицями — explain one-to-many with ER diagram (ASCII art: Note ---< Tag). Show TagModel code, ForeignKey, relationship(), cascade. Side-by-side: JSON tags (old) vs FK tags (new). Show actual model files. Ukrainian text
- [x] T026 [US1] Write Section 4: Міграція для зв'язку — show how to generate and apply the second migration. Show the migration file content. Explain what autogenerate detected. Ukrainian text
- [x] T027 [US1] Write Section 5: Оновлення коду — show updated repository (create tags as related objects), service (convert TagModel → string), schemas. Show diffs or before/after. Ukrainian text
- [x] T028 [US1] Write Exercise 2 — students add a unique constraint on Tag(name, note_id) or add an index on notes.title. Generate a migration for it. Ukrainian text
- [x] T029 [US1] Write Section 6: Принципи проєктування БД — indexes (when, why, trade-offs), constraints (unique, not null, FK), "think about queries before designing tables". Brief, practical. Ukrainian text
- [x] T030 [US1] Write Section 7: Тестування — show updated conftest.py and test examples with relationship. Contrast with L7 in-memory approach. Ukrainian text
- [x] T031 [US1] Write Section 8: psql діагностика — show connection command, \dt, \d notes, \d tags, simple SELECT with JOIN. Brief practical toolkit. Ukrainian text
- [x] T032 [US1] Write Summary, What's Next, References — summary (5-6 bullets + meme), What's Next (L11: pandas analytics), references (Alembic docs, SQLAlchemy relationships). Ukrainian text
- [x] T033 [US1] Verify notebook content minimums — 5+ code examples, 2 exercises with solutions, 2 memes (use http.cat or similar verified URLs), 1+ ER diagram, no time estimates, Ukrainian text. Fix gaps

**Checkpoint**: Notebook complete, references real project code.

---

## Phase 6: Polish & Cross-Cutting Concerns

- [x] T034 [P] Verify all project code in `project/notes-api/` — ruff + black + pytest pass
- [x] T035 [P] Verify notebook cross-references in `lectures/10-migrations-relationships/lecture-10.ipynb` — prerequisites reference L9, What's Next references L11, no broken paths
- [x] T036 Run quickstart.md validation — execute verification steps from `specs/015-lecture10-content/quickstart.md`

**Checkpoint**: Everything verified end-to-end.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies
- **Phase 2 (Alembic)**: Depends on Phase 1
- **Phase 3 (US2 - Relationships)**: Depends on Phase 2
- **Phase 4 (US3 - DB Design)**: No code dependencies, can overlap with Phase 3
- **Phase 5 (US1 - Notebook)**: Depends on Phases 2-4
- **Phase 6 (Polish)**: Depends on all previous

### Parallel Opportunities

- T009 (Tag model) can run parallel with other model work
- T034, T035 can run in parallel (different targets)

---

## Implementation Strategy

### MVP First (Phases 1-3)

1. Setup + Alembic init + initial migration
2. Add Tag model + migration + update all layers
3. Tests pass — MVP complete

### Full Delivery

1. Phases 1-3: Project changes (~2 hours)
2. Phase 4: Verify psql (~15 min)
3. Phase 5: Write notebook (~2-3 hours)
4. Phase 6: Polish (~15 min)

**Estimated total**: ~5 hours

---

## Notes

- Tags move from JSON column to separate table — this is a breaking change by design (demonstrates migrations)
- Alembic migrations are for production; tests keep using create_all (simpler)
- Tag model uses integer PK (simpler than UUID)
- No time estimates in notebook content (constitution v1.5.1)
- Ukrainian text, English only for specific technical terms
