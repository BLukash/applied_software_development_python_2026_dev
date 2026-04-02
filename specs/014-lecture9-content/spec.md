# Feature Specification: Lecture 9 — Docker + PostgreSQL + SQLAlchemy: Real Persistence

**Feature Branch**: `014-lecture9-content`
**Created**: 2026-04-02
**Status**: Draft
**Input**: User description: "Implement Lecture 9, make sure to follow notes project together with the lecture content and show examples on top of it."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Lecture Notebook Delivery (Priority: P1)

A student opens the Lecture 9 Jupyter notebook and follows along during a 1.5-hour session. The lecture takes the existing notes-api project (stub endpoints from L6, async/testing from L7) and transforms it into a real application with persistent storage. The student learns Docker as a practical tool (not a deep topic), sets up PostgreSQL via docker compose, connects the app to the database, defines SQLAlchemy models, replaces stub endpoints with real CRUD operations, and introduces a basic repository layer. All examples build directly on the notes-api project files students already know. By the end, `docker compose up` starts both the database and the API, and endpoints persist real data.

**Why this priority**: The notebook is the primary deliverable — it bridges the gap from "toy stubs" to "real application" which is the most impactful moment in the course.

**Independent Test**: Open the notebook in Jupyter, read all cells top-to-bottom, verify all explanatory cells are clear and all code examples are consistent with the notes-api project structure.

**Acceptance Scenarios**:

1. **Given** a student who completed Lectures 1-8, **When** they open the Lecture 9 notebook, **Then** they see prerequisites referencing L6 (FastAPI project), L7 (async, config, testing), and learning objectives covering Docker, PostgreSQL, SQLAlchemy, and CRUD persistence.
2. **Given** a student reading the notebook, **When** they follow code examples, **Then** every example references real files from the notes-api project (app/main.py, app/routers/notes.py, app/schemas/notes.py, etc.) and shows the actual changes being made.
3. **Given** a student reading the Docker section, **When** they finish, **Then** they understand enough to run `docker compose up` — without needing to understand Docker internals like image layers or volume drivers.
4. **Given** a student reading the SQLAlchemy section, **When** they finish, **Then** they can define a model class that maps to a database table and perform basic CRUD operations through a session.

---

### User Story 2 - Runnable Project with Real Persistence (Priority: P1)

A student follows the notebook instructions to extend the notes-api project with real database persistence. They add a docker-compose.yml (PostgreSQL + FastAPI), a Dockerfile for the app, SQLAlchemy models, a database connection module, and a repository layer. They replace the stub endpoints with real CRUD operations. After running `docker compose up`, they can create notes via POST /notes/create and see them persisted — GET /notes/{id} returns the same note after restart. Tests still pass using a test database fixture.

**Why this priority**: Equal to Story 1 — the runnable project is what students take away. Without working persistence, the lecture is theoretical.

**Independent Test**: Run `docker compose up`, hit each endpoint with curl or Swagger, restart the containers, verify data persists.

**Acceptance Scenarios**:

1. **Given** a student with Docker installed, **When** they run `docker compose up` in the notes-api directory, **Then** PostgreSQL starts on port 5432 and the FastAPI app starts on port 8000, both healthy.
2. **Given** the stack is running, **When** the student sends POST /notes/create with valid data, **Then** they receive a 201 response and the note is stored in PostgreSQL.
3. **Given** a note was created, **When** the student sends GET /notes/{note_id}, **Then** they receive the note with correct data.
4. **Given** a note was created, **When** the student sends POST /notes/search with a matching query, **Then** the search results include that note.
5. **Given** a note exists, **When** the student sends DELETE /notes/{note_id}, **Then** they receive 204 and the note is removed from the database.
6. **Given** a non-existent note ID, **When** the student sends GET /notes/{non_existent_id}, **Then** they receive a 404 with consistent error payload.
7. **Given** the stack is running, **When** the student opens /docs, **Then** Swagger UI works and all endpoints are documented.
8. **Given** the project code, **When** `make check` is run, **Then** ruff, black, and pytest all pass.
9. **Given** the student restarts the containers, **When** they query previously created notes, **Then** the data is still there (persistence verified).

---

### User Story 3 - Repository Layer Understanding (Priority: P2)

A student reads the layering section and understands why ORM models should not be returned directly from API endpoints. They see a repository.py file introduced as a thin database access wrapper, and understand the router → service → repository flow. The existing notes.py router is refactored to call a service/repository instead of containing inline logic.

**Why this priority**: The layering concept is important for maintainability but is secondary to getting persistence working. Students can build working apps without it, but professionals need this separation.

**Independent Test**: Review the repository.py and service layer code, verify that router files contain no direct database access.

**Acceptance Scenarios**:

1. **Given** the updated project, **When** a student reads app/routers/notes.py, **Then** it contains no SQLAlchemy imports or session usage — it delegates to a service or repository.
2. **Given** the updated project, **When** a student reads the repository module, **Then** they see functions for create, get_by_id, search, and delete that accept a session and return model instances.
3. **Given** the notebook, **When** a student reads the layering section, **Then** they see a clear diagram or explanation of router → service → repository → database flow and why "don't leak ORM models into API schemas" matters.

---

### Edge Cases

- What happens when Docker is not installed? The notebook MUST include a prerequisites check and link to Docker installation instructions.
- What happens when port 5432 or 8000 is already in use? The notebook MUST mention how to change ports in docker-compose.yml and .env.
- What happens when the database container is not ready when the app starts? The docker-compose.yml MUST include a healthcheck or the app MUST handle connection retries.
- What happens when a student creates a note with duplicate data? The system MUST handle it gracefully (allow duplicates or return appropriate error).
- What happens when the database volume is deleted? Students MUST understand that data is lost and how to recreate it.

## Requirements *(mandatory)*

### Functional Requirements

**Notebook Content:**

- **FR-001**: The notebook MUST contain learning objectives covering: containerized development, database connection, ORM basics, CRUD persistence, and layered architecture
- **FR-002**: The notebook MUST include a Docker section treating Docker as a practical tool — explain just enough to run `docker compose up` (what is a container, what is compose, how to read docker-compose.yml), NOT a deep dive into images/layers/volumes/networking
- **FR-003**: The notebook MUST show the complete docker-compose.yml file with PostgreSQL and FastAPI services, explaining each key field
- **FR-004**: The notebook MUST show a Dockerfile for the notes-api application, explaining each instruction
- **FR-005**: The notebook MUST include a connection setup section showing how to configure the database URL via .env and pydantic-settings (building on L7's config pattern)
- **FR-006**: The notebook MUST include a SQLAlchemy section covering: ORM concept (class maps to table), defining a Note model, creating Engine and Session, Base.metadata.create_all
- **FR-007**: The notebook MUST show CRUD operations with SQLAlchemy: create (session.add + commit), read (session.get or select), search (select with filters), delete (session.delete + commit)
- **FR-008**: The notebook MUST show error handling patterns: not found → 404 HTTPException, unique constraint violations → 409, general database errors → 500
- **FR-009**: The notebook MUST include a layering section explaining the "don't leak ORM models into API schemas" rule and introducing repository.py as a thin database access wrapper
- **FR-010**: The notebook MUST show the router → service → repository flow with a before/after comparison (stub code vs layered code)
- **FR-011**: The notebook MUST include a prerequisites section referencing L6 (FastAPI project structure), L7 (pydantic-settings, pytest), and listing Docker as a required tool
- **FR-012**: The notebook MUST end with Summary and "What's Next" previewing L10 (migrations, relationships, data integrity)
- **FR-013**: All notebook examples MUST reference actual notes-api project files (app/main.py, app/routers/notes.py, etc.) — students see changes to their existing project, not abstract examples
- **FR-014**: The notebook MUST contain at least 5 runnable code examples
- **FR-015**: The notebook MUST contain at least 2 practical exercises with solutions
- **FR-016**: The notebook MUST contain at least 2 memes or visual humor elements
- **FR-017**: The notebook MUST contain at least 1 diagram (e.g., app ↔ database architecture, layering diagram)
- **FR-018**: All explanatory text MUST be in Ukrainian with English technical terms in parentheses on first use, but ONLY for specific technical terms — NOT for obvious phrases
- **FR-019**: The notebook MUST NOT include per-section time estimates in student-facing content
- **FR-020**: The notebook duration MUST target 1.5 hours of lecture content

**Project Changes:**

- **FR-021**: The notes-api project MUST have a docker-compose.yml defining PostgreSQL and FastAPI services with a shared network
- **FR-022**: The notes-api project MUST have a Dockerfile for the FastAPI application
- **FR-023**: The project MUST have a database module (e.g., app/database.py) with engine creation, session factory, and Base declarative class
- **FR-024**: The project MUST have a SQLAlchemy model for Note (e.g., app/models/note.py) mapping to a notes table with columns: id (UUID primary key), title, content, tags, created_at
- **FR-025**: The project MUST have a repository module (e.g., app/repositories/notes.py) with functions: create_note, get_note_by_id, search_notes, delete_note
- **FR-026**: The existing stub endpoints in app/routers/notes.py MUST be replaced with real implementations that persist to PostgreSQL via the repository layer
- **FR-027**: A GET /notes/{note_id} endpoint MUST be added (or confirmed present) returning 200 with note data or 404
- **FR-028**: The DELETE /notes/{note_id} endpoint MUST be wired to actually delete from the database
- **FR-029**: The app/config.py Settings class MUST be extended with database_url field loaded from .env
- **FR-030**: The .env.example MUST be updated with DATABASE_URL example
- **FR-031**: The project MUST pass `make check` (ruff + black + pytest) after all changes
- **FR-032**: Existing tests MUST be updated to work with the new database-backed implementation (using a test database or test fixtures)
- **FR-033**: The docker-compose.yml MUST include a volume for PostgreSQL data persistence

### Key Entities

- **Note**: The central resource — has id (UUID), title (string, 1-200 chars), content (string), tags (list of strings), created_at (timestamp). Exists as both a Pydantic schema (API layer) and a SQLAlchemy model (database layer)
- **Database Session**: A connection to PostgreSQL managed by SQLAlchemy — created per request, committed on success, rolled back on error
- **Repository**: A thin abstraction over database operations — accepts a session and Note data, returns model instances. Keeps SQL out of routers

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can start the full application stack (database + API) with a single command and interact with it within 5 minutes of reading the setup instructions
- **SC-002**: Students can create a note via the API and retrieve it after restarting the application — verifying data persists across restarts
- **SC-003**: Students can explain in their own words why ORM models should not be returned directly from API endpoints — verified by discussion or written reflection
- **SC-004**: The notebook contains all required structural elements: learning objectives, at least 5 code examples, at least 2 exercises, at least 2 memes, at least 1 diagram, summary, and references — verified by checklist review
- **SC-005**: All project code passes linting, formatting, and test checks in a clean environment — verified by running `make check`
- **SC-006**: Students can add a new field to the Note model and see it reflected in the API response — demonstrating they understand the model-to-schema relationship

### Assumptions

- Students have completed Lectures 1-8 and have a working notes-api project with stub endpoints, pydantic-settings config, and pytest setup
- Students have Docker and Docker Compose installed (or the notebook includes brief installation pointers)
- The notes-api project currently lives at `project/notes-api/` in the repository
- PostgreSQL is accessed only through Docker — no local installation required
- The SQLAlchemy models use synchronous sessions (async SQLAlchemy is out of scope for this lecture)
- Tags are stored as a PostgreSQL ARRAY type or as a JSON column — the simplest approach that works
- No authentication or authorization is needed at this stage
- The instructor has Docker running and can demonstrate live if students encounter individual setup issues
