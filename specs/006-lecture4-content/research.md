# Research: Lecture 4 — Functions (continue) + Modules + Errors + Intro to OOP

**Feature**: 006-lecture4-content
**Date**: 2026-02-18

## R1: Spec vs Constitution Gap Analysis

**Decision**: Expand the implementation beyond the spec to cover all constitution-mandated Lecture 4 topics.

**Rationale**: The constitution (v1.1.0) is the binding document. The spec was written conservatively for the OOP section and omitted several topics explicitly listed in the constitution's Lecture 4 outline.

**Gaps identified and resolution**:

| # | Constitution Topic | In Spec? | Resolution |
|---|-------------------|----------|------------|
| 1 | Sorting with `key` parameter | No (implied in FR-006) | Add to Functions section under "functions as parameters" |
| 2 | Iterators and generators | No | Add as sub-topic in Functions section (generators are natural extension of functions) |
| 3 | Docstrings / PEP 257 style | No | Add as sub-topic in Functions section (readable APIs) |
| 4 | Basic debugging (breakpoints) + minimal logging | No | Add as standalone sub-section between Errors and OOP |
| 5 | Building a tiny reusable module (utils/validators.py) | Implied in FR-007 | Make explicit in Modules section with hands-on example |
| 6 | OOP: encapsulation, polymorphism, inheritance, abstraction | Partially (spec has basics only) | Expand OOP section to cover all 4 pillars at introductory level |
| 7 | Classes in Python vs C#/Java/C++ mindset | No | Add comparison sub-topic in OOP section |

**Alternatives considered**: Keeping the spec's conservative scope. Rejected because the constitution explicitly lists these topics for Lecture 4.

## R2: Lecture 3 Content Already Covered (Avoid Duplication)

**Decision**: The following topics were covered in Lecture 3 and must NOT be re-taught in Lecture 4 (only cross-referenced):

- Basic function definition (`def`, parameters, return, defaults)
- `*args` and `**kwargs`
- Basic docstrings (one-line)
- Function return of multiple values via tuple

**Rationale**: Constitution principle III requires avoiding content duplication. Lecture 4 should open with a brief recap referencing Lecture 3, then advance to new material.

**What Lecture 4 builds on**: Lambda, higher-order functions, sorting with keys, map/filter/reduce, scope/closures, decorators, generators, type hints — all new territory.

## R3: Visual Sourcing Strategy

**Decision**: Use internet-sourced visuals from stable, reputable sources. Prefer direct image URLs that are unlikely to break.

**Rationale**: User explicitly requested internet-found visuals over custom-generated ones, noting "better impact."

**Preferred sources** (in priority order):
1. Real Python articles (stable, educational, well-illustrated)
2. Official Python docs diagrams
3. GeeksforGeeks (stable, widely used)
4. Python Morsels / Trey Hunner blog (excellent Python visuals)
5. Medium/Dev.to articles with clear licensing
6. Programiz (clean educational diagrams)
7. W3Schools Python (simple visuals)

**Attribution approach**: Each image embedded as `![Alt text](URL)` with a markdown comment or caption line: `*Source: [Site Name](page URL)*`

**Fallback**: If a suitable internet visual cannot be found for a sub-topic after reasonable search, a simple text-based diagram in a markdown cell is acceptable (not matplotlib-generated).

## R4: OOP Depth for Lecture 4 vs Lecture 5

**Decision**: Cover all 4 OOP pillars (encapsulation, inheritance, polymorphism, abstraction) at introductory level in Lecture 4. Lecture 5 goes deeper with `@dataclass`, magic methods, composition vs inheritance, and advanced patterns.

**Rationale**: Constitution explicitly states Lecture 4 should cover "Basics of OOP on Python, class definitions, encapsulation, polymorphism, inheritance, abstraction principles in Python" plus "Classes in Python vs C#/Java/C++ mindset."

**Scope boundary**:
- Lecture 4: Define classes, `__init__`, `self`, instance/class attributes, methods, single inheritance (one example), polymorphism (method overriding, one example), encapsulation (naming conventions `_` and `__`), abstraction concept (brief), Python vs C#/Java/C++ comparison
- Lecture 5: Deep dive into all of the above plus `@dataclass`, `__repr__`/`__str__`, composition > inheritance, file I/O, JSON/CSV

## R5: Iterators and Generators Placement

**Decision**: Place iterators and generators in the Functions section, after map/filter/reduce and before closures.

**Rationale**: Generators are defined with `def` + `yield` and are a natural extension of functions. They also connect to the iteration protocol which students encountered with `for` loops. The constitution mentions "xranges, iterators and generators" — `xrange` is Python 2, so we cover `range()` as a lazy iterator, then introduce the iterator protocol and generators.

**Sub-topics**:
1. Iterator protocol (`__iter__`, `__next__`) — conceptual, light
2. `range()` as a lazy iterator (connects to Lecture 2 knowledge)
3. Generator functions (`yield`)
4. Generator expressions (similar to comprehensions)
5. Why generators matter: memory efficiency

## R6: Debugging and Logging Placement

**Decision**: Add a focused sub-section "Debugging and Logging" between Error Handling and OOP intro.

**Rationale**: Constitution explicitly lists "Basic debugging (breakpoints) + minimal logging (logging)" as a Lecture 4 topic. It fits naturally after error handling (debugging is what you do when errors occur) and before OOP.

**Sub-topics**:
1. `breakpoint()` function (Python 3.7+) — basic usage
2. Using pdb: step, next, continue, print
3. `logging` module basics: levels, basic config, simple usage
4. When to use print() vs logging vs debugger

## R7: Section Time Budget

**Decision**: Allocate time proportionally to constitution emphasis and spec priorities.

| Section | Estimated Cells | Time (min) | Priority |
|---------|----------------|------------|----------|
| Functions (continued) | 15–18 | 30 | P1 |
| Modules & Imports | 8–10 | 15 | P1 |
| Error Handling | 10–12 | 20 | P1 |
| Debugging & Logging | 4–5 | 8 | P1 |
| Intro to OOP | 12–15 | 22 | P2 |
| Exercises + Mini-Project | 5–7 | — (homework) | P2 |
| **Total** | **54–67** | **~95 min** | — |

**Rationale**: Constitution mandates 1.5 hours (90 min) target. Slightly over is acceptable since exercises are partly homework. Functions section gets the most time as it has the most sub-topics.
