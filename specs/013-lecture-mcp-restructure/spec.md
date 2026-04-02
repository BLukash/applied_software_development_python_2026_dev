# Feature Specification: Restructure Lectures 6, 7 & Add Lecture 8 (MCP Separation)

**Feature Branch**: `013-lecture-mcp-restructure`
**Created**: 2026-04-02
**Status**: Draft
**Input**: User description: "Move MCP content out of Lectures 6 and 7 into a dedicated new Lecture 8. Update Lecture 6 to focus purely on Web Fundamentals & FastAPI. Update Lecture 7 to focus on Async, HTTPX, Testing & Quality Workflow with expanded depth. Create Lecture 8 consolidating all MCP content from L6 and L7 with additional depth enabled by a full lecture slot."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Lecture 6 Update: Web Fundamentals & FastAPI (Priority: P1)

A student opens the updated Lecture 6 notebook and finds a focused, single-theme lecture on web fundamentals and FastAPI. All MCP content (Section 9: host/client/server, primitives, keep-mcp example) has been removed. The freed ~10 minutes are used to expand the REST section with a real-world API design example (e.g., GitHub API as "REST in the wild") and add a third exercise where students implement a DELETE /notes/{note_id} endpoint. The "What's Next" section previews async programming, HTTP clients, testing, and quality workflow — with no mention of MCP (that comes in L8). The lecture directory is renamed from `lectures/06-web-fastapi-mcp` to `lectures/06-web-fastapi`. The empty `clients/` directory in the project skeleton is removed (it was for MCP integration).

**Why this priority**: Lecture 6 is already delivered content that students have seen. Removing MCP cleanly without breaking existing flow is the most critical change — it unblocks Lectures 7 and 8.

**Independent Test**: Open the updated notebook, verify no MCP content remains, all code cells execute, three exercises exist, and "What's Next" references L7 topics (async/testing) only.

**Acceptance Scenarios**:

1. **Given** the updated Lecture 6 notebook, **When** a student searches for "MCP", "Model Context Protocol", "keep-mcp", "host/client/server" (in MCP context), or "tools/resources/prompts" (MCP primitives), **Then** zero results are found.
2. **Given** the updated notebook, **When** a student reads the REST section, **Then** they find a brief real-world API design example showing how a public API (e.g., GitHub API) follows REST principles covered in the lecture.
3. **Given** the updated notebook, **When** a student reaches the exercises, **Then** they find three exercises: (1) Book schema with Pydantic validation, (2) GET /notes/{note_id} endpoint, (3) DELETE /notes/{note_id} endpoint.
4. **Given** the updated notebook, **When** a student reads "What's Next", **Then** it previews: async programming, HTTP clients (httpx), testing (pytest), and quality workflow — with no MCP mention.
5. **Given** the updated project structure, **When** a student inspects the directory tree, **Then** there is no `clients/` directory.
6. **Given** the updated lecture directory, **When** checking the filesystem, **Then** the directory is named `lectures/06-web-fastapi` (renamed from `lectures/06-web-fastapi-mcp`).

---

### User Story 2 - Lecture 7 Update: Async, HTTPX, Testing & Quality Workflow (Priority: P1)

A student opens the updated Lecture 7 notebook and finds a focused lecture on async programming, HTTP clients, testing, and quality workflow. All MCP content has been removed: Section 5 (practical MCP setup), Section 6 (safety mindset), MCP-specific mocking examples, and MCP references in learning objectives. The freed ~20 minutes are used to expand testing with proper pytest fixtures, parametrize decorator, testing error cases (404, 422), a testing exercise (students write 3-4 tests for their notes API), and to expand the async section with a practical exercise (convert sync endpoint to async + httpx call to a public API). The "What's Next" section previews MCP (L8) and Docker + PostgreSQL (L9). The lecture directory is renamed from `lectures/07-integrations-async-mcp` to `lectures/07-async-testing`.

**Why this priority**: Equal to Story 1 — Lecture 7 is also delivered content. The MCP removal and testing expansion are co-dependent with the L6 changes.

**Independent Test**: Open the updated notebook, verify no MCP content remains, all code cells execute, expanded testing section is present, and "What's Next" references L8 (MCP) and L9 (Docker).

**Acceptance Scenarios**:

1. **Given** the updated Lecture 7 notebook, **When** a student searches for "keep-mcp", "MCP server", "pipx run keep-mcp", "safe mode", "unsafe mode", "Google Master Token" (as practical setup steps), **Then** zero results are found in sections/content (brief forward-references to L8 are acceptable).
2. **Given** the updated notebook, **When** a student reads the testing section, **Then** they find: pytest basics, FastAPI TestClient, pytest fixtures introduction, `@pytest.mark.parametrize` for testing multiple inputs, testing error cases (404, 422 responses), and organized test structure.
3. **Given** the updated notebook, **When** a student reaches the testing exercise, **Then** they are asked to write 3-4 tests: test create note, test search notes, test validation error (422), test not-found (404).
4. **Given** the updated notebook, **When** a student reads the expanded async section, **Then** they find a practical exercise: convert a sync endpoint to async and make an external API call with httpx (e.g., fetch a random quote from a public API).
5. **Given** the updated notebook, **When** a student reads "What's Next", **Then** it previews: MCP — Model Context Protocol (L8), then Docker + PostgreSQL (L9).
6. **Given** the updated lecture directory, **When** checking the filesystem, **Then** the directory is named `lectures/07-async-testing` (renamed from `lectures/07-integrations-async-mcp`).
7. **Given** the updated project extensions, **When** a student checks the project, **Then** config.py, .env, tests/, and Makefile are present, but no MCP-related test files or client wrappers exist.

---

### User Story 3 - New Lecture 8: MCP — AI Tool Integration (Priority: P2)

A student opens the new Lecture 8 notebook and finds a complete, dedicated lecture on Model Context Protocol. The lecture consolidates all MCP content previously split across Lectures 6 and 7 (conceptual intro from L6 Section 9, practical setup from L7 Section 5, safety mindset from L7 Section 6, MCP-specific testing from L7) into a single cohesive narrative. With a full 90-minute slot, each topic gets proper depth: architecture deep dive with REST-to-MCP mapping, lifecycle and transport mechanisms, hands-on keep-mcp setup, safety principles, testing MCP integrations, and a conceptual preview of how the notes-api could become an MCP server. Almost no new content needs to be written — existing content is reorganized, unified, and given room to breathe.

**Why this priority**: P2 because it depends on content being removed from L6 and L7 first. The content itself is largely migration, not creation.

**Independent Test**: Open the notebook, verify it covers all MCP topics from L6 and L7 plus lifecycle/transport depth, all code cells execute, two exercises exist, and "What's Next" previews Docker + PostgreSQL (L9).

**Acceptance Scenarios**:

1. **Given** a student who completed Lectures 1-7, **When** they open Lecture 8, **Then** they see prerequisites referencing L6 (FastAPI, REST) and L7 (async, httpx, testing) and learning objectives covering MCP architecture, setup, safety, and testing.
2. **Given** the notebook, **When** a student reads the architecture section, **Then** they find: Host/Client/Server diagram, three primitives (Tools, Resources, Prompts) explained, and a mapping showing how REST endpoints correspond to MCP tools.
3. **Given** the notebook, **When** a student reads the lifecycle section, **Then** they find: subprocess spawn model diagram, transport comparison table (stdio vs SSE vs Streamable HTTP), annotated config JSON with every field explained.
4. **Given** the notebook, **When** a student follows the practical setup section, **Then** they can install keep-mcp via pipx, configure Google authentication, set up an LLM client, verify the connection, and perform at least 3 operations (search, create, list).
5. **Given** the notebook, **When** a student reads the safety section, **Then** they find: safe mode vs unsafe mode explanation, secure defaults, principle of least privilege, real-world risks (prompt injection, unintended actions), and tool annotations (readOnlyHint, destructiveHint).
6. **Given** the notebook, **When** a student reads the testing section, **Then** they find: how to mock MCP tool calls with monkeypatch, integration test flag pattern, and a runnable code example.
7. **Given** the notebook, **When** a student reads the project connection section, **Then** they find a conceptual preview of how notes-api CRUD endpoints could map to MCP tools — no implementation, purely a thinking exercise.
8. **Given** the notebook exercises, **When** a student completes them, **Then** they have done: (1) an MCP primitive identification exercise (given a hypothetical service, identify which primitives to expose), and (2) a hands-on keep-mcp exercise (install and perform 3 operations).
9. **Given** the notebook, **When** a student reads "What's Next", **Then** it previews L9: Docker + PostgreSQL — containerizing the API and adding real persistence.
10. **Given** the lecture directory, **When** checking the filesystem, **Then** the directory is `lectures/08-mcp`.

---

### Edge Cases

- What happens if MCP content references in other lectures (e.g., cross-references from L5 or earlier) point to L6/L7? All cross-references must be audited and updated to point to L8.
- What happens if students have already studied L6/L7 with MCP content? The restructured lectures should not break any knowledge they already have — L8 consolidates and deepens, not contradicts.
- What happens if the existing notebook assets (images, diagrams) for MCP are in L6/L7 asset directories? Assets must be moved to L8's asset directory with correct paths.
- What happens if a student cannot obtain a Google master token? L8 must include the same troubleshooting steps and alternative demonstration path from the original L7.
- What happens if the lecture directory rename breaks relative paths in notebooks or project files? All internal references must be audited after rename.

## Requirements *(mandatory)*

### Functional Requirements

**Lecture 6 Changes:**

- **FR-001**: The Lecture 6 notebook MUST have all MCP content removed: Section 9 (MCP — Model Context Protocol) including the host/client/server explanation, three primitives, keep-mcp example, config JSON snippet, and "why this matters" subsection
- **FR-002**: The Lecture 6 notebook MUST include an expanded REST section with a brief real-world API design example (e.g., GitHub API endpoints shown as "REST in the wild")
- **FR-003**: The Lecture 6 notebook MUST include a third exercise: students implement a DELETE /notes/{note_id} endpoint with proper status code (200 or 204) and error handling (404 if not found)
- **FR-004**: The Lecture 6 "What's Next" section MUST preview async programming, HTTP clients, testing, and quality workflow — with zero MCP references
- **FR-005**: The Lecture 6 learning objectives MUST be updated to remove any MCP-related objective
- **FR-006**: The project skeleton MUST have the empty `clients/` directory removed
- **FR-007**: The lecture directory MUST be renamed from `lectures/06-web-fastapi-mcp` to `lectures/06-web-fastapi`
- **FR-008**: The Lecture 6 notebook MUST still contain at least 5 runnable code examples, at least 3 exercises (up from 2) with solutions, at least 2 memes, and at least 3 diagrams after changes
- **FR-009**: The Lecture 6 notebook duration MUST remain within the 1.5-hour target after content changes

**Lecture 7 Changes:**

- **FR-010**: The Lecture 7 notebook MUST have all MCP content removed: Section 5 (practical MCP setup — pipx, auth, config, demo), Section 6 (safety mindset — safe/unsafe mode), MCP-specific mocking examples in the testing section, and MCP references in learning objectives
- **FR-011**: The Lecture 7 testing section MUST be expanded to include: pytest fixtures introduction, `@pytest.mark.parametrize` decorator for testing multiple inputs, testing error cases (404, 422 responses), and organized test file structure
- **FR-012**: The Lecture 7 notebook MUST include a testing exercise where students write 3-4 tests: test create note, test search notes, test validation error (422), test not-found (404)
- **FR-013**: The Lecture 7 async section MUST be expanded with a practical exercise: convert a sync endpoint to async and make an external API call with httpx (e.g., fetch a random quote from a public API and return it)
- **FR-014**: The Lecture 7 notebook MAY include a brief mention of httpx as a test client alternative, since students just learned httpx
- **FR-015**: The Lecture 7 "What's Next" section MUST preview: MCP — Model Context Protocol (L8), then Docker + PostgreSQL (L9)
- **FR-016**: The lecture directory MUST be renamed from `lectures/07-integrations-async-mcp` to `lectures/07-async-testing`
- **FR-017**: Project extensions (config.py, .env, tests/, Makefile) MUST remain, but any MCP-related test files or client wrapper modules MUST be removed
- **FR-018**: The Lecture 7 notebook MUST still contain at least 5 runnable code examples, at least 2 exercises with solutions (testing exercise counts), at least 2 memes, and at least 2 diagrams after changes
- **FR-019**: The Lecture 7 notebook duration MUST remain within the 1.5-hour target after content changes

**New Lecture 8:**

- **FR-020**: A new Lecture 8 notebook MUST be created at `lectures/08-mcp/lecture-08.ipynb` covering MCP as a dedicated topic
- **FR-021**: Lecture 8 MUST consolidate MCP content from Lecture 6 Section 9 (conceptual: architecture, primitives, USB-C analogy, keep-mcp example) and Lecture 7 Sections 5-6 (practical: pipx setup, auth, LLM client config, safety mindset) plus MCP-specific testing content
- **FR-022**: Lecture 8 MUST include an Introduction & Motivation section (~10 min): the standardization problem, USB-C analogy, real-world examples (Claude Desktop, Cursor, Windsurf), why it matters for Python developers
- **FR-023**: Lecture 8 MUST include an MCP Architecture Deep Dive section (~15 min): Host/Client/Server diagram, three primitives explained, REST-to-MCP mapping showing how endpoints correspond to tools
- **FR-024**: Lecture 8 MUST include an MCP Lifecycle & Transports section (~10 min): subprocess spawn model, transport comparison (stdio vs SSE vs Streamable HTTP), annotated config JSON, connection to FastAPI knowledge (SSE is HTTP streaming)
- **FR-025**: Lecture 8 MUST include a Practical Setup section (~20 min): keep-mcp installation via pipx, Google Master Token auth flow, LLM client configuration (Claude Desktop or alternatives), connection verification, troubleshooting guide, live demo with at least 3 operations
- **FR-026**: Lecture 8 MUST include a Safety Mindset section (~10 min): safe mode vs unsafe mode, secure defaults, principle of least privilege, real-world risks (prompt injection, unintended actions), tool annotations (readOnlyHint, destructiveHint)
- **FR-027**: Lecture 8 MUST include a Testing MCP Integrations section (~10 min): mocking MCP tool calls with monkeypatch, integration test flag pattern, runnable code example
- **FR-028**: Lecture 8 MUST include a Connection to Our Project section (~10 min): conceptual preview of notes-api as MCP server, CRUD-to-tools mapping, what would need to be added — NO implementation, thinking exercise only
- **FR-029**: Lecture 8 MUST include Exercise 1: given a hypothetical service, identify which MCP primitives to expose (markdown cell / pen-and-paper exercise)
- **FR-030**: Lecture 8 MUST include Exercise 2: students install keep-mcp and perform at least 3 operations through an LLM client (hands-on exercise)
- **FR-031**: Lecture 8 MUST include prerequisites referencing L6 (FastAPI, REST) and L7 (async, httpx, testing)
- **FR-032**: Lecture 8 MUST include a "What's Next" section previewing L9: Docker + PostgreSQL
- **FR-033**: Lecture 8 MUST contain at least 5 runnable code examples (config snippets, mock tests, httpx calls)
- **FR-034**: Lecture 8 MUST contain at least 2 memes or visual humor elements
- **FR-035**: Lecture 8 MUST contain at least 3 diagrams (architecture, lifecycle, transport comparison)
- **FR-036**: Lecture 8 duration MUST target 90 minutes (1.5-hour lecture slot)
- **FR-037**: Lecture 8 MUST NOT modify the notes-api project code — all code examples are standalone or in the notebook only

**Cross-cutting:**

- **FR-038**: All explanatory text across L6, L7, and L8 MUST be in Ukrainian with English technical terms in parentheses on first use
- **FR-039**: All cross-references between lectures MUST be updated to reflect the new structure (L6 no longer mentions MCP, L7 points to L8 for MCP, L8 references L6 and L7 as prerequisites)
- **FR-040**: All MCP-related assets (images, diagrams) currently in L6 or L7 asset directories MUST be moved to L8's asset directory with updated references
- **FR-041**: The existing specs (009-lecture6-content, 010-lecture7-mcp-content, 011-lecture7-async-mcp-enhance) remain as historical records — this spec supersedes their MCP-related requirements

### Key Entities

- **Note**: The central resource for the stub API in L6/L7 — used to demonstrate CRUD, Pydantic schemas, testing, and (conceptually in L8) MCP tool mapping
- **MCP Server (keep-mcp)**: A locally running server exposing Google Keep operations as MCP tools — the primary hands-on example in L8
- **MCP Primitive**: One of three capability types (Tools, Resources, Prompts) that an MCP server exposes to clients
- **Test Client (FastAPI)**: Testing utility for endpoint testing without a running server — expanded coverage in L7
- **Settings Object**: Configuration container loading from .env — remains in L7, used in L8 for MCP credential management context

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Lecture 6 contains zero MCP-related content — verified by text search across the entire notebook for MCP keywords
- **SC-002**: Lecture 6 contains 3 exercises (up from 2) — verified by counting exercise cells in the notebook
- **SC-003**: Lecture 7 contains zero MCP practical setup or safety mindset content — verified by text search
- **SC-004**: Lecture 7 testing section covers fixtures, parametrize, and error case testing — verified by reviewing the section content
- **SC-005**: Lecture 7 includes a testing exercise where students write 3-4 tests — verified by the exercise cell
- **SC-006**: Lecture 8 covers all MCP topics previously in L6 and L7 — verified by comparing L8 content against the removed sections from L6/L7
- **SC-007**: Lecture 8 contains at least 5 code examples, 2 exercises, 2 memes, 3 diagrams — verified by content count
- **SC-008**: All three notebooks execute without errors in a clean kernel — verified by running all cells sequentially
- **SC-009**: Each lecture fits within the 1.5-hour (90-minute) target — verified by time estimates per section
- **SC-010**: No broken cross-references exist between any of the three lectures — verified by checking all inter-lecture links and references

### Assumptions

- Students have completed Lectures 1-5 and have a working Python 3.13+ environment with Jupyter
- The existing MCP content in L6 (Section 9) and L7 (Sections 5-6) is well-written and can be migrated with minimal rewriting — primarily reorganization and expansion
- The keep-mcp package remains available and functional at the time of lecture delivery
- The constitution will be updated to v1.4.0 reflecting the 15-lecture structure before this implementation begins
- Lecture 9+ numbering shifts are handled by a separate constitution update, not by this spec
- The notes-api project code is NOT modified by this restructuring — only notebook content and directory names change

## Scope Boundaries

**In scope**:
- Removing MCP content from Lecture 6 notebook
- Adding REST real-world example and DELETE exercise to Lecture 6
- Removing MCP content from Lecture 7 notebook
- Expanding testing and async sections in Lecture 7
- Creating new Lecture 8 notebook consolidating all MCP content
- Renaming lecture directories (06-web-fastapi-mcp -> 06-web-fastapi, 07-integrations-async-mcp -> 07-async-testing)
- Moving MCP assets between directories
- Updating cross-references across all three lectures
- Removing empty `clients/` directory from project skeleton

**Out of scope**:
- Modifying the notes-api project code (endpoints, schemas, etc.)
- Changing Lectures 1-5 content
- Renumbering or modifying Lectures 9-14 (handled by constitution update)
- Creating lab work for Lecture 8 (separate phase per constitution)
- Implementing MCP server functionality in the notes-api project
