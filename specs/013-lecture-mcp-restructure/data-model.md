# Data Model: Restructure Lectures 6, 7 & Add Lecture 8 (MCP Separation)

**Feature**: 013-lecture-mcp-restructure
**Date**: 2026-04-02

This feature does not introduce traditional data entities or database changes. The "data model" here is the **notebook section structure** — the content organization that defines each lecture's flow.

## Lecture 6 Section Map (Updated)

**Title**: "Web Fundamentals & FastAPI: API Skeleton"
**Directory**: `lectures/06-web-fastapi/`
**Duration**: ~100 minutes

| # | Section | Duration | Status |
|---|---------|----------|--------|
| 0 | Header + Prerequisites (L1-L5) | 3 min | KEEP as-is |
| 1 | Learning Objectives (remove MCP objective) | 2 min | MODIFY |
| 2 | Web Server Basics (client/server, request-response, ports) | 12 min | KEEP as-is |
| 3 | HTTP Essentials (methods, status codes, headers, JSON, params, curl) | 15 min | KEEP as-is |
| 4 | Raw HTTP Demo (http.server) | 5 min | KEEP as-is |
| 5 | REST Essentials (resources, CRUD, idempotency, error payloads) | 10 min | EXPAND: add real-world API example (~3 min) |
| 6 | FastAPI Basics (app, routers, endpoints, params) | 15 min | KEEP as-is |
| 7 | Pydantic Schemas (request/response, validation, HTTPException) + Exercise 1 (Book schema) | 12+10 min | KEEP as-is |
| 8 | OpenAPI/Swagger + uvicorn | 5 min | KEEP as-is |
| 9 | Project Bootstrap (uv init, structure, ruff + black) + Exercise 2 (GET endpoint) | 15+15 min | MODIFY: remove clients/ from structure table |
| ~~10~~ | ~~MCP — Model Context Protocol~~ | ~~10 min~~ | **REMOVE entirely** |
| 10 | Exercise 3: DELETE /notes/{note_id} endpoint (NEW) | 7 min | **NEW** |
| 11 | Summary | 3 min | KEEP as-is |
| 12 | What's Next (update: async, httpx, testing, quality) | 2 min | MODIFY: remove MCP references |
| 13 | References | 1 min | MODIFY: remove MCP references if any |

**Changes summary**: Remove Section 10 (MCP), add Exercise 3 (DELETE endpoint), expand REST section, update learning objectives and What's Next.

## Lecture 7 Section Map (Updated)

**Title**: "Async, HTTPX, Testing & Quality Workflow"
**Directory**: `lectures/07-async-testing/`
**Duration**: ~90 minutes

| # | Section | Duration | Status |
|---|---------|----------|--------|
| 0 | Header + Prerequisites (L6) | 2 min | MODIFY: remove MCP from prereqs |
| 1 | Learning Objectives (remove MCP objective) | 2 min | MODIFY |
| 2 | Async Essentials (event loop, async/await, threads vs asyncio, GIL) | 15 min | KEEP as-is |
| 2b | Async Exercise: convert sync endpoint + httpx external call (NEW) | 10 min | **NEW** |
| 3 | HTTP Client with httpx (sync/async, timeouts, errors) | 12 min | KEEP as-is |
| 4 | Config Basics (.env, pydantic-settings) | 8 min | KEEP as-is |
| ~~5~~ | ~~Practical MCP (keep-mcp setup, auth, lifecycle, transports)~~ | ~~15 min~~ | **REMOVE entirely** |
| ~~6~~ | ~~Safety Mindset (safe/unsafe mode)~~ | ~~5 min~~ | **REMOVE entirely** |
| 5 | Testing with pytest (EXPANDED) | 20 min | **EXPAND** |
| | - pytest basics (test functions, assertions, running) | 5 min | KEEP from original |
| | - FastAPI TestClient | 5 min | KEEP from original |
| | - pytest fixtures (`@pytest.fixture`, conftest.py) | 4 min | **NEW** |
| | - `@pytest.mark.parametrize` | 3 min | **NEW** |
| | - Testing error cases (404, 422) | 3 min | **NEW** |
| 5b | Testing Exercise: write 3-4 tests for notes API (NEW) | 10 min | **NEW** |
| 6 | Makefile Quality Workflow (lint + format + test) | 5 min | KEEP as-is |
| 7 | Summary | 3 min | KEEP as-is |
| 8 | What's Next (update: MCP in L8, Docker+PostgreSQL in L9) | 2 min | MODIFY |
| 9 | References | 1 min | MODIFY: remove MCP references |

**Changes summary**: Remove Sections 5-6 (MCP + safety), expand testing from ~15 min to ~30 min (with exercise), add async exercise, update learning objectives and What's Next.

## Lecture 8 Section Map (New)

**Title**: "MCP: Model Context Protocol — AI Tool Integration"
**Directory**: `lectures/08-mcp/`
**Duration**: ~90 minutes

| # | Section | Duration | Source |
|---|---------|----------|--------|
| 0 | Header + Prerequisites (L6 FastAPI/REST, L7 async/httpx/testing) | 2 min | NEW |
| 1 | Learning Objectives (6 measurable outcomes) | 2 min | NEW |
| 2 | Introduction & Motivation | 10 min | PARTIAL from L6 (USB-C analogy) + NEW (real-world examples) |
| | - The standardization problem | | From L6 Section 9 intro |
| | - USB-C analogy | | From L6 Section 9 |
| | - Real-world MCP adoption (Claude Desktop, Cursor, Windsurf) | | NEW |
| | - Why this matters for Python developers | | From L6 "Why this matters" |
| 3 | MCP Architecture Deep Dive | 15 min | From L6 Section 9 (expanded) |
| | - Three participants: Host, Client, Server + diagram | | From L6 |
| | - Three primitives: Tools, Resources, Prompts | | From L6 |
| | - REST-to-MCP mapping (endpoints ↔ tools) | | NEW |
| | - Exercise 1: Identify primitives for a hypothetical service | 5 min | NEW |
| 4 | MCP Lifecycle & Transports | 10 min | From L7 Section 4.4-4.5 |
| | - Subprocess spawn model + lifecycle diagram | | From L7 (uses mcp-lifecycle.png) |
| | - Transport comparison: stdio vs SSE vs Streamable HTTP | | From L7 |
| | - Annotated config JSON | | From L7 Section 4.6 |
| | - Connection to FastAPI: SSE is HTTP streaming | | NEW (1-2 sentences) |
| 5 | Practical Setup: keep-mcp | 20 min | From L7 Section 4.1-4.3, 4.7 |
| | - What is keep-mcp + CRUD tool mapping | | From L6 Section 9.4 |
| | - Installation via pipx | | From L7 |
| | - Google Master Token auth flow | | From L7 |
| | - LLM client configuration | | From L7 |
| | - Connection verification | | From L7 |
| | - Troubleshooting guide | | From L7 |
| | - Exercise 2: Install and perform 3 operations | 15 min | From L7 (expanded timing) |
| 6 | Safety Mindset | 10 min | From L7 Section 5 (expanded) |
| | - Safe mode vs unsafe mode | | From L7 |
| | - Secure defaults and why they matter | | From L7 |
| | - Principle of least privilege | | From L7 |
| | - Real-world risks: prompt injection, unintended actions | | NEW |
| | - Tool annotations (readOnlyHint, destructiveHint) | | NEW |
| 7 | Testing MCP Integrations | 10 min | From L7 testing section (MCP-specific parts) |
| | - Why mock MCP calls | | From L7 |
| | - monkeypatch for MCP tool responses | | From L7 |
| | - Integration test flag pattern | | From L7 |
| | - Runnable code example | | From L7 |
| 8 | Connection to Our Project | 10 min | NEW |
| | - Conceptual: notes-api CRUD → MCP tools mapping | | NEW |
| | - What we'd need to add (server wrapper, tool definitions) | | NEW |
| | - Optional homework: sketch MCP server definition | | NEW |
| 9 | Summary | 3 min | NEW |
| 10 | What's Next: L9 Docker + PostgreSQL | 2 min | NEW |
| 11 | References | 1 min | Combined from L6 + L7 MCP references |

**Content origin breakdown**:
- ~65 min migrated from L6/L7 (with light editing)
- ~25 min new content (motivation examples, REST mapping, project connection, exercises, risks/annotations)

## Asset Migration Map

| Asset | Current Location | New Location | Action |
|-------|-----------------|--------------|--------|
| mcp-lifecycle.png | lectures/07-integrations-async-mcp/assets/ | lectures/08-mcp/assets/ | MOVE |
| threads-vs-asyncio.png | lectures/07-integrations-async-mcp/assets/ | lectures/07-async-testing/assets/ | KEEP (moves with dir rename) |
| Inline MCP diagrams (text/markdown) | L6 notebook cells | L8 notebook cells | MIGRATE with cell content |

## Cross-Reference Update Map

| Source | Current Reference | Updated Reference |
|--------|------------------|-------------------|
| L6 "What's Next" | "MCP practical setup in L7" | "async, httpx, testing in L7" |
| L6 Learning Objectives | "explain what MCP is" | REMOVE |
| L7 Prerequisites | "MCP concepts from L6" | REMOVE MCP mention |
| L7 Learning Objectives | "install and run MCP server" | REMOVE |
| L7 "What's Next" | "Docker + PostgreSQL (L8)" | "MCP (L8), Docker + PostgreSQL (L9)" |
| L8 Prerequisites | N/A (new) | "L6 (FastAPI, REST), L7 (async, httpx, testing)" |
| L8 "What's Next" | N/A (new) | "Docker + PostgreSQL (L9)" |
