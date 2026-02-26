# Implementation Plan: Lecture 4 Refinement — Remove OOP & Fix Images

**Branch**: `007-lecture4-refinement` | **Date**: 2026-02-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/007-lecture4-refinement/spec.md`

## Summary

Refine the existing Lecture 4 notebook by: (1) removing all OOP content (Section 5, Exercise 4, OOP references in title/objectives/summary/mini-project), (2) fixing all broken remote image URLs by replacing them with locally downloaded images, and (3) cleaning up orphaned assets and temporary files. This aligns the notebook with constitution v1.2.0 which moved OOP entirely to Lecture 5.

## Technical Context

**Language/Version**: Python 3.13+ (code examples must work in Python 3.13+)
**Primary Dependencies**: Jupyter Notebook (delivery format), matplotlib (fallback diagram generation if needed)
**Storage**: N/A (educational content, no data persistence)
**Testing**: Manual validation — restart kernel, run all cells, verify images render
**Target Platform**: Jupyter Notebook / JupyterLab / Google Colab
**Project Type**: Educational content (Jupyter notebook + image assets)
**Performance Goals**: N/A
**Constraints**: Standard library only for code examples; all images must be local files
**Scale/Scope**: 1 notebook (~70 cells after OOP removal), ~36 local images, 18 sub-topics across 4 sections

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Gate | Requirement | Status |
|------|-------------|--------|
| Lecture 4 scope | Functions (continue) + modules + errors (no OOP) | PASS — constitution v1.2.0 |
| Learning objectives | 3-5 measurable outcomes | PASS — 4 objectives (functions, modules, errors, debugging) |
| Ukrainian language | All explanatory text in Ukrainian | PASS — existing content already Ukrainian |
| English terms | Technical terms in parentheses | PASS — existing pattern maintained |
| Memes | At least 2 per lecture | PASS — will verify 2+ memes remain after OOP removal |
| Exercises | At least 2 practical exercises with solutions | PASS — 3 exercises remain (lambda/map, modules, errors) |
| References | Official docs + additional materials | PASS — existing references section |
| Summary + What's Next | Required sections | PASS — will update to remove OOP, add Lecture 5 OOP preview |
| No external packages | Standard library only | PASS — all code uses stdlib |
| Duration | 1.5 hours target | PASS — removing OOP reduces from ~2h to ~1.5h |
| Icons/emojis | Sparingly, 1-2 per section max | PASS — will verify during cleanup |
| Contextual analysis | Must analyze previous lectures | PASS — done in 006-lecture4-content |

All gates pass. No violations requiring justification.

## Project Structure

### Documentation (this feature)

```text
specs/007-lecture4-refinement/
├── plan.md              # This file
├── research.md          # Phase 0: image sourcing strategy + OOP removal scope
├── data-model.md        # Phase 1: notebook cell inventory (before/after)
├── quickstart.md        # Phase 1: validation checklist
├── contracts/           # Phase 1: cell-by-cell modification contract
│   └── modifications.md # Exact cells to remove, modify, or keep
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
lectures/04-functions-modules-errors-oop/
├── lecture-04.ipynb          # Primary artifact (modified in place)
└── assets/
    ├── diagrams/             # Downloaded educational images (clean up OOP, add missing)
    └── memes/                # Meme images (ensure 2+ remain)
```

**Structure Decision**: No new directories needed. Modify the existing notebook and assets in place. Delete orphaned files.

## Complexity Tracking

No constitution violations requiring justification. All gates pass.
