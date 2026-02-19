# Implementation Plan: Lecture 4 — Functions (continue) + Modules + Errors + Intro to OOP

**Branch**: `006-lecture4-content` | **Date**: 2026-02-18 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/006-lecture4-content/spec.md`

## Summary

Create Lecture 4 as a Jupyter Notebook covering advanced functions (lambda, higher-order functions, map/filter/reduce, iterators/generators, scope/closures, decorators intro, type hints, docstrings), modules and imports, error handling (exceptions, try/except, custom exceptions), debugging/logging basics, and an introduction to OOP (all 4 pillars at introductory level, Python vs C#/Java/C++ comparison). The lecture uses internet-sourced visuals (minimum 2 per sub-topic, ~52 total) instead of custom-generated diagrams. Content is in Ukrainian, following Lectures 1–3 conventions.

## Technical Context

**Language/Version**: Python 3.13+ (code examples must work in Python 3.13+)
**Primary Dependencies**: Jupyter Notebook, matplotlib (for custom diagrams when internet sources unavailable — fallback only)
**Storage**: N/A (educational content, no data persistence)
**Testing**: Manual — run all cells top-to-bottom, verify outputs
**Target Platform**: Jupyter Notebook (local or JupyterLab/Colab)
**Project Type**: Educational content (Jupyter Notebook)
**Performance Goals**: N/A
**Constraints**: No external pip packages; standard library only; ~1.5 hours lecture duration; internet-sourced visuals must come from stable URLs
**Scale/Scope**: Single notebook, 55–70 cells, ~52 internet-sourced visuals, 26 sub-topics across 5 major sections

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Pre-Phase 0 Check

| Principle | Status | Notes |
|-----------|--------|-------|
| I. Student-Centered Design | PASS | Learning objectives defined, real-world analogies planned, exercises throughout, all code runnable |
| II. Practical Application Focus | PASS | Mini-project included, industry patterns demonstrated, standard library only |
| III. Progressive Skill Building | PASS | Builds on Lectures 1–3 (functions basics, collections), avoids duplication (see research.md R2). Contextual analysis of Lecture 3 completed. |
| IV. Quality Content Standards | PASS | Ukrainian text, 5+ code examples, 3+ exercises, references, memes (2+), visuals (52+), summary + What's Next |
| V. Iterative Development | PASS | Spec → Plan → Tasks → Implementation workflow |

### Constitution Lecture 4 Topics Coverage

| Constitution Topic | Covered In | Status |
|-------------------|-----------|--------|
| Functions deep dive, lambda, functions as parameters | Section 1.1–1.2 | PASS |
| Sorting and keys | Section 1.2 | PASS |
| map, reduce, filter | Section 1.3 | PASS |
| Iterators and generators | Section 1.4 | PASS |
| Scope: local/global, closures (deep dive with memes) | Section 1.5 | PASS |
| Decorators intro | Section 1.6 | PASS |
| Docstrings and readable APIs (PEP 257) | Section 1.8 | PASS |
| Type hints intro | Section 1.7 | PASS |
| Exceptions: try/except/else/finally, raising your own | Section 3 | PASS |
| Basic debugging (breakpoints) + minimal logging | Section 4 | PASS |
| Modules & imports, package layout | Section 2 | PASS |
| Building a tiny reusable module (utils/validators.py) | Section 2.3 | PASS |
| Basics of OOP: classes, encapsulation, polymorphism, inheritance, abstraction | Section 5 | PASS |
| Classes in Python vs C#/Java/C++ mindset | Section 5.8 | PASS |

### Prohibited Practices Check

| Rule | Status |
|------|--------|
| No Python 2 syntax | PASS — `xrange` mentioned in constitution but plan covers `range()` as lazy iterator |
| No outdated libraries | PASS — standard library only |
| No broken/untested code | PASS — validation step in quickstart.md |
| No excessive icons/emojis | PASS — plan limits to 1–2 per section max |
| No 3rd-party packages when stdlib suffices | PASS |

### Post-Phase 1 Re-check

All gates pass. The plan now covers all constitution Lecture 4 topics that were missing from the original spec (iterators/generators, docstrings, debugging/logging, full OOP pillars, Python vs C#/Java/C++ comparison). See [research.md](research.md) R1 for the full gap analysis.

## Project Structure

### Documentation (this feature)

```text
specs/006-lecture4-content/
├── plan.md                          # This file
├── spec.md                          # Feature specification
├── research.md                      # Phase 0: gap analysis, visual strategy, scope decisions
├── data-model.md                    # Phase 1: notebook content structure (sections, cells, visuals)
├── quickstart.md                    # Phase 1: implementation guide
├── contracts/
│   └── section-outlines.md          # Phase 1: detailed content contract per sub-topic
├── checklists/
│   └── requirements.md              # Spec quality checklist
└── tasks.md                         # Phase 2 output (created by /speckit.tasks)
```

### Source Code (repository root)

```text
lectures/04-functions-modules-errors-oop/
├── lecture-04.ipynb                  # Main lecture notebook
└── assets/
    └── memes/                       # Locally stored memes (if any)
```

**Structure Decision**: Educational content project — single Jupyter Notebook with assets directory. Internet-sourced visuals are embedded via URL (not stored locally). Only memes are stored locally in `assets/memes/` if needed. Follows the pattern established by `lectures/01-python-intro/`, `lectures/02-core-mechanics/`, and `lectures/03-data-structures/`.

## Implementation Phases

### Phase 1: Functions (continued) Section — ~28 cells

Build the largest section first. 8 sub-topics:

1. **Lambda expressions** — syntax, comparison with `def`, inline usage
2. **Functions as parameters + sorting** — first-class functions, `sorted()` with `key`
3. **map/filter/reduce** — functional programming patterns, comparison with comprehensions
4. **Iterators and generators** — iterator protocol, `yield`, generator expressions, memory efficiency
5. **Scope (LEGB) + closures** — variable resolution, `global`/`nonlocal`, closure pattern (with memes)
6. **Decorators intro** — wrapping functions, `@` syntax, timing decorator
7. **Type hints** — basic annotations, `Optional`, runtime behavior
8. **Docstrings / PEP 257** — multi-line format, `help()`, docstring styles

Each sub-topic: markdown explanation → 2+ internet visuals → runnable code cells

### Phase 2: Modules & Imports Section — ~11 cells

4 sub-topics:

1. **Import mechanisms** — `import`, `from`, `as`, PEP 8 order
2. **Standard library overview** — os, sys, math, datetime, random, json, collections, pathlib
3. **Custom modules + `__name__`** — creating validators.py, `__name__` guard
4. **Package structure** — `__init__.py`, relative imports, project layout

### Phase 3: Error Handling Section — ~12 cells

4 sub-topics:

1. **Exception types and hierarchy** — common exceptions, hierarchy tree
2. **try/except/else/finally** — full syntax, multiple except, practical examples
3. **raise + custom exceptions** — raising, re-raising, custom classes, chaining
4. **Best practices** — EAFP vs LBYL, specific catches, logging errors

### Phase 4: Debugging & Logging Section — ~5 cells

2 sub-topics:

1. **breakpoint() + pdb** — basic debugger usage (explained, not interactive in notebook)
2. **logging module** — levels, basicConfig, when to use vs print()

### Phase 5: Intro to OOP Section — ~19 cells

8 sub-topics:

1. **Why OOP?** — motivation, 4 pillars overview
2. **Classes/objects/__init__/self** — basic class definition
3. **Instance vs class attributes + methods** — shared vs per-instance, method types
4. **Encapsulation** — `_`/`__` conventions, name mangling, `@property`
5. **Inheritance** — parent/child, `super()`, method overriding
6. **Polymorphism** — duck typing, same interface different behavior
7. **Abstraction** — hiding complexity, brief `abc.ABC` mention
8. **Python vs C#/Java/C++** — comparison table, simplicity emphasis

### Phase 6: Exercises + Mini-Project + Closing — ~18 cells

1. **3 exercises + 1 bonus** — with TODO cells and `<details>` solutions
2. **Mini-project: Student Grade Manager** — integrates OOP + functions + errors
3. **Summary** — key takeaways
4. **What's Next** — Lecture 5 preview (OOP deep dive, files, JSON/CSV)
5. **Homework** — 3–4 assignments
6. **References** — official docs, Real Python, educational resources

### Phase 7: Validation

1. Restart kernel, run all cells top-to-bottom
2. Verify all internet image URLs load
3. Count visuals per sub-topic (min 2 each)
4. Check Ukrainian text consistency with Lectures 1–3
5. Verify no external pip dependencies
6. Review against constitution checklist

## Complexity Tracking

No constitution violations requiring justification. All gaps between spec and constitution have been resolved by expanding the plan scope (documented in research.md R1).
