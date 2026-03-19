# Data Model: Lecture 7 — Notebook Sections & Project Extensions

This is an educational content feature. The "data model" maps to (A) notebook section structure and (B) files added/modified in the Lecture 6 FastAPI project.

## A. Notebook Section Map

| # | Section Title | Duration | Code Examples | Exercises | Visuals | FR Coverage |
|---|---------------|----------|---------------|-----------|---------|-------------|
| 0 | Header + Prerequisites | 2 min | 0 | 0 | 0 | FR-002 |
| 1 | Learning Objectives | 2 min | 0 | 0 | 0 | FR-001 |
| 2 | Async Essentials | 15 min | 3 (sleep demo, sync endpoint, async endpoint) | 0 | 1 (event loop diagram) | FR-003 |
| 3 | HTTP Client with httpx | 12 min | 2 (sync request, async request with timeout) | 0 | 0 | FR-004 |
| 4 | Config Basics | 8 min | 2 (dotenv simple, pydantic-settings) | 0 | 0 | FR-005 |
| 5 | Practical MCP: keep-mcp Setup | 15 min | 0 (command-line only) | 1 (configure + run MCP server) | 1 (data flow diagram) | FR-006, FR-007, FR-017 |
| 6 | Safety Mindset | 5 min | 0 | 0 | 0 | FR-007 |
| 7 | Testing with pytest | 15 min | 3 (health test, POST test, monkeypatch mock) | 1 (write a test for search endpoint) | 0 | FR-008 |
| 8 | Quality Workflow | 5 min | 1 (Makefile + run demo) | 0 | 0 | FR-009 |
| 9 | Summary | 3 min | 0 | 0 | 0 | FR-014 |
| 10 | What's Next | 2 min | 0 | 0 | 0 | FR-014 |
| 11 | References | 1 min | 0 | 0 | 0 | — |
| **Total** | | **~85 min** | **11** | **2** | **2** | |

**Validation against FR-018**: 11 code examples > 5 minimum. PASS.
**Validation against FR-010**: 2 exercises. PASS.
**Validation against FR-011**: 2+ memes distributed across sections 2, 5, 7. PASS (planned).
**Validation against FR-012**: 2 visuals (event loop + MCP data flow). PASS.

## B. Project File Changes (Lecture 6 → Lecture 7)

### New Files

| File | Purpose | Section |
|------|---------|---------|
| `notes-api/app/config.py` | Settings object with pydantic-settings, reads .env | Section 4 |
| `notes-api/.env.example` | Template with placeholder env vars | Section 4 |
| `notes-api/.env` | Local env vars (gitignored) | Section 4 |
| `notes-api/tests/__init__.py` | Test package marker | Section 7 |
| `notes-api/tests/test_health.py` | Health endpoint test | Section 7 |
| `notes-api/tests/test_notes.py` | Notes endpoints tests + monkeypatch example | Section 7 |
| `notes-api/Makefile` | Quality workflow: check, fix, test targets | Section 8 |

### Modified Files

| File | Change | Section |
|------|--------|---------|
| `notes-api/pyproject.toml` | Add `pydantic-settings` to deps, `pytest` to dev deps | Sections 4, 7 |
| `notes-api/app/main.py` | Import settings, optionally use in app title/debug | Section 4 |
| `notes-api/app/routers/notes.py` | Convert `async def` endpoints (already async — demonstrate awareness) | Section 2 |

### Unchanged Files

| File | Reason |
|------|--------|
| `notes-api/app/schemas/*.py` | Pydantic schemas from Lecture 6 — no changes needed |
| `notes-api/app/routers/health.py` | Already minimal, no changes needed |
| `notes-api/app/services/__init__.py` | Remains empty placeholder (DB integration in Lecture 8) |

## C. Key Entities (from spec)

### Settings Object
- **Fields**: `app_name: str`, `debug: bool`, `port: int`, `google_email: str | None`, `google_master_token: str | None`
- **Source**: `.env` file, environment variables, defaults
- **Validation**: pydantic-settings auto-validates types
- **Usage**: Imported as singleton `settings = Settings()` in `config.py`

### Test Suite
- **Framework**: pytest (no plugins)
- **Test count**: 3-4 tests minimum
- **Mocking**: monkeypatch only (no fixtures, no mock.patch)
- **Runner**: `pytest` or `make test`

### Makefile Targets
- `check`: `ruff check . && black --check . && pytest`
- `fix`: `ruff check --fix . && black .`
- `test`: `pytest`
