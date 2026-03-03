# Quickstart: Lecture 6 — Web Fundamentals & FastAPI

## Prerequisites

- Python 3.13+ installed
- Jupyter Notebook / JupyterLab / VS Code with Jupyter extension
- `uv` installed (`pip install uv` or `pipx install uv`)
- Lectures 1–5 completed (OOP, modules, file I/O concepts)

## Running the Lecture Notebook

```bash
# Navigate to the lecture directory
cd lectures/06-web-fastapi-mcp/

# Open the notebook
jupyter notebook lecture-06.ipynb
# or: jupyter lab lecture-06.ipynb
# or: open in VS Code
```

Execute cells top-to-bottom. The http.server demo (Section 4) requires manual stop (Ctrl+C or kernel restart).

## Running the FastAPI Project

```bash
# Navigate to the project directory (created during lecture)
cd lectures/06-web-fastapi-mcp/notes-api/

# Install dependencies
uv sync

# Start the dev server
uvicorn app.main:app --reload

# Server runs at http://localhost:8000
# Swagger docs at http://localhost:8000/docs
```

## Testing the Endpoints

```bash
# Health check
curl http://localhost:8000/health

# Create a note (stub)
curl -X POST http://localhost:8000/notes/create \
  -H "Content-Type: application/json" \
  -d '{"title": "Test", "content": "Hello!", "tags": ["demo"]}'

# Search notes (stub)
curl -X POST http://localhost:8000/notes/search \
  -H "Content-Type: application/json" \
  -d '{"query": "test", "limit": 5}'

# Trigger validation error (missing title)
curl -X POST http://localhost:8000/notes/create \
  -H "Content-Type: application/json" \
  -d '{"content": "No title"}'
```

## Code Quality Check

```bash
cd lectures/06-web-fastapi-mcp/notes-api/

# Lint
ruff check .

# Format check
black --check .
```

## Verification Checklist

- [ ] Notebook opens and all cells execute without errors
- [ ] `uv sync` installs dependencies successfully
- [ ] `uvicorn app.main:app --reload` starts server on port 8000
- [ ] GET /health returns `{"status": "ok", "version": "0.1.0"}`
- [ ] POST /notes/create with valid body returns 201
- [ ] POST /notes/search returns 200 with empty results
- [ ] Invalid input returns 422 with ErrorResponse shape
- [ ] /docs shows Swagger UI with all endpoints
- [ ] `ruff check .` passes
- [ ] `black --check .` passes
