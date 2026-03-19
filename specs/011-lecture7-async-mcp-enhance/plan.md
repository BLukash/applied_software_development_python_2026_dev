# Implementation Plan: Enhance Lecture 7 — Deeper Asyncio & MCP Lifecycle

**Branch**: `011-lecture7-async-mcp-enhance` | **Date**: 2026-03-19 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/011-lecture7-async-mcp-enhance/spec.md`

## Summary

Enhance two sections of the existing Lecture 7 notebook:
1. **Async section (Section 1)**: Add threading vs asyncio comparison with GIL explanation, visual diagram, and runnable side-by-side code example
2. **MCP section (Section 4)**: Add subprocess lifecycle explanation, stdio vs SSE transport comparison, and annotated config JSON

This is a content-only enhancement — no changes to the `project/notes-api/` codebase. New cells are inserted into existing sections of `lectures/07-integrations-async-mcp/lecture-07.ipynb`.

## Technical Context

**Language/Version**: Python 3.13+ (code examples in Jupyter Notebook)
**Primary Dependencies**: Standard library only (`threading`, `asyncio`, `time`) — no new dependencies
**Storage**: N/A — educational content, no data persistence
**Testing**: Manual kernel execution (Run All Cells)
**Target Platform**: Jupyter Notebook (.ipynb)
**Project Type**: Educational content (notebook enhancement)
**Performance Goals**: N/A
**Constraints**: Total lecture duration must stay within 85–100 minutes (~15 minutes of new content max)
**Scale/Scope**: 2 existing sections enhanced with ~6–8 new cells total

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status | Notes |
|------|--------|-------|
| Learning objectives at start | PASS | Existing objectives cover async and MCP; no new objectives needed (depth increase, not new topics) |
| At least 5 runnable code examples | PASS | Existing notebook has 13 code cells; adding 1–2 more |
| At least 2 practical exercises with solutions | PASS | Existing: Exercise 1 (MCP setup) + Exercise 2 (test writing) |
| At least 2 memes/visuals | PASS | Existing: 2 memes + 2 diagrams; adding 2 new diagrams |
| Ukrainian text with English terms in parentheses | PASS | Must maintain for new content |
| Duration ≤ 1.5 hours | PASS | Current ~85 min + ~15 min new = ~100 min (within 1.5h) |
| No deprecated patterns | PASS | Using `threading` and `asyncio` from stdlib |
| Emoji: max 1–2 per section | PASS | Must maintain for new cells |
| Contextual analysis of previous lecture | PASS | L6 content already analyzed in prior feature |
| Code tested in clean environment | PENDING | Must verify after writing |

**Gate Result**: PASS — no violations. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/011-lecture7-async-mcp-enhance/
├── plan.md              # This file
├── research.md          # Phase 0: threading vs asyncio teaching, MCP transport details
├── data-model.md        # Phase 1: notebook cell map (what to insert where)
├── quickstart.md        # Phase 1: verification checklist
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
lectures/07-integrations-async-mcp/
├── lecture-07.ipynb                    # Enhanced notebook (existing file, cells added)
└── assets/
    ├── event-loop.png                 # Existing
    ├── mcp-data-flow.png              # Existing
    ├── threads-vs-asyncio.png         # NEW: side-by-side execution diagram
    ├── mcp-lifecycle.png              # NEW: subprocess spawn/communicate/shutdown
    └── memes/
        ├── async-meme.png             # Existing
        └── testing-meme.png           # Existing
```

**Structure Decision**: No new files or directories beyond 2 new diagram assets. All content is inserted into the existing notebook.

## Notebook Enhancement Map

### Async Section (Section 1) — Insert after cell-8 (sync→async conversion example)

| New Cell | Type | Content |
|----------|------|---------|
| A1 | markdown | **1.4 Потоки (Threads) vs Asyncio — чому не просто потоки?** — 2-sentence thread primer, GIL explanation, comparison table (5+ dimensions) |
| A2 | code | Side-by-side demo: `threading` vs `asyncio.gather` for 3 simulated I/O tasks, timing comparison |
| A3 | markdown | Visual: `![Threads vs Asyncio](assets/threads-vs-asyncio.png)` + FastAPI design connection paragraph |

### MCP Section (Section 4) — Insert after cell-24 (LLM client config) before cell-25 (verification)

| New Cell | Type | Content |
|----------|------|---------|
| M1 | markdown | **4.4 Як MCP-клієнт запускає сервер? (MCP Lifecycle)** — subprocess model, NOT a traditional server |
| M2 | markdown | Lifecycle diagram: `![MCP Lifecycle](assets/mcp-lifecycle.png)` + step-by-step explanation |
| M3 | markdown | Annotated Claude Desktop JSON config — each field explained |
| M4 | markdown | Transport comparison table: stdio vs SSE/HTTP (4+ dimensions) |

**Renumber existing subsections**: Current 4.4 (Перевірка з'єднання) → 4.6, current 4.5 (Troubleshooting) → 4.7

## Complexity Tracking

No violations — no complexity tracking needed.
