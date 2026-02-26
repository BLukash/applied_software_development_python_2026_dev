# Notebook Structure Contract: Lecture 5 — OOP in Python and Working with Files

**Date**: 2026-02-26
**Branch**: `008-lecture5-oop-files`
**Deliverable**: `lectures/05-oop-files/lecture-05.ipynb`

> This contract defines the required sections, their order, content type, and acceptance criteria. It serves as the authoritative spec for the notebook implementation in `/speckit.tasks`.

---

## Structural Rules (from Constitution + Research)

1. All markdown text in Ukrainian; English technical terms in parentheses on first use
2. Section headers: `## N. Назва розділу (English Name)`; subsections: `### N.N Підтема (English Subtopic)`
3. Code cells: inline Ukrainian comments; no wall-of-code without comments
4. Output cells immediately follow their code cell — no explanatory markdown between them
5. Exercise solutions hidden in `<details><summary>Рішення (клікніть щоб побачити)</summary>` HTML blocks
6. Memes embedded as `![alt](path)` in markdown cells
7. Diagrams in `assets/diagrams/` with `*Джерело: [link]*` attribution
8. Content duration: ≤ 1.5 hours (90 min) — see R10 timing in research.md

---

## Section 0: Header & Setup

**Cell type**: Markdown
**Required content**:
- Lecture number: `# Лекція 5: ООП в Python та Робота з файлами`
- Date, course name
- Prerequisites: "Ви вже знаєте: функції (Lecture 4), виключення, модулі, type hints"
- Learning objectives (3–5 bullet points):
  1. Визначати та використовувати класи (classes) в Python
  2. Застосовувати 4 принципи ООП (OOP pillars) на практиці
  3. Використовувати Pythonic-патерни: @property, @dataclass, ABC
  4. Читати та записувати файли (files), JSON та CSV
  5. Побудувати міні-проєкт з ООП + серіалізацією (serialization)

**Acceptance**: Cell renders without errors; all 5 objectives present.

---

## Section 0.1: Introduction + Meme

**Cell type**: Markdown
**Required content**:
- Motivational hook: "Чому ООП?"
- OOP meme (embedded image)
- Brief context: "Сьогодні ми переходимо від процедурного коду до об'єктно-орієнтованого підходу..."

**Acceptance**: At least 1 meme present in this section.

---

## Section 1: Основи ООП (OOP Foundations)

**Target time**: ~15 minutes

### 1.1 Навіщо ООП? (Why OOP?)

**Cell type**: Markdown + 2 Code cells
**Required content**:
- Side-by-side comparison: dict+functions approach vs class approach for same problem (e.g., representing a Book)
- Code cell 1: The "dict + functions" version (shows the pain point)
- Code cell 2: The class version (shows clean solution)
- Markdown explanation of the benefit

**Acceptance**: Both code cells run without error; student can see the contrast immediately.

### 1.2 Синтаксис класу: `class`, `__init__`, `self`

**Cell type**: Markdown + 2 Code cells
**Required content**:
- Markdown explaining `class` keyword, `__init__` as constructor, `self` as reference to instance
- Code cell 1: Minimal class definition with `__init__` and 1–2 attributes
- Code cell 2: Instantiating and accessing attributes

**Acceptance**: Code cells run; students see `obj.attribute` returning the value set in `__init__`.

### 1.3 Атрибути та методи: instance vs class

**Cell type**: Markdown + 2 Code cells
**Required content**:
- Instance attributes (set per object in `__init__`) vs class attributes (shared, set at class body level)
- Code cell demonstrating the mutation difference: changing a class attribute affects all instances; changing an instance attribute does not
- At minimum: `Counter.count` (class attribute) vs `counter.value` (instance attribute)

**Acceptance**: Running the mutation example shows the distinction clearly in output.

---

## Section 2: 4 Принципи ООП (The Four Pillars)

**Target time**: ~20 minutes

### 2.1 Інкапсуляція (Encapsulation)

**Cell type**: Markdown + 2 Code cells
**Required content**:
- Markdown: "Python does not enforce access control — only conventions"
- `_protected` (single underscore): convention, not enforced
- `__private` (double underscore): name mangling to `_ClassName__attr`
- Code cell: Demonstrate name mangling — accessing `__private` directly fails, but `_ClassName__attr` works
- Brief note: `@property` for controlled access (preview — detailed in Section 3)

**Acceptance**: Name mangling demonstrated; `AttributeError` shown when accessing `__attr` directly.

### 2.2 Успадкування (Inheritance)

**Cell type**: Markdown + 3 Code cells
**Required content**:
- Code cell 1: Simple single inheritance — `class Animal` → `class Dog(Animal)` with `super().__init__()`
- Code cell 2: Multiple inheritance + MRO example using `ClassName.__mro__`
- Code cell 3: Diamond inheritance MRO resolution
- Markdown: "composition > inheritance" principle with example of refactoring a deep hierarchy into composition

**Acceptance**: `super().__init__()` demonstrated; `.mro()` or `.__mro__` output shown; composition example runs.

### 2.3 Поліморфізм (Polymorphism)

**Cell type**: Markdown + 1 Code cell
**Required content**:
- Method overriding: `Shape.area()` as base, `Circle.area()` and `Rectangle.area()` as overrides
- Calling `shape.area()` on a list of mixed shapes — demonstrates polymorphism
- Note on duck typing: "Python's polymorphism is structural, not nominal"

**Acceptance**: Looping over `[Circle(5), Rectangle(3, 4)]` and calling `.area()` produces correct results.

### 2.4 Абстракція (Abstraction)

**Cell type**: Markdown + 1 Code cell
**Required content**:
- `from abc import ABC, abstractmethod`
- Abstract class `Shape(ABC)` with `@abstractmethod def area(self) -> float`
- Demonstrate: `Shape()` raises `TypeError`; `Circle(5)` works
- Note: This is also how we enforce the "contract" before we even write the implementation

**Acceptance**: `TypeError` raised for abstract class instantiation; concrete subclass instantiates cleanly.

### 2.5 Магічні методи (Dunder Methods)

**Cell type**: Markdown + 1 Code cell (demonstrating multiple dunders in one class)
**Required content**:
- All required dunders: `__repr__`, `__str__`, `__eq__`, `__len__`, `__hash__`
- Use one class (e.g., `Point` or `Vector`) to show all 5 in context
- Show the "before" (default `object.__repr__` output) vs "after" (custom `__repr__`)
- Table: each dunder, when triggered, return type expected

**Acceptance**: All 5 dunders demonstrated in one runnable cell; before/after contrast visible in output.

---

## Section 3: Pythonic ООП (Pythonic OOP Patterns)

**Target time**: ~20 minutes

### 3.1 `@property`

**Cell type**: Markdown + 1 Code cell
**Required content**:
- Show Java-style `get_balance()`/`set_balance()` anti-pattern first
- Replace with `@property` + `@balance.setter` with validation (`if value < 0: raise ValueError`)
- Demonstrate: assigning negative value raises `ValueError`

**Acceptance**: `ValueError` raised on invalid assignment; property access works like a regular attribute.

### 3.2 `@classmethod` та `@staticmethod`

**Cell type**: Markdown + 1 Code cell
**Required content**:
- `@classmethod` as alternative constructor: `Contact.from_dict(d)` pattern
- `@staticmethod` as class-scoped utility: `Contact.validate_phone(phone)` pattern
- Contrast table:

  | | Instance method | @classmethod | @staticmethod |
  |--|----------------|-------------|--------------|
  | First arg | `self` | `cls` | None |
  | Access to instance | Yes | No | No |
  | Access to class | Via `self.__class__` | Yes | No |
  | Use case | Object behavior | Alternative constructor | Utility |

**Acceptance**: Both decorators demonstrated; table renders correctly.

### 3.3 `@dataclass`

**Cell type**: Markdown + 2 Code cells
**Required content**:
- Code cell 1: Side-by-side — manual `__init__` vs `@dataclass` for same class
- Code cell 2: `field(default_factory=list)` for mutable defaults; `frozen=True` demo with `FrozenInstanceError`
- Mention `__post_init__` for post-initialization logic (brief)

**Acceptance**: `FrozenInstanceError` raised on mutation of frozen dataclass; `field(default_factory=list)` produces separate lists per instance.

### 3.4 ABC та абстрактні методи (revisited)

**Cell type**: Markdown + 1 Code cell (brief, references Section 2.4)
**Required content**:
- Cross-reference to Section 2.4 where ABC was introduced
- Show ABC used with `@property` as abstract property (brief advanced note)
- Note: this is Python's alternative to Java `interface` and C# `interface`

**Acceptance**: Single cell runs; cross-reference visible.

### 3.5 Python vs Java/C# (sidebar)

**Cell type**: Markdown only (no code)
**Required content**:
- Comparison table:

  | Feature | Java/C# | Python |
  |---------|---------|--------|
  | Access modifiers | `private`, `protected`, `public` | Convention: `_`, `__` |
  | Interfaces | `interface` keyword | ABC + `@abstractmethod` |
  | Getters/Setters | Explicit methods | `@property` |
  | Null | `null`/`None` | `None` |
  | Type system | Nominal (explicit types) | Duck typing + type hints |

**Acceptance**: Table renders; labeled as "sidebar" so students from procedural Python can skip.

### 3.6 Цікаві можливості та особливості (Tips and Quirks)

**Cell type**: Markdown + 2 Code cells
**Required content**:
- Code cell 1: `__slots__` — reduced memory, no arbitrary attributes
- Code cell 2: Mutable default footgun in `__init__` (without `__slots__`) + the `field(default_factory=list)` fix
- Markdown: `__getitem__` briefly — "making your class subscriptable" (1 example)
- Context manager protocol: `__enter__` / `__exit__` — brief example + note "this is what `with open()` uses!"

**Acceptance**: `__slots__` prevents arbitrary attribute; mutable default issue demonstrated and fixed.

---

## Section 4: Робота з файлами (File I/O)

**Target time**: ~8 minutes

### 4.1 `open()` та контекстні менеджери (Context Managers)

**Cell type**: Markdown + 2 Code cells
**Required content**:
- Code cell 1: Writing a file with `with open(..., 'w', encoding='utf-8') as f:`
- Code cell 2: Reading a file with `with open(..., 'r', encoding='utf-8') as f:`
- Explain WHY context manager (`with`) is better than explicit `.close()` — show resource leak risk

**Acceptance**: File written and read without error; Ukrainian characters preserved.

### 4.2 Кодування (Encoding)

**Cell type**: Markdown + 1 Code cell
**Required content**:
- Code cell: Write Ukrainian text WITHOUT specifying encoding on Windows (show platform warning), then repeat WITH `encoding='utf-8'`
- Explicit rule: "Always use `encoding='utf-8'` in all file operations"

**Acceptance**: UTF-8 round-trip demonstrated with Ukrainian characters.

### 4.3 `pathlib.Path`

**Cell type**: Markdown + 1 Code cell
**Required content**:
- `Path("data") / "contacts.json"` — path construction with `/` operator
- `path.exists()`, `path.read_text(encoding="utf-8")`, `path.write_text(...)`
- Note: `os.path` exists but `pathlib` is preferred in modern Python 3.4+

**Acceptance**: Path constructed without string concatenation; file read/written via `pathlib`.

---

## Section 5: JSON

**Target time**: ~8 minutes

### 5.1 Основи JSON (JSON Basics)

**Cell type**: Markdown + 2 Code cells
**Required content**:
- Code cell 1: `json.dumps()` and `json.loads()` (string-based)
- Code cell 2: `json.dump()` and `json.load()` (file-based)
- When to use which: strings for APIs, files for persistence

**Acceptance**: Round-trip JSON → string → JSON demonstrated; file-based round-trip demonstrated.

### 5.2 Схема-подібне мислення (Schema-like Thinking)

**Cell type**: Markdown (table)
**Required content**:
- Python ↔ JSON type mapping table:

  | Python | JSON |
  |--------|------|
  | `dict` | `object {}` |
  | `list` | `array []` |
  | `str` | `string ""` |
  | `int`, `float` | `number` |
  | `True`/`False` | `true`/`false` |
  | `None` | `null` |
  | `datetime`, `set`, class | ❌ Not natively supported |

**Acceptance**: Table renders; native limits clear.

### 5.3 Не-серіалізовані типи (Non-Serializable Types)

**Cell type**: Markdown + 1 Code cell
**Required content**:
- Demonstrate: `json.dumps(datetime.now())` raises `TypeError`
- Fix 1: `default=str` (simple, lossy)
- Fix 2: Custom encoder class (brief mention, not deep dive)

**Acceptance**: `TypeError` demonstrated; `default=str` workaround shown.

---

## Section 6: CSV

**Target time**: ~7 minutes

### 6.1 Читання CSV (Reading CSV)

**Cell type**: Markdown + 1 Code cell
**Required content**:
- `csv.reader` (list-of-lists)
- `csv.DictReader` (list-of-dicts, keyed by header)
- Show both on same file; contrast output format

**Acceptance**: Both readers demonstrated; difference in output format visible.

### 6.2 Запис CSV (Writing CSV)

**Cell type**: Markdown + 1 Code cell
**Required content**:
- `csv.writer` with `writerow()` / `writerows()`
- `csv.DictWriter` with `writeheader()` and `writerows()`

**Acceptance**: CSV file written; readable as plain text.

### 6.3 Роздільники (Delimiters)

**Cell type**: Markdown + 1 Code cell
**Required content**:
- `csv.reader(f, delimiter=';')` for semicolon-separated
- Note: Tab-separated files (`\t`) common in data science

**Acceptance**: Semicolon-delimited file read correctly.

### 6.4 pandas — короткий огляд (Teaser)

**Cell type**: Markdown + 1 Code cell (pandas)
**Required content**:
- `import pandas as pd; df = pd.read_csv("data.csv"); print(df)`
- Forward reference: "У Лекції 11 ми глибоко розберемо pandas для аналітики"
- Note: `pip install pandas` required for this cell

**Acceptance**: Cell runs if pandas installed; produces DataFrame output.

---

## Section 7: Практичні вправи (Exercises)

**Target time**: ~10 minutes (guided)

### Exercise 1: BankAccount

**Cell type**: Code (starter) + Markdown (solution in `<details>`)
**Required content**:
- Starter code: `class BankAccount:` with TODO comments
- Student must implement: `__init__(owner, balance)`, `@property balance` with validation, `deposit()`, `withdraw()` with overdraft check, `__repr__`
- Solution hidden in `<details>` block

**Acceptance**: Completed class works; invalid operations raise appropriate errors.

### Exercise 2: Shape Hierarchy

**Cell type**: Code (starter) + Markdown (solution in `<details>`)
**Required content**:
- Starter: abstract `Shape(ABC)` with `@abstractmethod area()` and `perimeter()`
- Student implements: `Circle(Shape)` and `Rectangle(Shape)` with both methods
- Solution hidden in `<details>` block

**Acceptance**: Both shapes compute area and perimeter; `Shape()` raises `TypeError`.

---

## Section 8: Міні-проєкт — Контактна книга (Mini-Project: Contact Book)

**Target time**: ~25 minutes in-class; ~35 min homework extension

**Cell type**: 5 stepped code cells + 1 full solution `<details>` + 1 homework extension markdown

**Steps**:

| Step | Cell content | Student task |
|------|-------------|-------------|
| Крок 1 | `@dataclass class Contact` skeleton | Add fields, optional email |
| Крок 2 | `class ContactBook` skeleton | Implement `add()`, `search()`, `remove()`, `__len__`, `__repr__` |
| Крок 3 | `save_to_json()` + `@classmethod load_from_json()` skeleton | Complete serialization/deserialization |
| Крок 4 | Demo cell | Run: add 3 contacts, save, reload, search, verify |
| Full solution | `<details>` | Complete implementation |
| Homework | Markdown | Add `export_to_csv()` method; make `Contact` frozen; add email validation |

**Acceptance**: Demo cell runs top-to-bottom without error; saving and reloading produces identical ContactBook.

---

## Section 9: Підсумок (Summary) + Що далі? (What's Next)

**Cell type**: 3 Markdown cells + 1 References cell

### Summary cell
- `## Підсумок (Summary)`
- Bullet list of all topics covered (6 categories: OOP foundations, pillars, Pythonic patterns, File I/O, JSON, CSV)

### What's Next cell
- Preview Lecture 6: `FastAPI`, REST, HTTP methods, Pydantic models
- Note: "Your `Contact` model from today is exactly the pattern Pydantic uses in Lecture 6"

### Homework cell
- Task 1: Extend Contact Book with `export_to_csv()` method
- Task 2: Add a `@property` for full contact info formatted string
- Task 3: Add basic email validation using string methods

### References cell
- **Офіційна документація**: Python docs for `classes`, `dataclasses`, `abc`, `json`, `csv`, `pathlib`
- **Туторіали**: Real Python links for OOP, dataclasses, pathlib
- **Поглиблене вивчення**: Fluent Python (Chapter on OOP), Python Tricks book

---

## Asset Requirements

### `assets/diagrams/`

| Filename | Content | Source |
|----------|---------|--------|
| `oop-pillars-table.png` or inline markdown table | 4 OOP pillars with Python mechanisms | Local (markdown table preferred) |
| `mro-diagram.png` | MRO C3 linearization diagram | Real Python or Python docs |
| `json-types-table.png` or inline markdown table | Python ↔ JSON type mapping | Local (markdown table preferred) |
| `class-vs-dict.png` (optional) | Side-by-side comparison diagram | Any open educational source |

### `assets/memes/`

| Filename | Content | Placement |
|----------|---------|-----------|
| `oop-meme.jpg/png` | OOP humor (classes, encapsulation) | Section 0.1 introduction |
| `encoding-meme.jpg/png` | Encoding/character issues humor | Section 4.2 encoding |

---

## Acceptance Criteria Summary

| Gate | Criterion |
|------|-----------|
| Cell execution | All cells run top-to-bottom without error in Python 3.11+ clean kernel |
| Language | All markdown text in Ukrainian; English terms in parentheses |
| Constitution minimums | ≥5 code examples, ≥2 exercises, ≥2 memes, ≥1 diagram/table |
| Topics coverage | All 12 constitution topics + 5 educator enhancements covered |
| Mini-project | Contact Book save/load round-trip verified |
| Timing | ≤ 90 minutes of content |
| Consistency | Same section/cell style as Lectures 1–4 |
