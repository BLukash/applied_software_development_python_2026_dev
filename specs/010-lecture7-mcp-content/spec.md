# Feature Specification: Lecture 7 — Python Web Server Integrations: Async, HTTPX, Testing, Practical MCP

**Feature Branch**: `010-lecture7-mcp-content`
**Created**: 2026-03-19
**Status**: Draft
**Input**: User description: "Implement lecture 7. As its main outcome I want running MCP server on local machine so I can access Google Keep notes from claude or any other llm I use https://github.com/feuerdev/keep-mcp"

## Clarifications

### Session 2026-03-19

- Q: Should the spec include all constitution-mandated Lecture 7 topics (async, httpx, config, testing, quality workflow) or focus only on MCP? → A: Include all constitution topics. Shrink MCP to practical-only (Lecture 6 already covers host/client/server, three primitives, keep-mcp tools list, config JSON, safe defaults concept, "USB-C for AI" analogy). Lecture 7 MCP = install keep-mcp + connect to Gemini as practical demo. No re-explaining Lecture 6 concepts.
- Q: Should the FastAPI project from Lecture 6 be extended to call keep-mcp as a backend (wiring stubs to real MCP calls), or should MCP remain a standalone demo? → A: MCP stays standalone demo (install + configure + use via Gemini). Project increment = add async endpoints + tests + config + quality workflow to existing Lecture 6 project. No wiring FastAPI stubs to keep-mcp.
- Q: How deep should the pytest/testing section go, given this is students' first exposure to pytest? → A: Minimal — monkeypatch only, one simple mock example. No fixtures, no unittest.mock.patch, no parameterized tests. Keep it introductory.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Lecture Notebook Delivery (Priority: P1)

A student opens the Lecture 7 Jupyter notebook and follows along during a 1.5-hour session. The notebook builds on the Lecture 6 FastAPI project and MCP concepts, covering seven topic areas: (1) async essentials — event loop intuition, async/await syntax, why FastAPI uses async; (2) HTTP client with httpx — sync vs async requests, timeouts, error handling, JSON parsing; (3) config basics — .env files, environment variables, a minimal settings object; (4) practical MCP — installing keep-mcp, obtaining a Google master token, connecting to Gemini (or another MCP-compatible LLM client) as a live demo; (5) safety mindset — safe mode vs unsafe mode, why secure defaults matter; (6) testing — pytest basics, FastAPI TestClient, mocking external calls (including MCP), optional integration test flag; (7) quality workflow — running lint/format/tests as a single local routine. All explanatory text is in Ukrainian with English technical terms in parentheses on first use.

**Why this priority**: The notebook is the primary deliverable — it delivers all seven constitution-mandated topics in a structured, progressive format. Without it, there is no lecture.

**Independent Test**: Can be fully tested by opening the notebook in Jupyter, reading all cells top-to-bottom, and verifying all code cells execute without errors and all seven topic areas are present.

**Acceptance Scenarios**:

1. **Given** a student who completed Lecture 6, **When** they open the Lecture 7 notebook, **Then** they see learning objectives, prerequisites referencing Lecture 6, and seven major content sections matching the constitution topics.
2. **Given** a student reading the notebook, **When** they execute all code cells sequentially in a clean kernel, **Then** every cell runs without errors.
3. **Given** a student who followed the Lecture 6 FastAPI project, **When** they reach the async and httpx sections, **Then** they see how to convert sync endpoints to async and how to make HTTP requests from within the project.
4. **Given** a student reading the MCP practical section, **When** they follow the setup steps, **Then** they can install keep-mcp, configure credentials, and connect it to Gemini without needing external documentation.

---

### User Story 2 - Running MCP Server on Local Machine (Priority: P2)

A student follows the notebook instructions to install the keep-mcp server on their local machine using pipx. They obtain a Google master token following the documented authentication flow, configure environment variables (GOOGLE_EMAIL, GOOGLE_MASTER_TOKEN), and verify the server starts successfully. They then configure Gemini (or another MCP-compatible LLM client) to connect to the keep-mcp server and verify the connection works by performing at least one tool call (e.g., listing notes). This section does NOT re-explain MCP architecture or primitives (already covered in Lecture 6) — it is purely practical setup and demo.

**Why this priority**: This is the headline practical outcome — students leave with a working local MCP server connected to their Google Keep. It demonstrates the real-world value of MCP concepts from Lecture 6.

**Independent Test**: Can be fully tested by following the setup steps on a clean machine with Python and pipx installed, verifying the server starts, and confirming the LLM client can list keep-mcp tools.

**Acceptance Scenarios**:

1. **Given** a student with Python 3.13+ and pipx installed, **When** they run the keep-mcp installation command, **Then** the server package is installed without errors.
2. **Given** the package is installed, **When** the student configures their Google credentials and starts the server, **Then** the server starts and authenticates with Google Keep successfully.
3. **Given** the server is running, **When** the student configures their LLM client (Gemini as primary example) with the keep-mcp server entry, **Then** the client connects and the student can see the available tools.
4. **Given** the server is connected to an LLM, **When** the student asks the LLM to "list my Google Keep notes," **Then** the LLM uses the keep-mcp find tool and returns the student's actual notes.
5. **Given** the server is connected to an LLM, **When** the student asks the LLM to "create a note titled 'MCP Test'," **Then** a new note appears in Google Keep with that title and the "keep-mcp" label.

---

### User Story 3 - Async, HTTPX, and Testing Fundamentals (Priority: P3)

A student works through the notebook sections on async programming, HTTP clients, and testing. They learn event loop intuition (why async exists, what it solves), convert a sync FastAPI endpoint to async, make HTTP requests using httpx (both sync and async), write their first pytest tests using FastAPI TestClient, and learn to mock external calls. These skills connect directly to the MCP integration: understanding async is needed for non-blocking MCP calls, httpx is the standard way to call external services, and mocking is essential for testing code that depends on MCP servers.

**Why this priority**: These are foundational skills for all remaining lectures (DB access, analytics endpoints, deployment). While MCP is the exciting demo, async/httpx/testing are the skills students will use daily.

**Independent Test**: Can be tested by running the async code examples, httpx request examples, and pytest test suite from the notebook — all should pass in a clean environment.

**Acceptance Scenarios**:

1. **Given** a student reading the async section, **When** they finish, **Then** they can explain what an event loop does and convert a simple sync function to async/await.
2. **Given** a student with the Lecture 6 FastAPI project, **When** they follow the httpx section, **Then** they can make both sync and async HTTP requests with timeout handling and JSON parsing.
3. **Given** a student reading the testing section, **When** they run the example test suite, **Then** all tests pass and they understand how TestClient and mocking work.
4. **Given** a student reading the config section, **When** they finish, **Then** they understand how to load settings from .env files and environment variables instead of hardcoding values.

---

### User Story 4 - Quality Workflow (Priority: P4)

A student follows the quality workflow section to set up a single command that runs linting (ruff), formatting (black), and tests (pytest) together. They understand why this matters for team development and CI/CD pipelines.

**Why this priority**: This is the capstone habit — ensuring students leave with a repeatable quality check they can run before every commit. Lower priority because the individual tools (ruff, black) were introduced in Lecture 6.

**Independent Test**: Can be tested by running the combined quality command on the Lecture 6 project — all checks should pass.

**Acceptance Scenarios**:

1. **Given** a student with the Lecture 6 FastAPI project, **When** they run the quality workflow command, **Then** linting, formatting, and tests all execute and report results.
2. **Given** a student reading the section, **When** they finish, **Then** they understand why running quality checks locally before pushing is important for team workflows.

---

### Edge Cases

- What happens when a student cannot obtain a Google master token (e.g., 2FA issues, institutional Google account restrictions)? The notebook MUST include troubleshooting steps and an alternative demonstration path (e.g., watching a recorded demo or using instructor's screen share).
- What happens when the keep-mcp server fails to start due to authentication errors? The notebook MUST include common error messages and their solutions.
- What happens when a student's LLM client does not support MCP? The notebook MUST list at least 2 MCP-compatible clients (Gemini as primary, Claude Desktop as alternative) and explain how to configure each one.
- What happens when the student's firewall or network blocks the Google Keep connection? The notebook MUST mention network requirements and suggest using a mobile hotspot as a fallback.
- What happens when keep-mcp modifies notes the student didn't intend to change? The notebook MUST explain the safety label mechanism and recommend keeping UNSAFE_MODE disabled.
- What happens when an async endpoint raises an unhandled exception? The notebook MUST show how FastAPI handles async exceptions and how to write proper error handling.
- What happens when an httpx request times out? The notebook MUST demonstrate timeout configuration and error handling patterns.
- What happens when tests depend on external services (MCP, Google Keep)? The notebook MUST show how to mock external dependencies so tests run offline.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The notebook MUST contain learning objectives at the start listing 4–6 specific, measurable outcomes covering async programming, HTTP clients, configuration management, practical MCP setup, testing, and quality workflows
- **FR-002**: The notebook MUST include a prerequisites section referencing Lecture 6 (FastAPI project, MCP concepts, ruff/black tooling) and listing required tools (Python 3.13+, pipx, an MCP-compatible LLM client)
- **FR-003**: The notebook MUST include an async essentials section covering: event loop intuition (what problem async solves), async/await syntax, converting sync functions to async, and why FastAPI uses async — with at least 2 runnable code examples
- **FR-004**: The notebook MUST include an httpx section covering: making sync and async HTTP requests, configuring timeouts, handling errors, and parsing JSON responses — with at least 2 runnable code examples
- **FR-005**: The notebook MUST include a config basics section covering: reading from .env files, using environment variables, and creating a minimal settings object for managing configuration — with a runnable example
- **FR-006**: The notebook MUST include a practical MCP section that does NOT re-explain Lecture 6 concepts (host/client/server, primitives, "USB-C" analogy) but provides: (a) step-by-step keep-mcp installation via pipx, (b) Google master token authentication with security warnings, (c) LLM client configuration for Gemini (primary) and at least one alternative client, (d) a live demo showing at least 3 tool invocations (search, read, create)
- **FR-007**: The notebook MUST include a safety mindset section covering: safe mode vs unsafe mode in keep-mcp, why secure defaults matter, and the principle of least privilege for credential handling — reinforcing the concept introduced in Lecture 6
- **FR-008**: The notebook MUST include a testing section covering: pytest basics (test functions, assertions, running pytest), FastAPI TestClient for endpoint testing, and one simple monkeypatch example to mock an external call — no fixtures, no unittest.mock.patch, no parameterized tests (first exposure to pytest). Optional integration test flag pattern shown conceptually. At least 2 runnable test examples
- **FR-009**: The notebook MUST include a quality workflow section showing how to run linting (ruff), formatting (black), and tests (pytest) as a single local routine — building on the individual tool introductions from Lecture 6
- **FR-010**: The notebook MUST include at least 2 practical exercises with solutions: (1) one exercise involving async/httpx or testing, and (2) one exercise involving the MCP server setup or usage
- **FR-011**: The notebook MUST contain at least 2 relevant memes or visual humor elements maintaining educational tone
- **FR-012**: The notebook MUST contain at least 2 diagrams or visuals (e.g., async event loop flow, data flow from LLM through MCP to Google Keep, test pyramid)
- **FR-013**: The notebook MUST include troubleshooting guidance for common issues: authentication failures, network problems, client configuration errors, async pitfalls, and test isolation
- **FR-014**: The notebook MUST end with a Summary section and a "What's Next" section previewing Lecture 8 topics (Docker, PostgreSQL, API-DB connection)
- **FR-015**: All explanatory text MUST be in Ukrainian with English technical terms in parentheses on first use
- **FR-016**: The notebook duration MUST target 1.5 hours of lecture content
- **FR-017**: The notebook MUST include security best practices: environment variables over hardcoding, .gitignore for sensitive files, principle of least privilege (UNSAFE_MODE disabled), and never committing tokens to version control
- **FR-018**: The notebook MUST contain at least 5 runnable code examples (across all topic sections, excluding the MCP setup which is command-line based)

### Key Entities

- **MCP Server (keep-mcp)**: A locally running server that exposes Google Keep operations as MCP tools — installed via pipx, configured with Google credentials, and connected to by LLM clients
- **MCP Tool**: A callable operation exposed by the server (e.g., find, get_note, create_note) — has a name, description, input schema, and maps to a specific Google Keep API operation
- **Google Master Token**: An authentication credential that grants the MCP server access to the user's Google Keep data — obtained through a specific authentication flow, must be kept secure
- **Settings Object**: A minimal configuration container that loads values from .env files and environment variables — centralizes config instead of scattering hardcoded values
- **Test Client**: A testing utility that sends requests to a local application without needing a running server — used for fast, isolated endpoint testing

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can explain what an event loop does and write a simple async/await function — verified by the async exercise in the notebook
- **SC-002**: Students can make HTTP requests using httpx with proper timeout and error handling — verified by the httpx code examples running successfully
- **SC-003**: Students can install and run the keep-mcp server on their local machine and connect it to Gemini (or another LLM client) within 15 minutes — verified by live demonstration during lecture
- **SC-004**: Students can write a basic pytest test using TestClient and mock an external dependency — verified by the testing exercise in the notebook
- **SC-005**: Students can run a combined quality check (lint + format + test) on their project as a single routine — verified by running the command on the Lecture 6 project
- **SC-006**: The notebook contains all required structural elements covering all 7 constitution-mandated topic areas — verified by checklist review
- **SC-007**: 90% of students who follow the setup instructions achieve a working MCP connection on their first attempt — verified by show of hands or quick poll during lecture

### Assumptions

- Students have completed Lecture 6 and have a working FastAPI project (app/routers/schemas/services/clients structure) and understand MCP concepts at a conceptual level
- Students have a Google account with Google Keep enabled
- Students have Python 3.13+ and pipx installed (or the notebook includes brief installation instructions for pipx)
- Students have at least one MCP-compatible LLM client installed (Gemini is the primary recommendation; Claude Desktop as alternative)
- The keep-mcp package (https://github.com/feuerdev/keep-mcp) is available on PyPI and installable via pipx at the time of the lecture
- Network access to Google services is available during the lecture (university Wi-Fi or mobile hotspot)
- The instructor has a working keep-mcp setup to demonstrate live if students encounter individual setup issues
- Lecture 6's ruff and black setup is still in place — Lecture 7 builds on it, does not re-teach it
