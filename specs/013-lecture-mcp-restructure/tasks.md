# Tasks: Restructure Lectures 6, 7 & Add Lecture 8 (MCP Separation)

**Input**: Design documents from `/specs/013-lecture-mcp-restructure/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, quickstart.md

**Tests**: Not requested — no test tasks included.

**Organization**: Tasks grouped by user story. US1 and US2 can run in parallel after setup. US3 depends on content extracted from US1 and US2.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Phase 1: Setup (Directory Renames & Asset Migration)

**Purpose**: Rename directories and move assets before editing notebook content. This prevents broken paths during editing.

- [x] T001 Rename lecture 6 directory using `git mv lectures/06-web-fastapi-mcp lectures/06-web-fastapi`
- [x] T002 Rename lecture 7 directory using `git mv lectures/07-integrations-async-mcp lectures/07-async-testing`
- [x] T003 Create lecture 8 directory structure: `lectures/08-mcp/`, `lectures/08-mcp/assets/`, `lectures/08-mcp/assets/memes/`
- [x] T004 Move MCP lifecycle asset using `git mv lectures/07-async-testing/assets/mcp-lifecycle.png lectures/08-mcp/assets/mcp-lifecycle.png`
- [x] T005 Remove empty clients/ directory from project skeleton (if it exists): `lectures/06-web-fastapi/notes-api/app/clients/` — already absent, no action needed

**Checkpoint**: Directory structure is clean — all three lecture directories exist with correct names, asset is in L8.

---

## Phase 2: Foundational (Extract MCP Content for Migration)

**Purpose**: Before editing L6 and L7, extract the MCP cells/content that will be migrated to L8. This ensures nothing is lost during removal.

**CRITICAL**: Complete this phase before any notebook editing begins.

- [x] T006 Read and document all MCP cells from `lectures/06-web-fastapi/lecture-06.ipynb` — extract Section 9 content (cells j0mcp through j5whymcp): USB-C analogy, architecture diagram, three primitives, keep-mcp example, config JSON, "why this matters". Save extracted content as reference in `specs/013-lecture-mcp-restructure/extracted-l6-mcp.md`
- [x] T007 Read and document all MCP cells from `lectures/07-async-testing/lecture-07.ipynb` — extract Section 4 (practical MCP: 4.1-4.7), Section 5 (safety mindset), and MCP-specific mocking code from testing section. Save extracted content as reference in `specs/013-lecture-mcp-restructure/extracted-l7-mcp.md`

**Checkpoint**: All MCP content is safely extracted and documented. Editing can now begin.

---

## Phase 3: User Story 1 — Lecture 6 Update: Web Fundamentals & FastAPI (Priority: P1)

**Goal**: Remove all MCP content from Lecture 6, add REST real-world example and DELETE exercise, update cross-references.

**Independent Test**: Open `lectures/06-web-fastapi/lecture-06.ipynb` in Jupyter — search for "MCP" returns 0 results, 3 exercises exist, "What's Next" mentions async/testing only, all cells execute.

### Implementation for User Story 1

- [x] T008 [US1] Remove MCP Section 9 entirely from `lectures/06-web-fastapi/lecture-06.ipynb` — delete all cells from Section 9 header ("MCP — Model Context Protocol") through Section 9.5 ("Why this matters for us"), including inline diagrams and code snippets
- [x] T009 [US1] Update learning objectives cell in `lectures/06-web-fastapi/lecture-06.ipynb` — remove MCP-related objective (e.g., "explain what MCP is and name its three primitives"), renumber remaining objectives
- [x] T010 [US1] Expand REST Essentials section (Section 5) in `lectures/06-web-fastapi/lecture-06.ipynb` — add a brief real-world API design example (e.g., show 3-4 GitHub API endpoints as "REST in the wild": GET /repos/{owner}/{repo}, POST /repos/{owner}/{repo}/issues, etc.) demonstrating REST principles taught in the section. Ukrainian text, ~3 minutes of content
- [x] T011 [US1] Add Exercise 3 (DELETE endpoint) to `lectures/06-web-fastapi/lecture-06.ipynb` — after the Project Bootstrap section, add a new exercise: "Implement DELETE /notes/{note_id} endpoint that returns 204 on success or 404 if note not found." Include starter code cell and hidden solution cell. Ukrainian text, follows existing exercise format
- [x] T012 [US1] Update "What's Next" section in `lectures/06-web-fastapi/lecture-06.ipynb` — replace any MCP references with preview of L7 topics: async programming, HTTP clients (httpx), testing (pytest), quality workflow. Remove any "MCP practical setup" mention
- [x] T013 [US1] Update References section in `lectures/06-web-fastapi/lecture-06.ipynb` — remove any MCP-related references (MCP spec links, keep-mcp GitHub, etc.)
- [x] T014 [US1] Update project structure table in `lectures/06-web-fastapi/lecture-06.ipynb` — remove `clients/` directory row from the project skeleton description (it was described as "for MCP in Lecture 7")
- [x] T015 [US1] Renumber sections in `lectures/06-web-fastapi/lecture-06.ipynb` — ensure section numbers are sequential after MCP removal (old Section 10 Summary becomes new Section 10 or adjust to fit new Exercise 3 placement)
- [x] T016 [US1] Verify Lecture 6 content minimums in `lectures/06-web-fastapi/lecture-06.ipynb` — confirm: at least 5 runnable code examples, 3 exercises with solutions, 2 memes, 3 diagrams, Ukrainian text throughout. Fix any gaps

**Checkpoint**: Lecture 6 is MCP-free, has 3 exercises, and all cross-references point to L7 (async/testing). Run all cells to verify no errors.

---

## Phase 4: User Story 2 — Lecture 7 Update: Async, HTTPX, Testing & Quality Workflow (Priority: P1)

**Goal**: Remove all MCP content from Lecture 7, expand testing section with fixtures/parametrize/error cases, add async exercise, update cross-references.

**Independent Test**: Open `lectures/07-async-testing/lecture-07.ipynb` in Jupyter — search for MCP practical content returns 0 results, expanded testing section exists with exercise, async exercise exists, "What's Next" mentions L8 MCP and L9 Docker.

### Implementation for User Story 2

- [x] T017 [US2] Remove MCP Section 4 (practical MCP) entirely from `lectures/07-async-testing/lecture-07.ipynb` — delete all cells from Section 4 header ("Practical MCP") through Section 4.7 (troubleshooting), including pipx commands, auth flow, LLM config, lifecycle diagram reference, transport comparison, annotated config JSON
- [x] T018 [US2] Remove Safety Mindset Section 5 entirely from `lectures/07-async-testing/lecture-07.ipynb` — delete all cells covering safe/unsafe mode, secure defaults, least privilege (MCP-specific safety content)
- [x] T019 [US2] Remove MCP-specific mocking example from testing section in `lectures/07-async-testing/lecture-07.ipynb` — remove the monkeypatch example that mocks MCP tool calls. Keep general monkeypatch/mocking if it exists for non-MCP use cases
- [x] T020 [US2] Update learning objectives cell in `lectures/07-async-testing/lecture-07.ipynb` — remove MCP-related objectives (e.g., "install and configure keep-mcp"), renumber remaining objectives
- [x] T021 [US2] Update prerequisites cell in `lectures/07-async-testing/lecture-07.ipynb` — remove "MCP concepts from Lecture 6" from prerequisites list. Keep FastAPI project, ruff/black references
- [x] T022 [US2] Add async practical exercise to `lectures/07-async-testing/lecture-07.ipynb` — after the Async Essentials section (Section 2), add an exercise: "Convert a sync endpoint to async and use httpx to call a public API (e.g., fetch a random quote/joke from a free API). Return the result in the endpoint response." Include starter code and hidden solution. Ukrainian text, ~10 min
- [x] T023 [US2] Expand testing section in `lectures/07-async-testing/lecture-07.ipynb` — add new subsections after the existing pytest basics and TestClient content: (1) pytest fixtures — `@pytest.fixture` with a simple example (e.g., fixture that creates a TestClient), mention conftest.py; (2) `@pytest.mark.parametrize` — test same endpoint with multiple inputs; (3) testing error cases — write tests that expect 404 and 422 responses. Ukrainian text, runnable code cells, ~10 min of new content
- [x] T024 [US2] Add testing exercise to `lectures/07-async-testing/lecture-07.ipynb` — after the expanded testing section, add exercise: "Write 3-4 tests for the notes API: (1) test create note returns 201, (2) test search notes returns 200, (3) test create with invalid data returns 422, (4) test get non-existent note returns 404." Include starter code and hidden solution. Ukrainian text, ~10 min
- [x] T025 [US2] Update "What's Next" section in `lectures/07-async-testing/lecture-07.ipynb` — change from "Docker + PostgreSQL (L8)" to "MCP — Model Context Protocol: AI Tool Integration (L8), then Docker + PostgreSQL (L9)"
- [x] T026 [US2] Update References section in `lectures/07-async-testing/lecture-07.ipynb` — remove MCP-related references (keep-mcp GitHub, MCP spec links, Google auth docs). Add pytest fixtures and parametrize documentation links
- [x] T027 [US2] Renumber sections in `lectures/07-async-testing/lecture-07.ipynb` — ensure section numbers are sequential after MCP removal (Sections 4-5 removed, testing becomes new Section 5, Makefile becomes Section 6, etc.)
- [x] T028 [US2] Verify Lecture 7 content minimums in `lectures/07-async-testing/lecture-07.ipynb` — confirm: at least 5 runnable code examples, 2+ exercises with solutions, 2 memes, 2 diagrams (threads-vs-asyncio.png still referenced correctly from `assets/threads-vs-asyncio.png`), Ukrainian text throughout. Fix any gaps

**Checkpoint**: Lecture 7 is MCP-free, has expanded testing with exercise, async exercise exists, all cross-references updated. Run all cells to verify no errors.

---

## Phase 5: User Story 3 — New Lecture 8: MCP — AI Tool Integration (Priority: P2)

**Goal**: Create a new dedicated MCP lecture consolidating content extracted from L6 and L7, plus new sections for depth.

**Independent Test**: Open `lectures/08-mcp/lecture-08.ipynb` in Jupyter — 8 main sections exist, 2 exercises, 3+ diagrams, 2+ memes, all cells execute, "What's Next" previews L9.

**Depends on**: T006 and T007 (extracted content references) must be complete.

### Implementation for User Story 3

- [x] T029 [US3] Create lecture 8 notebook skeleton at `lectures/08-mcp/lecture-08.ipynb` — set up Jupyter notebook with header cell (Лекція 8, title "MCP: Model Context Protocol — AI Tool Integration", date, draft status), prerequisites cell (references L6 FastAPI/REST and L7 async/httpx/testing), and learning objectives cell (6 measurable outcomes per FR-020 through FR-031). Ukrainian text with English technical terms in parentheses
- [x] T030 [US3] Create Section 2: Introduction & Motivation (~10 min) in `lectures/08-mcp/lecture-08.ipynb` — migrate USB-C analogy and problem statement from extracted L6 content (specs/013-lecture-mcp-restructure/extracted-l6-mcp.md). Add NEW content: real-world MCP adoption examples (Claude Desktop, Cursor, Windsurf as MCP hosts), why MCP matters for Python developers. Include at least 1 meme. Ukrainian text
- [x] T031 [US3] Create Section 3: MCP Architecture Deep Dive (~15 min) in `lectures/08-mcp/lecture-08.ipynb` — migrate Host/Client/Server architecture and three primitives (Tools, Resources, Prompts) from extracted L6 content. Add NEW content: REST-to-MCP mapping table showing how familiar REST endpoints (GET /notes, POST /notes, DELETE /notes/{id}) correspond to MCP tools. Include architecture diagram (inline markdown or image). Add Exercise 1: "Given a hypothetical library management service, identify which MCP primitives to expose" (markdown cell exercise with hidden solution). Ukrainian text
- [x] T032 [US3] Create Section 4: MCP Lifecycle & Transports (~10 min) in `lectures/08-mcp/lecture-08.ipynb` — migrate lifecycle subprocess model and transport comparison from extracted L7 content (specs/013-lecture-mcp-restructure/extracted-l7-mcp.md). Reference `assets/mcp-lifecycle.png`. Migrate annotated config JSON. Add NEW: brief connection to FastAPI knowledge ("SSE is just HTTP streaming you already know from web fundamentals"). Ukrainian text
- [x] T033 [US3] Create Section 5: Practical Setup — keep-mcp (~20 min) in `lectures/08-mcp/lecture-08.ipynb` — migrate from extracted L7 content: keep-mcp description + CRUD tool mapping (from L6 extract), pipx installation, Google Master Token auth flow, LLM client configuration (Gemini primary + alternatives), connection verification, troubleshooting guide. Add Exercise 2: "Install keep-mcp and perform 3 operations (search notes, create a note, list notes) through your LLM client" with step-by-step instructions. Ukrainian text
- [x] T034 [US3] Create Section 6: Safety Mindset (~10 min) in `lectures/08-mcp/lecture-08.ipynb` — migrate safe/unsafe mode and secure defaults from extracted L7 content. Add NEW content: real-world risks (prompt injection through tool descriptions, unintended destructive actions), tool annotations (readOnlyHint, destructiveHint, openWorldHint) with examples. Include at least 1 meme. Ukrainian text
- [x] T035 [US3] Create Section 7: Testing MCP Integrations (~10 min) in `lectures/08-mcp/lecture-08.ipynb` — migrate MCP-specific mocking example from extracted L7 content (monkeypatch for MCP tool responses). Include integration test flag pattern (`@pytest.mark.skipif` or environment variable check). Add runnable code example showing a test function that mocks an MCP tool call and asserts the response. Ukrainian text
- [x] T036 [US3] Create Section 8: Connection to Our Project (~10 min) in `lectures/08-mcp/lecture-08.ipynb` — NEW content: conceptual preview showing how notes-api CRUD endpoints could map to MCP tools (table: POST /notes/create → create_note tool, POST /notes/search → search_notes tool, etc.). Discuss what would need to be added (MCP server wrapper, tool definitions, transport setup). Optional homework suggestion: "sketch an MCP server definition for the notes-api." NO implementation code — purely conceptual. Ukrainian text
- [x] T037 [US3] Create Summary, What's Next, and References sections in `lectures/08-mcp/lecture-08.ipynb` — Summary with key takeaways (5-6 bullet points). "What's Next" previewing L9: Docker + PostgreSQL — containerizing the API and adding real persistence. References combining MCP spec links, keep-mcp GitHub, transport docs from both L6 and L7 originals. Ukrainian text
- [x] T038 [US3] Verify Lecture 8 content minimums in `lectures/08-mcp/lecture-08.ipynb` — confirm: at least 5 runnable code examples (config snippets, mock test code, JSON examples), 2 exercises with solutions, 2 memes, 3 diagrams (architecture, lifecycle/mcp-lifecycle.png, transport comparison table), Ukrainian text throughout, ~90 min duration. Fix any gaps

**Checkpoint**: Lecture 8 is complete, all MCP content from L6/L7 is present plus new depth. Run all cells to verify no errors.

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Final verification across all three lectures and cleanup.

- [x] T039 [P] Audit cross-references in `lectures/06-web-fastapi/lecture-06.ipynb` — verify no remaining references to MCP, L8 as "Docker" lecture, or old directory names. Verify all internal asset paths work
- [x] T040 [P] Audit cross-references in `lectures/07-async-testing/lecture-07.ipynb` — verify no remaining MCP practical content, L8 reference says "MCP" not "Docker", old directory name references are gone. Verify `assets/threads-vs-asyncio.png` path works
- [x] T041 [P] Audit cross-references in `lectures/08-mcp/lecture-08.ipynb` — verify prerequisites reference L6 and L7 by correct names, `assets/mcp-lifecycle.png` loads, no "as we'll see in L7" forward-references from migrated content remain
- [x] T042 Scan Lectures 1-5 notebooks for any references to L6/L7 MCP content that may need updating — check `lectures/01-*/`, `lectures/02-*/`, `lectures/03-*/`, `lectures/04-*/`, `lectures/05-*/` notebooks for mentions of "MCP" or "Лекція 6" or "Лекція 7" that reference MCP topics. Update if found
- [x] T043 Clean up extracted content files — delete `specs/013-lecture-mcp-restructure/extracted-l6-mcp.md` and `specs/013-lecture-mcp-restructure/extracted-l7-mcp.md` (temporary migration references, no longer needed)
- [x] T044 Run quickstart.md validation — execute all 10 verification steps from `specs/013-lecture-mcp-restructure/quickstart.md` to confirm the restructuring is complete and correct

**Checkpoint**: All three lectures are consistent, cross-references are correct, no MCP content leaks remain in L6/L7, L8 is complete and self-contained.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 (T001-T002 renames must complete before reading notebooks at new paths)
- **US1 - Lecture 6 (Phase 3)**: Depends on Phase 2 (T006 extraction complete). Can run **in parallel** with Phase 4
- **US2 - Lecture 7 (Phase 4)**: Depends on Phase 2 (T007 extraction complete). Can run **in parallel** with Phase 3
- **US3 - Lecture 8 (Phase 5)**: Depends on Phase 2 (T006 + T007 extractions provide content to migrate)
- **Polish (Phase 6)**: Depends on all user story phases (3, 4, 5) being complete

### User Story Dependencies

- **US1 (L6 Update)**: Independent after Phase 2 — can start as soon as MCP content is extracted
- **US2 (L7 Update)**: Independent after Phase 2 — can start as soon as MCP content is extracted
- **US3 (L8 Create)**: Depends on extracted content from Phase 2. Does NOT depend on US1 or US2 completing, but migrated content references should be used

### Within Each User Story

- Removal tasks before addition tasks (clear space before filling it)
- Content additions before cross-reference updates (write content, then link it)
- Verification as final task per story

### Parallel Opportunities

**Phase 1**: T001, T002, T003 can run in parallel (different directories)
**Phase 2**: T006, T007 can run in parallel (different notebooks)
**Phase 3 + Phase 4**: Entire US1 and US2 phases can run in parallel (different notebooks)
**Phase 5**: Can start as soon as Phase 2 completes (doesn't wait for US1/US2)
**Phase 6**: T039, T040, T041 can run in parallel (different notebooks)

---

## Parallel Example: Setup Phase

```bash
# Launch all directory operations together:
Task T001: "git mv lectures/06-web-fastapi-mcp lectures/06-web-fastapi"
Task T002: "git mv lectures/07-integrations-async-mcp lectures/07-async-testing"
Task T003: "mkdir -p lectures/08-mcp/assets/memes"
```

## Parallel Example: US1 + US2

```bash
# After Phase 2, launch both lecture updates simultaneously:
Agent A: Phase 3 (T008-T016) — editing lectures/06-web-fastapi/lecture-06.ipynb
Agent B: Phase 4 (T017-T028) — editing lectures/07-async-testing/lecture-07.ipynb
```

---

## Implementation Strategy

### MVP First (US1 + US2 Only)

1. Complete Phase 1: Setup (directory renames)
2. Complete Phase 2: Extract MCP content
3. Complete Phase 3: Lecture 6 update (remove MCP, add exercises)
4. Complete Phase 4: Lecture 7 update (remove MCP, expand testing)
5. **STOP and VALIDATE**: Both lectures work independently, MCP-free
6. Proceed to Phase 5 (Lecture 8 creation) when ready

### Full Delivery

1. Phases 1-2: Setup + extraction (~15 min)
2. Phases 3-4 in parallel: L6 + L7 updates (~45 min each)
3. Phase 5: L8 creation (~60 min — mostly migration + light authoring)
4. Phase 6: Polish + validation (~15 min)

**Estimated total**: ~2-3 hours of implementation work

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- This is primarily a content reorganization — ~70% migration, ~30% new content
- All notebook content must be in Ukrainian with English technical terms in parentheses
- The notes-api project code is NOT modified by any task
- Commit after each phase completion for clean git history
- Extracted content files (T006, T007) are temporary — deleted in Phase 6 (T043)
