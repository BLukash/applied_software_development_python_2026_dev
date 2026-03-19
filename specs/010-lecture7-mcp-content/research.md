# Research: Lecture 7 — Python Web Server Integrations

## 1. Async in FastAPI — Teaching Approach

**Decision**: Use the "restaurant waiter" analogy for event loop intuition. Teach sync-to-async conversion pattern on existing Lecture 6 endpoints.

**Rationale**: The waiter analogy is universally understood — a sync waiter stands at the kitchen waiting for one dish; an async waiter takes orders from other tables while the kitchen cooks. One waiter (one thread) serves many tables by not standing idle during I/O.

**Key teaching sequence**:
1. Show `time.sleep()` vs `asyncio.sleep()` — blocking vs non-blocking
2. Convert existing sync Lecture 6 endpoint to `async def`
3. Critical rule: never use blocking calls (e.g., `requests.get()`) inside `async def`
4. Show only endpoint-level async — skip `asyncio.gather`, `create_task`, `async for`

**Alternatives considered**:
- Coffee shop analogy — less universal
- Thread pool diagram — too technical for first exposure
- Full asyncio tutorial — too deep for 1.5h lecture with 6 other topics

## 2. httpx — Sync vs Async HTTP Client

**Decision**: Use httpx for all HTTP client examples. Already in Lecture 6 pyproject.toml as dev dependency.

**Rationale**: httpx has identical sync/async API shapes, is the underlying client for FastAPI TestClient, and mirrors the familiar `requests` library. Perfect for teaching the sync-to-async transition.

**Demo APIs (no auth, reliable)**:
- JSONPlaceholder (`https://jsonplaceholder.typicode.com`) — fake REST with /posts, /users, /todos
- httpbin.org — echoes back request data, great for showing headers/params

**Key teaching points**:
- `httpx.get(url)` (sync) → `await client.get(url)` (async)
- `httpx.Client()` → `httpx.AsyncClient()` (context managers)
- Timeout configuration: `httpx.get(url, timeout=5.0)`
- Error handling: `response.raise_for_status()`, `httpx.TimeoutException`

**Alternatives considered**:
- `requests` library — no async support, would need two libraries
- `aiohttp` — different API shape from sync, steeper learning curve

## 3. pytest + FastAPI TestClient — Minimal Setup

**Decision**: Minimal pytest with monkeypatch only. No fixtures, no parameterization, no unittest.mock.

**Rationale**: First pytest exposure for students. Three tests in one file is sufficient: (1) GET endpoint, (2) POST endpoint, (3) monkeypatch mock of external call. TestClient wraps ASGI app and handles async endpoints transparently — no pytest-asyncio needed.

**Key pattern**:
```python
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_create_note():
    response = client.post("/notes/create", json={"title": "Test", "content": "Body", "tags": []})
    assert response.status_code == 201

def test_with_mock(monkeypatch):
    monkeypatch.setattr(httpx, "get", lambda *a, **kw: MockResponse(...))
    response = client.get("/weather")
    assert response.json()["temp"] == 20
```

**Alternatives considered**:
- `unittest.mock.patch` — decorator/context manager pattern is more complex
- `pytest.fixture` — powerful but adds conceptual overhead for first exposure
- `pytest-asyncio` — not needed since TestClient handles async transparently

## 4. keep-mcp + LLM Client Setup

**Decision**: Demo with Claude Desktop as primary MCP client. Mention Cursor and Gemini CLI as alternatives.

**Rationale**: Claude Desktop has the most mature and well-documented MCP support. Gemini has announced MCP support but documentation is thinner and changes frequently. Cursor is a viable alternative students may already use. keep-mcp is installable via pipx (`pipx run keep-mcp`).

**Setup steps**:
1. Install: `pipx install keep-mcp` (or `pipx run keep-mcp`)
2. Obtain Google master token via gkeepapi auth flow
3. Configure LLM client JSON with command + env vars
4. Test: ask LLM to "list my Google Keep notes"

**Auth challenge**: Google master token requires a separate OAuth flow. The notebook must include step-by-step instructions and fallback (instructor demo) for students who can't complete auth.

**Claude Desktop config** (`claude_desktop_config.json`):
```json
{
  "mcpServers": {
    "keep-mcp": {
      "command": "pipx",
      "args": ["run", "keep-mcp"],
      "env": {
        "GOOGLE_EMAIL": "your-email@example.com",
        "GOOGLE_MASTER_TOKEN": "your-token"
      }
    }
  }
}
```

**Alternatives considered**:
- Gemini as primary — MCP support less mature, docs in flux
- VS Code + Continue — more setup steps, less direct interaction
- Building custom MCP server — out of scope for this lecture

## 5. Config Basics — .env and Settings Object

**Decision**: Show python-dotenv first (3 min), then pydantic-settings as the "FastAPI way" (7 min). Use pydantic-settings for the project.

**Rationale**: Showing the simple way first (dotenv + os.getenv) builds motivation for why a typed settings object is better. pydantic-settings is the officially recommended pattern for FastAPI, provides validation, type conversion, and IDE autocompletion.

**Minimal pydantic-settings example**:
```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Notes API"
    debug: bool = False
    port: int = 8000

    model_config = {"env_file": ".env"}

settings = Settings()
```

**Dependency**: `pydantic-settings` needs to be added to the project (`uv add pydantic-settings`).

**Security teaching points**: Always `.gitignore` the `.env` file. Ship `.env.example` with placeholder values. Never hardcode credentials.

**Alternatives considered**:
- python-dotenv only — no validation, no types, no IDE support
- dynaconf — overkill for this context
- Raw `os.environ` — too low-level, no defaults

## 6. Quality Workflow — Single Command

**Decision**: Use a Makefile with three targets: `make check`, `make fix`, `make test`. Include Windows fallback instructions (Git Bash + make, or a simple bash script).

**Rationale**: Makefile is the most transparent option — students see exactly what runs. It teaches a transferable skill (make is universal in open-source projects). The targets are:
- `make check` = `ruff check . && black --check . && pytest`
- `make fix` = `ruff check --fix . && black .`
- `make test` = `pytest`

**Windows note**: `make` is not installed by default. Options: (1) `choco install make`, (2) use Git Bash with make from MSYS2, (3) fallback: `bash scripts/check.sh` with equivalent commands.

**Alternatives considered**:
- pyproject.toml scripts via Hatch — adds Hatch dependency
- pre-commit hooks — too complex for lecture setting, mention as "real project" pattern
- Python subprocess script — works but less readable than Makefile
- Drop black, use `ruff format` — possible simplification, but Lecture 6 already teaches both tools separately
