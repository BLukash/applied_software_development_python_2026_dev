# Tasks: Enhance Lecture 7 — Deeper Asyncio & MCP Lifecycle

**Input**: Design documents from `/specs/011-lecture7-async-mcp-enhance/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: No test tasks — this is educational content enhancement, not software development.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2)
- Include exact file paths in descriptions

## Path Conventions

- **Notebook**: `lectures/07-integrations-async-mcp/lecture-07.ipynb`
- **Assets**: `lectures/07-integrations-async-mcp/assets/`
- **Specs**: `specs/011-lecture7-async-mcp-enhance/`

---

## Phase 1: Setup

**Purpose**: Verify baseline state and prepare assets directory

- [ ] T001 Verify existing notebook `lectures/07-integrations-async-mcp/lecture-07.ipynb` opens and all existing cells execute without errors in a clean kernel
- [ ] T002 Verify assets directory exists at `lectures/07-integrations-async-mcp/assets/` with existing diagram references (`event-loop.png`, `mcp-data-flow.png`)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Read research and data-model to understand exact insertion points and content specifications

**CRITICAL**: No user story work can begin until content plan is reviewed

- [ ] T003 Read `specs/011-lecture7-async-mcp-enhance/research.md` in full — extract comparison table dimensions, GIL explanation approach, MCP lifecycle steps, transport comparison dimensions, and annotated config JSON structure
- [ ] T004 Read `specs/011-lecture7-async-mcp-enhance/data-model.md` — confirm cell insertion points (after `cell-8` for async, after `cell-24` for MCP) and subsection renumbering plan

**Checkpoint**: Content plan is clear — cell insertion can now begin.

---

## Phase 3: User Story 1 — Deeper Asyncio with Thread Comparison (Priority: P1) MVP

**Goal**: Expand Section 1 (Async Essentials) with threading comparison, GIL explanation, visual diagram, and runnable code example.

**Independent Test**: New subsection 1.4 exists with comparison table (5+ dimensions), runnable threading vs asyncio demo, diagram reference, and FastAPI design connection. All cells execute without errors.

### Implementation for User Story 1

- [ ] T005 [P] [US1] Create or source diagram `lectures/07-integrations-async-mcp/assets/threads-vs-asyncio.png` — side-by-side timeline showing 3 threads (each with I/O wait) vs 1 event loop switching between 3 coroutines at `await` points. Include memory labels (~MB per thread vs ~KB per coroutine). See `specs/011-lecture7-async-mcp-enhance/research.md` R3 for layout spec
- [ ] T006 [US1] Insert markdown cell after `cell-8` in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — new subsection "### 1.4 Потоки (Threads) vs Asyncio — чому не просто потоки?" containing: (1) 2-sentence thread primer ("Потік (thread) — це..."), (2) GIL explanation paragraph in Ukrainian with English terms, (3) comparison table with 5+ dimensions from research.md (scheduling, memory, GIL, best use, race conditions, scalability, error handling, FastAPI connection). Must match L7 style: Ukrainian text, English terms in parentheses
- [ ] T007 [US1] Insert code cell after the new markdown cell in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — runnable side-by-side demo: (1) `threading` approach with 3 threads each doing `time.sleep(1)`, timed; (2) `asyncio.gather` approach with 3 coroutines each doing `asyncio.sleep(1)`, timed; (3) print comparison showing both take ~1 second vs sequential ~3 seconds. Use `import threading, asyncio, time`. Code comments in Ukrainian/English mix matching L7 style
- [ ] T008 [US1] Insert markdown cell after the code cell in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — reference diagram `![Потоки vs Asyncio](assets/threads-vs-asyncio.png)` + 1 paragraph connecting GIL/async to FastAPI design: "Тому FastAPI використовує `async def` за замовчуванням — event loop обслуговує тисячі з'єднань з мінімальними витратами пам'яті, без ризику race conditions."
- [ ] T009 [US1] Verify all new and existing cells in Section 1 execute sequentially without errors in a clean kernel. Confirm the threading demo prints ~1 second for both approaches and ~3 seconds for sequential baseline

**Checkpoint**: Async section is enhanced. Student can see threads vs asyncio comparison, understand GIL, and connect to FastAPI design.

---

## Phase 4: User Story 2 — MCP Client-Server Lifecycle Explanation (Priority: P2)

**Goal**: Expand Section 4 (Practical MCP) with subprocess lifecycle explanation, stdio vs SSE transport comparison, and annotated config JSON.

**Independent Test**: New subsections 4.4–4.5 exist with lifecycle diagram, annotated config, and transport comparison table. Existing subsections are renumbered (4.4→4.6, 4.5→4.7). All cells execute without errors.

### Implementation for User Story 2

- [ ] T010 [P] [US2] Create or source diagram `lectures/07-integrations-async-mcp/assets/mcp-lifecycle.png` — vertical sequence diagram showing: Host (Claude Desktop) spawns subprocess (`pipx run keep-mcp`) → stdin/stdout JSON-RPC communication → `initialize` exchange → `tools/call` request/response → `shutdown` → process exits. See `specs/011-lecture7-async-mcp-enhance/research.md` R3 for layout spec
- [ ] T011 [US2] Insert markdown cell after `cell-24` (LLM client configs) in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — new subsection "### 4.4 Як MCP-клієнт запускає сервер? (MCP Lifecycle)" containing: (1) opening statement that MCP "server" is NOT a traditional web server, (2) explanation that host spawns server as subprocess (дочірній процес), (3) reference diagram `![MCP Lifecycle](assets/mcp-lifecycle.png)`, (4) numbered step-by-step lifecycle from research.md (7 steps: host starts → reads config → spawns subprocess → initialize → operation → shutdown → process terminates). Ukrainian text with English terms in parentheses
- [ ] T012 [US2] Insert markdown cell after the lifecycle cell in `lectures/07-integrations-async-mcp/lecture-07.ipynb` — new subsection "### 4.5 Анотований конфіг + транспорт (stdio vs SSE)" containing: (1) annotated Claude Desktop JSON config from research.md with Ukrainian comments explaining each field (`command` = що запустити, `args` = як запустити, `env` = змінні середовища для subprocess), (2) key teaching point: "Це НЕ URL. Це shell-команда, яку хост виконує.", (3) transport comparison table with 4+ dimensions from research.md (how server starts, communication, network, config format, typical use case, lifecycle management), (4) brief note that SSE/HTTP exists for remote/shared deployments but stdio is the default for local tools
- [ ] T013 [US2] Update subsection numbering in existing cells of Section 4: rename current "### 4.4 Перевірка з'єднання" to "### 4.6 Перевірка з'єднання" and "### 4.5 Усунення проблем" to "### 4.7 Усунення проблем" in `lectures/07-integrations-async-mcp/lecture-07.ipynb`
- [ ] T014 [US2] Verify all new and existing cells in Section 4 execute sequentially without errors in a clean kernel. Confirm subsection numbering is consistent (4.1 through 4.7)

**Checkpoint**: MCP section is enhanced. Student understands subprocess lifecycle, can explain config fields, and knows the difference between stdio and SSE transport.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Final quality pass and content consistency

- [ ] T015 Review all new cells for Ukrainian text quality — consistent terminology, English terms in parentheses on first use, no Russian sources
- [ ] T016 Review emoji/icon usage in new cells — max 1–2 per subsection, matching L7 style
- [ ] T017 Verify total lecture duration estimate stays within 85–100 minutes — count cells, estimate reading/execution time for new content (~15 min max)
- [ ] T018 Run full notebook (all cells) in clean kernel — zero errors, all outputs as expected
- [ ] T019 Run quickstart validation from `specs/011-lecture7-async-mcp-enhance/quickstart.md` — check all items

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories
- **US1 Async (Phase 3)**: Depends on Phase 2 — can start after foundational review
- **US2 MCP (Phase 4)**: Depends on Phase 2 — can run in parallel with US1 (different notebook sections)
- **Polish (Phase 5)**: Depends on both US1 and US2 completion

### User Story Dependencies

- **US1 (Async)**: Independent — modifies Section 1 only
- **US2 (MCP)**: Independent — modifies Section 4 only
- US1 and US2 can be implemented in parallel (different sections of the notebook)

### Parallel Opportunities

- T005 (async diagram) and T010 (MCP diagram) can run in parallel [P]
- US1 (T005–T009) and US2 (T010–T014) can run in parallel (different notebook sections)

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup verification
2. Complete Phase 2: Read research and data-model
3. Complete Phase 3: US1 — Async enhancement
4. **STOP and VALIDATE**: Verify Section 1 works independently
5. Proceed to US2 or stop if time-constrained

### Full Delivery

1. Setup + Foundational → ready
2. US1 (Async) + US2 (MCP) → can run in parallel
3. Polish → final quality pass
4. Total: 19 tasks, ~7 new notebook cells, 2 new diagrams

---

## Notes

- This is a content enhancement — no code project changes to `project/notes-api/`
- Diagram creation (T005, T010) may require external tools (draw.io, matplotlib, or sourcing from web)
- All new content must match the existing L7 notebook style established in feature 010
- Cell insertion order matters — insert from bottom to top to avoid shifting cell indices
