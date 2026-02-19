# Data Model: Lecture 4 Notebook Structure

**Feature**: 006-lecture4-content
**Date**: 2026-02-18

## Overview

This document defines the content structure (sections, sub-topics, cell types, and visual requirements) for the Lecture 4 Jupyter Notebook. Since this is educational content (not a software system), "data model" maps to the notebook's content architecture.

## Notebook Structure

### Header Block

| Cell # | Type | Content |
|--------|------|---------|
| 1 | markdown | Title: "Лекція 4: Функції (продовження) + Модулі + Помилки + Вступ до ООП" + course name + year |
| 2 | markdown | Learning Objectives (Цілі навчання) — 5 measurable outcomes |
| 3 | markdown | Prerequisites (Передумови) — references Lectures 1–3 |
| 4 | markdown | Introduction (Вступ) — context, what was covered in Lecture 3, what's new + meme |

---

### Section 1: Functions (continued) — Функції (продовження)

| Sub-topic | Cells (est.) | Visuals Required (min 2 each) | Constitution Reference |
|-----------|-------------|-------------------------------|----------------------|
| 1.1 Lambda expressions (Лямбда-вирази) | 3 (1 md + 2 code) | 2 internet visuals | "lambda functions" |
| 1.2 Functions as parameters + sorting with `key` | 4 (2 md + 2 code) | 2 internet visuals | "functions as parameters, sorting and keys" |
| 1.3 `map`, `filter`, `reduce` | 4 (1 md + 3 code) | 2 internet visuals | "map, reduce, filter" |
| 1.4 Iterators and generators | 5 (2 md + 3 code) | 2 internet visuals | "xranges, iterators and generators" |
| 1.5 Scope: LEGB rule, closures | 4 (2 md + 2 code) | 2 internet visuals (memes + diagrams) | "Scope: local/global, closures (nice deep dive with memes)" |
| 1.6 Decorators intro | 3 (1 md + 2 code) | 2 internet visuals | Implied by closures extension |
| 1.7 Type hints intro | 3 (1 md + 2 code) | 2 internet visuals | "Type hints intro: list[int], dict[str, int], Optional" |
| 1.8 Docstrings / PEP 257 | 2 (1 md + 1 code) | 2 internet visuals | "Docstrings and readable APIs (PEP 257 style)" |

**Total Section 1**: ~28 cells, ~16 internet visuals

---

### Section 2: Modules & Imports — Модулі та імпорти

| Sub-topic | Cells (est.) | Visuals Required (min 2 each) | Constitution Reference |
|-----------|-------------|-------------------------------|----------------------|
| 2.1 Import mechanisms (`import`, `from...import`, `as`) | 3 (1 md + 2 code) | 2 internet visuals | "import, from x import y" |
| 2.2 Standard library overview (key modules) | 3 (1 md + 2 code) | 2 internet visuals | Implied |
| 2.3 Creating custom modules + `__name__ == "__main__"` | 3 (1 md + 2 code) | 2 internet visuals | "Building a tiny reusable module" |
| 2.4 Package structure basics | 2 (1 md + 1 code) | 2 internet visuals | "package layout" |

**Total Section 2**: ~11 cells, ~8 internet visuals

---

### Section 3: Error Handling — Обробка помилок

| Sub-topic | Cells (est.) | Visuals Required (min 2 each) | Constitution Reference |
|-----------|-------------|-------------------------------|----------------------|
| 3.1 Exception types and hierarchy | 3 (2 md + 1 code) | 2 internet visuals (hierarchy diagram) | "Exceptions" |
| 3.2 `try`/`except`/`else`/`finally` | 4 (1 md + 3 code) | 2 internet visuals (flow chart) | "try/except/else/finally" |
| 3.3 `raise` + custom exceptions | 3 (1 md + 2 code) | 2 internet visuals | "raising your own" |
| 3.4 Best practices | 2 (1 md + 1 code) | 2 internet visuals | Implied |

**Total Section 3**: ~12 cells, ~8 internet visuals

---

### Section 4: Debugging & Logging — Відлагодження та логування

| Sub-topic | Cells (est.) | Visuals Required (min 2 each) | Constitution Reference |
|-----------|-------------|-------------------------------|----------------------|
| 4.1 `breakpoint()` and pdb basics | 2 (1 md + 1 code) | 2 internet visuals | "Basic debugging (breakpoints)" |
| 4.2 `logging` module basics | 3 (1 md + 2 code) | 2 internet visuals | "minimal logging (logging)" |

**Total Section 4**: ~5 cells, ~4 internet visuals

---

### Section 5: Intro to OOP — Вступ до ООП

| Sub-topic | Cells (est.) | Visuals Required (min 2 each) | Constitution Reference |
|-----------|-------------|-------------------------------|----------------------|
| 5.1 Why OOP? Motivation | 2 (1 md + 1 code) | 2 internet visuals | "Basics of OOP" |
| 5.2 Classes, objects, `__init__`, `self` | 4 (1 md + 3 code) | 2 internet visuals | "class definitions" |
| 5.3 Instance vs class attributes + methods | 3 (1 md + 2 code) | 2 internet visuals | Implied |
| 5.4 Encapsulation (`_` and `__` conventions) | 2 (1 md + 1 code) | 2 internet visuals | "encapsulation" |
| 5.5 Inheritance basics | 3 (1 md + 2 code) | 2 internet visuals | "inheritance" |
| 5.6 Polymorphism (method overriding) | 2 (1 md + 1 code) | 2 internet visuals | "polymorphism" |
| 5.7 Abstraction concept | 1 (1 md) | 2 internet visuals | "abstraction principles" |
| 5.8 Python OOP vs C#/Java/C++ | 2 (1 md + 1 code) | 2 internet visuals | "Classes in Python vs C#/Java/C++ mindset" |

**Total Section 5**: ~19 cells, ~16 internet visuals

---

### Section 6: Practical Exercises — Практичні вправи

| Exercise | Topic Coverage | Cells |
|----------|---------------|-------|
| Exercise 1 | Functions: lambda, map/filter, sorting with key | 2 (empty + solution in `<details>`) |
| Exercise 2 | Modules: create and import a validator module | 2 (empty + solution in `<details>`) |
| Exercise 3 | Errors: build a safe file reader with proper exception handling | 2 (empty + solution in `<details>`) |
| Exercise 4 (bonus) | OOP: create a class hierarchy | 2 (empty + solution in `<details>`) |

**Total Section 6**: ~8 cells

---

### Section 7: Mini-Project — Міні-проєкт

**Title**: Student Grade Manager (Менеджер оцінок студентів)

**Integrates**: Functions (higher-order, lambda), Modules (custom module), Errors (input validation), OOP (Student class)

| Step | Description | Cells |
|------|-------------|-------|
| Description | Problem statement and requirements | 1 md |
| Step 1 | Define Student class with validation | 1 code (TODO) |
| Step 2 | Create grade processing functions (map/filter/sorted) | 1 code (TODO) |
| Step 3 | Add error handling for invalid inputs | 1 code (TODO) |
| Step 4 | Combine into working solution | 1 code (TODO) |
| Solution | Full solution in `<details>` | 1 md |

**Total Section 7**: ~6 cells

---

### Closing Block

| Cell # | Type | Content |
|--------|------|---------|
| Summary | markdown | Key takeaways (Підсумок) |
| What's Next | markdown | Preview of Lecture 5: OOP deep dive + files/JSON/CSV |
| Homework | markdown | Домашнє завдання — 3–4 assignments |
| References | markdown | Official docs + Real Python + educational resources |

**Total Closing**: ~4 cells

---

## Totals

| Metric | Value |
|--------|-------|
| Estimated total cells | 55–70 |
| Estimated code cells | 35–45 |
| Estimated markdown cells | 20–25 |
| Internet-sourced visuals (minimum) | ~52 (26 sub-topics × 2) |
| Exercises | 3 + 1 bonus |
| Mini-projects | 1 |
| Memes | 2–4 (constitution: at least 2) |

## Visual Asset Tracking

Each visual must have:
- **Alt text**: Descriptive text for accessibility
- **Source URL**: Direct link to the image
- **Attribution**: Caption with source site name and page link
- **Stability**: Prefer sources unlikely to change URLs (Real Python, official docs, established blogs)
