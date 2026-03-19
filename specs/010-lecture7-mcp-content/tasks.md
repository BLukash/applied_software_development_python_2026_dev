# Tasks: Lecture 7 — Python Web Server Integrations: Async, HTTPX, Testing, Practical MCP

**Input**: Design documents from `/specs/010-lecture7-mcp-content/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/, quickstart.md

**Tests**: No test tasks generated — the spec does not request TDD. Testing is a *teaching topic* within the notebook, not a development process requirement.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Notebook**: `lectures/07-integrations-async-mcp/lecture-07.ipynb`
- **Project**: `lectures/07-integrations-async-mcp/notes-api/`
- **Assets**: `lectures/07-integrations-async-mcp/assets/`
- **Specs**: `specs/010-lecture7-mcp-content/`

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create lecture directory structure, copy Lecture 6 project, prepare assets folder

- [ ] T001 Create lecture directory structure: `lectures/07-integrations-async-mcp/`, `lectures/07-integrations-async-mcp/assets/`, `lectures/07-integrations-async-mcp/assets/memes/`
- [ ] T002 Copy Lecture 6 FastAPI project from `lectures/06-web-fastapi-mcp/notes-api/` to `lectures/07-integrations-async-mcp/notes-api/` (exclude `.venv/`, `.ruff_cache/`, `uv.lock`)
- [ ] T003 Create empty notebook file `lectures/07-integrations-async-mcp/lecture-07.ipynb` with metadata (Python 3.13+ kernel)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Analyze Lecture 6 content for tone/style consistency and prepare project extensions that all notebook sections depend on

**CRITICAL**: No user story work can begin until this phase is complete

- [ ] T004 Read and analyze Lecture 6 notebook (`lectures/06-web-fastapi-mcp/lecture-06.ipynb`) in full — document tone patterns, Ukrainian phrasing style, emoji usage, cell structure, meme placement, and diagram conventions. Also briefly review Lectures 1–5 headings to ensure no content duplication
- [ ] T005 [P] Update `lectures/07-integrations-async-mcp/notes-api/pyproject.toml` — add `pydantic-settings` to dependencies and `pytest` to dev dependencies
- [ ] T006 [P] Create `lectures/07-integrations-async-mcp/notes-api/app/config.py` with pydantic-settings `Settings` class (fields: `app_name: str = "Notes API"`, `debug: bool = False`, `port: int = 8000`) loading from `.env`
- [ ] T007 [P] Create `lectures/07-integrations-async-mcp/notes-api/.env.example` with placeholder values and `lectures/07-integrations-async-mcp/notes-api/.env` with local defaults. Ensure `.env` is in `.gitignore`
- [ ] T008 Run `uv sync` in `lectures/07-integrations-async-mcp/notes-api/` to verify all dependencies install cleanly

**Checkpoint**: Project is ready with config, new dependencies, and clean environment. Notebook content can now be written.

---

## Phase 3: User Story 1 — Lecture Notebook Delivery (Priority: P1) MVP

**Goal**: Complete Jupyter notebook with all 7 constitution-mandated topic sections, Ukrainian text, code examples, exercises, memes, diagrams, and structural elements (objectives, prerequisites, summary, references).

**Independent Test**: Open notebook in Jupyter, execute all cells top-to-bottom in clean kernel — every cell runs without errors and all 7 topic areas are present.

### Implementation for User Story 1

- [ ] T009 [US1] Write Section 0 (Header + Prerequisites) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — lecture number, title, date, prerequisites referencing Lecture 6 (FastAPI project, MCP concepts, ruff/black), required tools list (Python 3.13+, pipx, MCP-compatible LLM client). Bridge from L6: "Your FastAPI skeleton is ready. Today we bring it to life." (FR-002)
- [ ] T010 [US1] Write Section 1 (Learning Objectives) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — 5 measurable outcomes: (1) async/event loop, (2) httpx requests, (3) config with .env/settings, (4) MCP server setup, (5) pytest basics (FR-001)
- [ ] T011 [P] [US1] Create or source event loop diagram and save to `lectures/07-integrations-async-mcp/assets/event-loop.png` — show single thread processing multiple I/O tasks, waiter analogy visual (FR-012)
- [ ] T012 [P] [US1] Create or source MCP data flow diagram and save to `lectures/07-integrations-async-mcp/assets/mcp-data-flow.png` — show LLM Client → MCP Protocol → keep-mcp server → Google Keep API (FR-012)
- [ ] T013 [P] [US1] Find or create 2+ memes and save to `lectures/07-integrations-async-mcp/assets/memes/` — at least one for async section ("blocking call inside async def" disaster), one for testing or MCP section (FR-011)
- [ ] T014 [US1] Write Section 2 (Async Essentials, ~15 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — waiter analogy, `time.sleep` vs `asyncio.sleep` demo, `def` vs `async def` in FastAPI, converting sync to async, critical rule (no blocking in async def), embed event-loop diagram. 3 runnable code examples (FR-003)
- [ ] T015 [US1] Write Section 3 (HTTP Client with httpx, ~12 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — why httpx, sync `httpx.get()` to JSONPlaceholder, async `httpx.AsyncClient`, timeout config, error handling (`raise_for_status`, `TimeoutException`). 2 runnable code examples (FR-004)
- [ ] T016 [US1] Write Section 4 (Config Basics, ~8 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — problem statement (hardcoded values), python-dotenv simple way (2 min), pydantic-settings as FastAPI way, show `config.py` from project, `.env` + `.env.example` + `.gitignore`. 2 runnable code examples (FR-005)
- [ ] T017 [US1] Write Section 5 (Practical MCP: keep-mcp Setup, ~15 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — brief 2-sentence recap (NOT re-explaining L6 concepts), `pipx install keep-mcp`, Google master token auth with gkeepapi link + security warnings, Claude Desktop JSON config (primary) + Cursor/Gemini alternatives, test connection, live demo with screenshots/transcripts showing 3 tool invocations (search, read, create). Embed MCP data flow diagram. Include troubleshooting subsection (FR-006, FR-013)
- [ ] T018 [US1] Write Section 6 (Safety Mindset, ~5 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — safe mode recap from L6, `UNSAFE_MODE=true` risks, principle of least privilege, credential hygiene (.env, .gitignore), connection to config section (FR-007, FR-017)
- [ ] T019 [US1] Write Section 7 (Testing with pytest, ~15 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — why test, pytest basics (test files/functions/assert), `uv add --dev pytest`, FastAPI TestClient, test_health (GET /health assert 200), test_create_note (POST assert 201), test_invalid (assert 422), monkeypatch mock example (replace httpx.get with fake). Integration test flag concept (brief). 3 runnable code examples. Monkeypatch only — no fixtures, no mock.patch, no parameterization (FR-008)
- [ ] T020 [US1] Write Section 8 (Quality Workflow, ~5 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — Makefile with check/fix/test targets, demo `make check` output, why run before every commit, Windows fallback note (choco install make or bash script). 1 code example (FR-009)
- [ ] T021 [US1] Write Section 9 (Summary, ~3 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — bullet list of key takeaways covering all 7 topics (FR-014)
- [ ] T022 [US1] Write Section 10 (What's Next, ~2 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — bridge to Lecture 8: Docker, PostgreSQL, docker compose, connection strings building on Settings pattern (FR-014)
- [ ] T023 [US1] Write Section 11 (References, ~1 min) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — links to Python asyncio docs, httpx docs, FastAPI async docs, pydantic-settings docs, pytest docs, keep-mcp repo, gkeepapi docs, MCP official docs, ruff docs, GNU Make manual
- [ ] T024 [US1] Verify all code cells in notebook execute sequentially in a clean kernel without errors. Fix any broken imports, missing dependencies, or cell ordering issues
- [ ] T025 [US1] Validate notebook against FR checklist: count code examples (>=5), exercises (>=2), memes (>=2), diagrams (>=2), verify Ukrainian text with English terms in parentheses, check duration estimate (~85 min target)

**Checkpoint**: Notebook is complete and all cells run. This is the MVP — the lecture can be delivered with just this.

---

## Phase 4: User Story 2 — Running MCP Server on Local Machine (Priority: P2)

**Goal**: The MCP setup instructions in the notebook are verified to work end-to-end — a student can install keep-mcp, authenticate, configure an LLM client, and perform tool calls.

**Independent Test**: Follow setup steps on a clean machine with Python + pipx, verify server starts, LLM client lists tools, and at least one tool call succeeds.

### Implementation for User Story 2

- [ ] T026 [US2] Verify keep-mcp installation: run `pipx install keep-mcp` on a clean environment and confirm it installs without errors. Document exact version and any platform-specific notes
- [ ] T027 [US2] Verify Google master token authentication flow: follow the gkeepapi docs link from the notebook, obtain a token, and confirm keep-mcp connects to Google Keep. Document any gotchas or extra steps needed
- [ ] T028 [US2] Verify LLM client configuration: test the Claude Desktop JSON config from the notebook, confirm the client connects to keep-mcp and lists available tools. Take screenshots for the notebook demo section
- [ ] T029 [US2] Verify 3 tool invocations: search notes (find), read a note (get_note), create a note (create_note). Take screenshots or capture transcripts for the notebook demo section in `lectures/07-integrations-async-mcp/lecture-07.ipynb` Section 5
- [ ] T030 [US2] Update Section 5 troubleshooting in `lectures/07-integrations-async-mcp/lecture-07.ipynb` with any real issues encountered during T026–T029 (auth errors, network issues, config mistakes)

**Checkpoint**: MCP setup is verified end-to-end. Screenshots/transcripts are embedded in notebook.

---

## Phase 5: User Story 3 — Async, HTTPX, and Testing Fundamentals (Priority: P3)

**Goal**: The project extensions (config.py, tests/, updated pyproject.toml) work correctly and the notebook code examples for async/httpx/testing all run as expected.

**Independent Test**: Run async examples, httpx requests, and `uv run pytest` in the project — all pass in a clean environment.

### Implementation for User Story 3

- [ ] T031 [US3] Create `lectures/07-integrations-async-mcp/notes-api/tests/__init__.py` (empty package marker)
- [ ] T032 [P] [US3] Create `lectures/07-integrations-async-mcp/notes-api/tests/test_health.py` — test_health_returns_200 using FastAPI TestClient (GET /health, assert status 200, assert JSON body has status field)
- [ ] T033 [P] [US3] Create `lectures/07-integrations-async-mcp/notes-api/tests/test_notes.py` — test_create_note_returns_201 (POST with valid body), test_create_note_invalid_returns_422 (POST with empty body), test_search_notes_returns_200 (POST /notes/search with query body), one monkeypatch mock example
- [ ] T034 [US3] Run `uv run pytest` in `lectures/07-integrations-async-mcp/notes-api/` and confirm all tests pass. Fix any failures
- [ ] T035 [US3] Update `lectures/07-integrations-async-mcp/notes-api/app/main.py` to import and use `settings` from `config.py` (e.g., `app = FastAPI(title=settings.app_name, debug=settings.debug)`)
- [ ] T036 [US3] Verify async/httpx code examples from notebook Sections 2–3 run correctly in the notebook kernel. Fix any issues with imports or async context

**Checkpoint**: Project tests pass, config is wired, async/httpx examples verified.

---

## Phase 6: User Story 4 — Quality Workflow (Priority: P4)

**Goal**: Makefile with check/fix/test targets works, all quality checks pass on the extended project.

**Independent Test**: Run `make check` in the project — ruff, black, and pytest all pass.

### Implementation for User Story 4

- [ ] T037 [US4] Create `lectures/07-integrations-async-mcp/notes-api/Makefile` with three targets: `check` (`ruff check . && black --check . && pytest`), `fix` (`ruff check --fix . && black .`), `test` (`pytest`). Add `.PHONY` declarations
- [ ] T038 [US4] Run `make check` in `lectures/07-integrations-async-mcp/notes-api/` and confirm all three steps pass (zero ruff violations, black formatted, all tests green). Fix any issues
- [ ] T039 [US4] Write Exercise 1 (MCP setup exercise) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` Section 5 — configure and run keep-mcp, verify by asking LLM to list notes. Include solution in hidden/collapsed cell (FR-010)
- [ ] T040 [US4] Write Exercise 2 (testing exercise) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` Section 7 — write a test for POST /notes/search endpoint verifying 200 status, empty results list, schema match. Include solution in hidden/collapsed cell (FR-010)

**Checkpoint**: Quality workflow works. Both exercises are written with solutions.

---

## Phase 7: Polish & Cross-Cutting Concerns

**Purpose**: Final quality pass, content consistency, and quickstart validation

- [ ] T041 Review entire notebook for Ukrainian text quality — consistent terminology, English terms in parentheses on first use, no Russian sources in references (FR-015)
- [ ] T042 Review notebook for emoji/icon usage — max 1-2 per section, following Lecture 6 pattern (constitution: prohibited excessive emoji)
- [ ] T043 Verify cross-references to Lecture 6 are accurate — section numbers, concept names, project structure references all match actual L6 content
- [ ] T044 Run full quickstart validation from `specs/010-lecture7-mcp-content/quickstart.md` — check all items in the verification checklist
- [ ] T045 Verify notebook duration estimate — count cells, estimate reading/execution time, target ~85 minutes (FR-016)
- [ ] T046 Final `make check` pass on project: `ruff check . && black --check . && pytest` — all green, zero warnings

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion — BLOCKS all user stories
- **US1 Notebook (Phase 3)**: Depends on Foundational. This is the MVP
- **US2 MCP Verification (Phase 4)**: Depends on US1 Section 5 being written (T017). Can start partially in parallel with later US1 tasks
- **US3 Project Extensions (Phase 5)**: Depends on Foundational (T005–T008). Can run in parallel with US1 notebook writing
- **US4 Quality Workflow (Phase 6)**: Depends on US3 (tests must exist for `make check`). Exercises depend on US1 sections being written
- **Polish (Phase 7)**: Depends on all previous phases being complete

### User Story Dependencies

- **US1 (Notebook)**: Can start after Foundational — no dependencies on other stories
- **US2 (MCP Verification)**: Depends on US1 Section 5 (T017) for the notebook content to verify against
- **US3 (Project Extensions)**: Can start after Foundational — independent of US1 (creates files, not notebook cells)
- **US4 (Quality + Exercises)**: Depends on US3 (Makefile needs tests to exist) and US1 (exercises go into existing notebook sections)

### Within Each User Story

- Assets (diagrams, memes) before notebook sections that embed them
- Notebook sections in order (0 → 11) since later sections reference earlier ones
- Project files before notebook sections that reference them
- Verification tasks after all content tasks

### Parallel Opportunities

- T005, T006, T007 can run in parallel (different project files)
- T011, T012, T013 can run in parallel (different asset files)
- T032, T033 can run in parallel (different test files)
- US1 notebook writing and US3 project extensions can overlap significantly
- Within US1: asset creation (T011–T013) can happen in parallel with each other and before sections that use them

---

## Parallel Example: User Story 1

```bash
# Launch all asset tasks together:
Task T011: "Create event loop diagram in assets/event-loop.png"
Task T012: "Create MCP data flow diagram in assets/mcp-data-flow.png"
Task T013: "Find/create memes in assets/memes/"

# Then write notebook sections sequentially (they reference each other):
Task T009 → T010 → T014 → T015 → T016 → T017 → T018 → T019 → T020 → T021 → T022 → T023
```

## Parallel Example: User Story 3

```bash
# Launch test files in parallel:
Task T032: "Create test_health.py"
Task T033: "Create test_notes.py"

# Then verify:
Task T034: "Run pytest and confirm all pass"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T003)
2. Complete Phase 2: Foundational (T004–T008)
3. Complete Phase 3: User Story 1 (T009–T025)
4. **STOP and VALIDATE**: Open notebook, run all cells, verify 7 topic areas present
5. Lecture can be delivered with just this

### Incremental Delivery

1. Setup + Foundational → Project ready
2. US1 (Notebook) → Lecture deliverable (MVP!)
3. US2 (MCP Verification) → Screenshots/transcripts embedded, setup proven
4. US3 (Project Extensions) → Real test files and config wired
5. US4 (Quality + Exercises) → Makefile works, exercises complete
6. Polish → Final quality pass

### Optimal Single-Developer Order

1. T001–T003 (Setup)
2. T004–T008 (Foundational — T005/T006/T007 in parallel)
3. T011–T013 (Assets — all in parallel)
4. T009–T023 (Notebook sections — sequential)
5. T026–T030 (MCP verification — requires access to Google Keep + LLM client)
6. T031–T036 (Project extensions — T032/T033 in parallel)
7. T037–T040 (Quality workflow + exercises)
8. T024–T025, T041–T046 (Validation and polish)

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- MCP verification tasks (US2) require live Google account + LLM client — schedule these when network access is available
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Total: 46 tasks across 7 phases
