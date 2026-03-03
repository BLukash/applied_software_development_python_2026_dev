# Research: Lecture 6 — Web Fundamentals & FastAPI + MCP Introduction

**Date**: 2026-03-03
**Feature**: 009-lecture6-content

## 1. Visual Resources for Web Server Concepts

### Decision: Use MDN SVG diagrams + notebook markdown tables

**MDN Diagrams (educational-quality SVGs, language-neutral):**

| Diagram | URL | Use In Lecture |
|---------|-----|----------------|
| Client-Server Simple | `https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works/simple-client-server.png` | Section 1: web server basics |
| Client-Server Chain (with proxies) | `https://mdn.github.io/shared-assets/images/diagrams/http/overview/client-server-chain.svg` | Section 1: deeper request flow |
| HTTP Layers | `https://mdn.github.io/shared-assets/images/diagrams/http/overview/http-layers.svg` | Section 1: where HTTP sits in the stack |
| Fetching a Page | `https://mdn.github.io/shared-assets/images/diagrams/http/overview/fetching-a-page.svg` | Section 1: multiple resources composing one page |
| HTTP Request Format | `https://mdn.github.io/shared-assets/images/diagrams/http/overview/http-request.svg` | Section 2: HTTP essentials |
| HTTP Response Format | `https://mdn.github.io/shared-assets/images/diagrams/http/overview/http-response.svg` | Section 2: HTTP essentials |
| Static vs Dynamic Server | `https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction/web_application_with_html_and_steps.png` | Section 1: motivation for FastAPI |

**Source pages:**
- [Overview of HTTP - MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview)
- [HTTP Messages - MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Messages)
- [How the Web Works - MDN](https://developer.mozilla.org/en-US/docs/Learn_web_development/Getting_started/Web_standards/How_the_web_works)

**Rationale**: MDN diagrams are CC-licensed, professional, and minimal-text (easy to annotate in Ukrainian). SVG format scales well in notebooks.

**Alternatives considered**: Custom matplotlib diagrams (rejected — too much effort for concepts that already have excellent visuals), ASCII art (rejected — works for simple hierarchies like in Lecture 5, but request-response cycles need proper visuals).

## 2. HTTP Methods / Status Codes Reference

### Decision: Recreate as markdown tables in the notebook

**HTTP Methods with CRUD Mapping:**

| Method | CRUD | Has Body | Idempotent | Safe |
|--------|------|:---:|:---:|:---:|
| GET | Read | No | Yes | Yes |
| POST | Create | Yes | No | No |
| PUT | Update (full) | Yes | Yes | No |
| PATCH | Update (partial) | Yes | No | No |
| DELETE | Delete | No | Yes | No |

**Status Code Families:**

| Range | Category | Key Codes for API Work |
|-------|----------|----------------------|
| 2xx | Success | 200 OK, 201 Created, 204 No Content |
| 4xx | Client Error | 400 Bad Request, 404 Not Found, 422 Unprocessable Entity |
| 5xx | Server Error | 500 Internal Server Error |

**Rationale**: Tables in the notebook allow Ukrainian annotations and are interactive (students scroll, copy). No need for external image.

**Sources**: [MDN HTTP Methods](https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Methods), [MDN Idempotent](https://developer.mozilla.org/en-US/docs/Glossary/Idempotent)

## 3. MCP (Model Context Protocol)

### Decision: Conceptual-only intro with official architecture diagram

**Official resources:**

| Resource | URL |
|----------|-----|
| Official docs | [modelcontextprotocol.io](https://modelcontextprotocol.io) |
| Architecture | [modelcontextprotocol.io/docs/learn/architecture](https://modelcontextprotocol.io/docs/learn/architecture) |
| Specification | [modelcontextprotocol.io/specification/2025-11-25](https://modelcontextprotocol.io/specification/2025-11-25) |
| Simple diagram | `https://mintcdn.com/mcp/bEUxYpZqie0DsluH/images/mcp-simple-diagram.png` |

**Architecture — Three Participants:**

| Participant | Role | Example |
|-------------|------|---------|
| **Host** | AI application that coordinates clients | Claude Desktop, VS Code, Claude Code |
| **Client** | Component that maintains connection to one server | Instantiated by host per server |
| **Server** | Provides context via tools/resources/prompts | keep-mcp, filesystem MCP, DB MCP |

**Three Core Primitives (server-side):**

| Primitive | Control | Description |
|-----------|---------|-------------|
| **Tools** | Model-controlled | Executable functions the AI can invoke (e.g., search notes, create file) |
| **Resources** | Application-controlled | Data sources providing contextual info (e.g., file contents, DB records) |
| **Prompts** | User-controlled | Reusable templates for structured LLM interactions |

**Key analogy**: "USB-C for AI" — standardized connector between AI apps and tools.

**Protocol foundation**: JSON-RPC 2.0, inspired by LSP (Language Server Protocol).

**Rationale**: Concept-only — students grasp the WHY (standardized AI-tool integration) without running code. keep-mcp serves as a concrete, relatable example.

## 4. keep-mcp (Google Keep MCP Server)

### Decision: Use as the motivating example for MCP concepts

| Detail | Value |
|--------|-------|
| Repository | [github.com/feuerdev/keep-mcp](https://github.com/feuerdev/keep-mcp) |
| Author | Jannik Feuerhahn |
| Install | `pipx run keep-mcp` |

**Tools exposed (CRUD mapping — connects to REST lesson):**

| Category | Tools | Maps to CRUD |
|----------|-------|--------------|
| Read | `find`, `get_note` | Read |
| Create | `create_note`, `create_list` | Create |
| Update | `update_note`, `set_note_color`, `pin_note` | Update |
| Delete | `trash_note`, `delete_note` | Delete |

**Safety feature**: By default, destructive operations only affect notes with the `keep-mcp` label. `UNSAFE_MODE=true` overrides. This is a great teaching moment about safe defaults.

**Rationale**: Familiar product (Google Keep), clear CRUD mapping reinforces REST lesson, safety pattern previews Lecture 7 topic.

## 5. FastAPI Project Structure

### Decision: Flat app-level structure (educational simplicity)

**Chosen structure for Lecture 6:**

```text
notes-api/
├── pyproject.toml
├── app/
│   ├── __init__.py
│   ├── main.py           # FastAPI app + include_router
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── health.py     # GET /health
│   │   └── notes.py      # POST /notes/create, POST /notes/search
│   ├── schemas/
│   │   ├── __init__.py
│   │   ├── notes.py      # NoteCreate, NoteResponse, NoteSearchQuery, NoteSearchResult
│   │   └── common.py     # ErrorResponse, HealthStatus
│   ├── services/          # Empty for now — placeholder for Lecture 7+
│   │   └── __init__.py
│   └── clients/           # Empty for now — placeholder for MCP client in Lecture 7
│       └── __init__.py
```

**Rationale**: Matches the constitution-specified structure (`app/routers/schemas/services/clients`). Services and clients are empty placeholders now, establishing the pattern for Lecture 7 when MCP integration happens. Avoids overengineering while teaching proper layering.

**Alternative considered**: Netflix Dispatch-style domain-based structure (rejected — too complex for a first web project; appropriate for Lecture 10+ when refactoring happens).

**Source**: [FastAPI Bigger Applications](https://fastapi.tiangolo.com/tutorial/bigger-applications/)

## 6. Lecture Tone & Style (from Lecture 5 Analysis)

### Decision: Match Lecture 5 patterns exactly

| Pattern | How to Apply in Lecture 6 |
|---------|--------------------------|
| Start with contrast | Show raw http.server → then FastAPI (old way vs new way) |
| Tables for taxonomy | HTTP methods table, status codes table, MCP primitives table |
| 1:1 markdown:code ratio | Aim for ~45 markdown + ~45 code cells |
| Bilingual terms | **Веб-сервер** (web server), **маршрут** (route), **ідемпотентність** (idempotency) |
| Emoji usage | 💡 insights, ⚠️ warnings, ✅/❌ correct/incorrect, sparingly |
| Memes | 1 meme early (web/API humor), 1 later (REST/MCP) |
| Arrow notation | → for output, flow diagrams |
| What's Next | Bridge to Lecture 7 + 4-5 bullet list |
