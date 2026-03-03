# Tasks: Lecture 6 — Web Fundamentals & FastAPI + MCP Introduction

**Input**: Design documents from `/specs/009-lecture6-content/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/api.yaml, quickstart.md

**Tests**: Not requested — testing is introduced in Lecture 7. No test tasks generated.

**Organization**: Tasks are grouped by user story to enable independent implementation. US2 (FastAPI project) can be built in parallel with early US1 (notebook) sections.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: US1 = Notebook Delivery, US2 = FastAPI Project, US3 = HTTP Fundamentals Demo
- Exact file paths included in descriptions

## Path Conventions

- Lecture content: `lectures/06-web-fastapi-mcp/`
- FastAPI project: `lectures/06-web-fastapi-mcp/notes-api/`
- Visual assets: `lectures/06-web-fastapi-mcp/assets/`
- Spec documents: `specs/009-lecture6-content/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create directory structure and gather all visual/media assets needed across user stories

- [ ] T001 Create lecture directory structure: `lectures/06-web-fastapi-mcp/`, `lectures/06-web-fastapi-mcp/assets/`, `lectures/06-web-fastapi-mcp/assets/memes/`, `lectures/06-web-fastapi-mcp/notes-api/`
- [ ] T002 [P] Gather web server visual assets: download/save client-server architecture diagram and request-response lifecycle diagram to `lectures/06-web-fastapi-mcp/assets/` (source: MDN SVGs from research.md §1, or generate with matplotlib if URLs unavailable)
- [ ] T003 [P] Gather HTTP visuals: download/save HTTP request format and HTTP response format diagrams to `lectures/06-web-fastapi-mcp/assets/` (source: MDN SVGs from research.md §1, or generate with matplotlib if URLs unavailable)
- [ ] T004 [P] Gather MCP architecture visual: download/save MCP architecture diagram to `lectures/06-web-fastapi-mcp/assets/mcp-architecture.png` (source: official MCP diagram from research.md §3, or generate a custom diagram)
- [ ] T005 [P] Find and save 2 memes: 1 web/API humor meme (for introduction section) and 1 REST or MCP meme (for later section) to `lectures/06-web-fastapi-mcp/assets/memes/`

**Checkpoint**: All directories exist and visual assets are ready for embedding in the notebook.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Analyze previous lectures to ensure tone/style consistency — MUST complete before writing any notebook content

- [ ] T006 Read and analyze Lecture 5 in full detail at `lectures/05-oop-files/lecture-05.ipynb`: document tone patterns, recurring phrases, Ukrainian terminology conventions, exercise format, meme placement, emoji usage, cell ratio, and how @dataclass was introduced (needed for Pydantic bridge)
- [ ] T007 Skim Lectures 1–4 headings and key examples at `lectures/01-python-intro/lecture-01.ipynb`, `lectures/02-core-mechanics/lecture-02.ipynb`, `lectures/03-data-structures/lecture-03.ipynb`, `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: note cross-reference opportunities (JSON from L5, modules/imports from L4, functions from L3-4) and content to avoid duplicating

**Checkpoint**: Foundation ready — notebook writing can begin. Author has full awareness of prior content, tone, and terminology.

---

## Phase 3: User Story 1 - Lecture Notebook Delivery (Priority: P1) — MVP

**Goal**: Complete Jupyter notebook with all 14 sections (header through references), Ukrainian text, 5+ runnable code examples, 2 exercises, 2+ memes, 3+ diagrams, summary, and What's Next — targeting 1.5 hours of lecture content.

**Independent Test**: Open `lectures/06-web-fastapi-mcp/lecture-06.ipynb` in Jupyter, execute all cells top-to-bottom in a clean kernel — every cell runs without errors, all structural elements present.

### Implementation for User Story 1

- [ ] T008 [US1] Create notebook skeleton with header cell (lecture number, title, date), prerequisites section linking to Lectures 1–5 (OOP from L5, modules from L4), and bridge statement ("Your Contact class and JSON skills are the foundation for Pydantic models") in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 0)
- [ ] T009 [US1] Write learning objectives section with 5 measurable outcomes (web server concepts, HTTP methods/status codes, FastAPI+Pydantic+Swagger, uv+ruff+black, MCP concepts) in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 1)
- [ ] T010 [US1] Write web server basics section: client/server architecture, request-response cycle, ports analogy (IP=building, port=apartment), localhost:8000 explanation — embed 2 visual diagrams from `lectures/06-web-fastapi-mcp/assets/` — include first meme in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 2, FR-002, FR-020)
- [ ] T011 [US1] Write HTTP essentials section: methods table (GET/POST/PUT/PATCH/DELETE with CRUD/idempotent/safe columns), status codes table (2xx/4xx/5xx with key codes), request/response anatomy, JSON as data format, path vs query params, quick curl usage demo — embed HTTP request/response format visuals in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 3, FR-003, FR-020)
- [ ] T012 [US1] Write REST essentials section: resources as nouns, CRUD-to-HTTP mapping table, idempotency deep-dive (PUT/DELETE idempotent vs POST not), consistent error payload shape `{detail, error_code}`, good vs bad error response examples (✅/❌) in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 5, FR-005)
- [ ] T013 [US1] Write FastAPI basics section: minimal app creation, @app.get/@app.post progression, path parameters, query parameters, body parameters with Pydantic model, APIRouter + include_router — all with runnable inline code cells in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 6, FR-006)
- [ ] T014 [US1] Write Pydantic schemas section: BaseModel (bridge from @dataclass — "dataclass on steroids"), request vs response models, field validation (types, min/max_length, defaults), auto 422 demo, HTTPException for custom errors — add Exercise 1 (BookCreate/BookResponse schema with validation + POST endpoint) with hidden solution cell in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 7, FR-007, FR-018)
- [ ] T015 [US1] Write OpenAPI/Swagger + uvicorn section: auto-generated docs at /docs, screenshot or description of Swagger UI, running with `uvicorn app.main:app --reload`, `--port` flag mention in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 8, FR-008)
- [ ] T016 [US1] Write project bootstrap section: `uv init notes-api`, `uv add fastapi uvicorn`, `uv add --dev ruff black`, project structure walk-through, create files step-by-step referencing the notes-api/ project, `ruff check .` + `black --check .` demo, final run + curl test commands — add Exercise 2 (add GET /notes/{note_id} endpoint returning hardcoded data or 404) with hidden solution cell in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 9, FR-009, FR-010, FR-018). Depends on T023–T028.
- [ ] T017 [US1] Write MCP introduction section: problem statement (every AI tool needs custom integrations), "USB-C for AI" analogy, three participants table (Host/Client/Server with examples), three primitives table (Tools/Resources/Prompts with control type), keep-mcp concrete example (CRUD mapping to REST lesson, safety feature, Claude Desktop config JSON snippet — no running), why it matters bridge to Lecture 7 — embed MCP architecture diagram from `lectures/06-web-fastapi-mcp/assets/mcp-architecture.png`, include second meme in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 10, FR-011, FR-019, FR-020)
- [ ] T018 [US1] Write summary section (key takeaways with ✅ markers), What's Next section (bridge to Lecture 7: async, httpx, MCP integration, testing, quality workflow), and references section (MDN HTTP docs, FastAPI docs, Pydantic docs, MCP official docs, keep-mcp repo, uv docs, ruff docs) in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Sections 11–13, FR-022)

**Checkpoint**: Notebook has all 14 sections, Ukrainian text with bilingual terms, 5+ code examples, 2 exercises with solutions, 2+ memes, 3+ diagrams, summary, and references. All code cells execute without errors.

---

## Phase 4: User Story 2 - Runnable FastAPI Project (Priority: P2)

**Goal**: Complete, runnable FastAPI stub project under `lectures/06-web-fastapi-mcp/notes-api/` with GET /health (200), POST /notes/create (201), POST /notes/search (200), consistent error shapes, Swagger docs, passing ruff+black.

**Independent Test**: `cd lectures/06-web-fastapi-mcp/notes-api/ && uv sync && uvicorn app.main:app --reload` — hit all endpoints with curl per quickstart.md, open /docs, run `ruff check . && black --check .`.

### Implementation for User Story 2

- [ ] T019 [P] [US2] Create `pyproject.toml` with project metadata (name=notes-api, version=0.1.0, python>=3.13), dependencies (fastapi, uvicorn), and dev dependencies (ruff, black) in `lectures/06-web-fastapi-mcp/notes-api/pyproject.toml`
- [ ] T020 [P] [US2] Create common Pydantic schemas: `HealthStatus` (status, version) and `ErrorResponse` (detail, error_code) in `lectures/06-web-fastapi-mcp/notes-api/app/schemas/common.py` per data-model.md and contracts/api.yaml
- [ ] T021 [P] [US2] Create note Pydantic schemas: `NoteCreate` (title, content, tags with validation), `NoteResponse` (id, title, content, tags, created_at), `NoteSearchQuery` (query, tags, limit with min/max), `NoteSearchResult` (results, total) in `lectures/06-web-fastapi-mcp/notes-api/app/schemas/notes.py` per data-model.md and contracts/api.yaml
- [ ] T022 [P] [US2] Create `__init__.py` files for all packages: `lectures/06-web-fastapi-mcp/notes-api/app/__init__.py`, `app/routers/__init__.py`, `app/schemas/__init__.py`, `app/services/__init__.py`, `app/clients/__init__.py`
- [ ] T023 [US2] Create health router with GET /health returning 200 + HealthStatus in `lectures/06-web-fastapi-mcp/notes-api/app/routers/health.py` (depends on T020)
- [ ] T024 [US2] Create notes router with POST /notes/create (returns 201 + hardcoded NoteResponse) and POST /notes/search (returns 200 + empty NoteSearchResult) with consistent error handling via HTTPException in `lectures/06-web-fastapi-mcp/notes-api/app/routers/notes.py` (depends on T020, T021)
- [ ] T025 [US2] Create FastAPI app entry point: create app instance, include health and notes routers, add custom exception handler for consistent ErrorResponse shape on all 4xx/5xx in `lectures/06-web-fastapi-mcp/notes-api/app/main.py` (depends on T023, T024)
- [ ] T026 [US2] Run `uv sync` to install dependencies, then verify `uvicorn app.main:app --reload` starts on port 8000 without errors in `lectures/06-web-fastapi-mcp/notes-api/`
- [ ] T027 [US2] Verify all endpoints: GET /health returns 200, POST /notes/create with valid body returns 201, POST /notes/search returns 200 with empty results, invalid input returns 422 with ErrorResponse shape, /docs shows Swagger UI — test per quickstart.md curl commands
- [ ] T028 [US2] Run `ruff check .` and `black --check .` in `lectures/06-web-fastapi-mcp/notes-api/` — fix any violations until both pass with zero errors

**Checkpoint**: FastAPI project is fully functional, all endpoints respond correctly, Swagger docs are readable, and code passes linting/formatting.

---

## Phase 5: User Story 3 - HTTP Fundamentals Understanding (Priority: P3)

**Goal**: The raw http.server demo section of the notebook clearly shows a request-response cycle, explains ports, and motivates why frameworks exist.

**Independent Test**: Run the http.server demo cell in the notebook, observe request/response in browser or via curl — notebook explains each step.

### Implementation for User Story 3

- [ ] T029 [US3] Write raw http.server demo section: minimal stdlib demo (http.server.HTTPServer with custom handler), instructions to open browser/use curl, step-by-step explanation of what happens (client connects → sends request → server processes → sends response → connection closes), clear stop instructions (Ctrl+C / kernel interrupt / separate terminal approach), transition statement to FastAPI in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (Section 4, FR-004)

**Checkpoint**: http.server demo runs, students see raw HTTP cycle, and understand why frameworks exist.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final validation and integration across all user stories

- [ ] T030 Review all notebook text for Ukrainian language quality: grammar, bilingual term consistency (English term in parentheses on first use), matching Lecture 5 tone patterns per research.md §6 in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (FR-023)
- [ ] T031 Verify notebook meets all constitution content requirements: count code examples (need 5+ excluding project), count exercises (need 2+ with solutions), count memes (need 2+), count diagrams (need 3+), verify duration estimate (~110 min target), verify emoji usage is sparse (1-2 per section max) in `lectures/06-web-fastapi-mcp/lecture-06.ipynb` (FR-017 through FR-020, FR-025)
- [ ] T032 Run full notebook top-to-bottom in a clean Python 3.13+ kernel: restart kernel, run all cells sequentially, fix any execution errors in `lectures/06-web-fastapi-mcp/lecture-06.ipynb`
- [ ] T033 [P] Verify all visual assets render correctly in notebook: check that all embedded images (diagrams, memes, MCP architecture) display properly — fix broken paths or missing files in `lectures/06-web-fastapi-mcp/lecture-06.ipynb`
- [ ] T034 [P] Update README.md with Lecture 6 entry: add "Лекція 6: Веб-основи та FastAPI: API Skeleton + MCP Introduction" with topic bullet list matching constitution, following existing README format in `README.md`
- [ ] T035 Run quickstart.md full verification checklist: execute all steps from `specs/009-lecture6-content/quickstart.md` in a clean environment — notebook opens, uv sync works, uvicorn starts, all endpoints respond correctly, /docs loads, ruff+black pass

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: No hard dependency on Phase 1, but assets should be ready before notebook writing
- **US1 Notebook (Phase 3)**: Depends on Phase 2 (lecture analysis) completion. T016 (project bootstrap section) depends on Phase 4 (US2) being complete
- **US2 FastAPI Project (Phase 4)**: Can start in parallel with Phase 2 and early Phase 3 tasks (T008–T012). No dependency on notebook content
- **US3 http.server Demo (Phase 5)**: Can start after Phase 2. No dependency on US1 or US2
- **Polish (Phase 6)**: Depends on all user stories being complete

### User Story Dependencies

- **US1 (P1)**: Depends on Phase 2. T016 (project bootstrap section) also depends on US2 completion
- **US2 (P2)**: Can start after Phase 1 setup — fully independent of notebook content
- **US3 (P3)**: Depends on Phase 2 only — can start in parallel with US1 and US2

### Within Each User Story

- **US1**: Sections are mostly sequential (narrative flow), but T010–T012 (Sections 2, 3, 5) can be written in parallel since they cover distinct topics
- **US2**: Schemas (T020, T021) before routers (T023, T024) before main.py (T025) before verification (T026–T028)
- **US3**: Single task (T029)

### Parallel Opportunities

- Phase 1: T002, T003, T004, T005 can all run in parallel (different asset types)
- Phase 2 + Phase 4 early tasks: T006/T007 (lecture analysis) can run in parallel with T019–T022 (project scaffolding)
- Phase 3 early sections: T010, T011, T012 (Sections 2, 3, 5) can be written in parallel
- Phase 4 schemas: T020, T021, T022 can be created in parallel (different files)
- Phase 6: T033, T034 can run in parallel with each other

---

## Parallel Example: Kickoff

```text
# Phase 1 — all asset gathering in parallel:
Task T002: "Gather web server visual assets to lectures/06-web-fastapi-mcp/assets/"
Task T003: "Gather HTTP visuals to lectures/06-web-fastapi-mcp/assets/"
Task T004: "Gather MCP architecture visual to lectures/06-web-fastapi-mcp/assets/"
Task T005: "Find and save 2 memes to lectures/06-web-fastapi-mcp/assets/memes/"

# Phase 2 + Phase 4 scaffolding — in parallel:
Task T006: "Analyze Lecture 5 tone/style"
Task T019: "Create pyproject.toml"
Task T020: "Create common schemas"
Task T021: "Create note schemas"
Task T022: "Create __init__.py files"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (directories + assets)
2. Complete Phase 2: Foundational (lecture analysis)
3. Complete Phase 3: User Story 1 (full notebook — skip T016 project bootstrap section initially)
4. **STOP and VALIDATE**: All cells execute, structural elements present
5. Notebook is usable as lecture material even without the runnable project

### Incremental Delivery

1. Setup + Foundational → directories and assets ready
2. US2 (FastAPI project) + US3 (http.server demo) can proceed in parallel
3. US1 notebook sections written progressively (Sections 0–5, then 6–8, then 10–13)
4. US1 T016 (project bootstrap section) added last after US2 is verified
5. Polish phase validates everything end-to-end

### Recommended Single-Developer Flow

1. T001 → T002–T005 (parallel) → T006, T007
2. T019–T022 (parallel, project scaffolding)
3. T008, T009 (notebook header/objectives)
4. T010, T011, T029 (web basics, HTTP, http.server demo — can interleave)
5. T012 (REST essentials)
6. T013, T014, T015 (FastAPI, Pydantic, Swagger — sequential, narrative flow)
7. T023–T028 (project routers/main/verification)
8. T016 (project bootstrap notebook section — now that project is verified)
9. T017, T018 (MCP intro, summary/references)
10. T030–T035 (polish)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- No test tasks generated — testing is not requested for this feature (introduced in Lecture 7)
- US3 is a single-task story (T029) because the http.server demo is one focused notebook section
- T016 has a cross-story dependency: it references the US2 FastAPI project files, so US2 must be at least partially complete before T016 is written
- All Ukrainian text must follow bilingual convention: **Ukrainian term** (English term) on first use
- Commit after each completed section or logical group of files
