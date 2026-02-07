# Data Model: Lecture 2 Section Structure

**Branch**: `004-lecture2-restructure` | **Date**: 2026-02-06

## Overview

This document defines the section structure for the restructured Lecture 2. Since this is educational content, the "data model" represents the organizational structure of the notebook.

## Section Hierarchy

```
Lecture 2: Механіка мови Python
├── Header (cells 0-2)
│   ├── Title
│   ├── Learning Objectives
│   └── Prerequisites
├── Introduction (cell 3)
│   └── Cross-reference to Lecture 1
├── Section 1: Names & Objects [MODIFIED]
│   ├── Concept explanation (keep)
│   ├── id() with simple types (keep)
│   └── [List aliasing moved out]
├── Section 2: Memory Representation [MOVED HERE]
│   ├── PyObject structure
│   ├── sys.getsizeof() comparison
│   └── Tuple vs List efficiency
├── Section 3: Identity vs Equality (Simple Types) [NEW SPLIT]
│   ├── Concept: is vs ==
│   ├── Integer caching (-5 to 256)
│   ├── None comparison (is None)
│   └── String interning
├── Section 4: Complex Data Types [NEW]
│   ├── list introduction
│   ├── tuple introduction
│   ├── dict introduction
│   ├── set introduction
│   └── Preview reference to Lecture 3
├── Section 5: Mutability [MOVED HERE]
│   ├── Meme: mutability-bug.png
│   ├── Concept explanation
│   ├── Mutable/Immutable table
│   ├── List alias modification
│   ├── String immutability
│   └── Mutable default argument bug
├── Section 6: Identity vs Equality (Lists) [NEW SPLIT]
│   ├── List comparison: is vs ==
│   ├── Aliasing example (b = a)
│   └── Copy vs alias (a.copy())
├── Section 7: Truthiness [UNCHANGED]
│   ├── Falsy values list
│   ├── Idiomatic checks
│   ├── Comparison chaining
│   └── Short-circuit evaluation
├── Section 8: Control Flow [UNCHANGED]
│   ├── if/elif/else
│   ├── match statement (3 examples)
│   ├── for loop with range()
│   ├── while loop
│   └── for...else pattern
├── Section 9: Practical Patterns [UNCHANGED]
│   ├── Counting pattern
│   ├── Search with early exit
│   └── Accumulation pattern
├── Section 10: Timing [UNCHANGED]
│   ├── Meme: timing-meme.png
│   ├── time.perf_counter()
│   └── Loop vs builtin comparison
├── Exercises [UNCHANGED]
│   ├── Exercise 1: Predict result
│   ├── Exercise 2: Fix bug
│   └── Exercise 3: Control flow
├── Summary [UPDATED ORDER]
└── References [UNCHANGED]
```

## Section Entities

### Section

| Field | Type | Description |
|-------|------|-------------|
| number | int | Section number (1-10) |
| title_uk | string | Ukrainian title |
| title_en | string | English title in parentheses |
| status | enum | KEEP, MOVE, SPLIT, NEW, MODIFY |
| source_cells | list[int] | Original cell IDs (if applicable) |
| target_position | int | Position in restructured lecture |
| transition_text | string | Connecting text to previous section |
| estimated_duration | int | Minutes |

### Cell

| Field | Type | Description |
|-------|------|-------------|
| id | string | Original cell ID (e.g., "cell-4") |
| type | enum | markdown, code |
| action | enum | KEEP, MOVE, DELETE, MODIFY |
| target_section | int | New section number |
| notes | string | Implementation notes |

## Section Details

### Section 1: Names & Objects

| Field | Value |
|-------|-------|
| number | 1 |
| title_uk | "Імена та Об'єкти" |
| title_en | "Names and Objects" |
| status | MODIFY |
| source_cells | [4, 5, 6, 7] |
| transition_text | N/A (first main section) |
| estimated_duration | 10 min |
| changes | Remove list aliasing example (move to Section 6) |

### Section 2: Memory Representation

| Field | Value |
|-------|-------|
| number | 2 |
| title_uk | "Представлення в Пам'яті" |
| title_en | "Memory Representation" |
| status | MOVE |
| source_cells | [18, 19, 20, 21] |
| transition_text | "Тепер, коли ми розуміємо, що імена — це посилання на об'єкти, подивимося, як ці об'єкти зберігаються в пам'яті." |
| estimated_duration | 8 min |
| changes | Section number change only |

### Section 3: Identity vs Equality (Simple Types)

| Field | Value |
|-------|-------|
| number | 3 |
| title_uk | "Ідентичність vs Рівність (Прості Типи)" |
| title_en | "Identity vs Equality (Simple Types)" |
| status | SPLIT |
| source_cells | [22, 23, 24, 25, 27, 28, 29] |
| transition_text | "Знаючи структуру об'єктів у пам'яті, ми можемо зрозуміти різницю між ідентичністю (identity) та рівністю (equality). Почнемо з простих типів." |
| estimated_duration | 10 min |
| changes | Move list comparison (cell 26) to Section 6 |

### Section 4: Complex Data Types

| Field | Value |
|-------|-------|
| number | 4 |
| title_uk | "Складні Типи Даних" |
| title_en | "Complex Data Types" |
| status | NEW |
| source_cells | [] |
| transition_text | "Ми побачили, як `is` та `==` працюють з числами та рядками. Перш ніж йти далі, познайомимося зі складними типами даних." |
| estimated_duration | 7 min |
| changes | Entirely new content |

### Section 5: Mutability

| Field | Value |
|-------|-------|
| number | 5 |
| title_uk | "Мутабельність" |
| title_en | "Mutability" |
| status | MOVE |
| source_cells | [11, 12, 13, 14, 15, 16, 17] |
| transition_text | "Тепер, коли ви знаєте, що таке списки, словники та множини, ми можемо поговорити про їх ключову властивість — мутабельність (mutability)." |
| estimated_duration | 12 min |
| changes | Section number change, add "details in Lecture 3" note |

### Section 6: Identity vs Equality (Lists)

| Field | Value |
|-------|-------|
| number | 6 |
| title_uk | "Ідентичність vs Рівність (Списки)" |
| title_en | "Identity vs Equality (Lists)" |
| status | SPLIT |
| source_cells | [9, 10, 26] |
| transition_text | "Розуміючи мутабельність, повернемося до порівняння `is` та `==` — цього разу на прикладі списків, де різниця критична." |
| estimated_duration | 8 min |
| changes | Combine list examples from Names section and Identity section |

### Sections 7-10: Unchanged

These sections remain in their current form and order:
- Section 7: Truthiness (cells 30-35)
- Section 8: Control Flow (cells 36-46)
- Section 9: Practical Patterns (cells 47-50)
- Section 10: Timing (cells 51-55)

## Duration Summary

| Section | Duration (min) |
|---------|----------------|
| Header + Intro | 5 |
| 1. Names & Objects | 10 |
| 2. Memory Representation | 8 |
| 3. Identity (Simple) | 10 |
| 4. Complex Types | 7 |
| 5. Mutability | 12 |
| 6. Identity (Lists) | 8 |
| 7. Truthiness | 8 |
| 8. Control Flow | 15 |
| 9. Practical Patterns | 7 |
| 10. Timing | 5 |
| Exercises | 10 |
| Summary | 5 |
| **Total** | **110 min (1h 50min)** |

**Note:** This is slightly over the 90-minute target. Consider:
- Reducing Control Flow by 5 min (fewer match examples)
- Making exercises homework

## Validation Checklist

- [x] Memory Representation immediately follows Names & Objects
- [x] Identity split into Simple Types and Lists
- [x] Complex Types before Mutability
- [x] All transitions have connecting text
- [x] No content duplication with Lecture 1
- [x] No detailed coverage that belongs in Lecture 3
- [x] 2 memes preserved (mutability-bug, timing-meme)
- [x] All code examples work in Python 3.11+
