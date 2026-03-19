# Quickstart: Lecture 7 Verification

## Prerequisites

- Python 3.13+
- Jupyter Notebook / JupyterLab
- pipx installed (`pip install pipx`)
- Lecture 6 notes-api project working (`lectures/06-web-fastapi-mcp/notes-api/`)
- An MCP-compatible LLM client (Claude Desktop recommended)
- Google account with Google Keep enabled

## Verification Checklist

### 1. Notebook Opens and Runs

```bash
cd lectures/07-integrations-async-mcp/
jupyter notebook lecture-07.ipynb
```

- [ ] Notebook opens without errors
- [ ] All cells execute sequentially in a clean kernel
- [ ] Ukrainian text renders correctly
- [ ] Memes and diagrams display properly

### 2. Async Code Examples Work

- [ ] `asyncio.sleep()` vs `time.sleep()` demo shows non-blocking behavior
- [ ] Sync-to-async endpoint conversion example runs
- [ ] httpx sync request returns JSON from JSONPlaceholder
- [ ] httpx async request with timeout works

### 3. Config Setup

```bash
cd lectures/07-integrations-async-mcp/notes-api/
# After adding pydantic-settings
uv sync
```

- [ ] `pydantic-settings` installs via `uv add pydantic-settings`
- [ ] `.env.example` exists with placeholder values
- [ ] `Settings()` loads values from `.env` file
- [ ] Missing required env var raises validation error

### 4. MCP Server Setup

```bash
pipx install keep-mcp
# Or: pipx run keep-mcp (one-time run)
```

- [ ] keep-mcp installs via pipx without errors
- [ ] LLM client config JSON is correct
- [ ] Server connects to Google Keep (with valid credentials)
- [ ] At least one tool call works (e.g., listing notes)

### 5. Testing

```bash
cd lectures/07-integrations-async-mcp/notes-api/
uv run pytest
```

- [ ] `pytest` is in dev dependencies
- [ ] `tests/test_health.py` passes
- [ ] `tests/test_notes.py` passes
- [ ] Monkeypatch mock test passes

### 6. Quality Workflow

```bash
cd lectures/07-integrations-async-mcp/notes-api/
make check
```

- [ ] `ruff check .` passes (zero violations)
- [ ] `black --check .` passes (already formatted)
- [ ] `pytest` passes (all tests green)
- [ ] `make fix` auto-fixes formatting

### 7. Content Completeness

- [ ] Learning objectives present (4-6 outcomes)
- [ ] Prerequisites reference Lecture 6
- [ ] 7 major content sections present (async, httpx, config, MCP, safety, testing, quality)
- [ ] At least 5 runnable code examples
- [ ] At least 2 exercises with solutions
- [ ] At least 2 memes/humor elements
- [ ] At least 2 diagrams/visuals
- [ ] Summary section present
- [ ] "What's Next" previews Lecture 8 (Docker, PostgreSQL)
- [ ] References section with links to official docs
- [ ] All text in Ukrainian with English terms in parentheses
- [ ] Duration fits ~1.5 hours
