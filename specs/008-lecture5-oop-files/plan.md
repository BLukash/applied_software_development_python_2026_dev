# Implementation Plan: Lecture 5 — OOP in Python and Working with Files

**Branch**: `008-lecture5-oop-files` | **Date**: 2026-02-26 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/008-lecture5-oop-files/spec.md`

## Summary

Create `lectures/05-oop-files/lecture-05.ipynb` — a Jupyter Notebook covering Object-Oriented Programming in Python (foundations, pillars, Pythonic patterns) and file I/O (plain text, JSON, CSV) in Ukrainian. Includes 5 educator-suggested enhancements beyond the constitution's base topic list (`@property`, `@classmethod`/`@staticmethod`, ABC, `pathlib`, context manager protocol). Closes with a mini-project — Contact Book — that unifies `@dataclass`, OOP composition, and JSON persistence in 20–30 minutes of in-class coding.

## Technical Context

**Language/Version**: Python 3.13+ (all code examples validated against 3.13; `@dataclass` features used require 3.7+; `tomllib` and other 3.13-specific additions not needed)
**Primary Dependencies**: Standard library only — `json`, `csv`, `abc`, `dataclasses`, `pathlib`, `io`; `pandas` for one teaser cell (requires `pip install pandas`)
**Storage**: Local JSON file (`contacts.json`) for mini-project persistence; N/A for lecture content itself
**Testing**: Manual execution — all notebook cells MUST run top-to-bottom in a clean Python 3.13+ kernel without errors
**Target Platform**: Jupyter Notebook / JupyterLab / Google Colab (all three must be compatible)
**Project Type**: Educational content (single Jupyter Notebook + local assets)
**Performance Goals**: Lecture fits 1.5 hours of delivery; mini-project completable in 20–30 min in-class
**Constraints**: Standard library only (no 3rd-party packages except pandas teaser); no deprecated Python 2 patterns; no untested code; max 1.5 hours content
**Scale/Scope**: Single notebook (~90–110 cells), 2 exercises, 1 mini-project, 2+ memes, 3+ diagrams

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Rule | Status | Notes |
|------|--------|-------|
| Jupyter Notebook format (.ipynb) | PASS | Single notebook `lecture-05.ipynb` |
| Ukrainian language for all text | PASS | Spec explicitly requires Ukrainian with English terms in parentheses |
| English technical terms in parentheses on first use | PASS | Captured in FR-035 |
| 3–5 measurable learning objectives at start | PASS | FR-030 |
| At least 5 runnable code examples | PASS | FR-031 (spec has 10+ examples across sections) |
| At least 2 practical exercises with solutions | PASS | FR-032 |
| At least 2 memes/visual humor elements | PASS | FR-033 |
| At least 1 diagram/table/visual | PASS | FR-034 (OOP pillar table, MRO diagram, JSON schema) |
| Summary + "What's Next" section | PASS | FR-036 previewing Lecture 6 (REST + FastAPI) |
| Mini-project (Lecture 5 onward, required) | PASS | FR-028 (Contact Book) |
| Python 3.11+ | PASS | FR-037 |
| No deprecated Python 2 patterns | PASS | All code uses modern Python 3 idioms |
| No 3rd-party packages when stdlib suffices | PASS | json, csv, pathlib, abc, dataclasses all stdlib; pandas only for teaser |
| No untested/broken code | PASS | All examples verified during content creation (Phase 2) |
| No overuse of icons/emojis | PASS | Consistent with Lectures 1–4 style |
| DO NOT hallucinate facts — link to official docs | PASS | References section required (FR-036) |
| Content duration target ≤ 1.5 hours | PASS | Scope bounded by section count; Phase 1 contract enforces section limits |
| Read/analyze previous lecture before creating content | PASS | Lecture 4 fully analyzed (see research.md) |

**Gate result**: ALL PASS — no violations to justify. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/008-lecture5-oop-files/
├── plan.md              # This file
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/
│   └── notebook-structure.md   # Phase 1 output: section-by-section notebook contract
└── tasks.md             # Phase 2 output (/speckit.tasks — NOT created here)
```

### Source Code (repository root)

```text
lectures/
└── 05-oop-files/
    ├── lecture-05.ipynb          # Main deliverable
    └── assets/
        ├── diagrams/             # OOP pillars table, MRO diagram, JSON schema visual
        └── memes/                # 2+ meme images
```

**Structure Decision**: Matches the established pattern from Lectures 1–4. The single-notebook layout (`lecture-05.ipynb` + `assets/`) is consistent with `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`.
