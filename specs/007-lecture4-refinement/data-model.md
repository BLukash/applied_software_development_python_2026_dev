# Data Model: Lecture 4 Notebook Cell Inventory

**Feature**: 007-lecture4-refinement
**Date**: 2026-02-18

## Current State (Before Refinement)

**Total cells**: 91 (43 markdown, 48 code)
**Total images**: 54 (38 broken, 16 working via local downloads)
**Sections**: 10 (Header + 5 main + Exercises + Mini-Project + Summary/Next + References)

### Cell Map

| Cell Range | Section | Type | Action |
|------------|---------|------|--------|
| 0 | Title | md | MODIFY — remove "Вступ до ООП" |
| 1 | Learning Objectives | md | MODIFY — remove OOP objective (#5) |
| 2 | Prerequisites | md | KEEP |
| 3 | Introduction | md | MODIFY — remove OOP mention from preview |
| 4–6 | S1.1 Lambda | md+code | KEEP — fix image URLs |
| 7–9 | S1.2 Functions as params | md+code | KEEP — fix image URLs |
| 10–13 | S1.3 map/filter/reduce | md+code | KEEP — fix image URLs |
| 14–17 | S1.4 Iterators/generators | md+code | KEEP — fix image URLs |
| 18–20 | S1.5 LEGB/closures | md+code | KEEP — fix image URLs |
| 21–23 | S1.6 Decorators | md+code | KEEP — fix image URLs |
| 24–26 | S1.7 Type hints | md+code | KEEP — fix image URLs |
| 27–28 | S1.8 Docstrings | md+code | KEEP — fix image URLs |
| 29–31 | S2.1 Import mechanisms | md+code | KEEP — fix image URLs |
| 32–34 | S2.2 Standard library | md+code | KEEP — fix image URLs |
| 35–36 | S2.3 `__name__` | md+code | KEEP — fix image URLs |
| 37–38 | S2.4 Package structure | md+code | MODIFY cell 38 — remove `class Student` reference |
| 39–40 | S3.1 Exception types | md+code | KEEP — fix image URLs |
| 41–43 | S3.2 try/except | md+code | KEEP — fix image URLs |
| 44–46 | S3.3 raise/custom | md+code | KEEP (class Exception syntax is OK) |
| 47–48 | S3.4 Best practices | md+code | KEEP — fix image URLs |
| 49–50 | S4.1 Debugging/pdb | md+code | KEEP — fix image URLs |
| 51–53 | S4.2 Logging | md+code | KEEP — fix image URLs |
| **54–69** | **S5 OOP (all)** | md+code | **DELETE — 16 cells** |
| 70–72 | Exercise 1 (functions) | md+code+md | KEEP |
| 73–75 | Exercise 2 (modules) | md+code+md | KEEP |
| 76–78 | Exercise 3 (errors) | md+code+md | KEEP |
| **79–81** | **Exercise 4 (OOP)** | md+code+md | **DELETE — 3 cells** |
| **82–87** | **Mini-project (OOP-based)** | md+code | **REWRITE — remove class, keep functions+errors** |
| 88 | Summary | md | MODIFY — remove OOP takeaways |
| 89 | What's Next | md | MODIFY — OOP as Lecture 5 preview |
| 90 | References | md | MODIFY — remove OOP references, keep function/module/error refs |

## Target State (After Refinement)

**Total cells**: ~72 (91 - 16 OOP section - 3 Exercise 4)
**Total images**: ~36 (all local, min 2 per sub-topic)
**Sections**: 8 (Header + 4 main + Exercises + Mini-Project + Summary/Next + References)

### Section Numbering (After)

| # | Section | Sub-topics | Images (min) |
|---|---------|-----------|-------------|
| — | Header block | Title, Objectives, Prerequisites, Introduction | 1 meme |
| 1 | Functions (continued) | 1.1–1.8 (8 sub-topics) | 16 |
| 2 | Modules & Imports | 2.1–2.4 (4 sub-topics) | 8 |
| 3 | Error Handling | 3.1–3.4 (4 sub-topics) | 8 |
| 4 | Debugging & Logging | 4.1–4.2 (2 sub-topics) | 4 |
| — | Exercises | 3 exercises (functions, modules, errors) | 0 |
| — | Mini-Project | Data Processing Pipeline | 0 |
| — | Closing | Summary, What's Next, References | 0 |

**Total sub-topics**: 18
**Total images needed**: 36 minimum (18 × 2) + 2 memes = 38

## Asset Files

### Files to DELETE (OOP-related)

| File | Size | Reason |
|------|------|--------|
| `39-4-pillars-of-oop.gif` | 20KB | OOP content |
| `45-encapsulation.webp` | 7KB | OOP content |
| `46-access-modifiers.webp` | 7KB | OOP content |
| `47-inheritance.png` | 56KB | OOP content |
| `49-polymorphism.webp` | 17KB | OOP content |
| `programiz-inheritance2.png` | 24KB | OOP content |
| `programiz-polymorphism.png` | 56KB | OOP content |
| `scaler-abstraction.webp` | 52KB | OOP content |
| `scaler-encapsulation.webp` | 54KB | OOP content |
| `scaler-init.webp` | 12KB | OOP content |
| `scaler-oop.webp` | 50KB | OOP content |
| `scaler-polymorphism.webp` | 14KB | OOP content |
| `scaler-self.webp` | 50KB | OOP content |
| `scaler-super.webp` | 40KB | OOP content |

### Files to KEEP (non-OOP)

| File | Maps to | Sub-topic |
|------|---------|-----------|
| `02-lambda-syntax-diagram.webp` | S1.1 | Lambda |
| `10-legb-rule.png` | S1.5 | LEGB |
| `13-decorator-pattern.webp` | S1.6 | Decorators |
| `14-decorator-step.png` | S1.6 | Decorators |
| `29-try-except-flow.png` | S3.2 | Try/Except |
| `embedinv-exception-hierarchy-1.png` | S3.1 | Exception hierarchy |
| `embedinv-exception-hierarchy-2.png` | S3.1 | Exceptions |
| `embedinv-exception-header.webp` | S3.1 | Exceptions |
| `scaler-docstring.webp` | S1.8 | Docstrings |
| `scaler-exceptions.webp` | S3.1 | Exceptions |
| `scaler-functions.webp` | S1.2 | Functions |
| `scaler-generators.webp` | S1.4 | Generators |
| `scaler-iterators.webp` | S1.4 | Iterators |
| `scaler-lambda-filter.webp` | S1.3 | Lambda/filter |
| `scaler-lambda-map.webp` | S1.3 | Map |
| `scaler-lambda-overview.webp` | S1.1 | Lambda |
| `scaler-lambda-syntax.webp` | S1.1 | Lambda |
| `scaler-logging.webp` | S4.2 | Logging |
| `scaler-map.webp` | S1.3 | Map |
| `scaler-pdb.webp` | S4.1 | PDB |
| `scaler-sorted.webp` | S1.2 | Sorted |

### Files to DELETE (temporary)

| File | Reason |
|------|--------|
| `download_images.py` | Generation script, not lecture content |
| `image_mapping.json` | Generation artifact |
