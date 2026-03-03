# Implementation Plan: Lecture 6 — Web Fundamentals & FastAPI + MCP Introduction

**Branch**: `009-lecture6-content` | **Date**: 2026-03-03 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/009-lecture6-content/spec.md`

## Summary

Create Lecture 6 as a Jupyter notebook covering web server fundamentals, HTTP essentials, REST principles, FastAPI project setup with Pydantic schemas, and a conceptual MCP introduction. The deliverable includes the notebook (~90 cells, 1.5 hours content, Ukrainian text) and a runnable FastAPI stub project bootstrapped with `uv` that has GET /health, POST /notes/create, POST /notes/search endpoints with proper validation and Swagger docs.

**Key visual emphasis**: The user specifically requested great visual explanations for complex concepts. The plan prioritizes MDN diagrams for HTTP/web concepts and custom/sourced visuals for MCP architecture.

## Technical Context

**Language/Version**: Python 3.13+ (code examples in Jupyter Notebook + standalone FastAPI project)
**Primary Dependencies**: FastAPI, Pydantic, uvicorn (project); Jupyter (notebook delivery); ruff, black (tooling)
**Storage**: N/A — stub endpoints only, no persistence
**Testing**: N/A for this lecture (testing introduced in Lecture 7)
**Target Platform**: Cross-platform (student laptops: Windows/macOS/Linux)
**Project Type**: Educational content (notebook + embedded project)
**Performance Goals**: N/A — educational stub
**Constraints**: 1.5 hours lecture duration; all code must run in clean Python 3.13+ environment
**Scale/Scope**: Single notebook (~90 cells) + single FastAPI project (~8 files)

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Gate | Status |
|-----------|------|--------|
| I. Student-Centered Design | Learning objectives at start; real-world analogies; progressive difficulty; interactive elements throughout | PASS — planned in sections 0–1; analogies in sections 2–5; exercises after sections 7, 9 |
| II. Practical Application Focus | Mini-project from Lecture 5 onward; 20–30 min in-class + homework extension | PASS — FastAPI project bootstrap (section 9, ~15 min in-class); Exercise 2 extends it (~15 min) |
| III. Progressive Skill Building | Must analyze Lecture 5 first; maintain tone; avoid repetition; cross-references | PASS — Lecture 5 analysis done (research.md §6); OOP→Pydantic bridge planned |
| IV. Quality Content Standards | Ukrainian text; 5+ code examples; 2+ exercises; 2+ memes; 3+ diagrams; summary; What's Next | PASS — all planned (see data-model.md section table) |
| V. Iterative Development | Code tested in clean env; reviewed for accuracy | PASS — quickstart.md verification checklist defined |
| Prohibited: No excessive emoji | Max 1-2 per section | PASS — following Lecture 5 pattern (💡⚠️✅❌ only) |
| Prohibited: No 3rd-party when stdlib works | http.server demo uses stdlib; FastAPI/Pydantic justified (they ARE the teaching subject) | PASS |
| Prohibited: No hallucinated facts | All claims link to official docs (MDN, FastAPI docs, MCP docs) | PASS — sources collected in research.md |

**Post-Phase 1 re-check**: All gates still pass. No violations.

## Project Structure

### Documentation (this feature)

```text
specs/009-lecture6-content/
├── plan.md              # This file
├── research.md          # Phase 0: visuals, MCP, keep-mcp, FastAPI patterns
├── data-model.md        # Phase 1: notebook sections + Pydantic schemas
├── quickstart.md        # Phase 1: how to run notebook + project
├── contracts/
│   └── api.yaml         # Phase 1: OpenAPI spec for stub endpoints
├── checklists/
│   └── requirements.md  # Spec quality checklist
└── tasks.md             # Phase 2 output (created by /speckit.tasks)
```

### Source Code (repository root)

```text
lectures/06-web-fastapi-mcp/
├── lecture-06.ipynb              # Main lecture notebook
├── assets/                       # Images, diagrams used in notebook
│   ├── client-server.svg         # MDN client-server diagram (or link)
│   ├── http-request.svg          # MDN HTTP request format
│   ├── http-response.svg         # MDN HTTP response format
│   ├── mcp-architecture.png      # MCP architecture diagram
│   └── memes/                    # Meme images (2 minimum)
└── notes-api/                    # Runnable FastAPI project
    ├── pyproject.toml            # uv project config (fastapi, uvicorn, ruff, black)
    ├── app/
    │   ├── __init__.py
    │   ├── main.py               # FastAPI app + include_router
    │   ├── routers/
    │   │   ├── __init__.py
    │   │   ├── health.py         # GET /health
    │   │   └── notes.py          # POST /notes/create, POST /notes/search
    │   ├── schemas/
    │   │   ├── __init__.py
    │   │   ├── notes.py          # NoteCreate, NoteResponse, NoteSearchQuery, NoteSearchResult
    │   │   └── common.py         # ErrorResponse, HealthStatus
    │   ├── services/
    │   │   └── __init__.py       # Empty — placeholder for Lecture 7
    │   └── clients/
    │       └── __init__.py       # Empty — placeholder for MCP client in Lecture 7
    └── README.md                 # Brief project description (optional)
```

**Structure Decision**: Educational content layout under `lectures/06-web-fastapi-mcp/`. The FastAPI project lives inside the lecture directory as `notes-api/` — it is the mini-project students build during the lecture. The `services/` and `clients/` directories are intentionally empty, establishing the pattern that Lecture 7 will fill with MCP integration and async service logic.

## Notebook Sections — Detailed Content Plan

### Section 0: Header + Prerequisites (3 min)

- Lecture number, title, date
- Prerequisites: Lectures 1–5 (specifically: OOP + `@dataclass` from L5, modules/imports from L4, functions from L3–4)
- Bridge from L5: "Your `Contact` class and JSON skills are the foundation for Pydantic models and API schemas"

### Section 1: Learning Objectives (2 min)

5 measurable outcomes:
1. Explain what a web server does and how HTTP request-response works
2. Use correct HTTP methods and status codes for CRUD operations
3. Build a FastAPI application with routers, Pydantic schemas, and auto-generated Swagger docs
4. Bootstrap a Python project with `uv` and apply `ruff`/`black` for code quality
5. Explain what MCP is, name its three primitives, and articulate why it exists

### Section 2: Web Server Basics (12 min) — VISUAL HEAVY

**Visuals (FR-020: at least 3 diagrams — this section contributes 2):**
- Client-server architecture diagram (MDN: `simple-client-server.png` or custom)
- Request-response lifecycle diagram (MDN: `client-server-chain.svg`)

**Content:**
- What is a web server? (analogy: restaurant — client=customer, server=kitchen, waiter=HTTP)
- Client sends request → server processes → server sends response
- Ports: "address of the apartment in the building" (IP = building, port = apartment)
- localhost:8000 — what each part means
- Brief: where HTTP sits in the network stack (MDN layers diagram optional)

### Section 3: HTTP Essentials (15 min)

**Content:**
- HTTP methods table (markdown — GET, POST, PUT, PATCH, DELETE with CRUD mapping)
- Status codes table (2xx, 4xx, 5xx with key codes for API work)
- Request anatomy: method + URL + headers + body
- Response anatomy: status code + headers + body
- JSON as the universal API data format (link to L5 JSON section)
- Path params vs query params: `/notes/123` vs `/notes?tag=demo`
- Quick curl demo: `curl -v http://httpbin.org/get` (shows headers live)

**Visuals**: MDN HTTP request/response format SVGs

### Section 4: Raw HTTP Demo (5 min)

**Content:**
- 3-line http.server demo (stdlib `http.server`)
- Students see: start server → open browser → see request in terminal
- "This is ALL a web server does. Now imagine adding routing, validation, JSON parsing by hand..."
- Transition: "This is why frameworks like FastAPI exist"
- Clear instructions for stopping (Ctrl+C / kernel interrupt)

### Section 5: REST Essentials (10 min)

**Content:**
- REST = Representational State Transfer (brief history, not academic)
- Resources as nouns: `/notes`, `/notes/{id}`, NOT `/getNotes`
- CRUD → HTTP mapping table (reinforces Section 3)
- Idempotency deep-dive: PUT + DELETE are idempotent, POST is not. Why it matters (retry safety)
- Consistent error payload shape: every 4xx/5xx returns same JSON structure `{detail, error_code}`
- Example: good vs bad API error responses (✅ consistent JSON vs ❌ mixed HTML/JSON)

### Section 6: FastAPI Basics (15 min)

**Content:**
- Install FastAPI + uvicorn (pip install / uv add)
- Minimal app: `app = FastAPI()` + one route
- `@app.get("/")` → `@app.post("/items")` progression
- Path parameters: `@app.get("/items/{item_id}")`
- Query parameters: `@app.get("/items?skip=0&limit=10")`
- Body parameters: `@app.post("/items")` with Pydantic model
- Routers: `APIRouter()` + `app.include_router()`
- Code cells: students run each example inline (uvicorn not needed for simple demo cells)

### Section 7: Pydantic Schemas (12 min)

**Content:**
- Pydantic BaseModel (bridge from `@dataclass` in L5 — "dataclass on steroids")
- Request model vs response model (why separate)
- Field validation: types, min/max length, default values
- Auto 422 on invalid input (demo: send bad data, see structured error)
- HTTPException for custom errors (404, 409, etc.)
- Show: how FastAPI auto-converts Pydantic models to JSON

**Exercise 1 (10 min)**: Define a `BookCreate` and `BookResponse` Pydantic schema with validation. Write a POST endpoint that accepts it.

### Section 8: OpenAPI/Swagger + uvicorn (5 min)

**Content:**
- FastAPI auto-generates OpenAPI spec → Swagger UI at `/docs`
- Show /docs screenshot or live demo
- Running: `uvicorn app.main:app --reload`
- `--reload` for development, `--port` to change port

### Section 9: Project Bootstrap (15 min)

**Content:**
- `uv init notes-api` → `cd notes-api` → `uv add fastapi uvicorn`
- Project structure walk-through (see Source Code tree above)
- Create each file step-by-step in the notebook
- `uv add --dev ruff black` → run `ruff check .` → run `black --check .`
- Final run: `uv run uvicorn app.main:app --reload`
- Test all 3 endpoints with curl commands

**Exercise 2 (15 min)**: Add a GET /notes/{note_id} endpoint that returns a hardcoded NoteResponse or 404 ErrorResponse.

### Section 10: MCP Introduction (10 min) — VISUAL HEAVY

**Visual (FR-020: contributes 1 diagram):**
- MCP architecture diagram (official `mcp-simple-diagram.png` or custom recreation)

**Content:**
- Problem statement: "Every AI tool (Claude, ChatGPT, Copilot) needs to connect to external services. Without a standard, every integration is custom."
- MCP = "USB-C for AI" analogy
- Three participants: Host → Client → Server (table)
- Three primitives: Tools (model-controlled), Resources (app-controlled), Prompts (user-controlled)
- Concrete example: keep-mcp
  - What it does: connects Claude to Google Keep
  - Tools it exposes: find, create_note, update_note, trash_note (CRUD mapping!)
  - Safety: `keep-mcp` label scoping, unsafe mode flag
  - Show the Claude Desktop config JSON snippet (no running)
- Why this matters: "In Lecture 7, you will build an MCP client wrapper and wire your FastAPI endpoints to keep-mcp tools"

### Section 11: Summary (3 min)

Key takeaways as bullet list with ✅ markers.

### Section 12: What's Next (2 min)

Bridge: "Your FastAPI project is a skeleton. In Lecture 7, we bring it to life."
Bullets:
- Async: event loop, async/await (why FastAPI uses it)
- httpx: calling external APIs from your server
- MCP practical integration: client wrapper + wire endpoints to keep-mcp
- Testing: pytest + FastAPI TestClient
- Quality workflow: lint + format + test as one routine

### Section 13: References (1 min)

Links to: MDN HTTP docs, FastAPI docs, Pydantic docs, MCP official docs, keep-mcp repo, uv docs, ruff docs.

## Complexity Tracking

No violations — no complexity tracking needed.
