# Implementation Plan: Lecture 2 Content Restructuring

**Branch**: `004-lecture2-restructure` | **Date**: 2026-02-06 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/004-lecture2-restructure/spec.md`

## Summary

Restructure Lecture 2 (Core Language Mechanics) to improve pedagogical flow by:
1. Moving Memory Representation immediately after Names and Objects
2. Splitting Identity vs Equality into two sections (simple types first, lists after mutability)
3. Adding a brief Complex Data Types introduction before Mutability
4. Keeping Truthiness, Control Flow, and Timing sections unchanged

## Technical Context

**Language/Version**: Python 3.11+ (code examples in Jupyter Notebook)
**Primary Dependencies**: Jupyter Notebook, matplotlib (for diagrams if needed)
**Storage**: N/A (educational content, no data persistence)
**Testing**: Manual validation - code execution in notebook, pedagogical review
**Target Platform**: Jupyter Notebook/JupyterLab, compatible with Colab
**Project Type**: Educational content (Jupyter Notebook)
**Performance Goals**: Lecture fits within 1.5 hours
**Constraints**: Must not duplicate Lecture 3's detailed coverage of complex data types
**Scale/Scope**: Single notebook restructure with ~5 new code cells and markdown sections

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Requirement | Status | Notes |
|-------------|--------|-------|
| Learning objectives at start | PASS | Already present, may need minor update for restructured flow |
| Content in Ukrainian | PASS | Already Ukrainian with English terms in parentheses |
| At least 5 runnable code examples | PASS | Current: 20+ code cells |
| At least 2 practical exercises | PASS | Current: 3 exercises |
| At least 2 memes | PASS | Current: 2 memes (mutability, timing) |
| At least 1 diagram/table/visual | PASS | Current: multiple diagrams and tables |
| 1.5 hours duration | VERIFY | May need adjustment after restructure |
| Prerequisites section | PASS | Already present |
| Summary and What's Next | PASS | Already present |
| No content duplication with previous lectures | PASS | Cross-references to Lecture 1 present |
| Analyze previous lecture before changes | REQUIRED | Must review Lecture 1 for consistency |

**Gate Result**: PASS - May proceed with research phase.

## Project Structure

### Documentation (this feature)

```text
specs/004-lecture2-restructure/
├── plan.md              # This file
├── research.md          # Phase 0 output - content analysis
├── data-model.md        # Phase 1 output - section structure
├── quickstart.md        # Phase 1 output - implementation guide
├── contracts/           # Phase 1 output - section specifications
│   └── sections.md      # Detailed section structure
└── tasks.md             # Phase 2 output (/speckit.tasks command)
```

### Source Code (repository root)

```text
lectures/02-core-mechanics/
├── lecture-02.ipynb     # Target file for restructuring
└── assets/
    ├── diagrams/
    │   ├── names-objects.webp
    │   └── memory-model.png
    └── memes/
        ├── mutability-bug.png
        └── timing-meme.png
```

**Structure Decision**: This is educational content restructuring within an existing Jupyter Notebook. No new source directories needed - modifications are to `lectures/02-core-mechanics/lecture-02.ipynb`.

## Complexity Tracking

> No complexity violations - this is content restructuring, not new architecture.

| Aspect | Assessment |
|--------|------------|
| New files created | 0 (restructure existing notebook) |
| Sections to move | 1 (Memory Representation) |
| Sections to split | 1 (Identity vs Equality → 2 sections) |
| New sections to add | 1 (Complex Data Types Introduction) |
| Sections unchanged | 3 (Truthiness, Control Flow, Timing) |

## Current vs Target Structure

### Current Structure (lecture-02.ipynb)

| # | Section | Cell Range |
|---|---------|------------|
| 1 | Names and Objects | cells 4-10 |
| 2 | Mutability | cells 11-17 |
| 3 | Memory Representation | cells 18-21 |
| 4 | Identity vs Equality | cells 22-29 |
| 5 | Truthiness | cells 30-35 |
| 6 | Control Flow | cells 36-46 |
| 7 | Practical Patterns | cells 47-50 |
| 8 | Timing | cells 51-55 |
| - | Exercises | cells 56-65 |
| - | Summary | cells 66-67 |
| - | References | cell 68 |

### Target Structure

| # | Section | Source | Action |
|---|---------|--------|--------|
| 1 | Names and Objects | cells 4-10 | KEEP (remove list examples, move to later) |
| 2 | Memory Representation | cells 18-21 | MOVE HERE |
| 3 | Identity vs Equality (Simple Types) | cells 22-29 (subset) | SPLIT - int, str, None only |
| 4 | Complex Data Types Introduction | NEW | ADD - brief intro to list, dict, set, tuple |
| 5 | Mutability | cells 11-17 | MOVE HERE |
| 6 | Identity vs Equality (Lists) | cells 22-29 (subset) | SPLIT - list examples here |
| 7 | Truthiness | cells 30-35 | KEEP |
| 8 | Control Flow | cells 36-46 | KEEP |
| 9 | Practical Patterns | cells 47-50 | KEEP |
| 10 | Timing | cells 51-55 | KEEP |
| - | Exercises | cells 56-65 | KEEP (update if needed) |
| - | Summary | cells 66-67 | UPDATE order in summary |
| - | References | cell 68 | KEEP |

## Transition Text Requirements

Each section transition must include connecting text:

1. **Names → Memory**: "Тепер, коли ми розуміємо, що імена — це посилання на об'єкти, подивимося, як ці об'єкти зберігаються в пам'яті."

2. **Memory → Identity (Simple)**: "Знаючи, як об'єкти представлені в пам'яті, ми можемо зрозуміти різницю між ідентичністю та рівністю. Почнемо з простих типів."

3. **Identity (Simple) → Complex Types**: "Ми побачили, як `is` та `==` працюють з числами та рядками. Тепер познайомимося зі складними типами даних, щоб зрозуміти повну картину."

4. **Complex Types → Mutability**: "Тепер, коли ви знаєте, що таке списки, словники та множини, ми можемо поговорити про їх ключову властивість — мутабельність."

5. **Mutability → Identity (Lists)**: "Розуміючи мутабельність, повернемося до порівняння `is` та `==` — цього разу на прикладі списків, де різниця критична."
