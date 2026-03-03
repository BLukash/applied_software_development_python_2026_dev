# Feature Specification: Lecture 6 — Web Fundamentals & FastAPI: API Skeleton + MCP Introduction

**Feature Branch**: `009-lecture6-content`
**Created**: 2026-03-03
**Status**: Draft
**Input**: User description: "Implement Lecture 6. Outcome: students understand what a web server/API is, can build a clean FastAPI skeleton with proper HTTP/REST behavior, and can explain what MCP is and why it exists (conceptually). Deliverable: a runnable FastAPI project with Pydantic schemas + stub endpoints + Swagger docs, formatted/linted, bootstrapped with uv. Non-goals: no real external API calls, no MCP integration, no persistence. Must-have user-facing capabilities: GET /health works, POST /notes/search and POST /notes/create exist as stubs, Swagger/OpenAPI is available and readable, students can run uv sync + uvicorn."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Lecture Notebook Delivery (Priority: P1)

A student opens the Lecture 6 Jupyter notebook and follows along during a 1.5-hour session. They read explanatory text in Ukrainian that introduces web server concepts (client/server, request-response, ports), HTTP essentials (methods, status codes, headers/body, JSON, path vs query), a tiny raw HTTP demo with http.server, REST essentials (resources, CRUD mapping, idempotency, consistent error payloads), FastAPI basics (app, routers, endpoints, path/query/body params), Pydantic schemas (request vs response, validation, HTTPException), OpenAPI/Swagger, project bootstrapping with uv, tooling (ruff + black), and MCP concepts (host/client/server, tools/resources/prompts with keep-mcp as a conceptual example). The notebook contains runnable code cells, exercises, memes, and diagrams that build understanding progressively.

**Why this priority**: The notebook is the primary deliverable — without it, there is no lecture. All other stories depend on this content existing.

**Independent Test**: Can be fully tested by opening the notebook in Jupyter, reading all cells top-to-bottom, and verifying all code cells execute without errors.

**Acceptance Scenarios**:

1. **Given** a student with Python 3.11+ and Jupyter installed, **When** they open the Lecture 6 notebook, **Then** they see a structured lecture with learning objectives, 10 major content sections, exercises, a summary, and references.
2. **Given** a student reading the notebook, **When** they execute all code cells sequentially in a clean kernel, **Then** every cell runs without errors.
3. **Given** a student who completed Lectures 1–5, **When** they read Lecture 6, **Then** they encounter prerequisites linking to prior lectures, no repeated content, and consistent tone/terminology.
4. **Given** a student reading the MCP section, **When** they finish the section, **Then** they can explain what MCP is (host/client/server architecture), name its three primitives (tools, resources, prompts), and articulate why MCP exists — without needing to run any MCP code.

---

### User Story 2 - Runnable FastAPI Project (Priority: P2)

A student follows the project bootstrap section of the notebook to create a FastAPI project from scratch. They run `uv init` and `uv sync`, then launch the dev server with `uvicorn`. The project has a clean structure (app/routers/schemas/services/clients), Pydantic request/response schemas, stub endpoints (GET /health, POST /notes/search, POST /notes/create) with correct status codes and error shapes, and auto-generated Swagger/OpenAPI docs. The code is formatted with black and linted with ruff.

**Why this priority**: The runnable project is the practical deliverable students take away. It demonstrates real-world FastAPI patterns and gives students a codebase to extend in Lecture 7.

**Independent Test**: Can be fully tested by following the bootstrap steps, running `uv sync && uvicorn app.main:app --reload`, hitting each endpoint, and opening /docs.

**Acceptance Scenarios**:

1. **Given** a student with Python 3.13+ and uv installed, **When** they follow the project bootstrap steps, **Then** `uv sync` succeeds and all dependencies are installed.
2. **Given** the project is bootstrapped, **When** the student runs `uvicorn app.main:app --reload`, **Then** the server starts on port 8000 without errors.
3. **Given** the server is running, **When** the student sends GET /health, **Then** they receive a 200 response with a JSON body indicating the service is healthy.
4. **Given** the server is running, **When** the student sends POST /notes/create with a valid JSON body, **Then** they receive a 201 response with the created note stub data matching the response schema.
5. **Given** the server is running, **When** the student sends POST /notes/search with a valid query body, **Then** they receive a 200 response with a list matching the response schema (empty or stub data).
6. **Given** the server is running, **When** the student sends a request with invalid data (e.g., missing required fields), **Then** they receive a 422 response with a consistent error payload shape.
7. **Given** the server is running, **When** the student opens /docs in a browser, **Then** they see a readable Swagger UI with all endpoints, schemas, and example payloads documented.
8. **Given** the project code, **When** `ruff check .` and `black --check .` are run, **Then** both pass with zero violations.

---

### User Story 3 - HTTP Fundamentals Understanding (Priority: P3)

A student who has never worked with web servers runs the tiny http.server demo from the notebook. They see a raw HTTP request/response cycle in action, understand what ports are, and grasp why a framework like FastAPI exists (vs. building everything manually).

**Why this priority**: This foundational understanding makes all subsequent web topics (FastAPI, REST, APIs) meaningful rather than mechanical.

**Independent Test**: Can be tested by running the http.server demo cell in the notebook and observing the request/response in a browser or curl output.

**Acceptance Scenarios**:

1. **Given** a student with Python 3.13+, **When** they run the http.server demo cell, **Then** they see a simple HTTP server start and can send a request to it (via browser or curl instruction in the notebook).
2. **Given** the demo is running, **When** the student observes the output, **Then** the notebook explains what happened at each step (client connects, sends request, server responds, connection closes).

---

### Edge Cases

- What happens when a student runs `uv sync` without Python 3.13+? The notebook MUST include a prerequisites check cell or clear version requirements note.
- What happens when port 8000 is already in use? The notebook MUST mention the `--port` flag for uvicorn.
- What happens when a student sends a request to a non-existent endpoint? The FastAPI project MUST return a consistent error shape (not a default HTML 404).
- What happens when the http.server demo cell blocks the notebook? The notebook MUST explain how to stop the server (Ctrl+C / kernel interrupt) and consider using a background approach or separate terminal instruction.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The notebook MUST contain learning objectives at the start listing 4–6 specific, measurable outcomes covering web fundamentals, HTTP, REST, FastAPI, Pydantic, and MCP concepts
- **FR-002**: The notebook MUST include a section on web server basics explaining client/server architecture, request-response cycle, and ports with at least one diagram or visual
- **FR-003**: The notebook MUST cover HTTP essentials: methods (GET, POST, PUT, DELETE, PATCH), status codes (2xx, 4xx, 5xx families), headers/body structure, JSON as data format, and path parameters vs query parameters
- **FR-004**: The notebook MUST include a tiny raw HTTP demo using Python's built-in http.server module, with clear instructions for running and stopping it, positioned as motivation for why frameworks exist
- **FR-005**: The notebook MUST explain REST essentials: resources as nouns, CRUD-to-HTTP mapping, idempotency (which methods are idempotent and why it matters), and consistent error payload shape across all endpoints
- **FR-006**: The notebook MUST cover FastAPI basics: creating an app, organizing routers, defining endpoints, and using path, query, and body parameters — with runnable code examples
- **FR-007**: The notebook MUST explain Pydantic schemas for request and response models, demonstrate automatic validation (422 errors), and show HTTPException usage for custom error responses
- **FR-008**: The notebook MUST show how OpenAPI/Swagger docs are auto-generated and how to run the dev server with uvicorn
- **FR-009**: The notebook MUST include a project bootstrap section where students create a minimal FastAPI project using `uv init` and `uv sync`, with a clear directory structure: app/, routers/, schemas/, services/, clients/
- **FR-010**: The notebook MUST cover tooling basics: how to run ruff (lint) and black (format), with examples on the project code
- **FR-011**: The notebook MUST include an MCP introduction section (concept only, no runnable MCP code) explaining: the host/client/server architecture, the three primitives (tools, resources, prompts), and keep-mcp as a concrete example of what an MCP server looks like — students MUST understand WHY MCP exists (standardized AI-tool integration), here visuals are also required
- **FR-012**: The runnable FastAPI project MUST include a GET /health endpoint returning 200 with a JSON health status
- **FR-013**: The runnable FastAPI project MUST include a POST /notes/create endpoint as a stub accepting a request body with Pydantic validation and returning 201 with a response schema
- **FR-014**: The runnable FastAPI project MUST include a POST /notes/search endpoint as a stub accepting a query body and returning 200 with a list response schema
- **FR-015**: All stub endpoints MUST return consistent error payloads (same shape for 4xx/5xx errors) and MUST use proper HTTP status codes
- **FR-016**: The project MUST pass `ruff check .` and `black --check .` with zero violations
- **FR-017**: The notebook MUST contain at least 5 runnable code examples (excluding the project code itself)
- **FR-018**: The notebook MUST contain at least 2 practical exercises with solutions (hidden/collapsed cells)
- **FR-019**: The notebook MUST contain at least 2 relevant memes or visual humor elements maintaining educational tone
- **FR-020**: The notebook MUST contain at least 3 diagrams or visual explanation (e.g.,web-server architecture, request-response cycle, REST CRUD mapping table, MCP architecture, etc.)
- **FR-021**: The notebook MUST include a Prerequisites section referencing Lectures 1–5 (specifically OOP from Lecture 5 for understanding Pydantic models, and modules/imports from Lecture 4)
- **FR-022**: The notebook MUST end with a Summary section and a "What's Next" section previewing Lecture 7 topics (async, httpx, testing, practical MCP)
- **FR-023**: All explanatory text MUST be in Ukrainian with English technical terms in parentheses on first use
- **FR-024**: The notebook MUST NOT include any real external API calls, any MCP integration code (only conceptual explanation), or any data persistence (endpoints are stubs only)
- **FR-025**: The notebook duration MUST target 1.5 hours of lecture content

### Key Entities

- **Note**: The central resource for the stub API — has attributes like title, content, tags; used to demonstrate CRUD endpoint patterns and Pydantic schema design
- **Error Response**: A consistent error payload shape used across all endpoints — has attributes like detail/message and error code; demonstrates REST best practices
- **Health Status**: A simple status object returned by the health endpoint — has attributes like status and optional version/timestamp

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can explain in their own words what a web server does, what HTTP methods exist and when to use each, and what REST means — verified by a quick oral or written check at end of lecture
- **SC-002**: Students can create a FastAPI project from scratch using uv, run it with uvicorn, and access auto-generated Swagger docs — verified by students completing the bootstrap exercise within 20 minutes
- **SC-003**: Students can define Pydantic request/response schemas and understand that invalid input automatically returns 422 — verified by the validation exercise in the notebook
- **SC-004**: Students can articulate what MCP is (host/client/server), name its three primitives (tools, resources, prompts), and explain why it exists — verified by a brief discussion or written reflection at end of lecture
- **SC-005**: The runnable project passes all acceptance scenarios from User Story 2: GET /health returns 200, POST /notes/create returns 201, POST /notes/search returns 200, invalid input returns 422, /docs shows readable Swagger, and linting/formatting passes
- **SC-006**: The notebook contains all required structural elements: learning objectives, at least 5 runnable examples, at least 2 exercises with solutions, at least 2 memes, at least 1 diagram, summary, and references — verified by checklist review

### Assumptions

- Students have completed Lectures 1–5 and have a working Python 3.13+ environment with Jupyter
- Students have `uv` installed (or the notebook includes brief installation instructions)
- The keep-mcp example is used only as a reference/screenshot to illustrate MCP concepts — no actual MCP server is run during the lecture
- Stub endpoints return hardcoded or empty data — no in-memory storage or database is involved
- The project structure established in this lecture will be extended in Lecture 7 (async, httpx, testing, MCP integration)
