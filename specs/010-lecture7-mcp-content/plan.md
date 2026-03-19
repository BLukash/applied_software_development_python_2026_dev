# Implementation Plan: Lecture 7 — Python Web Server Integrations: Async, HTTPX, Testing, Practical MCP

**Branch**: `010-lecture7-mcp-content` | **Date**: 2026-03-19 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/010-lecture7-mcp-content/spec.md`

## Summary

Create Lecture 7 as a Jupyter notebook covering seven constitution-mandated topics: async essentials, httpx HTTP client, config basics (.env + pydantic-settings), practical MCP (keep-mcp installation + Claude Desktop/Gemini connection), safety mindset, pytest testing (minimal: TestClient + monkeypatch), and quality workflow (Makefile). The deliverable includes the notebook (~70 cells, 1.5 hours content, Ukrainian text) and extensions to the Lecture 6 FastAPI project (config.py, tests/, Makefile). MCP is a standalone LLM-client demo — no wiring of FastAPI endpoints to keep-mcp.

## Technical Context

**Language/Version**: Python 3.13+ (code examples in Jupyter Notebook + extensions to Lecture 6 FastAPI project)
**Primary Dependencies**: FastAPI, httpx, pydantic-settings (project); pytest (testing); Jupyter (notebook delivery); ruff, black (tooling); keep-mcp via pipx (MCP demo)
**Storage**: N/A — no persistence changes to the project
**Testing**: pytest + FastAPI TestClient (monkeypatch only, no fixtures)
**Target Platform**: Cross-platform (student laptops: Windows/macOS/Linux)
**Project Type**: Educational content (notebook + project extensions)
**Performance Goals**: N/A — educational content
**Constraints**: 1.5 hours lecture duration; all code must run in clean Python 3.13+ environment; MCP demo requires network + Google account
**Scale/Scope**: Single notebook (~70 cells) + ~7 new/modified project files

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Status |
|-----------|------|--------|
| I. Student-Centered Design | Learning objectives at start; real-world analogies; progressive difficulty; interactive elements throughout | PASS — waiter analogy for async (section 2); exercises in sections 5, 7 |
| II. Practical Application Focus | Mini-project from Lecture 5 onward; 20–30 min in-class + homework extension | PASS — MCP setup exercise (~15 min in-class); testing exercise (~10 min); config + quality workflow extend existing project |
| III. Progressive Skill Building | Must analyze Lecture 6 first; maintain tone; avoid repetition; cross-references | PASS — Lecture 6 analyzed; MCP section explicitly avoids re-explaining L6 concepts; async builds on L6 endpoints |
| IV. Quality Content Standards | Ukrainian text; 5+ code examples; 2+ exercises; 2+ memes; 2+ visuals; summary; What's Next | PASS — 11 code examples, 2 exercises, 2+ memes, 2 visuals planned (see data-model.md) |
| V. Iterative Development | Code tested in clean env; reviewed for accuracy | PASS — quickstart.md verification checklist defined |
| Prohibited: No excessive emoji | Max 1-2 per section | PASS — following Lecture 6 pattern |
| Prohibited: No 3rd-party when stdlib works | httpx, pydantic-settings, pytest justified (they ARE the teaching subjects); keep-mcp is the demo subject | PASS |
| Prohibited: No hallucinated facts | All claims link to official docs | PASS — sources collected in research.md |

**Post-Phase 1 re-check**: All gates still pass. No violations.

## Project Structure

### Documentation (this feature)

```text
specs/010-lecture7-mcp-content/
├── plan.md              # This file
├── research.md          # Phase 0: async, httpx, pytest, MCP, config, quality patterns
├── data-model.md        # Phase 1: notebook sections + project file changes
├── quickstart.md        # Phase 1: how to verify notebook + project
├── contracts/
│   └── api-extensions.yaml  # Phase 1: project extensions (no new API endpoints)
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (created by /speckit.tasks)
```

### Source Code (repository root)

```text
lectures/07-integrations-async-mcp/
├── lecture-07.ipynb              # Main lecture notebook
├── assets/                       # Images, diagrams used in notebook
│   ├── event-loop.png           # Async event loop diagram
│   ├── mcp-data-flow.png        # LLM → MCP protocol → Google Keep flow
│   └── memes/                    # Meme images (2 minimum)
└── notes-api/                    # Extended Lecture 6 project (COPIED, not symlinked)
    ├── pyproject.toml            # Updated: +pydantic-settings, +pytest
    ├── .env.example              # NEW: template with placeholder env vars
    ├── .env                      # NEW: local env vars (gitignored)
    ├── Makefile                  # NEW: check/fix/test targets
    ├── app/
    │   ├── __init__.py
    │   ├── main.py               # Updated: import settings
    │   ├── config.py             # NEW: Settings class with pydantic-settings
    │   ├── routers/
    │   │   ├── __init__.py
    │   │   ├── health.py         # Unchanged from Lecture 6
    │   │   └── notes.py          # Unchanged (already async)
    │   ├── schemas/
    │   │   ├── __init__.py
    │   │   ├── notes.py          # Unchanged from Lecture 6
    │   │   └── common.py         # Unchanged from Lecture 6
    │   └── services/
    │       └── __init__.py       # Empty — placeholder for Lecture 8
    └── tests/
        ├── __init__.py           # NEW: test package
        ├── test_health.py        # NEW: health endpoint test
        └── test_notes.py         # NEW: notes tests + monkeypatch example
```

**Structure Decision**: Lecture 7 content lives under `lectures/07-integrations-async-mcp/`. The Lecture 6 `notes-api` project is copied into this directory and extended with config, tests, and Makefile. This gives students a clean snapshot showing "before (L6) vs after (L7)" while keeping each lecture self-contained. The `services/` directory remains empty — DB integration happens in Lecture 8.

## Notebook Sections — Detailed Content Plan

### Section 0: Header + Prerequisites (2 min)

- Lecture number, title, date
- Prerequisites: Lecture 6 (FastAPI project with stub endpoints, MCP concepts, ruff/black)
- Required tools: Python 3.13+, pipx, MCP-compatible LLM client
- Bridge from L6: "Your FastAPI skeleton is ready. Today we bring it to life with async, real HTTP calls, tests, and a working MCP server."

### Section 1: Learning Objectives (2 min)

5 measurable outcomes:
1. Explain what an event loop does and convert sync endpoints to async
2. Make HTTP requests with httpx (sync and async) with proper error handling
3. Manage configuration with .env files and a typed settings object
4. Install and run an MCP server (keep-mcp) and connect it to an LLM client
5. Write basic pytest tests for FastAPI endpoints and mock external dependencies

### Section 2: Async Essentials (15 min)

**Visuals**: Event loop diagram — single thread processing multiple I/O tasks

**Content**:
- The waiter analogy: sync waiter waits at kitchen for each dish; async waiter takes other orders while kitchen cooks
- `time.sleep(2)` vs `asyncio.sleep(2)` — blocking vs non-blocking demo
- `def` vs `async def` in FastAPI: sync runs in threadpool, async runs on event loop
- Converting a sync endpoint to async: add `async`, use `await` for I/O
- Critical rule: NEVER use blocking calls inside `async def` (no `requests.get()`, no `time.sleep()`)
- Show existing L6 endpoints — they're already `async def` but use no I/O, so no practical difference yet
- Meme opportunity: "blocking call inside async def" disaster meme

**Code examples** (3):
1. `asyncio.sleep()` demo showing non-blocking behavior
2. Side-by-side: sync endpoint with `time.sleep` vs async endpoint with `asyncio.sleep`
3. Simple async function with `await`

### Section 3: HTTP Client with httpx (12 min)

**Content**:
- Why httpx? Same API for sync and async; already in our project; powers TestClient
- Sync: `httpx.get("https://jsonplaceholder.typicode.com/posts/1")` → parse `.json()`
- Async: `async with httpx.AsyncClient() as client: await client.get(url)`
- Timeout: `httpx.get(url, timeout=5.0)` — what happens when timeout expires
- Error handling: `response.raise_for_status()`, catching `httpx.HTTPStatusError`, `httpx.TimeoutException`
- Connection to FastAPI: how your endpoints can call external APIs using httpx

**Code examples** (2):
1. Sync httpx GET request to JSONPlaceholder with JSON parsing
2. Async httpx request with timeout and error handling

### Section 4: Config Basics (8 min)

**Content**:
- Problem: hardcoded values scattered across code (port, debug flag, credentials)
- Simple way: `python-dotenv` + `os.getenv()` (brief, 2 min)
- Better way: `pydantic-settings` — typed settings with validation
- Create `config.py` with `Settings` class
- Create `.env` file + `.env.example`
- Add `.env` to `.gitignore`
- Import `settings` in `main.py`

**Code examples** (2):
1. python-dotenv simple example (os.getenv)
2. pydantic-settings Settings class with .env loading

### Section 5: Practical MCP — keep-mcp Setup (15 min)

**Visuals**: Data flow diagram — LLM Client → MCP Protocol → keep-mcp server → Google Keep API

**Content**:
- Brief recap (2 sentences max): "In Lecture 6 we learned MCP architecture and primitives. Now we set it up for real."
- Step 1: Install keep-mcp — `pipx install keep-mcp`
- Step 2: Obtain Google master token — link to gkeepapi docs, step-by-step with screenshots
- Security warning: NEVER commit tokens, NEVER share them, store in .env
- Step 3: Configure LLM client — show Claude Desktop config JSON (primary), mention Cursor/Gemini as alternatives
- Step 4: Test connection — ask LLM to "list my Google Keep notes"
- Live demo (screenshots/transcript): search notes, read a note, create a note (3 tool invocations per FR-006)
- Troubleshooting: auth failures, network issues, client config errors

**Exercise 1**: Configure and run the keep-mcp MCP server. Verify connection by asking your LLM to list notes. (Solution: step-by-step config JSON + expected output)

### Section 6: Safety Mindset (5 min)

**Content**:
- Recap from L6: keep-mcp's `keep-mcp` label scoping (safe mode)
- Why safe defaults matter: AI can take unintended actions
- `UNSAFE_MODE=true` — what it unlocks, why it's risky
- Principle of least privilege: give tools only the access they need
- Credential hygiene: env vars > hardcoding, .gitignore, .env.example pattern
- Connect to config section: "This is why we use Settings + .env — credentials never touch code"

### Section 7: Testing with pytest (15 min)

**Content**:
- Why test? Catch bugs before they reach users; confidence to refactor
- pytest basics: `test_*.py` files, `test_*` functions, `assert` keyword
- Install: `uv add --dev pytest` (update pyproject.toml)
- FastAPI TestClient: wraps ASGI app, sends requests without running server
- Test 1: `test_health_returns_200` — GET /health, assert 200
- Test 2: `test_create_note_returns_201` — POST /notes/create with valid body
- Test 3: `test_create_note_invalid_returns_422` — POST with empty body
- monkeypatch: temporarily replace a function for one test
- Mock example: replace `httpx.get` with a fake response to test without network
- Integration test flag concept (brief): `pytest -m "not integration"` to skip slow tests
- Run: `uv run pytest` — all green

**Code examples** (3):
1. test_health.py — minimal GET test
2. test_notes.py — POST test with valid/invalid data
3. monkeypatch mock example

**Exercise 2**: Write a test for the POST /notes/search endpoint that verifies: (a) 200 status, (b) returns empty results list, (c) response matches NoteSearchResult schema. (Solution: hidden cell)

### Section 8: Quality Workflow (5 min)

**Content**:
- Problem: running ruff, black, pytest separately is tedious
- Solution: Makefile with `check`, `fix`, `test` targets
- Show Makefile contents (3 targets)
- Demo: `make check` runs all three in sequence
- Why this matters: run before every commit; CI/CD pipelines do the same
- Windows note: install make via `choco install make` or use `bash scripts/check.sh` fallback
- Meme opportunity: "works on my machine" vs "make check passes"

**Code example** (1):
1. Makefile contents + `make check` output

### Section 9: Summary (3 min)

Key takeaways as bullet list:
- async/await makes I/O non-blocking — never block the event loop
- httpx for HTTP requests — same API sync and async
- pydantic-settings for typed, validated configuration
- MCP turns AI concepts into real tools — keep-mcp connects LLM to Google Keep
- Safe defaults and credential hygiene protect you and your users
- pytest + TestClient for fast, isolated endpoint tests
- Makefile ties quality checks into one repeatable command

### Section 10: What's Next (2 min)

Bridge: "Your project has async endpoints, tests, and a quality workflow. Next: real data persistence."
Bullets:
- Docker: containers for reproducible environments
- PostgreSQL: real database for your notes
- docker compose: FastAPI + Postgres in one command
- Connection strings, config separation (building on today's Settings pattern)

### Section 11: References (1 min)

Links to: Python asyncio docs, httpx docs, FastAPI async docs, pydantic-settings docs, pytest docs, keep-mcp repo, gkeepapi docs, MCP official docs, ruff docs, GNU Make manual.

## Complexity Tracking

No violations — no complexity tracking needed.
