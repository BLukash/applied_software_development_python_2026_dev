# Tasks: Lecture 5 — OOP in Python and Working with Files

**Input**: Design documents from `/specs/008-lecture5-oop-files/`
**Prerequisites**: plan.md ✅, spec.md ✅, research.md ✅, data-model.md ✅, contracts/notebook-structure.md ✅, quickstart.md ✅

**Tests**: No automated tests — validation is manual execution (Restart Kernel → Run All Cells).

**Organization**: Tasks grouped by User Story to enable independent section-by-section implementation. All tasks write to `lectures/05-oop-files/lecture-05.ipynb` unless otherwise stated.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (asset downloads, independent from notebook writing)
- **[Story]**: Which user story this task belongs to (US1–US5, maps to spec.md)
- All notebook cell tasks are **sequential within each phase** (cells build on prior cells)

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create directory structure and acquire all external assets before writing content. Asset tasks [P] can run in parallel with each other and in parallel with early notebook writing.

- [X] T001 Create lecture directory structure: `lectures/05-oop-files/`, `lectures/05-oop-files/assets/diagrams/`, `lectures/05-oop-files/assets/memes/`
- [X] T002 Create empty Jupyter notebook `lectures/05-oop-files/lecture-05.ipynb` with valid JSON skeleton (`{"nbformat": 4, "nbformat_minor": 5, "metadata": {...}, "cells": []}`)
- [ ] T003 [P] Acquire OOP humor meme image (search: "OOP meme python classes encapsulation") — download and save to `lectures/05-oop-files/assets/memes/oop-meme.png` (prefer CC or open license; fallback: any broadly shared Python meme)
- [ ] T004 [P] Acquire encoding/Unicode error meme image (search: "UTF-8 encoding error meme" or "mojibake meme") — save to `lectures/05-oop-files/assets/memes/encoding-meme.png`
- [X] T005 [P] Acquire MRO / Method Resolution Order diagram (search Real Python "Python MRO" or Python docs glossary) — save to `lectures/05-oop-files/assets/diagrams/mro-diagram.png`; if no suitable image found, note "use inline markdown diagram" in a placeholder file

**Checkpoint**: Directory exists, empty notebook valid, 2 memes and 1 diagram present in assets.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Notebook header and introduction cells that ALL subsequent sections depend on. Must be complete before writing any content section.

**⚠️ CRITICAL**: All subsequent phases write cells appended after these. Complete Phase 2 before US phases.

- [X] T006 Add header markdown cell to `lectures/05-oop-files/lecture-05.ipynb`: Lecture 5 title in Ukrainian (`# Лекція 5: ООП в Python та Робота з файлами`), date 2026-02-26, course name "Прикладна розробка ПЗ на Python 2026", and prerequisites block referencing Lectures 1–4 topics
- [X] T007 Add learning objectives markdown cell to `lectures/05-oop-files/lecture-05.ipynb` with exactly 5 bullet-point measurable objectives in Ukrainian: (1) define/use classes, (2) apply 4 OOP pillars, (3) use @property/@dataclass/ABC, (4) read/write files/JSON/CSV, (5) build OOP mini-project with serialization
- [X] T008 Add introduction markdown cell to `lectures/05-oop-files/lecture-05.ipynb`: motivational hook "Чому ООП?" with meme embedded as `![OOP Meme](assets/memes/oop-meme.png)` and 2–3 sentences of context bridging from Lecture 4 (procedural code) to today's OOP approach

**Checkpoint**: Notebook renders header, 5 objectives, and introduction meme without error.

---

## Phase 3: User Story 1 — OOP Foundations (Priority: P1) 🎯 MVP

**Goal**: Student can write their first Python class with `__init__`, `self`, instance attributes, class attributes, and call methods — after seeing WHY OOP is needed.

**Independent Test**: A student opens only the notebook cells from this section, defines `class Book(title, author, year)` with a `describe()` method, instantiates it, and calls the method — all without referencing other sections.

### Implementation for User Story 1

- [X] T009 [US1] Add Section 1 header markdown cell to `lectures/05-oop-files/lecture-05.ipynb`: `## 1. Основи ООП (OOP Foundations)` with a 2-sentence section overview in Ukrainian
- [X] T010 [US1] Add subsection 1.1 markdown + 2 code cells to `lectures/05-oop-files/lecture-05.ipynb` — "Why OOP?": (a) markdown explaining the motivation; (b) code cell showing the "dict + functions" approach for a Book (pain point); (c) code cell showing the equivalent `class Book` with `__init__` and `describe()` (clean solution); both cells must run without error and produce visible output
- [X] T011 [US1] Add subsection 1.2 markdown + 2 code cells to `lectures/05-oop-files/lecture-05.ipynb` — "`class`, `__init__`, `self`": (a) markdown explaining each keyword with English term in parentheses on first use; (b) minimal class definition cell (1 class, 2 attributes, `__init__`); (c) instantiation + attribute access cell showing `obj = MyClass(...)` and `print(obj.attr)`
- [X] T012 [US1] Add subsection 1.3 markdown + 2 code cells to `lectures/05-oop-files/lecture-05.ipynb` — "Instance vs Class Variables": (a) markdown explaining the difference with analogy; (b) code cell showing a `Counter` class with `count` as class variable and `value` as instance variable; (c) mutation demonstration cell showing that changing a class variable affects all instances but changing an instance variable does not — output must make the distinction visible

**Checkpoint (US1)**: Cells T009–T012 run independently. A student with zero OOP experience can write `class Book` with attributes and a method after reading Section 1.

---

## Phase 4: User Story 2 — OOP Pillars (Priority: P1)

**Goal**: Student understands and can implement all four OOP pillars in Python: encapsulation (name mangling + @property preview), inheritance (`super()`), polymorphism (method overriding), abstraction (ABC). Also learns the essential dunder methods and composition > inheritance.

**Independent Test**: Student writes `class Shape(ABC)` + `class Circle(Shape)` + `class Rectangle(Shape)` with `area()` — all without touching Section 1 cells. Running `[Circle(5), Rectangle(3, 4)]` loop with `.area()` returns correct results.

### Implementation for User Story 2

- [X] T013 [US2] Add Section 2 header markdown cell to `lectures/05-oop-files/lecture-05.ipynb`: `## 2. Чотири Принципи ООП (The Four Pillars)` with OOP pillars summary table (Markdown table: 4 rows × 4 columns — Принцип, Що означає, Python-механізм, Приклад — in Ukrainian with English terms)
- [X] T014 [US2] Add subsection 2.1 markdown + 2 code cells to `lectures/05-oop-files/lecture-05.ipynb` — "Інкапсуляція (Encapsulation)": (a) markdown explaining `_protected` convention vs `__private` name mangling; (b) `BankAccount` class cell with `_balance` (protected) and `__pin` (private, name-mangled); (c) demonstration cell showing `AttributeError` when accessing `__pin` directly but `_BankAccount__pin` works — include explicit note in markdown: "Python не забороняє доступ — це лише конвенція (convention)"
- [X] T015 [US2] Add subsection 2.2 markdown + 3 code cells to `lectures/05-oop-files/lecture-05.ipynb` — "Успадкування (Inheritance)": (a) markdown explaining inheritance + `super()`; (b) `class Animal` → `class Dog(Animal)` cell with `super().__init__()` and overridden `speak()`; (c) multiple inheritance cell with `class C(A, B)` + `print(C.__mro__)` showing MRO; (d) diamond inheritance cell with MRO resolution; embed `assets/diagrams/mro-diagram.png` with attribution caption
- [X] T016 [US2] Add subsection 2.3 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "Поліморфізм (Polymorphism)": (a) markdown explaining method overriding + duck typing note; (b) `Shape` base class + `Circle` + `Rectangle` cell where each overrides `area()` — demo: loop over `[Circle(5), Rectangle(3, 4)]` calling `.area()` and print results, showing polymorphism in action
- [X] T017 [US2] Add subsection 2.4 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "Абстракція (Abstraction)": (a) markdown: "abc.ABC — Python's mechanism for interface-like contracts"; (b) `from abc import ABC, abstractmethod`; abstract `Shape(ABC)` with `@abstractmethod def area(self) -> float`; `Circle(Shape)` with concrete `area()`; demonstrate `Shape()` raises `TypeError` and `Circle(5).area()` succeeds — cross-reference to Section 3 where ABC is revisited
- [X] T018 [US2] Add subsection 2.5 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "Магічні методи (Dunder Methods)": (a) markdown with table listing `__repr__`, `__str__`, `__eq__`, `__len__`, `__hash__` — when triggered, return type; (b) `Point(x, y)` class cell implementing all 5 methods with Ukrainian comments; show "before" (commented-out class without `__repr__`) and "after" output contrast in cell output
- [X] T019 [US2] Add subsection 2.6 markdown + 2 code cells to `lectures/05-oop-files/lecture-05.ipynb` — "Композиція > Успадкування (Composition > Inheritance)": (a) markdown explaining the fragile base class problem; (b) "bad" deep inheritance chain cell (3 levels, tightly coupled, labeled ПОГАНО); (c) refactored composition cell where same behavior is achieved via "has-a" relationship (labeled ДОБРЕ) — include brief note: "Favour composition over inheritance"

**Checkpoint (US2)**: All Section 2 cells run independently of Section 1. `Shape()` raises `TypeError`; `Circle(5).area()` and `Rectangle(3,4).area()` return correct values; MRO output visible.

---

## Phase 5: User Story 3 — Pythonic OOP Patterns (Priority: P2)

**Goal**: Student learns Python-specific OOP patterns: `@property`, `@classmethod`/`@staticmethod`, `@dataclass`, ABC (revisited), Python vs Java/C# comparison, and OOP quirks (`__slots__`, mutable defaults, `__getitem__`, context manager protocol).

**Independent Test**: Student takes any class and converts it to `@dataclass`, adds a `@property` computed attribute, adds a `@classmethod` factory — all from this section alone.

### Implementation for User Story 3

- [X] T020 [US3] Add Section 3 header markdown cell to `lectures/05-oop-files/lecture-05.ipynb`: `## 3. Pythonic ООП (Pythonic OOP Patterns)` with 2-sentence section intro in Ukrainian
- [X] T021 [US3] Add subsection 3.1 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "`@property`": (a) markdown: show Java-style `get_balance()`/`set_balance()` as anti-pattern first, then explain `@property` as Python's solution; (b) `BankAccount` class cell with `@property def balance(self)` and `@balance.setter` that validates `value >= 0` (raise `ValueError` otherwise); demonstrate: `account.balance = -100` raises `ValueError`; `account.balance = 500` works
- [X] T022 [US3] Add subsection 3.2 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "`@classmethod` та `@staticmethod`": (a) markdown contrasting instance method vs classmethod vs staticmethod using a 4-column table (First arg, Access instance, Access class, Use case); (b) `Contact` class cell (non-dataclass, simple) with: instance method `display()`, `@classmethod from_dict(cls, d)` as alternative constructor, `@staticmethod validate_phone(phone)` as utility — show all three being called
- [X] T023 [US3] Add subsection 3.3 markdown + 2 code cells to `lectures/05-oop-files/lecture-05.ipynb` — "`@dataclass`": (a) side-by-side comparison markdown/code — manual `__init__` class vs `@dataclass` equivalent producing identical behavior with fewer lines; (b) advanced dataclass cell: `field(default_factory=list)` for mutable default (demonstrate the footgun without it), `frozen=True` demo raising `FrozenInstanceError`, brief mention of `__post_init__`
- [X] T024 [US3] Add subsection 3.4 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "ABC (revisited + advanced note)": brief cross-reference to Section 2.4; add `@property` as `@abstractmethod` example (abstract property); note "ABC is Python's interface — альтернатива до Java `interface` та C# `interface`"
- [X] T025 [US3] Add subsection 3.5 markdown cell (no code) to `lectures/05-oop-files/lecture-05.ipynb` — "Python vs Java/C# (sidebar)": labeled `> **Sidebar для тих, хто знає Java/C#:**`; Markdown table comparing: access modifiers, interfaces, getters/setters, null, type system — 5 features × 3 columns (Feature, Java/C#, Python)
- [X] T026 [US3] Add subsection 3.6 markdown + 3 code cells to `lectures/05-oop-files/lecture-05.ipynb` — "Цікаві особливості (Tips and Quirks)": (a) `__slots__` cell: define class with `__slots__`, show reduced attribute flexibility + memory note; (b) mutable default footgun cell: `class Bag: def __init__(self, items=[])` broken example (ПОГАНО) vs `def __init__(self, items=None): self.items = items or []` fix (ДОБРЕ); (c) context manager protocol cell: implement `__enter__` + `__exit__` on a `Timer` class — show `with Timer() as t:` usage — add note: "Це той самий протокол, що використовує `with open()`!"

**Checkpoint (US3)**: Section 3 cells run. `FrozenInstanceError` raised on frozen dataclass mutation. `@property` setter rejects negative balance. `@classmethod` factory constructs object from dict.

---

## Phase 6: User Story 4 — File I/O and Data Serialization (Priority: P2)

**Goal**: Student can open/write/read files with context managers, handle UTF-8 encoding, use `pathlib.Path`, serialize Python objects to JSON and back, read/write CSV with stdlib, and see the pandas teaser.

**Independent Test**: Student writes a Python snippet in a fresh cell: creates a list of dicts, writes to JSON, reads back, prints result — without touching any OOP cell.

### Implementation for User Story 4

- [X] T027 [US4] Add Section 4 header markdown cell to `lectures/05-oop-files/lecture-05.ipynb`: `## 4. Робота з файлами (File I/O)` with 1-sentence intro; embed `encoding-meme.png`: `![Encoding Meme](assets/memes/encoding-meme.png)` with caption
- [X] T028 [US4] Add subsection 4.1 markdown + 2 code cells to `lectures/05-oop-files/lecture-05.ipynb` — "`open()` та контекстні менеджери (Context Managers)": (a) markdown explaining `with open(...) as f:` — why context manager prevents resource leaks; (b) write cell: `with open("test.txt", "w", encoding="utf-8") as f: f.write("Привіт, Іванко!")` — creates `test.txt`; (c) read cell: `with open("test.txt", "r", encoding="utf-8") as f: content = f.read(); print(content)` — reads and prints; both cells must run and show output
- [X] T029 [US4] Add subsection 4.2 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "Кодування (Encoding)": (a) markdown: explain why encoding matters for Ukrainian text; state the rule "Завжди використовуйте `encoding='utf-8'`"; (b) code cell demonstrating UTF-8 round-trip: write file with Ukrainian characters, read back, verify characters intact — output shows the Ukrainian string unchanged
- [X] T030 [US4] Add subsection 4.3 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "`pathlib.Path`": (a) markdown explaining `pathlib` as modern path API (Python 3.4+), mentioning `os.path` exists for legacy; (b) code cell: `from pathlib import Path`; `p = Path("data") / "contacts.json"`; `print(p, p.suffix, p.parent)`; `p.parent.mkdir(exist_ok=True)`; `p.write_text('{"test": 1}', encoding="utf-8")`; `print(p.read_text(encoding="utf-8"))` — all in one runnable cell
- [X] T031 [US4] Add Section 5 header + subsection 5.1 markdown + 2 code cells to `lectures/05-oop-files/lecture-05.ipynb` — JSON basics: section header `## 5. JSON`; (a) markdown explaining when to use `json.dumps/loads` (strings) vs `json.dump/load` (files); (b) string-based cell: `import json`; round-trip with `json.dumps(data)` → `json.loads(s)` with a dict including nested keys; (c) file-based cell: write list of dicts with `json.dump()` to `contacts.json`, read back with `json.load()`, print and compare — both cells produce visible output
- [X] T032 [US4] Add subsection 5.2 markdown cell to `lectures/05-oop-files/lecture-05.ipynb` — "Schema-like Thinking": Markdown table mapping Python types to JSON types (7 rows: dict→object, list→array, str→string, int/float→number, True/False→true/false, None→null, datetime/set/class→❌ Not supported); brief note on schema validation tools for the future
- [X] T033 [US4] Add subsection 5.3 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "Не-серіалізовані типи (Non-Serializable Types)": (a) markdown: "What happens when JSON can't handle your type?"; (b) code cell: `from datetime import datetime`; `json.dumps({"now": datetime.now()})` — catches `TypeError` in try/except, prints error; then `json.dumps({"now": datetime.now()}, default=str)` works; print result — demonstrates both failure and fix
- [X] T034 [US4] Add Section 6 header + subsection 6.1 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — CSV reading: section header `## 6. CSV`; create sample `sample.csv` file in the same directory with 3 columns and 3 data rows; (a) markdown explaining `csv.reader` (list-of-lists) vs `csv.DictReader` (list-of-dicts); (b) code cell: read same file with both `csv.reader` AND `csv.DictReader` in sequence, print output for each — contrast visible
- [X] T035 [US4] Add subsection 6.2 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — CSV writing: (a) markdown explaining `csv.writer` vs `csv.DictWriter`; (b) code cell: write 3 rows using `csv.DictWriter` with `writeheader()` and `writerows()`; read back and print to verify — single cell covering both write and verify
- [X] T036 [US4] Add subsection 6.3 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "Роздільники (Delimiters)": (a) markdown: "CSV does not always mean comma"; (b) code cell: write a semicolon-delimited file, read back with `csv.reader(f, delimiter=';')` — show correct parsing; add comment noting `delimiter='\t'` for tab-separated files
- [X] T037 [US4] Add subsection 6.4 markdown + 1 code cell to `lectures/05-oop-files/lecture-05.ipynb` — "pandas — короткий огляд (Teaser)": (a) markdown forward reference to Lecture 11; note `pip install pandas` required; (b) code cell: `import pandas as pd`; `df = pd.read_csv("sample.csv")`; `print(df)` — if pandas not installed, show expected output as comment; include `# pip install pandas` comment at top of cell

**Checkpoint (US4)**: Section 4–6 cells run in isolation from Sections 1–3. UTF-8 round-trip verified with Ukrainian characters. JSON save/load round-trip produces identical data. CSV write/read verified.

---

## Phase 7: User Story 5 — Mini-Project: Contact Book (Priority: P3)

**Goal**: Student builds a Contact Book combining `@dataclass` (Contact), `ContactBook` class (add/search/remove/save/load), and JSON persistence — completing it in 20–30 minutes in-class.

**Independent Test**: Student runs all mini-project cells top-to-bottom, adds 3 contacts, saves to `contacts.json`, restarts kernel, reloads from `contacts.json`, searches for a contact — finds it intact.

### Implementation for User Story 5

- [X] T038 [US5] Add mini-project intro markdown cell to `lectures/05-oop-files/lecture-05.ipynb`: `## 8. Міні-проєкт: Контактна книга (Contact Book Mini-Project)`; explain what will be built and the 4 steps; state the goal: "combine @dataclass + OOP + JSON"; explain homework extension
- [X] T039 [US5] Add Крок 1 starter code cell to `lectures/05-oop-files/lecture-05.ipynb` — `Contact @dataclass`: skeleton with `from dataclasses import dataclass, field`; `@dataclass class Contact:` with `# Крок 1: Додайте поля (fields): name, phone, email (optional with default "")` — student fills in the fields; after student section, add `# Приклад використання:` demo block showing instantiation
- [X] T040 [US5] Add Крок 2 starter code cell to `lectures/05-oop-files/lecture-05.ipynb` — `ContactBook` skeleton: class definition with `def __init__(self)`, `# Крок 2: Реалізуйте методи:` comments for `add(self, contact)`, `search(self, name) -> list[Contact]` (partial match), `remove(self, name) -> bool`, `__len__`, `__repr__` — student implements each; include type hints on all method signatures
- [X] T041 [US5] Add Крок 3 code cells to `lectures/05-oop-files/lecture-05.ipynb` — JSON persistence: (a) `save_to_json(self, path)` stub with `# Крок 3: Серіалізуйте контакти в JSON (serialize contacts to JSON)`; convert each Contact to dict, write with `json.dump`; (b) `@classmethod load_from_json(cls, path)` stub with `# Крок 3: Відновіть ContactBook з JSON (restore ContactBook from JSON)`; read with `json.load`, reconstruct `Contact` objects using `Contact(**d)` — student fills in the body
- [X] T042 [US5] Add Крок 4 demo code cell to `lectures/05-oop-files/lecture-05.ipynb`: fully runnable demonstration — create `ContactBook()`, add 3 Ukrainian-named contacts, print book (`__repr__`), call `save_to_json("contacts.json")`, create new `ContactBook` via `ContactBook.load_from_json("contacts.json")`, call `search()` for one name, print results — this cell must succeed only after steps 1–3 are complete
- [X] T043 [US5] Add full solution markdown cell to `lectures/05-oop-files/lecture-05.ipynb` — complete Contact Book implementation in `<details><summary>Повне рішення (клікніть щоб побачити)</summary>` HTML block containing the complete `Contact @dataclass` + `ContactBook` class with all methods implemented correctly and commented in Ukrainian
- [X] T044 [US5] Add homework extension markdown cell to `lectures/05-oop-files/lecture-05.ipynb`: describe 3 homework extension tasks — (1) add `export_to_csv(self, path)` method using `csv.DictWriter`; (2) make `Contact` frozen (`frozen=True`) and update `ContactBook` accordingly; (3) add email validation `@property` or `@staticmethod` that checks for "@" in email

**Checkpoint (US5)**: Demo cell (T042) runs top-to-bottom after steps 1–3 are completed. Save → reload → search round-trip succeeds. Homework tasks are clear and actionable.

---

## Phase 8: Exercises (Validation & Practice)

**Purpose**: Two standalone exercises placed after all content sections (per contract Section 7). Exercises reinforce US1+US2 learning.

- [X] T045 Add Exercise 1 starter code cell to `lectures/05-oop-files/lecture-05.ipynb` — `## 7. Практичні Вправи (Exercises)`; `### Вправа 1: BankAccount`; starter: `class BankAccount:` with `# Вправа 1: Ваш код тут` and TODO comments for `__init__(owner, initial_balance)`, `@property balance` with validation, `deposit(amount)`, `withdraw(amount)` with overdraft check, `__repr__` — include 3 test calls showing expected behavior
- [X] T046 Add Exercise 1 solution markdown cell to `lectures/05-oop-files/lecture-05.ipynb` — full `BankAccount` solution in `<details><summary>Рішення (клікніть щоб побачити)</summary>` block with complete implementation and Ukrainian comments
- [X] T047 Add Exercise 2 starter code cell to `lectures/05-oop-files/lecture-05.ipynb` — `### Вправа 2: Ієрархія Фігур (Shape Hierarchy)`; starter: `from abc import ABC, abstractmethod`; abstract `class Shape(ABC):` with `@abstractmethod area()` and `perimeter()` stubs; empty `class Circle(Shape):` and `class Rectangle(Shape):` — student implements both concrete classes
- [X] T048 Add Exercise 2 solution markdown cell to `lectures/05-oop-files/lecture-05.ipynb` — full `Circle` + `Rectangle` solution in `<details>` block with `area()` and `perimeter()` using `math.pi`, plus a demo loop

**Note**: Exercises are placed in the notebook at Section 7 (after CSV, before mini-project). In the task file they appear here as Phase 8 for clarity but must be inserted at the correct notebook position between T037 and T038.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Summary, What's Next, References, asset validation, and full notebook validation.

- [X] T049 Add Summary markdown cell to `lectures/05-oop-files/lecture-05.ipynb` — `## Підсумок (Summary)`: bullet list of ALL topics covered organized by 6 categories (OOP Foundations, 4 Pillars, Pythonic Patterns, File I/O, JSON, CSV); each bullet references the section number
- [X] T050 Add "What's Next" markdown cell to `lectures/05-oop-files/lecture-05.ipynb` — `## Що далі? (What's Next)`: preview of Lecture 6 (REST + FastAPI, Pydantic); note: "Ваш клас `Contact` з сьогодні — це концептуальна основа для Pydantic-моделей у FastAPI"; bullet list of Lecture 6 topics from constitution (HTTP, endpoints, Pydantic, Swagger)
- [X] T051 Add Homework markdown cell to `lectures/05-oop-files/lecture-05.ipynb` — `## Домашнє завдання (Homework)`: exactly 3 tasks: (1) extend Contact Book with `export_to_csv()`; (2) implement a `Library` class that manages a collection of `Book` objects with search and JSON persistence; (3) add `__enter__`/`__exit__` to `BankAccount` so it can be used with `with` statement
- [X] T052 Add References markdown cell to `lectures/05-oop-files/lecture-05.ipynb` — `## Джерела (References)`: three sections — "Офіційна документація" (Python docs: classes, dataclasses, abc, json, csv, pathlib), "Туторіали" (Real Python: OOP, dataclasses, pathlib, JSON), "Поглиблене вивчення" (Fluent Python Chapter on OOP, Python Tricks book)
- [X] T053 [P] Verify all asset files exist and are referenced correctly in `lectures/05-oop-files/lecture-05.ipynb`: confirm `assets/memes/oop-meme.png`, `assets/memes/encoding-meme.png`, `assets/diagrams/mro-diagram.png` are present; fix any broken references
- [X] T054 [P] Clean up temporary test files created during development (`test.txt`, `data/contacts.json` if in wrong location, `sample.csv` if should be in assets) — ensure only intended files remain in `lectures/05-oop-files/`
- [ ] T055 Validate notebook: Restart kernel → Run All Cells — verify ZERO errors. If any cell fails, fix before proceeding
- [X] T056 Validate constitution compliance for `lectures/05-oop-files/lecture-05.ipynb`: count and confirm ≥ 5 runnable code examples, ≥ 2 exercises with `<details>` solutions, ≥ 2 memes (local files), ≥ 1 table/diagram, Summary present, "What's Next" present, mini-project completable independently
- [X] T057 Validate consistency with Lectures 1–4: check section header format (`## N. Назва (English)`), Ukrainian language in all markdown, English terms in parentheses on first use, `<details>` solution format, diagram attribution captions — fix any inconsistencies

**Checkpoint (Final)**: All 57 tasks complete. Notebook runs clean top-to-bottom. All constitution requirements met.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately; T003/T004/T005 [P] can run in parallel with each other
- **Foundational (Phase 2)**: Depends on T001 + T002 (directory and notebook must exist)
- **US1 Phase 3**: Depends on Phase 2 completion — BLOCKS US2 (Section 2 cells follow Section 1 cells)
- **US2 Phase 4**: Depends on Phase 3 completion — BLOCKS US3
- **US3 Phase 5**: Depends on Phase 4 completion
- **US4 Phase 6**: Can start in parallel with US3 (File I/O sections are independent from OOP sections in notebook structure); however in a single-author context, complete US3 first
- **US5 Phase 7**: Depends on US3 (uses `@dataclass`) and US4 (uses JSON) — BOTH must be complete
- **Exercises Phase 8**: Depends on US2 (exercises use OOP pillars)
- **Polish Phase 9**: Depends on ALL prior phases

### User Story Dependencies

- **US1 (P1)**: Foundational → can start immediately
- **US2 (P1)**: Depends on US1 (builds on basic class knowledge)
- **US3 (P2)**: Depends on US2 (Pythonic patterns require understanding pillars)
- **US4 (P2)**: Independent of US1–US3; can start in parallel after Foundational
- **US5 (P3)**: Depends on US3 (@dataclass) AND US4 (JSON) — must be last

### Within Each Phase

- Asset tasks [P] can run in parallel with each other
- Notebook cell tasks are sequential (cells appended in order)

### Parallel Opportunities

```bash
# Phase 1 parallel assets (can run simultaneously):
Task: "T003 — Download OOP meme to assets/memes/"
Task: "T004 — Download encoding meme to assets/memes/"
Task: "T005 — Download MRO diagram to assets/diagrams/"

# Phase 6 (US4) can start alongside Phase 5 (US3) with two authors:
Author A: "T020–T026 — Pythonic OOP sections"
Author B: "T027–T037 — File I/O + JSON + CSV sections"

# Phase 9 polish parallel:
Task: "T053 — Verify assets"
Task: "T054 — Clean up temp files"
```

---

## Implementation Strategy

### MVP First (US1 + US2 Only — Core OOP)

1. Complete Phase 1: Setup + asset downloads
2. Complete Phase 2: Foundational header cells
3. Complete Phase 3 (US1): OOP Foundations
4. Complete Phase 4 (US2): OOP Pillars
5. **STOP and VALIDATE**: Students can understand Python classes end-to-end
6. Deliver partial lecture (OOP-only) for review

### Full Incremental Delivery

1. Setup + Foundational → header ready
2. US1 → Students can write their first class
3. US2 → Students understand OOP pillars
4. US3 → Students use Pythonic patterns
5. US4 → Students handle File I/O + serialization
6. US5 → Mini-project synthesizes everything
7. Exercises + Polish → Production-ready notebook

### Notebook Cell Order (Physical Order in .ipynb)

```text
T006 → T007 → T008                          (Header + Intro)
T009 → T010 → T011 → T012                  (Section 1: OOP Foundations / US1)
T013 → T014 → T015 → T016 → T017 → T018 → T019  (Section 2: Pillars / US2)
T020 → T021 → T022 → T023 → T024 → T025 → T026  (Section 3: Pythonic / US3)
T027 → T028 → T029 → T030                  (Section 4: File I/O / US4)
T031 → T032 → T033                         (Section 5: JSON / US4)
T034 → T035 → T036 → T037                  (Section 6: CSV / US4)
T045 → T046 → T047 → T048                  (Section 7: Exercises)
T038 → T039 → T040 → T041 → T042 → T043 → T044  (Section 8: Mini-project / US5)
T049 → T050 → T051 → T052                  (Section 9: Summary + References)
```

---

## Notes

- `[P]` tasks = different files or purely independent downloads — no shared state
- `[Story]` label maps each task to its user story for traceability
- Each user story's section is independently runnable as a standalone notebook extract
- The mini-project (US5) depends on US3 (@dataclass, @classmethod) and US4 (JSON) — implement last
- Exercises (Phase 8) are placed at Section 7 in the **notebook** but listed as Phase 8 in tasks for clarity — remember to insert them at the correct position between CSV (T037) and mini-project (T038)
- All code cells must run in Python 3.13+ clean kernel (plan.md update: 3.13+, not 3.11+)
- Pandas teaser cell (T037) may require `pip install pandas` — add `# pip install pandas` comment
- Avoid using remote image URLs — all assets must be local (lesson from Lecture 4 refinement, research R5)
- Address the learner as "ви" throughout (research R1 update: polite form confirmed)
