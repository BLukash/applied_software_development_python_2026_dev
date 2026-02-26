# Feature Specification: Lecture 5 — OOP in Python and Working with Files

**Feature Branch**: `008-lecture5-oop-files`
**Created**: 2026-02-26
**Status**: Draft
**Input**: User description: "I want you, experienced educator and Python staff engineer to create Lecture 5 (OOP in Python and working with files). Stick to the predefined in constitution list of topics, but enhance in depth or maybe add more topics where you suggest it is required"

## User Scenarios & Testing *(mandatory)*

### User Story 1 — OOP Foundations: Writing the First Python Class (Priority: P1)

A student who has been writing procedural Python code (functions, modules, error handling from Lectures 1–4) encounters a problem where related data and behavior are scattered across multiple functions and dicts. The student learns why OOP exists, writes their first class from scratch — defining `__init__`, understanding `self`, working with instance attributes, and calling methods — and immediately recognizes when OOP is and isn't the right tool.

**Why this priority**: Without this foundation, every subsequent OOP topic becomes abstract. Students must be able to construct and instantiate a class before any other concept lands. This is the P1 MVP: a student who completes only this story can already replace "dict + function" patterns with a clean class.

**Independent Test**: The student can open a fresh notebook, define a class `Book` with title, author, and year fields, add a method `describe()`, instantiate it, and call the method — all without looking anything up. The notebook section covering this topic is fully runnable in isolation.

**Acceptance Scenarios**:

1. **Given** a student with no OOP experience opens the notebook, **When** they read the motivation section, **Then** they can articulate in one sentence why classes exist (grouping related state and behavior)
2. **Given** the introductory code example, **When** a student runs it, **Then** they observe a class being defined with `__init__` and `self`, an instance being created, and a method being called — with zero errors
3. **Given** Exercise 1 starter code, **When** the student completes it, **Then** they have a working class with at least 2 attributes and 1 method
4. **Given** a student familiar with C# or Java, **When** they read the "Python vs other languages" sidebar, **Then** they understand Python does not require explicit access modifiers or interface declarations at this stage

---

### User Story 2 — OOP Pillars: Encapsulation, Inheritance, and Polymorphism (Priority: P1)

A student who can define basic classes now needs to understand the four OOP pillars as applied in Python — not theoretically, but as concrete patterns. The student learns name mangling for encapsulation, writes subclasses using `super()`, observes polymorphism via method overriding, and understands when composition is preferable over deep inheritance chains. The student also learns the essential dunder (magic) methods (`__repr__`, `__str__`, `__eq__`, `__len__`, `__hash__`) that make objects behave like "real" Python citizens.

**Why this priority**: These are the core patterns that make OOP useful in practice. Without them, students cannot reason about library code (e.g., SQLAlchemy models, Pydantic schemas in later lectures) or write maintainable class hierarchies.

**Independent Test**: A student can write two related classes — a base `Shape` and a subclass `Circle` — with proper inheritance, `super().__init__()`, `__repr__`, and a working `area()` method. They can run both classes in a cell without touching any other section of the notebook.

**Acceptance Scenarios**:

1. **Given** a code example demonstrating private/protected attributes, **When** a student runs it, **Then** they observe that `_protected` is a convention and `__private` triggers name mangling — and neither enforces true access restriction
2. **Given** a class hierarchy example, **When** a student adds a third subclass, **Then** the base class methods still work without modification (polymorphism verified)
3. **Given** Exercise 2 on inheritance, **When** a student implements `super().__init__()` in a subclass, **Then** the parent class attributes are correctly initialized
4. **Given** an example of 3-level deep inheritance, **When** the student reads the "composition > inheritance" section, **Then** they can rewrite the example using composition and explain why it is more maintainable
5. **Given** a class without `__repr__`, **When** printed, **Then** students see a cryptic object address; after adding `__repr__`, they see a useful string — the contrast makes the lesson concrete

---

### User Story 3 — Pythonic OOP: Properties, Class/Static Methods, Dataclasses, and Quirks (Priority: P2)

A student who understands basic OOP now learns Python-specific patterns that separate "Python-flavored OOP" from Java/C# OOP. This includes `@property` for controlled attribute access without explicit getters/setters, `@classmethod` and `@staticmethod` for alternative constructors and utilities, `@dataclass` for eliminating boilerplate, abstract base classes (ABC) for interface-like contracts, and a curated set of "interesting Python class tips and quirks" (e.g., `__slots__`, metaclass curiosity, mutable default pitfalls).

**Why this priority**: These patterns appear throughout the Python ecosystem — Pydantic, SQLAlchemy, FastAPI models, standard library — so students will encounter them even before Lecture 6. A student who understands `@property` and `@dataclass` can already read FastAPI/Pydantic source code with comprehension.

**Independent Test**: A student can take an existing "vanilla" class with a `__init__` and convert it to a `@dataclass`, add a `@property` for a computed attribute, add a `@classmethod` factory method — all in a single cell without referencing other sections.

**Acceptance Scenarios**:

1. **Given** a class with a raw `age` attribute, **When** the student adds `@property` with a setter that validates age ≥ 0, **Then** assigning a negative age raises `ValueError`
2. **Given** a `@dataclass` example, **When** compared side-by-side with the equivalent `__init__` version, **Then** students see identical behavior with significantly less boilerplate
3. **Given** a frozen dataclass (`frozen=True`), **When** a student tries to mutate a field, **Then** a `FrozenInstanceError` is raised — students understand immutability without needing `tuple`
4. **Given** an ABC example with `@abstractmethod`, **When** a student tries to instantiate the abstract class, **Then** a `TypeError` is raised — the contract enforcement is demonstrated concretely
5. **Given** the "quirks" section, **When** students run the `__slots__` example, **Then** they observe reduced memory footprint and the inability to add arbitrary attributes — and understand when `__slots__` is worth it

---

### User Story 4 — File I/O and Data Serialization: Files, JSON, and CSV (Priority: P2)

A student who can model data with classes now needs to persist it. The student learns how Python opens and reads/writes files safely with context managers, handles encoding correctly, serializes Python objects to JSON and reads them back, and processes tabular data with the `csv` module — while getting a brief preview of what `pandas` adds on top. A natural bridge between this section and OOP is demonstrated: the student serializes a custom object to JSON and reconstructs it.

**Why this priority**: File I/O and serialization are universal practical skills. They also serve as the natural "output" for the OOP mini-project: after modelling data with classes, students save it to disk. This section is independently useful even without the rest of the lecture.

**Independent Test**: A student can write a Python snippet that creates a list of dicts, writes it to a JSON file, reads it back, and prints the result — without touching any OOP cell. Similarly, a second snippet reads a CSV file and prints column summaries using only the standard library.

**Acceptance Scenarios**:

1. **Given** a file-writing example, **When** the student uses `open()` with a context manager (`with` block), **Then** the file handle is automatically closed — no explicit `.close()` required
2. **Given** a file written with `encoding='utf-8'`, **When** the same file is read back with `encoding='utf-8'`, **Then** Ukrainian characters (е, и, і) round-trip without corruption
3. **Given** a Python object (e.g., list of dicts), **When** serialized with `json.dump()` and read back with `json.load()`, **Then** the result is structurally identical to the original
4. **Given** a CSV file with a header row, **When** read with `csv.DictReader`, **Then** each row is a `dict` keyed by column name — no manual parsing needed
5. **Given** a `pandas` teaser cell at the end of the CSV section, **When** run, **Then** the same CSV is read in one line with `pd.read_csv()` and printed as a DataFrame — students see why `pandas` becomes important in Lecture 11
6. **Given** the modern path handling sidebar, **When** students use `pathlib.Path` to construct file paths, **Then** the code is cross-platform and avoids string concatenation for paths

---

### User Story 5 — Mini-Project: OOP Contact Book with File Persistence (Priority: P3)

A student applies the full lecture in a 20–30 minute in-class mini-project: a small "Contact Book" application. Contacts are modelled as a `@dataclass`, a `ContactBook` class manages a collection of contacts (with add, search, remove), and the entire book is saved to and loaded from a JSON file using a `@classmethod` factory. This synthesizes OOP design (encapsulation, composition, dataclass, classmethod) with file I/O (JSON serialization).

**Why this priority**: The mini-project provides the "it all comes together" moment. It is the constitution-mandated practical artifact for Lecture 5 onward and serves as homework extension material.

**Independent Test**: A student can run the mini-project cells top-to-bottom in a clean kernel, add three contacts, save to `contacts.json`, restart the kernel, reload from `contacts.json`, and find all three contacts intact.

**Acceptance Scenarios**:

1. **Given** the `Contact` dataclass starter code, **When** the student instantiates it, **Then** all fields (name, phone, email) are accessible as attributes
2. **Given** the `ContactBook` class with `save_to_json()` and `load_from_json()` methods, **When** a student saves and reloads, **Then** the reconstructed `ContactBook` contains the same `Contact` objects
3. **Given** a search for a non-existent name, **When** `search()` is called, **Then** it returns an empty list (no crash)
4. **Given** the homework extension prompt, **When** a student adds a CSV export method, **Then** the file is readable by any spreadsheet application with correct column headers

---

### Edge Cases

- What if a student has no prior OOP experience in any language? The first section MUST include a strong "why OOP" motivation with a side-by-side comparison of "dict + functions" vs a class.
- What if a student comes from Java/C# and expects `private` to truly restrict access? The encapsulation section MUST clearly explain Python's "convention over enforcement" philosophy and show name mangling limitations.
- What if the JSON serializer encounters a non-serializable type (e.g., a `datetime` object)? The JSON section MUST include a brief note on custom serializers / `default=str` as a pragmatic workaround.
- What if a student tries to use `@dataclass` with mutable default arguments (e.g., a list field)? The spec MUST include the `field(default_factory=list)` pattern to prevent the shared-mutable-default footgun.
- What if a CSV file uses a different delimiter (semicolon, tab)? The `csv` section MUST demonstrate the `delimiter` parameter.
- What if multiple inheritance creates a diamond problem? The MRO (Method Resolution Order) sidebar MUST be included with a concrete example showing `ClassName.__mro__`.

## Requirements *(mandatory)*

### Functional Requirements

**OOP Fundamentals**

- **FR-001**: The notebook MUST include a "Why OOP?" motivational section with a before/after comparison of procedural code (dicts + functions) vs a class implementation of the same problem
- **FR-002**: The notebook MUST define and explain `class`, `__init__`, and `self` with at least 2 runnable code examples
- **FR-003**: The notebook MUST demonstrate instance variables vs class variables with a runnable example showing the difference in mutation behavior
- **FR-004**: The notebook MUST include at least 3 runnable method examples (instance method, reading an attribute, computed result)

**OOP Pillars & Dunder Methods**

- **FR-005**: The notebook MUST cover all four OOP pillars (encapsulation, inheritance, polymorphism, abstraction) with at least one runnable example each
- **FR-006**: The notebook MUST demonstrate encapsulation via name mangling (`__attr`) and the single-underscore convention (`_attr`), with an explicit note that Python does NOT enforce access restrictions
- **FR-007**: The notebook MUST demonstrate inheritance using `super().__init__()` in at least one subclass example
- **FR-008**: The notebook MUST cover multiple inheritance and MUST include a Method Resolution Order (MRO) example using `.__mro__` or `mro()`
- **FR-009**: The notebook MUST include a "composition over inheritance" section with a rewritten example demonstrating why deep inheritance hierarchies become fragile
- **FR-010**: The notebook MUST cover at minimum these dunder methods: `__repr__`, `__str__`, `__eq__`, `__len__`, `__hash__` — each with a runnable example and explanation of when/why to use it

**Pythonic OOP**

- **FR-011**: The notebook MUST demonstrate `@property` with at least one setter that includes validation logic
- **FR-012**: The notebook MUST explain and demonstrate `@classmethod` as an alternative constructor pattern
- **FR-013**: The notebook MUST explain and demonstrate `@staticmethod` and contrast it with `@classmethod` (when to use which)
- **FR-014**: The notebook MUST cover `@dataclass` with: basic usage, `field()` for mutable defaults, `frozen=True` for immutability, and a side-by-side comparison with a manually written `__init__`
- **FR-015**: The notebook MUST demonstrate Abstract Base Classes (`abc.ABC`, `@abstractmethod`) as Python's mechanism for interface-like contracts
- **FR-016**: The notebook MUST include a "Python vs Java/C#" sidebar explaining: no explicit access modifiers, duck typing, conventions over enforcement
- **FR-017**: The notebook MUST include a curated "tips and quirks" section covering at least: `__slots__`, the mutable default argument footgun in `__init__`, and one surprising/interesting dunder use case (e.g., `__getitem__` to make a class iterable)

**File I/O**

- **FR-018**: The notebook MUST demonstrate `open()` with context managers (`with` statement) for both reading and writing
- **FR-019**: The notebook MUST explicitly specify `encoding='utf-8'` in all `open()` examples and explain why encoding matters
- **FR-020**: The notebook MUST demonstrate `pathlib.Path` for file path construction as the modern alternative to string concatenation or `os.path`

**JSON**

- **FR-021**: The notebook MUST demonstrate `json.load()`, `json.loads()`, `json.dump()`, and `json.dumps()` with clear examples of when each is used
- **FR-022**: The notebook MUST include a "schema-like thinking" note: what JSON can and cannot represent natively (types, nested objects, arrays)
- **FR-023**: The notebook MUST address non-serializable types (e.g., `datetime`) with the `default=str` workaround and a note about custom encoder classes

**CSV**

- **FR-024**: The notebook MUST demonstrate reading a CSV file with `csv.reader` and `csv.DictReader`, showing the difference
- **FR-025**: The notebook MUST demonstrate writing a CSV file with `csv.writer` and `csv.DictWriter`
- **FR-026**: The notebook MUST demonstrate the `delimiter` parameter for non-comma separators
- **FR-027**: The notebook MUST end the CSV section with a `pandas` teaser: reading the same file in one line with `pd.read_csv()` and printing the DataFrame — with a forward reference to Lecture 11

**Mini-Project**

- **FR-028**: The notebook MUST include a mini-project fitting 20–30 minutes of in-class time: a "Contact Book" combining `@dataclass` (Contact model), a `ContactBook` class (add, search, remove, save, load), and JSON file persistence
- **FR-029**: The mini-project MUST include a homework extension prompt: add CSV export and/or simple search by partial name

**General Constitution Requirements**

- **FR-030**: The notebook MUST include 3–5 measurable learning objectives at the start
- **FR-031**: The notebook MUST contain at least 5 runnable code examples in total (counting all sections)
- **FR-032**: The notebook MUST contain at least 2 practical exercises with hidden solution cells
- **FR-033**: The notebook MUST contain at least 2 memes or visual humor elements
- **FR-034**: The notebook MUST contain at least one diagram, table, or visual explanation (e.g., an OOP pillars table, MRO diagram, or JSON schema illustration)
- **FR-035**: All explanatory text MUST be in Ukrainian, with English technical terms shown in parentheses on first use (e.g., "клас (class)", "конструктор (constructor)", "успадкування (inheritance)")
- **FR-036**: The notebook MUST end with a Summary section and a "What's Next" section previewing Lecture 6 (REST + FastAPI)
- **FR-037**: All code examples MUST run without errors in a clean Python 3.11+ environment using only the standard library (except the `pandas` teaser cell which may import `pandas`)

### Key Entities

- **Lecture Notebook**: A Jupyter Notebook (`lecture-05.ipynb`) containing all content, code examples, exercises, and the mini-project
- **Contact Dataclass**: The mini-project's core data model — a frozen or regular `@dataclass` with name, phone, and email fields
- **ContactBook Class**: The mini-project's container class — manages a list of `Contact` objects and handles JSON persistence
- **Assets Directory**: `assets/diagrams/` for visual explanations (OOP pillars diagram, MRO table, JSON schema illustration) and `assets/memes/` for humor elements

### Assumptions

- Students have completed Lectures 1–4 and are comfortable with: functions, type hints, `try/except`, list comprehensions, and basic module imports
- The lecture is delivered as a Jupyter Notebook in Ukrainian following the established pattern from Lectures 1–4
- The mini-project intentionally does not use a database (that comes in Lecture 8) — JSON file is the persistence layer
- `pathlib` is in Python's standard library (3.4+) and requires no installation
- The `pandas` teaser at the end of the CSV section intentionally requires `pip install pandas` — this is expected and acceptable for a teaser cell
- `@dataclass` is available from Python 3.7+; `@dataclass(frozen=True)` is available from 3.7+ as well
- The "Python vs Java/C#" sidebar will assume some students have prior experience with statically typed OOP languages; students without that background skip it without losing core content
- A context manager (`__enter__`/`__exit__`) implementation example is included in the "tips and quirks" section to demonstrate the bridge between OOP and File I/O — this is an enhancement beyond the constitution's base list

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A student with no prior OOP experience can, after the first two sections, write a class from scratch with attributes and methods — measurable by successful completion of Exercise 1
- **SC-002**: All code cells in the notebook run without errors top-to-bottom in a clean Python 3.11+ kernel with no extra dependencies (except the marked `pandas` teaser cell)
- **SC-003**: 100% of the constitution-mandated topics for Lecture 5 are covered: 12 base topics from the constitution + 5 educator-suggested enhancements (`@property`, `@classmethod`/`@staticmethod`, ABC, `pathlib`, context manager protocol)
- **SC-004**: The notebook contains at least 5 runnable code examples, 2 exercises with solutions, 2 memes, and 1 diagram/table — all constitution minimums met
- **SC-005**: The mini-project is completable in 20–30 minutes of in-class time, with a homework extension that adds 30–60 minutes of additional work — verified by instructor dry-run
- **SC-006**: All explanatory text is in Ukrainian with English technical terms in parentheses, consistent with Lectures 1–4 style and tone
- **SC-007**: Every OOP concept (encapsulation, inheritance, polymorphism, abstraction) has at least one runnable demonstration — students do not just read definitions, they observe behavior in code
- **SC-008**: The JSON and CSV sections are independently runnable without having completed any OOP section — the file I/O content is self-contained enough for students who need to reference it separately
