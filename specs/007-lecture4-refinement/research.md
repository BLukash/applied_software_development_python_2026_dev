# Research: Lecture 4 Refinement

**Feature**: 007-lecture4-refinement
**Date**: 2026-02-18

## R1: OOP Removal Scope Analysis

**Decision**: Remove cells 54–69 (Section 5 OOP), cells 79–81 (Exercise 4 OOP), and rewrite cells 82–87 (mini-project) to remove `class` keyword. Also update cells 0, 1, 3, 38, 88, 89.

**Rationale**: Constitution v1.2.0 moved all OOP to Lecture 5.

**Edge cases identified**:
- Cell 7 mentions "first-class objects" — this is about first-class functions, NOT OOP. Keep as-is.
- Cell 38 mentions `class Student` in a package structure example — modify to remove the class reference.
- Cells 44–45 define `class ValidationError(Exception)` — this is **exception handling** syntax, not OOP. Custom exception classes are taught as part of error handling in Python. The `class` keyword here is unavoidable and pedagogically correct. Keep as-is, but do not frame it as OOP.
- Cell 39 mentions "ієрархія (hierarchy)" for exceptions — this is exception hierarchy, not OOP inheritance. Keep.

## R2: Image Sourcing Strategy for Remaining Broken URLs

**Decision**: Multi-source download strategy with text-diagram fallback.

**Rationale**: Previous attempt showed:
- Real Python (files.realpython.com): 100% blocked (403 Forbidden)
- GeeksforGeeks (media.geeksforgeeks.org): ~70% blocked (403 Forbidden)
- Scaler Topics: ~60% accessible via cover images
- Programiz CDN: ~10% accessible (paths changed)
- EmbeddedInventor: Accessible

**Strategy (priority order)**:
1. Use already-downloaded images (35 valid files in assets/diagrams/)
2. Search Scaler Topics, Programiz, EmbeddedInventor for remaining topics
3. Search W3Schools, TutorialsPoint, Wikipedia for alternatives
4. For topics with no downloadable image: create text-based markdown diagrams (tables, ASCII art) inline

**Post-OOP-removal image count**:
- Header: 1 meme (currently broken — imgflip 403)
- S1 Functions (8 sub-topics): 17 images → need ~16 working
- S2 Modules (4 sub-topics): 8 images → need ~8 working
- S3 Errors (4 sub-topics): 8 images → need ~8 working
- S4 Debugging (2 sub-topics): 4 images → need ~4 working
- Total needed: ~37 images for 18 sub-topics (min 2 each = 36)

**Currently available working downloads (non-OOP)**:
1. `02-lambda-syntax-diagram.webp` — Lambda (S1.1)
2. `10-legb-rule.png` — LEGB (S1.5)
3. `13-decorator-pattern.webp` — Decorator (S1.6)
4. `14-decorator-step.png` — Decorator (S1.6)
5. `29-try-except-flow.png` — Try/Except (S3.2)
6. `embedinv-exception-hierarchy-1.png` — Exception hierarchy (S3.1)
7. `embedinv-exception-hierarchy-2.png` — Exception hierarchy (S3.1)
8. `scaler-docstring.webp` — Docstrings (S1.8)
9. `scaler-exceptions.webp` — Exceptions (S3.1)
10. `scaler-functions.webp` — Functions (S1.2)
11. `scaler-generators.webp` — Generators (S1.4)
12. `scaler-iterators.webp` — Iterators (S1.4)
13. `scaler-lambda-filter.webp` — Lambda/filter (S1.1/S1.3)
14. `scaler-lambda-map.webp` — Lambda/map (S1.3)
15. `scaler-lambda-overview.webp` — Lambda (S1.1)
16. `scaler-lambda-syntax.webp` — Lambda (S1.1)
17. `scaler-logging.webp` — Logging (S4.2)
18. `scaler-map.webp` — Map (S1.3)
19. `scaler-pdb.webp` — PDB (S4.1)
20. `scaler-sorted.webp` — Sorted (S1.2)

**Coverage gap (sub-topics still needing images)**:
- S1.5 Closures: need 1 more (have LEGB, need closure visual)
- S1.7 Type hints: need 2
- S1.8 Docstrings: need 1 more (have scaler-docstring)
- S2.1 Import mechanisms: need 2
- S2.2 Standard library: need 2
- S2.3 `__name__`: need 2
- S2.4 Package structure: need 2
- S3.2 Try/except: need 1 more (have try-except-flow)
- S3.3 Raise/custom: need 2
- S3.4 Best practices: need 2
- S4.1 Debugging: need 1 more (have scaler-pdb)
- S4.2 Logging: need 1 more (have scaler-logging)
- Header meme: need 1
- S1.5 Scope meme: need 1

**Total gaps**: ~20 images still needed. Strategy: search + text-diagram fallback.

## R3: Mini-Project Rewrite

**Decision**: Rewrite "Student Grade Manager" as "Data Processing Pipeline" (Конвеєр обробки даних).

**Rationale**: The original mini-project heavily uses `class Student`, which is OOP. A data processing pipeline naturally integrates:
- Functions: lambda, map/filter/sorted with key
- Modules: custom validators module
- Error handling: input validation, custom exceptions, try/except

**Alternative considered**: "Student Grades Processor" using dicts instead of classes — rejected because `Student` framing still implies OOP thinking.

**New mini-project outline**:
- Process a list of student records (as dicts, not classes)
- Use lambda/map/filter for data transformations
- Use custom validators module for input validation
- Use try/except for error handling
- No `class` keyword (except `class ValidationError(Exception)` which is error handling syntax)
