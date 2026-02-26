# Modification Contract: Lecture 4 Notebook

**Feature**: 007-lecture4-refinement
**Target**: `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`

## Cell-by-Cell Modifications

### MODIFY: Cell 0 (Title)

**Current**: `Лекція 4: Функції (продовження) + Модулі + Помилки + Вступ до ООП`
**Target**: `Лекція 4: Функції (продовження) + Модулі + Помилки`

### MODIFY: Cell 1 (Learning Objectives)

**Remove**: Objective #5 about classes/OOP
**Keep**: Objectives 1-4 (lambda/map/filter, modules, exceptions, debugging)

### MODIFY: Cell 3 (Introduction)

**Remove**: Line mentioning "Вступ до ООП — від функцій до класів"
**Keep**: All other preview items

### MODIFY: Cell 38 (Package structure code)

**Change**: Replace `student.py  # class Student` with a non-OOP example like `validators.py  # validation functions`

### DELETE: Cells 54–69 (Section 5 — OOP)

All 16 cells covering:
- 5.1 Why OOP
- 5.2 Classes, __init__, self
- 5.3 Instance vs class attributes
- 5.4 Encapsulation
- 5.5 Inheritance
- 5.6 Polymorphism
- 5.7 Abstraction
- 5.8 Python OOP vs C#/Java/C++

### DELETE: Cells 79–81 (Exercise 4 — OOP bonus)

Remove the entire OOP exercise block (problem + code cell + solution).

### REWRITE: Cells 82–87 (Mini-project)

**Current**: "Менеджер оцінок студентів" using `class Student`
**Target**: "Конвеєр обробки даних студентів" (Student Data Processing Pipeline) using dicts + functions + error handling

Steps rewrite:
- Step 1: Define data validation functions (replace class definition)
- Step 2: Create data processing functions (map/filter/sorted with lambda)
- Step 3: Add error handling for invalid inputs (try/except, custom ValidationError)
- Step 4: Combine into working pipeline
- Solution: Full solution using only functions + error handling

### MODIFY: Cell 88 (Summary)

**Remove**: OOP-related takeaways
**Keep**: Functions, modules, errors, debugging takeaways

### MODIFY: Cell 89 (What's Next)

**Update**: Clearly state "У Лекції 5 ми вивчимо ООП (об'єктно-орієнтоване програмування)" as the primary Lecture 5 topic.

### MODIFY: Cell 90 (References)

**Remove**: OOP-specific references (classes docs, OOP tutorials)
**Keep**: Functions, modules, exceptions, debugging references

## Image Modifications (All Cells)

Every `![alt](https://remote-url)` MUST be replaced with `![alt](assets/diagrams/local-file.ext)`.

For sub-topics missing local images, either:
1. Download from alternative sources (Scaler, Programiz, etc.)
2. Create inline text-based diagrams in markdown

### Meme Requirements

- Cell 3 (Introduction): 1 programming meme — need to find/download a working one
- Cell 18 (S1.5 Scope): 1 scope/closure meme — need to find/download a working one
- Total memes: 2 minimum (constitution requirement)
