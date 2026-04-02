# Research: Restructure Lectures 6, 7 & Add Lecture 8 (MCP Separation)

**Feature**: 013-lecture-mcp-restructure
**Date**: 2026-04-02

## Research Tasks

### R1: Current MCP Content Inventory

**Task**: Map exactly which cells/sections contain MCP content in L6 and L7 notebooks.

**Findings**:

**Lecture 6** (lectures/06-web-fastapi-mcp/lecture-06.ipynb):
- Section 9: "MCP — Model Context Protocol (Концептуальний вступ)" — ~10 minutes
  - Cell `j0mcp`: Section header + USB-C analogy + problem statement
  - Architecture: Host/Client/Server three-participant model with inline diagram
  - Three primitives: Tools, Resources, Prompts
  - Cell `j4keepmcp`: keep-mcp as concrete example (CRUD mapping, safety features, config JSON snippet)
  - Cell `j5whymcp`: "Why this matters for us" — L7 preview
- "What's Next" section: references MCP practical setup in L7
- Learning objectives: includes MCP comprehension objective
- Total MCP references: 38 occurrences of MCP/keep-mcp/Model Context Protocol
- No MCP-specific assets (no images/diagrams as separate files; diagrams are inline markdown/text)

**Lecture 7** (lectures/07-integrations-async-mcp/lecture-07.ipynb):
- Section 4: "Practical MCP — Setting up keep-mcp" — ~15 minutes
  - 4.1: Installation via pipx
  - 4.2: Google Master Token authentication
  - 4.3: LLM client configuration (Gemini primary)
  - 4.4: MCP Lifecycle — subprocess model (references `mcp-lifecycle.png`)
  - 4.5: Transport comparison — stdio vs SSE/HTTP
  - 4.6: Annotated config JSON
  - 4.7: Connection verification + troubleshooting
- Section 5: Safety Mindset (~5 min) — safe/unsafe mode, secure defaults, least privilege
- Testing section: includes MCP-specific mocking example with monkeypatch
- Learning objectives: references MCP setup
- Total MCP references: 53 occurrences
- MCP-specific asset: `assets/mcp-lifecycle.png` (86 KB)

**Decision**: Content boundaries are clear. L6 has conceptual MCP (no assets to move), L7 has practical MCP (1 asset to move). Migration is straightforward cut-and-paste with section renumbering.

### R2: Directory Rename Impact

**Task**: Assess impact of renaming lecture directories on cross-references.

**Findings**:
- Lecture notebooks use relative paths for assets (e.g., `assets/mcp-lifecycle.png`)
- No other lectures reference L6/L7 directories by path (cross-references use "Лекція 6" / "Лекція 7" text, not file paths)
- The `notes-api` project lives inside `lectures/06-web-fastapi-mcp/notes-api/` — renaming the parent directory does NOT affect project code (all imports are relative within app/)
- Git tracks renames cleanly — `git mv` preserves history

**Decision**: Directory renames are safe. Use `git mv` for both renames. No cross-reference path breakage expected.

### R3: Testing Section Expansion Scope

**Task**: Determine what testing content to add in L7 when MCP testing moves to L8.

**Findings**:
- Current L7 testing is intentionally minimal per spec 010 clarification: "monkeypatch only, one simple mock example. No fixtures, no unittest.mock.patch, no parameterized tests."
- With MCP removal, ~20 minutes freed. Testing can now cover:
  - pytest fixtures (`@pytest.fixture`) — students need this for L9+ database testing
  - `@pytest.mark.parametrize` — teaches DRY testing patterns
  - Testing error cases (404, 422) — practical FastAPI testing
  - Organized test structure (conftest.py, test file naming)
- This does NOT conflict with the original "first exposure" intent — it simply fills the time MCP vacated with depth that was previously cut for time

**Decision**: Expand testing to include fixtures, parametrize, and error case testing. This is the natural progression that was sacrificed when MCP shared the lecture.

**Alternatives considered**:
- Add more async depth instead → Rejected: async section already has threads-vs-asyncio enhancement from spec 011
- Add deployment preview → Rejected: premature, belongs in L14

### R4: Lecture 8 Content Authoring Estimate

**Task**: Estimate how much new content vs migrated content L8 requires.

**Findings**:
- **Migrated from L6** (~10 min content): USB-C analogy, architecture, three primitives, keep-mcp example — needs light editing for standalone context (remove "as we'll see in L7" forward-references)
- **Migrated from L7** (~20 min content): pipx setup, auth, LLM config, lifecycle, transports, config JSON, troubleshooting, safety mindset, MCP mocking
- **Total migrated**: ~30 min of existing content
- **Needs expansion to fill 90 min**:
  - Introduction & Motivation: ~5 min NEW (real-world MCP adoption examples: Claude Desktop, Cursor, Windsurf)
  - REST-to-MCP mapping exercise: ~5 min NEW (exercise 1 — identifying primitives)
  - Connection to our project: ~10 min NEW (conceptual preview of notes-api as MCP server)
  - Expanded architecture section: ~5 min NEW (deeper primitive explanation with examples)
  - Exercise timing: ~15 min (hands-on keep-mcp exercise already exists, but now has more time)
  - Summary/What's Next: ~3 min (standard)
- **New content estimate**: ~25 min of new material, ~65 min migrated/expanded existing

**Decision**: Lecture 8 is ~70% migration, ~30% new content. The new content is lightweight (examples, exercises, conceptual discussion) — no complex technical writing needed.

### R5: Asset Migration

**Task**: Identify all assets that need to move between directories.

**Findings**:
- `lectures/07-integrations-async-mcp/assets/mcp-lifecycle.png` → `lectures/08-mcp/assets/mcp-lifecycle.png`
- `lectures/07-integrations-async-mcp/assets/threads-vs-asyncio.png` — STAYS in L7 (async content)
- L6 has no asset files to move (MCP diagrams are inline text/markdown in notebook cells)
- L8 will need new diagrams:
  - MCP architecture diagram (can be inline or generated — currently inline in L6)
  - Transport comparison table (currently inline in L7)
  - These are text/markdown tables in cells, not image files — no asset creation needed unless we want PNG versions

**Decision**: Only 1 file physically moves (`mcp-lifecycle.png`). All other MCP visuals are inline notebook content that migrates with the cells.

## Summary of Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Content migration approach | Cut cells from L6/L7, paste into L8 with context edits | Preserves existing quality; minimizes rewriting |
| Directory rename method | `git mv` for both L6 and L7 | Preserves git history |
| L7 testing expansion | Add fixtures, parametrize, error cases | Natural progression; fills time freed by MCP removal |
| L8 new content scope | ~25 min new, ~65 min migrated | Manageable scope; new content is examples/exercises, not complex technical writing |
| Asset handling | Move 1 PNG file; all other MCP visuals are inline | Minimal file operations |
| clients/ directory | Remove reference from L6 notebook project structure table | Was placeholder for MCP integration that no longer lives in L6 |
