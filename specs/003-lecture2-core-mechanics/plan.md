# Implementation Plan: Lecture 2 - Core Language Mechanics

**Branch**: `003-lecture2-core-mechanics` | **Date**: 2026-01-31 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/003-lecture2-core-mechanics/spec.md`

## Summary

Create Lecture 2 Jupyter notebook covering Python's core language mechanics: the object model (names vs objects, id(), references), mutability concepts, identity vs equality (`is` vs `==`), truthiness, control flow (if/elif/else, match, loops), practical patterns, and basic timing. Content must maintain tone consistency with Lecture 1 while avoiding repetition of topics already covered (bytecode/PVM, duck typing, GIL).

## Technical Context

**Language/Version**: Python 3.13+ (code examples must work in Python 3.13+)
**Primary Dependencies**: Jupyter Notebook, matplotlib (for custom diagrams when internet sources unavailable)
**Storage**: N/A (educational content, no data persistence)
**Testing**: Manual validation - all code cells execute successfully in clean Python environment
**Target Platform**: Cross-platform (Jupyter Notebook / JupyterLab / Google Colab)
**Project Type**: Educational content (single lecture notebook)
**Performance Goals**: Lecture content fits within 1.5 hours including exercises
**Constraints**: Ukrainian text, English terms in parentheses, 5+ runnable examples, 2+ exercises with solutions, 2 memes, 3+ diagrams
**Scale/Scope**: 1 notebook (~60-80 cells), following Lecture 1 structure

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### I. Student-Centered Design

| Requirement | Status | How Addressed |
|-------------|--------|---------------|
| Learning objectives at start | WILL COMPLY | 5 objectives covering object model, mutability, identity, control flow, timing |
| Real-world analogies | WILL COMPLY | Box-and-label analogy for names/objects, filing cabinet for namespaces |
| Progressive difficulty | WILL COMPLY | Start with id(), build to mutability, then control flow, timing last |
| Interactive elements throughout | WILL COMPLY | Prediction exercises before revealing code output |
| Runnable code examples | WILL COMPLY | All examples executable in standard Python 3.11+ |

### II. Practical Application Focus

| Requirement | Status | How Addressed |
|-------------|--------|---------------|
| Mini-project (Lecture 5+) | N/A | Lecture 2 - mini-projects start from Lecture 5 |
| Industry patterns | WILL COMPLY | Mutable default argument fix, is None pattern, for...else |
| Code examples minimal but teachable | WILL COMPLY | Each example focuses on one concept |

### III. Progressive Skill Building

| Requirement | Status | How Addressed |
|-------------|--------|---------------|
| Previous lecture analysis | WILL COMPLY | Spec includes Contextual Analysis section with Lecture 1 review |
| Avoid content repetition | WILL COMPLY | FR-018/FR-019 explicitly forbid repeating duck typing, bytecode/PVM |
| Prerequisites section | WILL COMPLY | Reference Lecture 1 completion |
| Cross-references | WILL COMPLY | "Як ми бачили у Лекції 1..." patterns planned |
| Topics per constitution | WILL COMPLY | Covers all Lecture 2 topics from constitution |

### IV. Quality Content Standards

| Requirement | Status | How Addressed |
|-------------|--------|---------------|
| Format: Jupyter Notebook | WILL COMPLY | .ipynb with markdown + code cells |
| Language: Ukrainian | WILL COMPLY | All explanatory text in Ukrainian |
| Terminology: English in parentheses | WILL COMPLY | "мутабельність (mutability)", "ідентичність (identity)" |
| 5+ runnable code examples | WILL COMPLY | Minimum 10 planned (id(), mutability, is vs ==, truthiness, loops) |
| 2+ exercises with solutions | WILL COMPLY | 2-3 exercises planned |
| 2 memes | WILL COMPLY | Memes for mutability gotcha and timing sections |
| 1+ diagram | WILL COMPLY | 3 diagrams: memory model, names/objects, loop patterns |
| Summary + What's Next | WILL COMPLY | Standard lecture structure |
| 1.5 hour duration | WILL COMPLY | SC-008 success criterion |

### V. Iterative Development

| Requirement | Status | How Addressed |
|-------------|--------|---------------|
| Technical review | WILL COMPLY | All code tested in clean venv |
| Version control | WILL COMPLY | Git branch 003-lecture2-core-mechanics |

**GATE RESULT: PASSED** - No violations. Proceed to Phase 0.

## Project Structure

### Documentation (this feature)

```text
specs/003-lecture2-core-mechanics/
├── plan.md              # This file
├── research.md          # Phase 0: diagram sources, meme sources
├── data-model.md        # Phase 1: lecture structure breakdown
├── quickstart.md        # Phase 1: how to run/edit the lecture
├── contracts/           # Phase 1: N/A for educational content
│   └── README.md        # Explanation of why no contracts
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
lectures/
└── 02-core-mechanics/
    ├── lecture-02.ipynb     # Main lecture notebook
    └── assets/
        ├── diagrams/        # Memory model diagrams, flow charts
        │   ├── names-objects.png
        │   ├── memory-model.png
        │   └── [matplotlib-generated].png
        └── memes/
            ├── mutability-bug.png
            └── timing-meme.png
```

**Structure Decision**: Educational content structure following Lecture 1 pattern. Lecture files in `lectures/` directory with numbered subdirectory containing notebook and assets.

## Complexity Tracking

> No violations - section not applicable.

---

## Phase 0: Research Tasks

### R1: Memory Diagram Sources

**Task**: Find high-quality, freely-licensed diagrams showing:
- Python object model (PyObject structure)
- Names as references to objects (box-and-arrow diagrams)
- List vs tuple memory layout

**Sources to check**:
- Real Python articles (typically CC-licensed educational use)
- Python documentation
- GeeksForGeeks (already used in Lecture 1)
- Fallback: generate with matplotlib

### R2: Integer Caching Documentation

**Task**: Verify current integer caching range and document:
- Confirm -5 to 256 range for CPython 3.11+
- Note any version-specific changes
- Find official documentation reference

### R3: Match Statement Examples

**Task**: Research best educational examples for structural pattern matching:
- Simple literal matching (replacement for switch)
- Sequence unpacking patterns
- Guard clauses (when)

### R4: Meme Sources

**Task**: Find or create appropriate memes for:
- Mutability gotcha (mutable default argument bug)
- "It works on my machine" timing/performance variant
- Must be appropriate for educational setting

### R5: Timing Best Practices

**Task**: Research recommended timing approach for educational context:
- time.perf_counter() vs time.time() vs timeit
- How to show meaningful loop overhead comparison
- Keep it simple for introduction (no %timeit magic yet)

---

## Phase 1: Design Artifacts

See separate files:
- [research.md](research.md) - Research findings
- [data-model.md](data-model.md) - Lecture structure and content outline
- [quickstart.md](quickstart.md) - How to work with the lecture

---

## Post-Design Constitution Re-Check

**Date**: 2026-01-31
**Status**: PASSED

All Phase 1 artifacts have been generated. Constitution compliance verified:

| Principle | Status | Verification |
|-----------|--------|--------------|
| I. Student-Centered | COMPLIANT | data-model.md defines 5 learning objectives, progressive sections |
| II. Practical Focus | COMPLIANT | Industry patterns documented (mutable default fix, is None) |
| III. Progressive Building | COMPLIANT | Lecture 1 analysis complete, cross-references planned |
| IV. Quality Standards | COMPLIANT | 8 sections, 10+ examples, 3 exercises, 2 memes, 3+ diagrams |
| V. Iterative Development | COMPLIANT | Validation checklist in quickstart.md |

**Research Complete:**
- R1: Diagram sources identified (research.md)
- R2: Integer caching verified (-5 to 256, CPython-specific)
- R3: Match statement examples defined (3 progressive patterns)
- R4: Meme concepts planned (mutability, timing)
- R5: Timing approach selected (time.perf_counter())

**Ready for Phase 2**: Run `/speckit.tasks` to generate implementation tasks.

---

## Generated Artifacts Summary

| Artifact | Path | Status |
|----------|------|--------|
| Implementation Plan | `specs/003-lecture2-core-mechanics/plan.md` | Complete |
| Research | `specs/003-lecture2-core-mechanics/research.md` | Complete |
| Data Model | `specs/003-lecture2-core-mechanics/data-model.md` | Complete |
| Quickstart | `specs/003-lecture2-core-mechanics/quickstart.md` | Complete |
| Contracts | `specs/003-lecture2-core-mechanics/contracts/README.md` | N/A (educational) |
| Agent Context | `CLAUDE.md` | Updated |
