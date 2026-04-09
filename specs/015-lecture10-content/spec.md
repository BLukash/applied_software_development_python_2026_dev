# Feature Specification: Lecture 10 — Migrations, Relationships & Data Integrity

**Feature Branch**: `015-lecture10-content`
**Created**: 2026-04-02
**Status**: Draft
**Input**: User description: "Implement Lecture 10 as per constitution"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Lecture Notebook Delivery (Priority: P1)

A student opens the Lecture 10 Jupyter notebook and follows along during a 1.5-hour session. Building on the notes-api project from L9 (which has Docker, PostgreSQL, SQLAlchemy models, CRUD endpoints, and a repository layer), the student learns why database migrations matter, walks through Alembic once end-to-end, adds a relationship (e.g., Tag or User linked to Notes), applies DB design principles, learns to test with a real database, and picks up basic Postgres debugging commands. All examples extend the existing notes-api project.

**Why this priority**: The notebook is the primary deliverable. It completes the database story arc (L9 set up persistence, L10 adds schema evolution and relationships).

**Independent Test**: Open the notebook in Jupyter, verify all sections are present, examples reference real notes-api files, exercises are clear, and content follows the established Ukrainian-language style.

**Acceptance Scenarios**:

1. **Given** a student who completed L9, **When** they open the L10 notebook, **Then** they see prerequisites referencing L9 (Docker, PostgreSQL, SQLAlchemy, repository layer) and 5 learning objectives.
2. **Given** a student reading the migrations section, **When** they finish, **Then** they understand the schema evolution problem and can follow an Alembic init → revision → upgrade workflow.
3. **Given** a student reading the relationships section, **When** they finish, **Then** they understand one-to-many relationships, ForeignKey, and relationship() in the context of the notes-api project.
4. **Given** a student reading the testing section, **When** they finish, **Then** they can write test fixtures that create and teardown a test database, contrasting with L7's in-memory approach.

---

### User Story 2 - Project Extension with Relationships & Migrations (Priority: P1)

A student follows the notebook to extend the notes-api project. They initialize Alembic, generate at least one migration for the existing Note model, add a new entity (e.g., Tag with a one-to-many relationship to Notes), generate a migration for the relationship, and update tests to cover the new entity. After running migrations, the database schema matches the models without using create_all.

**Why this priority**: Equal to Story 1 — the project increment is how students verify they understood the concepts.

**Independent Test**: Run `alembic upgrade head`, verify the schema is correct, create a note with tags through the API, query related data.

**Acceptance Scenarios**:

1. **Given** the L9 notes-api project, **When** the student runs `alembic init`, **Then** an alembic/ directory and alembic.ini are created.
2. **Given** Alembic is initialized, **When** the student runs `alembic revision --autogenerate`, **Then** a migration file is generated reflecting the current models.
3. **Given** a migration exists, **When** the student runs `alembic upgrade head`, **Then** the database schema matches the models.
4. **Given** the student adds a new Tag model with a ForeignKey to Note, **When** they generate and apply a migration, **Then** the tags table is created with the correct foreign key constraint.
5. **Given** the relationship is set up, **When** the student creates a note and adds tags through the API, **Then** the related data is persisted and queryable.
6. **Given** the updated project, **When** `make check` is run, **Then** ruff, black, and pytest all pass.

---

### User Story 3 - DB Design & Debugging Skills (Priority: P2)

A student learns practical database design principles (indexes, constraints, "think about queries before designing tables") and picks up basic Postgres debugging commands (psql, \dt, \d). These are "professional toolkit" skills that complement the ORM knowledge from L9.

**Why this priority**: Important for professional development but secondary to getting migrations and relationships working.

**Independent Test**: Student can connect to Postgres with psql and inspect table structure.

**Acceptance Scenarios**:

1. **Given** the notebook, **When** a student reads the DB design section, **Then** they understand when to add indexes and what constraints protect data integrity.
2. **Given** the notebook, **When** a student reads the psql section, **Then** they can connect to the Postgres container and run \dt, \d notes to inspect schema.

---

### Edge Cases

- What happens when Alembic autogenerate misses a change? The notebook MUST mention that autogenerate is not perfect and manual review of migrations is always needed.
- What happens when a migration fails halfway? The notebook MUST briefly explain downgrade and how to recover.
- What happens when the student runs create_all AND Alembic? The notebook MUST explain that migrations replace create_all — they should not be used together in production.
- What happens when a foreign key constraint is violated? The notebook MUST show the error and how to handle it gracefully.

## Requirements *(mandatory)*

### Functional Requirements

**Notebook Content:**

- **FR-001**: The notebook MUST contain learning objectives covering: schema evolution, migrations, relationships, DB design principles, and database testing
- **FR-002**: The notebook MUST include a "Why Migrations" section explaining the schema evolution problem — what happens when you change a model but the database is already deployed with data
- **FR-003**: The notebook MUST include an Alembic walkthrough: init, revision --autogenerate, upgrade/downgrade — shown ONCE end-to-end, not drilled deep. MUST explain that Alembic replaces create_all for schema management
- **FR-004**: The notebook MUST include a relationships section showing one-to-many (e.g., Tag → Note or User → Notes) with ForeignKey and relationship(). This doubles as a migration exercise
- **FR-005**: The notebook MUST include a DB design principles section covering: indexes (when and why to add them), constraints (unique, not null, foreign key), and the principle "think about queries before designing tables"
- **FR-006**: The notebook MUST include a testing section showing test fixtures that create/teardown a test database. MUST contrast with L7's in-memory TestClient approach and build on L9's conftest.py pattern
- **FR-007**: The notebook MUST include a brief Postgres debugging toolkit: psql connection command, \dt (list tables), \d table_name (describe table), basic SELECT queries
- **FR-008**: The notebook MUST include prerequisites referencing L9 (Docker, PostgreSQL, SQLAlchemy, repository layer)
- **FR-009**: The notebook MUST end with Summary and "What's Next" previewing L11 (pandas analytics from DB exports)
- **FR-010**: All notebook examples MUST reference actual notes-api project files — students see changes to their existing project
- **FR-011**: The notebook MUST contain at least 5 runnable code examples
- **FR-012**: The notebook MUST contain at least 2 practical exercises with solutions
- **FR-013**: The notebook MUST contain at least 2 memes or visual humor elements
- **FR-014**: The notebook MUST contain at least 1 diagram (e.g., entity-relationship diagram for Note-Tag)
- **FR-015**: All explanatory text MUST be in Ukrainian with English technical terms in parentheses ONLY for specific terms
- **FR-016**: The notebook MUST NOT include per-section time estimates
- **FR-017**: The notebook duration MUST target 1.5 hours of lecture content

**Project Changes:**

- **FR-018**: The project MUST have Alembic initialized (alembic.ini + alembic/ directory with env.py configured for the project's models)
- **FR-019**: The project MUST have at least one Alembic migration for the existing Note model
- **FR-020**: The project MUST have a new entity with a one-to-many relationship to Note (e.g., Tag model with foreign key to notes table)
- **FR-021**: The project MUST have a migration for the new relationship
- **FR-022**: The notes-api main.py MUST be updated to remove create_all (replaced by Alembic migrations)
- **FR-023**: The repository layer MUST be extended to handle the new entity (create, query with related data)
- **FR-024**: Tests MUST be updated to cover the new relationship and migration-based schema setup
- **FR-025**: The project MUST pass `make check` (ruff + black + pytest) after all changes
- **FR-026**: Alembic MUST be added to project dependencies
- **FR-027**: The docker-compose.yml MAY be updated if needed for Alembic migration commands

### Key Entities

- **Note**: Existing entity from L9 — now gains a relationship to tags
- **Tag**: New entity — has id, name, note_id (foreign key to notes). Represents a one-to-many relationship where one note can have multiple tags
- **Migration**: An Alembic revision file that describes a schema change — has revision ID, upgrade function, downgrade function

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can explain why migrations are needed instead of create_all — verified by discussion or reflection exercise
- **SC-002**: Students can run the full Alembic workflow (init → revision → upgrade) within 10 minutes of reading the instructions
- **SC-003**: Students can add a new model with a relationship and generate a migration for it — verified by the exercise
- **SC-004**: Students can connect to PostgreSQL with psql and inspect table structure — verified by running the debugging commands
- **SC-005**: The notebook contains all required structural elements: learning objectives, 5+ code examples, 2+ exercises, 2+ memes, 1+ diagram, summary, references — verified by checklist
- **SC-006**: All project code passes linting, formatting, and test checks — verified by `make check`

### Assumptions

- Students have completed L9 and have a working notes-api project with Docker, PostgreSQL, SQLAlchemy models, CRUD endpoints, and repository layer
- Docker is installed and Docker Desktop is running
- The notes-api project uses synchronous SQLAlchemy (not async)
- Tags are currently stored as a JSON column in the Note model (from L9) — the relationship refactoring moves them to a separate table with a foreign key
- Alembic is added as a project dependency alongside existing SQLAlchemy
- The Tag entity is chosen as the simplest one-to-many example — no need for user authentication or complex authorization
