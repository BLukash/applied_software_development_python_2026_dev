# Implementation Plan: Lecture 1 Content Expansion

**Branch**: `002-lecture1-content-expansion` | **Date**: 2026-01-25 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/002-lecture1-content-expansion/spec.md`

## Summary

Expand Lecture 1 notebook with deeper educational content:
1. **Storytelling** about Python's design philosophy (ABC language influence, why indentation)
2. **Why Python is awesome + where it's slow** (GIL, performance trade-offs)
3. **Duck typing explanation** (static/dynamic + strong/weak typing matrix)
4. **Expanded venv/pip** + modules/packages explanation
5. **Python release philosophy** (annual cycle, deprecation policy)
6. **Student-friendly References** section with categorized resources

## Technical Context

**Language/Version**: Python 3.11+ (code examples must work in Python 3.11+)
**Primary Dependencies**: Jupyter Notebook, matplotlib (for new diagrams)
**Storage**: N/A (educational content, no data persistence)
**Testing**: Manual validation - all code cells must execute without errors
**Target Platform**: Jupyter Notebook (VS Code, JupyterLab, or Colab)
**Project Type**: Educational content (Jupyter notebook enhancement)
**Performance Goals**: N/A (content quality over performance)
**Constraints**: 1.5-hour lecture duration, Ukrainian language with English terms in parentheses
**Scale/Scope**: Enhance existing 40-cell notebook with ~10-15 new cells of content

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Student-Centered Design | PASS | Storytelling improves retention; duck typing prevents misconceptions |
| II. Practical Application Focus | PASS | Expanded venv/pip is directly practical for project work |
| III. Progressive Skill Building | PASS | Builds on existing Lecture 1 content, prepares for Lectures 2-4 |
| IV. Quality Content Standards | PASS | Will include code examples, diagrams, Ukrainian text |
| V. Iterative Development | PASS | Enhancing existing validated content |
| Icon Usage (v1.0.1) | PASS | Will use sparingly (1-2 per section max) |
| No Russian Resources | PASS | All references will be English/Ukrainian |
| 1.5-Hour Duration | REQUIRES CHECK | Must validate final content fits time constraint |

## Project Structure

### Documentation (this feature)

```text
specs/002-lecture1-content-expansion/
├── plan.md                  # This file
├── research.md              # Research findings (duck typing, GIL, ABC history)
├── lecture-structure.md     # Detailed cell-by-cell content plan
├── quickstart.md            # Implementation guide
└── tasks.md                 # Task list (created by /speckit.tasks)
```

### Content Structure (lecture)

```text
lectures/01-python-intro/
├── lecture-01.ipynb          # Enhanced notebook (existing + new cells)
├── assets/
│   ├── memes/                # Existing memes
│   └── diagrams/
│       ├── python-timeline.png      # Existing
│       ├── python-usage.png         # Existing
│       ├── typing-matrix.png        # NEW: static/dynamic vs strong/weak
│       └── modules-packages.png     # NEW: module vs package visualization
├── exercises/                # Unchanged
└── solutions/                # Unchanged
```

**Structure Decision**: Enhancing existing notebook structure. No new directories needed except new diagrams.

## Content Integration Plan

### New Content Placement

| Section | Current Cells | New Content | Position |
|---------|---------------|-------------|----------|
| 1. Що таке Python | cell-4 to cell-8 | ABC history storytelling, release philosophy | After cell-5 (history table) |
| 1. Що таке Python | cell-4 to cell-8 | Why Python awesome + slow | After ABC storytelling |
| 4. Virtual Environments | cell-18 to cell-20 | Expanded venv (how it works), pip details | Expand cell-18, add after cell-20 |
| 4. Virtual Environments | cell-18 to cell-20 | Modules vs packages | New subsection after pip |
| 5. Перша програма | cell-23 to cell-25 | Duck typing + typing matrix | After cell-25 (data types) |
| References | cell-40 | Categorized references | Replace cell-40 content |

### Estimated Time Impact

| Content | Estimated Duration |
|---------|-------------------|
| Current lecture content | ~75 min |
| ABC storytelling | +5 min |
| Why awesome/slow | +5 min |
| Duck typing explanation | +7 min |
| Expanded venv/pip + modules | +8 min |
| Release philosophy | +3 min |
| References (review time) | +2 min |
| **Total** | ~105 min (fits 1.5 hr with buffer) |

## Complexity Tracking

No constitution violations requiring justification.
