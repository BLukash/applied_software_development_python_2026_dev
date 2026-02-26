# Data Model: Lecture 5 — OOP in Python and Working with Files

**Date**: 2026-02-26
**Branch**: `008-lecture5-oop-files`

> **Scope note**: This lecture is educational content. The "data model" covers two layers:
> 1. **Pedagogical entities** — the concepts/objects taught in the notebook (what students learn to model)
> 2. **Mini-project entities** — the actual Python objects students will implement in the Contact Book mini-project

---

## Layer 1: Pedagogical Entities (Concepts Taught)

### 1.1 Class (Клас)

The fundamental unit of OOP. Students will learn to define and instantiate classes throughout the lecture.

**Core attributes introduced**:
- `__init__(self, ...)` — constructor method
- `self` — reference to the current instance
- Instance attributes — per-instance data set in `__init__`
- Class attributes — shared across all instances

**State transitions**:
- Class definition → instantiation → attribute access → method call

### 1.2 OOP Pillars (4 принципи ООП)

Four conceptual pillars, each demonstrated via a distinct class hierarchy:

| Pillar | Ukrainian | Python Mechanism | Demonstrated via |
|--------|-----------|------------------|-----------------|
| Encapsulation | Інкапсуляція | `_attr` (convention), `__attr` (name mangling), `@property` | `BankAccount` with balance |
| Inheritance | Успадкування | `class Dog(Animal)`, `super().__init__()` | `Animal → Dog → GuideDog` |
| Polymorphism | Поліморфізм | Method overriding, duck typing | `Shape → Circle, Rectangle` |
| Abstraction | Абстракція | `abc.ABC`, `@abstractmethod` | `Shape` as abstract base |

### 1.3 Dunder Methods (Магічні методи)

| Method | When triggered | Use case in lecture |
|--------|----------------|---------------------|
| `__init__` | `MyClass(...)` | Constructor — already taught in Section 1 |
| `__repr__` | `repr(obj)`, REPL | Developer-facing string representation |
| `__str__` | `str(obj)`, `print()` | User-facing string representation |
| `__eq__` | `obj1 == obj2` | Value equality vs identity |
| `__len__` | `len(obj)` | Makes container-like classes work with `len()` |
| `__hash__` | `hash(obj)`, dict keys, sets | Required when `__eq__` is defined |
| `__enter__` / `__exit__` | `with obj as ...:` | Context manager protocol — bridge to File I/O |
| `__getitem__` | `obj[key]` | Makes classes subscriptable (quirks section) |

### 1.4 Decorators (Декоратори класу)

| Decorator | Source | Purpose | Taught in |
|-----------|--------|---------|-----------|
| `@property` | stdlib | Controlled attribute access with validation | Section 3 |
| `@property.setter` | stdlib | Paired setter with validation logic | Section 3 |
| `@classmethod` | stdlib | Alternative constructor pattern | Section 3 |
| `@staticmethod` | stdlib | Utility function belonging to class namespace | Section 3 |
| `@dataclass` | `dataclasses` | Auto-generate `__init__`, `__repr__`, `__eq__` | Section 3 |
| `@abstractmethod` | `abc` | Enforce method override in subclasses | Section 3 |

### 1.5 File System Entities

| Entity | Python type | Key attributes |
|--------|-------------|----------------|
| File handle | `TextIOWrapper` | mode, encoding, name; opened via `open()` |
| Path | `pathlib.Path` | parts, suffix, stem, parent; supports `/` operator |
| JSON document | `dict` / `list` | Serialized with `json.dump()`, deserialized with `json.load()` |
| CSV document | `list[dict]` or `list[list]` | Read with `csv.DictReader`, written with `csv.DictWriter` |

---

## Layer 2: Mini-Project Entities (Contact Book)

### 2.1 Contact

The atomic unit of data in the mini-project. Implemented as a `@dataclass`.

```
Contact
├── name: str          (required, non-empty)
├── phone: str         (required, non-empty)
└── email: str         (optional, default="")
```

**Validation rules**:
- `name` and `phone` must be non-empty strings
- `email` is optional; if provided, should contain "@" (basic check, not enforced in class — shown as exercise extension)
- No setter validation — intentional simplicity; `@property` validation is shown on the main lecture `BankAccount` example

**Serialization**:
- To JSON dict: `{"name": ..., "phone": ..., "email": ...}`
- From JSON dict: `Contact(**d)` — direct unpacking works because field names match

**Python representation**:
```python
@dataclass
class Contact:
    name: str
    phone: str
    email: str = ""
```

**State**: Immutable by default (could be made `frozen=True` for homework extension).

---

### 2.2 ContactBook

The container class. Manages a collection of `Contact` objects. NOT a dataclass — demonstrates when to choose a full class over a dataclass.

```
ContactBook
├── _contacts: list[Contact]     (private, initialized empty)
│
├── add(contact: Contact) -> None
├── search(name: str) -> list[Contact]    (partial, case-insensitive match)
├── remove(name: str) -> bool             (removes first exact match; True if found)
├── save_to_json(path: str | Path) -> None
├── load_from_json(path: str | Path) -> ContactBook    (@classmethod)
├── __len__() -> int
└── __repr__() -> str
```

**Relationships**:
- `ContactBook` contains 0..N `Contact` objects (composition, not inheritance)
- `ContactBook` → `Contact`: one-to-many, via `list[Contact]`

**JSON persistence schema**:
```json
{
  "contacts": [
    {"name": "Іван Петренко", "phone": "+380501234567", "email": "ivan@example.com"},
    {"name": "Оля Коваль",    "phone": "+380671234567", "email": ""}
  ]
}
```

**State transitions**:
```
Empty ContactBook → add() → Non-empty → save_to_json() → JSON file
                                       ← load_from_json() ←
Non-empty → search(name) → list[Contact] (empty or matching)
Non-empty → remove(name) → True (found) | False (not found)
```

---

## Layer 3: Notebook Structure Entity

The notebook itself is the primary deliverable. Its structure is a data model for the `/speckit.tasks` phase.

```
Lecture05Notebook
├── header_section         (title, date, prerequisites)
├── learning_objectives    (3–5 bullet points)
├── intro_section          (motivation + meme)
│
├── section_1_oop_foundations
│   ├── motivation_cell    (dict+functions vs class comparison)
│   ├── class_syntax_cell  (class, __init__, self)
│   ├── instance_vs_class_vars_cell
│   └── methods_cell
│
├── section_2_oop_pillars
│   ├── encapsulation_cell (name mangling, conventions)
│   ├── inheritance_cell   (super(), MRO, multiple inheritance)
│   ├── polymorphism_cell  (method overriding)
│   ├── abstraction_cell   (ABC, @abstractmethod)
│   ├── dunder_methods_cell (repr, str, eq, len, hash)
│   └── composition_cell   (composition > inheritance)
│
├── section_3_pythonic_oop
│   ├── property_cell      (@property + setter with validation)
│   ├── classmethod_cell   (@classmethod as factory)
│   ├── staticmethod_cell  (@staticmethod, contrast with classmethod)
│   ├── dataclass_cell     (@dataclass, field(), frozen=True)
│   ├── abc_cell           (ABC, @abstractmethod, TypeError demo)
│   ├── python_vs_java_cell (sidebar comparison)
│   └── quirks_cell        (__slots__, mutable default, __getitem__)
│
├── section_4_file_io
│   ├── open_context_manager_cell
│   ├── encoding_cell      (utf-8, Ukrainian text demo)
│   └── pathlib_cell       (Path, /, exists, read_text, write_text)
│
├── section_5_json
│   ├── json_basics_cell   (load, loads, dump, dumps)
│   ├── schema_thinking_cell (JSON type table)
│   └── non_serializable_cell (datetime, default=str)
│
├── section_6_csv
│   ├── reader_dictreader_cell
│   ├── writer_dictwriter_cell
│   ├── delimiter_cell
│   └── pandas_teaser_cell
│
├── exercises
│   ├── exercise_1_cell    (starter: BankAccount class)
│   ├── exercise_1_solution (details tag)
│   ├── exercise_2_cell    (starter: inheritance/polymorphism)
│   └── exercise_2_solution (details tag)
│
├── mini_project
│   ├── intro_cell
│   ├── step_1_cell        (Contact @dataclass)
│   ├── step_2_cell        (ContactBook class skeleton)
│   ├── step_3_cell        (save/load JSON)
│   ├── step_4_cell        (demo: add, search, save, reload)
│   ├── full_solution_cell (details tag)
│   └── homework_extension_cell
│
├── summary_cell
├── whats_next_cell        (Lecture 6: REST + FastAPI)
├── homework_cell          (3 tasks)
└── references_cell
```
