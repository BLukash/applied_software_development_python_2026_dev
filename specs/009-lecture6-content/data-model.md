# Data Model: Lecture 6 — Web Fundamentals & FastAPI

**Date**: 2026-03-03
**Feature**: 009-lecture6-content

## Overview

This lecture has two data model contexts:
1. **Notebook structure** — the Jupyter notebook cells and sections (educational content)
2. **FastAPI project schemas** — the Pydantic models used in the stub API project

## Notebook Structure Model

### Sections (ordered)

| # | Section | Type | Est. Duration | Key Content |
|---|---------|------|---------------|-------------|
| 0 | Header + Prerequisites | markdown | 3 min | Title, date, links to Lectures 1–5 |
| 1 | Learning Objectives | markdown | 2 min | 5 measurable outcomes |
| 2 | Web Server Basics | markdown + code | 12 min | Client/server, request-response, ports, diagrams |
| 3 | HTTP Essentials | markdown + code | 15 min | Methods, status codes, headers/body, JSON, path vs query, curl |
| 4 | Raw HTTP Demo | code + markdown | 5 min | http.server motivation demo |
| 5 | REST Essentials | markdown | 10 min | Resources, CRUD mapping, idempotency, error payload shape |
| 6 | FastAPI Basics | markdown + code | 15 min | App, routers, endpoints, params (path/query/body) |
| 7 | Pydantic Schemas | markdown + code | 12 min | Request/response models, validation (422), HTTPException |
| 8 | OpenAPI/Swagger + uvicorn | markdown + code | 5 min | Auto-docs demo, running dev server |
| 9 | Project Bootstrap | markdown + code | 15 min | uv init/sync, project structure, ruff + black |
| 10 | MCP Introduction | markdown | 10 min | Architecture, primitives, keep-mcp example, visuals |
| 11 | Summary | markdown | 3 min | Key takeaways bullet list |
| 12 | What's Next | markdown | 2 min | Preview Lecture 7 topics |
| 13 | References | markdown | 1 min | Official docs links |

**Total**: ~110 min (fits 1.5-hour slot with buffer for questions)

### Exercise Slots

| Exercise | After Section | Duration | Description |
|----------|--------------|----------|-------------|
| Exercise 1 | Section 7 (Pydantic) | 10 min | Define a Pydantic schema for a `Book` resource with validation |
| Exercise 2 | Section 9 (Project) | 15 min | Add a new endpoint (e.g., GET /notes/{id}) to the project |

## FastAPI Project Schemas (Pydantic Models)

### Entity: Note

The central resource for the stub API.

**NoteCreate (request body for POST /notes/create):**

| Field | Type | Required | Validation | Description |
|-------|------|----------|------------|-------------|
| title | string | yes | min_length=1, max_length=200 | Note title |
| content | string | yes | min_length=1 | Note body text |
| tags | list of strings | no | default=[] | Optional categorization tags |

**NoteResponse (response body):**

| Field | Type | Description |
|-------|------|-------------|
| id | string (UUID) | Unique identifier (stub: hardcoded) |
| title | string | Note title |
| content | string | Note body text |
| tags | list of strings | Tags |
| created_at | datetime (ISO) | Creation timestamp (stub: current time) |

### Entity: NoteSearchQuery

**NoteSearchQuery (request body for POST /notes/search):**

| Field | Type | Required | Default | Description |
|-------|------|----------|---------|-------------|
| query | string | no | "" | Search text |
| tags | list of strings | no | [] | Filter by tags |
| limit | integer | no | 10 | Max results (1–100) |

**NoteSearchResult (response body):**

| Field | Type | Description |
|-------|------|-------------|
| results | list of NoteResponse | Matching notes (stub: empty list) |
| total | integer | Total count (stub: 0) |

### Entity: HealthStatus

**HealthStatus (response body for GET /health):**

| Field | Type | Description |
|-------|------|-------------|
| status | string | Always "ok" |
| version | string | API version (e.g., "0.1.0") |

### Entity: ErrorResponse

**ErrorResponse (consistent error payload for all 4xx/5xx):**

| Field | Type | Description |
|-------|------|-------------|
| detail | string | Human-readable error message |
| error_code | string | Machine-readable code (e.g., "NOT_FOUND", "VALIDATION_ERROR") |

### Relationships

```text
NoteCreate ──creates──> NoteResponse
NoteSearchQuery ──searches──> NoteSearchResult (contains list of NoteResponse)
All endpoints ──on error──> ErrorResponse
GET /health ──returns──> HealthStatus
```

### State Transitions

None — this is a stateless stub API. No persistence, no state changes.
All responses return hardcoded/empty data.
