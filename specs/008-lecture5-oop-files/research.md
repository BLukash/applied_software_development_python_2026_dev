# Research: Lecture 5 — OOP in Python and Working with Files

**Date**: 2026-02-26
**Branch**: `008-lecture5-oop-files`

## R1 — Lecture 4 Structure Analysis (Consistency Baseline)

**Decision**: Follow Lecture 4 conventions exactly for cell structure, markdown formatting, and Ukrainian style.

**Findings**:
- **Total cells**: Lecture 4 has 90 cells. Lecture 5 will target ~90–110 cells (OOP scope is larger than Lecture 4's).
- **Section numbering**: `## N.N Тема (English Translation)` format — e.g., `## 1.1 Основи (Basics)`.
- **Language style**: Conversational Ukrainian, addresses learner as "ви" (polite for students). Technical terms in backticks inline with Ukrainian prose. Key concepts in **bold**.
- **Code cells**: Inline Ukrainian comments. Complex logic split into labeled comment blocks. Output cells immediately follow code cells with no explanatory markdown between them.
- **Exercise format**: Starter code cells with `# Вправа N: Ваш код тут`. Solutions collapsed in `<details><summary>Рішення (клікніть щоб побачити)</summary>` HTML blocks.
- **Mini-project format**: 4–5 stepped code cells (`Крок 1`, `Крок 2`…) with full solution in final `<details>` block.
- **Memes**: Embedded via markdown `![alt](path)` — either remote URLs or `assets/memes/filename`. Appear in introduction and section intros.
- **Diagrams**: Stored in `assets/diagrams/`, referenced as `![alt](assets/diagrams/filename)` with `*Джерело: [link]*` attribution.
- **References section**: Grouped as "Офіційна документація", "Туторіали", "Поглиблене вивчення".
- **What's Next**: Previews next lecture with bullet list. Followed by Homework (3 tasks) and References.

**Rationale**: Consistency with Lectures 1–4 reduces cognitive load. Students focus on content, not navigation.

**Alternatives considered**: No alternatives — constitution mandates consistency.

---

## R2 — Content Already Covered in Lectures 1–4 (Avoid Repetition)

**Decision**: Do not repeat the following concepts in Lecture 5 — only cross-reference them.

**Already covered**:
- **Lecture 1**: Variables, types (int, float, str, bool, None), f-strings, print/input, venv, pip
- **Lecture 2**: Memory model, mutability, references vs values, collections intro, truthiness, control flow, loops
- **Lecture 3**: Collections deep dive (list/dict/set/tuple), comprehensions, enumerate/zip, complexity intuition, functions intro (parameters, defaults, args/kwargs)
- **Lecture 4**: Lambda, map/filter/reduce, iterators/generators (`__iter__`/`__next__` — already introduced!), LEGB scope, closures, decorators, type hints, modules/imports, try/except/else/finally, custom exceptions, logging

**Critical cross-reference opportunity**: `__iter__` and `__next__` were introduced in Lecture 4 as part of the iterator protocol. In Lecture 5, when teaching `__getitem__` and making classes iterable, we MUST cross-reference: "as we saw in Lecture 4 with iterators..." This avoids repetition while reinforcing the connection.

**Not yet covered (Lecture 5 scope)**:
- Classes, `__init__`, `self`, instance/class variables
- OOP pillars (encapsulation, inheritance, polymorphism, abstraction) as class-level constructs
- Dunder methods beyond `__iter__`/`__next__`: `__repr__`, `__str__`, `__eq__`, `__len__`, `__hash__`, `__getitem__`, `__enter__`/`__exit__`
- `@property`, `@classmethod`, `@staticmethod`
- `@dataclass`
- Abstract Base Classes (ABC)
- `__slots__`
- File I/O: `open()`, context managers, encoding
- `pathlib.Path`
- `json` module (json.load/loads/dump/dumps)
- `csv` module (reader/writer/DictReader/DictWriter)

---

## R3 — OOP Teaching Progression Best Practices

**Decision**: Use the "motivation → mechanics → pillars → patterns → quirks" progression.

**Findings**:
The following pedagogically validated sequence is used:

1. **Motivation first**: Show the "dict + functions" pain point before introducing classes. The before/after contrast makes the value immediate.
2. **Mechanics second**: `__init__`, `self`, instance attributes, calling methods. Students write a class before understanding why OOP has pillars.
3. **Pillars third**: Encapsulation (name mangling), inheritance (super()), polymorphism (method override), abstraction (ABC) — in that order, each with a concrete example.
4. **Pythonic patterns fourth**: `@property`, `@classmethod`, `@staticmethod`, `@dataclass` — the "Python way" that distinguishes Python OOP from Java/C#.
5. **Quirks last**: `__slots__`, mutable default footgun, context manager protocol. These land better after students already understand basic OOP.

**Rationale**: Research across Python educators (Real Python, Fluent Python, Python Tricks) confirms this sequence. Starting with pillars abstracts too early; starting with quirks confuses without context.

**Alternatives considered**: Starting with `@dataclass` (flipped classroom approach) — rejected because students need to understand what dataclass replaces before appreciating it.

---

## R4 — Mini-Project Scope: Contact Book Design

**Decision**: Contact Book using `@dataclass` (Contact) + `ContactBook` class + JSON persistence.

**Design rationale**:
- **Why Contact Book?**: Universally understood domain. No business logic complexity. Students focus on OOP patterns, not domain rules.
- **Why `@dataclass` for Contact?**: Natural showcase of dataclass value — a Contact has only fields, no methods. Contrast: ContactBook has methods but is NOT a dataclass, showing when each approach is appropriate.
- **Why JSON for persistence?**: Connects File I/O (just taught) with OOP. Students serialize their own objects. More motivating than reading pre-made files.
- **Why `@classmethod` for `load_from_json()`?**: Classic "alternative constructor" pattern. Natural bridge between classmethod theory and practice.

**Contact model**:
```python
@dataclass
class Contact:
    name: str
    phone: str
    email: str = ""  # Optional field with default
```

**ContactBook class**:
```python
class ContactBook:
    def __init__(self): self._contacts: list[Contact] = []
    def add(self, contact: Contact) -> None
    def search(self, name: str) -> list[Contact]  # partial match
    def remove(self, name: str) -> bool  # returns True if found and removed
    def save_to_json(self, path: str | Path) -> None
    @classmethod
    def load_from_json(cls, path: str | Path) -> "ContactBook"
    def __len__(self) -> int
    def __repr__(self) -> str
```

**Homework extension**: Add `export_to_csv(self, path)` method using `csv.DictWriter`.

**In-class time estimate**: ~25 minutes for steps 1–4, ~35 minutes for homework extension.

---

## R5 — Visual and Diagram Resources

**Decision**: Use a mix of local generated diagrams (tables, ASCII-style) and web images where available.

**Required visuals**:

1. **OOP Pillars Table** (local, markdown table):
   ```
   | Принцип        | Що означає                    | Приклад у Python                |
   |----------------|-------------------------------|---------------------------------|
   | Інкапсуляція   | Приховати деталі реалізації   | `_attr`, `__attr`, @property   |
   | Успадкування   | Перевикористання через super  | class Dog(Animal): ...          |
   | Поліморфізм    | Один інтерфейс, різна поведінка| override методів                |
   | Абстракція     | Контракт без реалізації       | ABC, @abstractmethod            |
   ```

2. **MRO Diagram** (local, ASCII or web image): Python's C3 linearization for diamond inheritance.
   - Source: [Python docs — MRO](https://docs.python.org/3/glossary.html#term-method-resolution-order) or Real Python

3. **JSON Schema Visual** (local, markdown code block showing JSON types):
   - A comparison table: Python type ↔ JSON type

4. **Memes**:
   - OOP meme: "When you have been writing spaghetti code for years and discover classes" — classic OOP meme format
   - File I/O meme: classic "encoding problems" meme or "try to open file without context manager" meme

**Attribution**: All downloaded images stored in `assets/diagrams/` or `assets/memes/` with attribution captions.

---

## R6 — `@property`, `@classmethod`, `@staticmethod` Teaching Pattern

**Decision**: Teach as "Python's answer to Java getters/setters and static utility methods."

**Findings**:
- `@property`: Introduce by showing the Java-style `get_age()`/`set_age()` anti-pattern, then replace with `@property`. Students from Java/C# immediately recognize the value.
- `@classmethod`: Teach as "alternative constructor" — most intuitive use case. Example: `Contact.from_dict(d)` vs `Contact(**d)` — the named constructor makes code self-documenting.
- `@staticmethod`: Teach as "utility function that logically belongs to the class but doesn't need `self` or `cls`." Example: `Contact.validate_phone(phone)`.
- Contrast table between all three: when to use instance method vs classmethod vs staticmethod — this table is a recurring request in Python courses.

---

## R7 — Abstract Base Classes (ABC) Scope Decision

**Decision**: Teach ABC as "Python's lightweight interface mechanism" with one concrete example, not deep dive.

**Rationale**: Full protocol/ABC coverage belongs in advanced Python. For Lecture 5, one clean example suffices:
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...

class Circle(Shape):
    def __init__(self, radius: float): self.radius = radius
    def area(self) -> float: return 3.14159 * self.radius ** 2
```
Show: trying to instantiate `Shape()` raises `TypeError`. Instantiating `Circle(5)` works.

**NOT covered** (too advanced for Lecture 5): `__abstractmethods__`, mixins, `register()`, `ABCMeta`.

---

## R8 — pathlib vs os.path Decision

**Decision**: Teach `pathlib.Path` as the primary API; mention `os.path` exists for legacy code.

**Rationale**: Python 3.6+ (PEP 519) made `pathlib` the recommended approach. All new code should use `pathlib`. `os.path` is shown once with a note: "legacy code uses this; prefer `pathlib` in new projects."

**Key `pathlib` features to cover**:
- `Path("contacts.json")` — relative path
- `Path.home() / "documents" / "contacts.json"` — chaining with `/` operator
- `path.exists()`, `path.read_text(encoding="utf-8")`, `path.write_text(...)`
- `path.suffix`, `path.stem`, `path.parent`

---

## R9 — Encoding and Ukrainian Characters

**Decision**: Always use `encoding='utf-8'` in all file examples. Demonstrate the encoding issue explicitly.

**Rationale**: Students on Windows may encounter encoding issues (`cp1251` default on Ukrainian Windows). The encoding section must:
1. Show what happens WITHOUT specifying encoding (platform-dependent behavior)
2. Show what happens WITH `encoding='utf-8'` (predictable, portable)
3. Demonstrate with Ukrainian text: "Привіт, Іванко!"

---

## R10 — Timing and Scope Validation

**Decision**: Estimated delivery time is ~85–95 minutes — within the 1.5-hour constitutional limit.

**Section timing estimates**:
| Section | Topic | Estimated time |
|---------|-------|----------------|
| Intro | Learning objectives, motivation | 5 min |
| 1. OOP Foundations | Why OOP, class/init/self, instance vs class vars | 15 min |
| 2. OOP Pillars | Encapsulation, inheritance, polymorphism, abstraction, dunder methods | 20 min |
| 3. Pythonic OOP | @property, classmethod, staticmethod, dataclass, ABC, quirks | 20 min |
| 4. File I/O | open(), context managers, encoding, pathlib | 8 min |
| 5. JSON | load/dump, schema thinking, non-serializable types | 8 min |
| 6. CSV | reader/writer/DictReader/DictWriter, delimiter, pandas teaser | 7 min |
| Exercises | 2 exercises | 10 min (guided) |
| Summary + What's Next | | 5 min |
| **Total** | | **~98 min** |

**Adjustment**: If timing exceeds 90 min, trim the "quirks" section to: `__slots__` (1 example only) and mutable default (1 example). Remove `__getitem__` example. This saves ~8–10 min.
