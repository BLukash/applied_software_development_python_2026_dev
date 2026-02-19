# Tasks: Lecture 4 — Functions (continue) + Modules + Errors + Intro to OOP

**Input**: Design documents from `/specs/006-lecture4-content/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: Not requested — this is educational content. Validation is manual (run all cells).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. All tasks modify the same notebook file (`lectures/04-functions-modules-errors-oop/lecture-04.ipynb`), so parallelization within stories is not possible. However, visual research tasks can be done in advance.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Notebook**: `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`
- **Meme assets**: `lectures/04-functions-modules-errors-oop/assets/memes/`
- **Design docs**: `specs/006-lecture4-content/`

---

## Phase 1: Setup

**Purpose**: Create directory structure and notebook skeleton

- [x] T001 Create directory structure: `lectures/04-functions-modules-errors-oop/` and `lectures/04-functions-modules-errors-oop/assets/memes/`
- [x] T002 Create empty Jupyter Notebook skeleton at `lectures/04-functions-modules-errors-oop/lecture-04.ipynb` with placeholder markdown cells for all 11 major sections defined in FR-003 (Learning Objectives, Prerequisites, Functions, Modules, Errors, Debugging, OOP, Exercises, Mini-Project, Summary/What's Next, References)

---

## Phase 2: Foundational (Contextual Analysis + Header Block)

**Purpose**: Analyze previous lectures for consistency and create the notebook header. MUST complete before any content sections.

- [x] T003 Read and analyze `lectures/03-data-structures/lecture-03.ipynb` in full detail. Skim `lectures/01-python-intro/lecture-01.ipynb` and `lectures/02-core-mechanics/lecture-02.ipynb`. Document: tone patterns, recurring phrases, Ukrainian terminology conventions (e.g., "винятки (exceptions)"), formatting style, section numbering convention, visual embedding patterns. Use findings to maintain consistency throughout Lecture 4. Reference: constitution Phase 2 Step 0, research.md R2
- [x] T004 Write the header block in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: (1) Title cell: "Лекція 4: Функції (продовження) + Модулі + Помилки + Вступ до ООП" with course name and year, (2) Learning Objectives cell: 5 measurable outcomes covering functions, modules, errors, debugging, and OOP, (3) Prerequisites cell: references Lectures 1–3 with specific concepts required, (4) Introduction cell: brief recap of Lecture 3 functions/collections, preview of Lecture 4 topics, include 1 meme. Reference: data-model.md Header Block

**Checkpoint**: Notebook skeleton ready with header. Content sections can now be filled.

---

## Phase 3: User Story 1 — Student Learns Advanced Function Concepts (Priority: P1)

**Goal**: Complete the "Functions (continued)" section with 8 sub-topics, each having Ukrainian markdown explanations, runnable Python 3.13+ code cells, and at least 2 internet-sourced visuals with attribution.

**Independent Test**: Open notebook, run all cells in Section 1 top-to-bottom — all execute without errors, all images render.

### Implementation for User Story 1

- [x] T005 [US1] Write sub-topic 1.1 "Лямбда-вирази (Lambda expressions)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining lambda syntax (`lambda args: expression`), when to use vs `def`, common use cases. Code cells: basic lambda vs equivalent `def`, lambda with multiple arguments, lambda as argument to `sorted()`. Find and embed 2 internet-sourced visuals (lambda syntax diagram, lambda vs def comparison) with alt-text and source attribution. Reference: contracts/section-outlines.md 1.1

- [x] T006 [US1] Write sub-topic 1.2 "Функції як параметри + сортування з `key`" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cells explaining first-class functions, passing functions as arguments, `sorted()` with `key`, `sort()` with `key` and `reverse`. Code cells: passing a function to another function, `sorted(students, key=lambda s: s["grade"])`, multi-criteria sorting. Find and embed 2 internet-sourced visuals (first-class functions concept, sorting with key diagram) with attribution. Reference: contracts/section-outlines.md 1.2

- [x] T007 [US1] Write sub-topic 1.3 "`map`, `filter`, `reduce`" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining `map(func, iterable)`, `filter(func, iterable)`, `functools.reduce(func, iterable)`, and comparison with comprehensions. Code cells: map converting strings to lengths, filter keeping positive numbers, reduce computing product, equivalent comprehension for each. Find and embed 2 internet-sourced visuals (map/filter/reduce flow diagram, comparison with comprehensions) with attribution. Reference: contracts/section-outlines.md 1.3

- [x] T008 [US1] Write sub-topic 1.4 "Ітератори та генератори (Iterators and generators)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cells explaining iterator protocol (`__iter__`/`__next__`), `range()` as lazy iterator (connect to Lecture 2), generator functions with `yield`, generator expressions, memory efficiency. Code cells: manual iteration with `iter()`/`next()`, simple generator function (countdown or fibonacci), generator expression vs list comprehension memory comparison (`sys.getsizeof`), chaining generators. Find and embed 2 internet-sourced visuals (generator yield flow, iterator protocol diagram) with attribution. Reference: contracts/section-outlines.md 1.4, research.md R5

- [x] T009 [US1] Write sub-topic 1.5 "Область видимості: правило LEGB та замикання (closures)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cells explaining LEGB (Local → Enclosing → Global → Built-in), `global` keyword, `nonlocal` keyword, what closures are and why they matter. Code cells: LEGB demonstration with same-named variables at each level, closure that "remembers" enclosing scope, practical closure `make_multiplier(n)`. Find and embed 2 internet-sourced visuals (LEGB diagram, closure visualization) + 1 scope/closure meme. Constitution requires "nice deep dive here with memes and visualizations". Reference: contracts/section-outlines.md 1.5

- [x] T010 [US1] Write sub-topic 1.6 "Декоратори — вступ (Decorators intro)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining what a decorator is (function wrapping another function), `@decorator` syntax as syntactic sugar. Code cells: manual wrapping `func = decorator(func)`, same with `@decorator` syntax, timing decorator example. Add brief note that decorators will be covered deeper in later lectures. Find and embed 2 internet-sourced visuals (decorator pattern diagram, @syntax explanation) with attribution. Reference: contracts/section-outlines.md 1.6

- [x] T011 [US1] Write sub-topic 1.7 "Підказки типів (Type hints intro)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining why type hints matter (readability, IDE support, mypy), basic syntax `def func(x: int) -> str:`, common types (`list[int]`, `dict[str, int]`, `tuple[int, ...]`), `Optional[X]` / `X | None`, and that type hints don't enforce at runtime. Code cells: function with type hints, variable annotations, `Optional` / `X | None` example. Find and embed 2 internet-sourced visuals (type hints syntax, mypy workflow or IDE tooltip) with attribution. Reference: contracts/section-outlines.md 1.7

- [x] T012 [US1] Write sub-topic 1.8 "Документаційні рядки (Docstrings / PEP 257)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining single-line vs multi-line docstrings, PEP 257 conventions, `help()` and `__doc__`, brief mention of Google/NumPy docstring styles. Code cells: function with proper multi-line docstring, accessing docstrings programmatically with `help()` and `.__doc__`. Find and embed 2 internet-sourced visuals (docstring format examples, PEP 257 reference) with attribution. Reference: contracts/section-outlines.md 1.8

**Checkpoint**: Functions (continued) section complete. All 8 sub-topics have Ukrainian explanations, runnable code, and 2+ internet visuals each (~16 visuals total). Section is independently testable by running all its cells.

---

## Phase 4: User Story 2 — Student Learns Modules and Imports (Priority: P1)

**Goal**: Complete the "Modules & Imports" section with 4 sub-topics, each having Ukrainian explanations, runnable code cells, and at least 2 internet-sourced visuals.

**Independent Test**: Run all cells in Section 2 — all imports resolve, code executes correctly, only standard library modules used.

### Implementation for User Story 2

- [x] T013 [US2] Write sub-topic 2.1 "Механізми імпорту (Import mechanisms)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining `import module`, `from module import name`, `from module import *` (and why to avoid), `import module as alias`, PEP 8 import order conventions. Code cells: different import styles demonstrated, aliasing (`import datetime as dt`). Find and embed 2 internet-sourced visuals (import mechanism diagram, import styles comparison) with attribution. Reference: contracts/section-outlines.md 2.1

- [x] T014 [US2] Write sub-topic 2.2 "Огляд стандартної бібліотеки (Standard library overview)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell with overview of key modules: `os`/`os.path`, `sys`, `math`, `datetime`, `random`, `json`, `collections` (Counter, defaultdict, namedtuple preview), `pathlib`. Code cells: quick demo of 3–4 modules (math, datetime, random, json), `collections.Counter` example. Find and embed 2 internet-sourced visuals (Python standard library map/overview, module categories) with attribution. Reference: contracts/section-outlines.md 2.2

- [x] T015 [US2] Write sub-topic 2.3 "Створення власних модулів + `__name__`" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining creating `.py` files as modules, `if __name__ == "__main__":` pattern and why it matters, building `utils/validators.py` (constitution requirement). Code cells: simulated module creation using `%%writefile` magic or showing file content in markdown, `__name__` behavior when imported vs run directly, practical validators module example. Find and embed 2 internet-sourced visuals (`__name__ == "__main__"` diagram, module import flow) with attribution. Reference: contracts/section-outlines.md 2.3, research.md R1 gap #5

- [x] T016 [US2] Write sub-topic 2.4 "Основи структури пакетів (Package structure basics)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining packages as directories with `__init__.py`, simple package layout, relative imports (brief), real-world project structure preview. Code cells: package directory tree as markdown diagram, import from package example. Find and embed 2 internet-sourced visuals (package structure diagram, `__init__.py` role) with attribution. Reference: contracts/section-outlines.md 2.4

**Checkpoint**: Modules & Imports section complete. All 4 sub-topics have Ukrainian explanations, runnable code, and 2+ internet visuals each (~8 visuals total).

---

## Phase 5: User Story 3 — Student Learns Error Handling (Priority: P1)

**Goal**: Complete the "Error Handling" section (4 sub-topics) and "Debugging & Logging" section (2 sub-topics), each with Ukrainian explanations, runnable code, and 2+ internet-sourced visuals.

**Independent Test**: Run all cells in Sections 3 and 4 — deliberate exceptions are caught, notebook doesn't crash, all code executes as expected.

### Implementation for User Story 3

- [x] T017 [US3] Write sub-topic 3.1 "Типи винятків та ієрархія (Exception types and hierarchy)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cells explaining common exceptions (`ValueError`, `TypeError`, `KeyError`, `IndexError`, `FileNotFoundError`, `ZeroDivisionError`), exception hierarchy (`BaseException` → `Exception` → specific), `isinstance()` for exceptions. Code cells: triggering different exception types, printing exception hierarchy. Find and embed 2 internet-sourced visuals (Python exception hierarchy tree, common exceptions cheat sheet) with attribution. Reference: contracts/section-outlines.md 3.1

- [x] T018 [US3] Write sub-topic 3.2 "`try`/`except`/`else`/`finally`" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining basic `try`/`except`, catching specific exceptions, multiple `except` blocks, `else` block (runs when no exception), `finally` block (always runs), `except Exception as e`. Code cells: basic try/except, multiple except blocks, full try/except/else/finally example, practical safe division function. Find and embed 2 internet-sourced visuals (try/except flow chart, else/finally behavior diagram) with attribution. Reference: contracts/section-outlines.md 3.2

- [x] T019 [US3] Write sub-topic 3.3 "`raise` + власні винятки (custom exceptions)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining `raise ValueError("message")`, re-raising exceptions (`raise` without argument), defining custom exception classes, exception chaining (`raise ... from ...`). Code cells: raising a built-in exception, custom `ValidationError` class, exception chaining example. Find and embed 2 internet-sourced visuals (raise flow, custom exception pattern) with attribution. Reference: contracts/section-outlines.md 3.3

- [x] T020 [US3] Write sub-topic 3.4 "Найкращі практики (Best practices)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining catching specific exceptions (not bare `except:`), EAFP vs LBYL (Easier to Ask Forgiveness vs Look Before You Leap), don't silence exceptions, logging exceptions. Code cells: bad vs good exception handling comparison, EAFP vs LBYL example. Find and embed 2 internet-sourced visuals (EAFP vs LBYL comparison, exception anti-patterns) with attribution. Reference: contracts/section-outlines.md 3.4

- [x] T021 [US3] Write sub-topic 4.1 "Відлагодження: `breakpoint()` та pdb" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining `breakpoint()` function (Python 3.7+), basic pdb commands (`n` next, `s` step, `c` continue, `p` print, `q` quit), when to use debugger vs print statements. Code cell: function with `breakpoint()` shown but not auto-run (explain pdb is interactive); show pdb session output as markdown. Find and embed 2 internet-sourced visuals (pdb commands cheat sheet, debugger workflow) with attribution. Reference: contracts/section-outlines.md 4.1, research.md R6

- [x] T022 [US3] Write sub-topic 4.2 "Модуль `logging`" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL), `logging.basicConfig()`, creating a logger, when to use logging vs `print()`. Code cells: basic logging setup, different logging levels, logging with format string. Find and embed 2 internet-sourced visuals (logging levels pyramid, logging vs print comparison) with attribution. Reference: contracts/section-outlines.md 4.2, research.md R6

**Checkpoint**: Error Handling + Debugging & Logging sections complete. All 6 sub-topics have Ukrainian explanations, runnable code, and 2+ internet visuals each (~12 visuals total).

---

## Phase 6: User Story 4 — Student Gets Introduction to OOP (Priority: P2)

**Goal**: Complete the "Intro to OOP" section with 8 sub-topics covering all 4 OOP pillars at introductory level plus Python vs C#/Java/C++ comparison. Each sub-topic has Ukrainian explanations, runnable code, and 2+ internet-sourced visuals.

**Independent Test**: Run all cells in Section 5 — all class definitions, instantiations, and method calls work without errors.

### Implementation for User Story 4

- [x] T023 [US4] Write sub-topic 5.1 "Навіщо ООП? Мотивація (Why OOP?)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining the problem (managing related data and functions together), progression from dicts/functions to classes, 4 pillars overview (encapsulation, inheritance, polymorphism, abstraction). Code cells: "Before OOP" example with dict + standalone functions, "After OOP" example with class encapsulating data + behavior. Find and embed 2 internet-sourced visuals (4 OOP pillars diagram, procedural vs OOP comparison) with attribution. Reference: contracts/section-outlines.md 5.1

- [x] T024 [US4] Write sub-topic 5.2 "Класи, об'єкти, `__init__`, `self`" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining `class` keyword, `__init__` as constructor, `self` parameter, creating instances, terminology (class = blueprint, object = instance). Code cells: simple `Student` class definition, creating multiple instances, accessing attributes. Find and embed 2 internet-sourced visuals (class vs object/blueprint analogy, `__init__` and `self` diagram) with attribution. Reference: contracts/section-outlines.md 5.2

- [x] T025 [US4] Write sub-topic 5.3 "Атрибути екземпляра vs класу + методи" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining instance attributes (set in `__init__`), class attributes (shared across instances), instance methods, `@classmethod` and `@staticmethod` (brief intro). Code cells: class with both instance and class attributes, method modifying instance state, brief classmethod example. Find and embed 2 internet-sourced visuals (instance vs class attributes diagram, method types comparison) with attribution. Reference: contracts/section-outlines.md 5.3

- [x] T026 [US4] Write sub-topic 5.4 "Інкапсуляція (Encapsulation)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining public attributes, `_protected` convention, `__private` name mangling, `@property` (brief intro), Python philosophy "We're all consenting adults". Code cells: class with public, `_protected`, `__private` attributes, name mangling demonstration, simple `@property` example. Find and embed 2 internet-sourced visuals (encapsulation levels diagram, Python naming conventions) with attribution. Reference: contracts/section-outlines.md 5.4, research.md R4

- [x] T027 [US4] Write sub-topic 5.5 "Наслідування (Inheritance basics)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining parent/child class relationship, `super().__init__()`, method inheritance and overriding, `isinstance()` and `issubclass()`. Code cells: `Animal` → `Dog`/`Cat` inheritance example, method overriding, `super()` usage. Find and embed 2 internet-sourced visuals (inheritance hierarchy diagram, `super()` flow) with attribution. Reference: contracts/section-outlines.md 5.5, research.md R4

- [x] T028 [US4] Write sub-topic 5.6 "Поліморфізм (Polymorphism)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining same method name with different behavior, duck typing in Python. Code cells: different classes with same `.speak()` or `.area()` method, loop calling same method on different objects. Find and embed 2 internet-sourced visuals (polymorphism diagram, duck typing meme/illustration) with attribution. Reference: contracts/section-outlines.md 5.6, research.md R4

- [x] T029 [US4] Write sub-topic 5.7 "Абстракція (Abstraction concept)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell explaining hiding complexity behind simple interfaces, brief mention of `abc.ABC` and `@abstractmethod`, real-world analogy (car dashboard hides engine complexity). Code cell: conceptual or very brief ABC example. Find and embed 2 internet-sourced visuals (abstraction analogy diagram, abstraction layers) with attribution. Reference: contracts/section-outlines.md 5.7, research.md R4

- [x] T030 [US4] Write sub-topic 5.8 "Python ООП vs C#/Java/C++" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell with comparison: no access modifiers (conventions instead), no interfaces (duck typing + ABC), no method overloading (use default arguments), multiple inheritance support, everything is an object, simpler syntax. Code cell or markdown table: side-by-side Python vs pseudo-Java/C# comparison. Find and embed 2 internet-sourced visuals (Python vs Java OOP comparison, Python simplicity meme) with attribution. Reference: contracts/section-outlines.md 5.8, research.md R1 gap #7

**Checkpoint**: Intro to OOP section complete. All 8 sub-topics have Ukrainian explanations, runnable code, and 2+ internet visuals each (~16 visuals total). All 4 OOP pillars covered at introductory level.

---

## Phase 7: User Story 5 — Student Completes Practical Exercises and Mini-Project (Priority: P2)

**Goal**: Create exercises with TODO cells and `<details>` solutions, plus a mini-project integrating Functions + Modules + Errors + OOP.

**Independent Test**: Verify exercise cells have TODO placeholders, solution blocks exist, solutions execute correctly when revealed.

### Implementation for User Story 5

- [x] T031 [US5] Write Exercise 1 "Функції: лямбда, map/filter, сортування з key" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell with problem statement (e.g., process a list of student records using lambda, map/filter, sorted with key), empty code cell with `# Ваш код тут` TODO comment, collapsible `<details><summary>Рішення</summary>` block with working solution code. Verify solution executes correctly. Reference: data-model.md Section 6 Exercise 1

- [x] T032 [US5] Write Exercise 2 "Модулі: створення та імпорт модуля валідаторів" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell with problem statement (create a validators module with functions for email, age, password validation), empty code cell with TODO comment, collapsible `<details>` block with working solution. Verify solution executes correctly. Reference: data-model.md Section 6 Exercise 2

- [x] T033 [US5] Write Exercise 3 "Помилки: безпечний зчитувач з обробкою винятків" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell with problem statement (build a safe data processor with proper exception handling, custom exceptions, logging), empty code cell with TODO comment, collapsible `<details>` block with working solution. Verify solution executes correctly. Reference: data-model.md Section 6 Exercise 3

- [x] T034 [US5] Write Exercise 4 (bonus) "ООП: ієрархія класів" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell with problem statement (create a class hierarchy, e.g., Shape → Circle/Rectangle with area/perimeter methods), empty code cell with TODO comment, collapsible `<details>` block with working solution. Verify solution executes correctly. Reference: data-model.md Section 6 Exercise 4

- [x] T035 [US5] Write Mini-Project "Менеджер оцінок студентів (Student Grade Manager)" in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell with problem statement and requirements. 4 TODO code cells: Step 1 — define `Student` class with validation, Step 2 — create grade processing functions (map/filter/sorted with lambda), Step 3 — add error handling for invalid inputs, Step 4 — combine into working solution. Collapsible `<details>` block with full integrated solution. Verify solution executes correctly. Integrates: OOP + Functions + Errors (+ optionally Modules). Reference: data-model.md Section 7, contracts/section-outlines.md Mini-Project

**Checkpoint**: All exercises (3 + 1 bonus) and 1 mini-project complete. Each has problem statement, TODO cells, and working `<details>` solutions.

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Closing sections, final validation, and quality assurance

- [x] T036 Write "Підсумок (Summary)" section in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell listing key takeaways from all 5 major sections (Functions, Modules, Errors, Debugging, OOP) in bullet-point format. Follow Lecture 3 summary style. Reference: data-model.md Closing Block

- [x] T037 Write "Що далі? (What's Next)" + "Домашнє завдання (Homework)" sections in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell previewing Lecture 5 topics (OOP deep dive: `@dataclass`, magic methods, composition > inheritance, file I/O, JSON/CSV). Homework section with 3–4 assignments reinforcing Lecture 4 concepts. Reference: data-model.md Closing Block

- [x] T038 Write "Джерела (References)" section in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: markdown cell with links to official Python documentation (functions, modules, exceptions, classes), Real Python tutorials, and other reputable educational resources. Follow Lecture 3 references format with sections for official docs, tutorials, and further reading. Reference: data-model.md Closing Block, FR-013

- [x] T039 Final validation of `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: (1) Restart kernel and run all cells top-to-bottom — verify zero errors, (2) Count internet-sourced visuals per sub-topic — verify minimum 2 each across all 26 sub-topics (~52+ total), (3) Verify all image URLs load correctly, (4) Check Ukrainian text consistency with Lectures 1–3 (terminology, tone, formatting), (5) Verify no external pip packages used, (6) Verify meme count (at least 2 per constitution), (7) Check section ordering matches FR-003, (8) Verify all `<details>` solution blocks work. Reference: quickstart.md Step 3, plan.md Phase 7

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 — BLOCKS all content phases
- **US1 Functions (Phase 3)**: Depends on Phase 2 — first content section in notebook
- **US2 Modules (Phase 4)**: Depends on Phase 3 — follows Functions section in notebook order
- **US3 Errors + Debug (Phase 5)**: Depends on Phase 4 — follows Modules section in notebook order
- **US4 OOP (Phase 6)**: Depends on Phase 5 — follows Errors/Debug section in notebook order
- **US5 Exercises (Phase 7)**: Depends on Phases 3–6 — exercises reference all prior sections
- **Polish (Phase 8)**: Depends on Phase 7 — closing sections and validation

### User Story Dependencies

- **US1 (P1)**: After Foundational — no dependency on other stories
- **US2 (P1)**: After US1 — must follow in notebook order (Section 2 after Section 1)
- **US3 (P1)**: After US2 — must follow in notebook order (Sections 3–4 after Section 2)
- **US4 (P2)**: After US3 — must follow in notebook order (Section 5 after Sections 3–4)
- **US5 (P2)**: After US1–US4 — exercises reference all prior content

**Note**: Stories must be sequential (not parallel) because they all modify the same notebook file and the content must appear in order. However, each story produces an independently testable section.

### Within Each User Story

- Sub-topics are sequential within each section (they build on each other conceptually)
- Each sub-topic task includes: markdown explanation → visual research + embedding → code cells
- Complete each sub-topic fully before moving to the next

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001–T002)
2. Complete Phase 2: Foundational (T003–T004)
3. Complete Phase 3: User Story 1 — Functions (T005–T012)
4. **STOP and VALIDATE**: Run all cells in Functions section, verify 16 visuals, check Ukrainian quality
5. Can be demoed as a partial lecture

### Incremental Delivery

1. Setup + Foundational → Notebook skeleton ready
2. Add US1 Functions → Test → 8 sub-topics with ~16 visuals
3. Add US2 Modules → Test → 4 sub-topics with ~8 visuals
4. Add US3 Errors + Debug → Test → 6 sub-topics with ~12 visuals
5. Add US4 OOP → Test → 8 sub-topics with ~16 visuals
6. Add US5 Exercises → Test → 3 exercises + 1 bonus + mini-project
7. Add Polish → Full validation → Complete lecture

### Content Quality Reminder

For EVERY sub-topic task:
- Write Ukrainian explanatory text with English technical terms in parentheses on first use
- Find 2+ internet-sourced visuals from stable sources (Real Python, Programiz, GeeksforGeeks, official docs)
- Embed visuals as `![Alt text](URL)` with `*Джерело: [Site](URL)*` attribution
- Write runnable Python 3.13+ code cells with minimal comments
- Keep emoji/icon usage to 1–2 per section maximum (constitution rule)

---

## Notes

- All tasks modify the same file: `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`
- No [P] parallelization within stories — single file constraint
- Each task is self-contained enough for an LLM to execute with the referenced design docs
- Commit after each completed phase (not after each task)
- Visual URLs should be verified during T039 final validation
- Total estimated cells: 55–70
- Total estimated internet-sourced visuals: ~52 (26 sub-topics × 2 minimum)
