# Implementation Plan: Restructure Lectures 6, 7 & Add Lecture 8 (MCP Separation)

**Branch**: `013-lecture-mcp-restructure` | **Date**: 2026-04-02 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/013-lecture-mcp-restructure/spec.md`

## Summary

Move all MCP (Model Context Protocol) content out of Lectures 6 and 7 into a new dedicated Lecture 8. Lecture 6 becomes a focused Web Fundamentals & FastAPI lecture. Lecture 7 becomes a focused Async, HTTPX, Testing & Quality Workflow lecture with expanded testing depth. Lecture 8 consolidates all MCP content with room to breathe in a full 90-minute slot. This is primarily a content reorganization — almost no new content needs to be authored; existing MCP material migrates from two lectures into one.

## Technical Context

**Language/Version**: Python 3.13+ (code examples in Jupyter Notebook)
**Primary Dependencies**: FastAPI, Pydantic, uvicorn, httpx, pydantic-settings, pytest (L6/L7 project); keep-mcp via pipx (L8 demo)
**Storage**: N/A — no data persistence changes
**Testing**: pytest + FastAPI TestClient (expanded in L7); monkeypatch for MCP mocking (moved to L8)
**Target Platform**: Jupyter Notebook (lecture delivery), local dev environment (project)
**Project Type**: Educational content (Jupyter notebooks + FastAPI project skeleton)
**Performance Goals**: N/A — educational content
**Constraints**: Each lecture MUST fit within 90 minutes (1.5-hour slot)
**Scale/Scope**: 3 notebooks affected (L6 edit, L7 edit, L8 create), 1 asset file to move, 2 directory renames

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Status | Notes |
|------|--------|-------|
| Each lecture has learning objectives | PASS | L6/L7 updated to remove MCP objectives; L8 gets new MCP-focused objectives |
| At least 5 runnable code examples per lecture | PASS | L6: 5+ (existing), L7: 5+ (existing + expanded testing), L8: 5+ (migrated + mock tests) |
| At least 2 exercises with solutions per lecture | PASS | L6: 3 exercises (up from 2), L7: 2+ (testing exercise added), L8: 2 (primitive identification + keep-mcp hands-on) |
| At least 2 memes per lecture | PASS | L6: existing memes retained, L7: existing retained, L8: MCP memes migrated + new if needed |
| At least 1 diagram per lecture | PASS | L6: 3+ (existing web diagrams), L7: 2+ (event loop, threads-vs-asyncio), L8: 3+ (architecture, lifecycle, transport) |
| Ukrainian text with English terms in parentheses | PASS | All content follows this pattern already; new content follows same style |
| Duration target 1.5 hours per lecture | PASS | L6: ~100 min (freed 10 min, added ~10 min exercises), L7: ~85 min (freed 20 min, added ~20 min testing), L8: ~90 min (consolidated content) |
| Prerequisites section linking prior lectures | PASS | L6: links L1-L5, L7: links L6, L8: links L6+L7 |
| Summary and "What's Next" section | PASS | L6→L7 (async/testing), L7→L8 (MCP), L8→L9 (Docker+PostgreSQL) |
| No real external API calls in L6 | PASS | L6 endpoints remain stubs |
| Code passes ruff + black | PASS | No project code changes; only notebook content |

**Gate result**: ALL PASS — no violations, no complexity tracking needed.

## Project Structure

### Documentation (this feature)

```text
specs/013-lecture-mcp-restructure/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output (notebook section maps)
├── quickstart.md        # Phase 1 output
└── checklists/
    └── requirements.md  # Spec quality checklist
```

### Source Code (repository root)

```text
lectures/
├── 06-web-fastapi/                    # RENAMED from 06-web-fastapi-mcp
│   ├── lecture-06.ipynb               # MODIFIED (MCP removed, exercises added)
│   ├── assets/
│   │   └── memes/
│   └── notes-api/                     # Project skeleton (clients/ dir removed)
│       ├── app/
│       │   ├── main.py
│       │   ├── routers/
│       │   ├── schemas/
│       │   └── services/              # clients/ directory REMOVED
│       └── pyproject.toml
│
├── 07-async-testing/                  # RENAMED from 07-integrations-async-mcp
│   ├── lecture-07.ipynb               # MODIFIED (MCP removed, testing expanded)
│   └── assets/
│       ├── threads-vs-asyncio.png     # KEPT (async content)
│       └── memes/
│
└── 08-mcp/                            # NEW
    ├── lecture-08.ipynb               # NEW (consolidated MCP content)
    └── assets/
        ├── mcp-lifecycle.png          # MOVED from 07-integrations-async-mcp/assets/
        └── memes/

project/notes-api/                     # NO CHANGES
```

**Structure Decision**: Educational content project — notebooks are the primary deliverables. No traditional src/tests structure; each lecture is a self-contained directory with notebook + assets. The notes-api project lives under `project/` (or `lectures/06-web-fastapi/notes-api/` depending on current placement) and is NOT modified by this feature.

## Complexity Tracking

> No violations detected — section intentionally left empty.
