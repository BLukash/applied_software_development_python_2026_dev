# Feature Specification: Enhance Lecture 7 — Deeper Asyncio & MCP Lifecycle

**Feature Branch**: `011-lecture7-async-mcp-enhance`
**Created**: 2026-03-19
**Status**: Draft
**Input**: User description: "Enhance Lecture 7 with deeper asyncio explanation (thread comparison, visuals) and MCP client-server lifecycle explanation (how clients run servers, not a traditional server)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Deeper Asyncio with Thread Comparison (Priority: P1)

A student reads the expanded async section of Lecture 7 and gains a clear mental model of **why** Python uses async/await instead of (or alongside) threads. The section includes a side-by-side comparison of threads vs async, an explanation of the GIL (Global Interpreter Lock) and its impact, and visual diagrams showing how tasks are scheduled in each model. After reading, the student can articulate when to use threads, when to use async, and why FastAPI defaults to async.

**Why this priority**: The current async section uses the waiter analogy but does not compare with threads — students who have heard of multithreading elsewhere will wonder "why not just use threads?" This is the most fundamental conceptual gap to fill.

**Independent Test**: A student who reads only this section can explain the difference between threading and asyncio, identify the GIL as a constraint, and correctly choose async for I/O-bound tasks in a FastAPI context.

**Acceptance Scenarios**:

1. **Given** the student has completed Lectures 1–6, **When** they read the enhanced async section, **Then** they encounter a clear comparison table (threads vs async) with at least 5 comparison dimensions (scheduling, memory, GIL impact, I/O suitability, CPU suitability).
2. **Given** the student is reading the async section, **When** they reach the visual aids, **Then** they see at least one diagram showing thread-based execution vs event-loop execution for the same set of I/O tasks.
3. **Given** the student has read the section, **When** they see a code example, **Then** there is a runnable side-by-side demo comparing `threading` vs `asyncio.gather` for multiple I/O-bound operations (e.g., simulated network calls).
4. **Given** the student wants to understand FastAPI's design choice, **When** they finish the section, **Then** there is a brief explanation connecting the GIL, I/O-bound web servers, and FastAPI's `async def` default.

---

### User Story 2 — MCP Client-Server Lifecycle Explanation (Priority: P2)

A student reads the enhanced MCP section and understands that MCP servers are **not** traditional long-running servers. Instead, the LLM client (host) **spawns** the MCP server as a subprocess, communicates via stdio (or SSE), and manages its lifecycle. The student understands the difference between stdio transport (local subprocess) and SSE transport (remote server), and can explain why `pipx run keep-mcp` appears in the config JSON rather than a URL.

**Why this priority**: Students familiar with web servers (from the same lecture) may assume MCP servers work the same way — running on a port, accepting connections. This misconception makes the config JSON confusing ("why is it a command, not a URL?"). Clearing this up is essential for practical MCP usage.

**Independent Test**: A student who reads only this section can draw the MCP lifecycle (host spawns server → stdio communication → host terminates server) and explain why the Claude Desktop config has `"command"` and `"args"` instead of a URL.

**Acceptance Scenarios**:

1. **Given** the student has learned MCP concepts from Lecture 6, **When** they read the lifecycle section, **Then** they see a step-by-step diagram showing: host starts → host spawns server subprocess → bidirectional stdio communication → host sends shutdown → server exits.
2. **Given** the student is reading the section, **When** they encounter the transport comparison, **Then** there is a clear table comparing stdio transport (local, subprocess, no port, typical for desktop tools) vs SSE/HTTP transport (remote, persistent server, URL-based, typical for shared/cloud deployments).
3. **Given** the student has seen the Claude Desktop JSON config, **When** they read this section, **Then** there is an annotated version of the config JSON explaining each field (`command` = what to run, `args` = how to run it, `env` = environment variables passed to the subprocess).
4. **Given** the student wants the full picture, **When** they finish the section, **Then** there is a brief mention that some MCP servers can also run as persistent HTTP/SSE servers (e.g., for shared team use), but the default and most common mode for local tools is stdio subprocess.

---

### Edge Cases

- What if a student has no prior knowledge of threading? The thread comparison section includes a 2-sentence primer on what threads are before comparing.
- What if a student tries to run an MCP server manually in a terminal? The section clarifies that while you *can* run `pipx run keep-mcp` manually for debugging, in normal use the host manages the lifecycle automatically.
- What if the student uses a remote MCP server? The section notes that SSE transport exists but is not the focus of this lecture.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The async section MUST include a comparison table with at least 5 dimensions contrasting threads and asyncio (e.g., scheduling model, memory overhead, GIL impact, best use case, error handling complexity).
- **FR-002**: The async section MUST include at least one visual diagram showing thread-based parallel execution vs event-loop task switching for I/O-bound operations.
- **FR-003**: The async section MUST include a runnable code example that demonstrates both `threading` and `asyncio` approaches for the same task, allowing students to compare execution time and behavior.
- **FR-004**: The async section MUST include a brief explanation of the GIL (Global Interpreter Lock) — what it is, why it exists, and how it makes threads less effective for I/O-bound tasks compared to async.
- **FR-005**: The async section MUST connect the GIL/async explanation to FastAPI's design — why web frameworks prefer async for handling concurrent requests.
- **FR-006**: The MCP section MUST include a lifecycle diagram showing the full subprocess flow: host starts → spawns MCP server → stdio communication → shutdown.
- **FR-007**: The MCP section MUST include a comparison table for stdio transport vs SSE/HTTP transport with at least 4 comparison dimensions.
- **FR-008**: The MCP section MUST include an annotated version of the Claude Desktop config JSON, explaining each field's role in the subprocess lifecycle.
- **FR-009**: The MCP section MUST clarify that "server" in MCP context does not mean a persistently running network service (in the default stdio mode).
- **FR-010**: All new content MUST be written in Ukrainian with English technical terms in parentheses on first use, matching the existing Lecture 7 style.
- **FR-011**: All new diagrams MUST be referenced from the notebook as image files in the assets directory, consistent with existing diagram references.
- **FR-012**: New content MUST be inserted into the existing notebook sections (expanding them), not creating separate standalone sections.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: After reading the enhanced async section, a student can correctly answer "When should you use threads vs async in Python?" — identifying I/O-bound = async, CPU-bound = threads/multiprocessing.
- **SC-002**: The enhanced async section contains at least 1 comparison table, 1 visual diagram, and 1 runnable code example that were not in the original version.
- **SC-003**: After reading the MCP lifecycle section, a student can explain why the Claude Desktop config uses `"command": "pipx"` instead of a URL, referencing the subprocess/stdio model.
- **SC-004**: The enhanced MCP section contains at least 1 lifecycle diagram, 1 transport comparison table, and 1 annotated config example that were not in the original version.
- **SC-005**: All new notebook cells execute without errors in a clean kernel when run sequentially with existing cells.
- **SC-006**: The total lecture duration estimate remains within 85–100 minutes after additions (no more than ~15 minutes of new content).

## Assumptions

- The existing Lecture 7 notebook structure and content remain as the baseline — this feature enhances specific sections, not rewrites them.
- The thread comparison uses only standard library (`threading`, `asyncio`) — no third-party concurrency libraries.
- Diagrams will be static images (PNG) referenced from the notebook, consistent with the existing pattern for `event-loop.png` and `mcp-data-flow.png`.
- The MCP lifecycle explanation focuses on stdio transport as the primary mode, with SSE/HTTP mentioned briefly as an alternative.
- Students have no prior knowledge of threading (a brief primer is included before the comparison).

## Scope Boundaries

**In scope**:
- Expanding the existing async section (Section 1) with thread comparison, GIL explanation, and visual
- Expanding the existing MCP section (Section 4) with lifecycle/subprocess explanation and transport comparison
- Creating new diagram assets for the additions

**Out of scope**:
- Rewriting existing content that already works well (waiter analogy, httpx examples, etc.)
- Adding multiprocessing or concurrent.futures content
- Implementing any code changes to the `project/notes-api/` codebase
- Adding new exercises (existing exercises remain unchanged)
