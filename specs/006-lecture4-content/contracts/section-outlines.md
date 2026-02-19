# Section Outlines (Contracts): Lecture 4

**Feature**: 006-lecture4-content
**Date**: 2026-02-18

This document defines the detailed content contract for each section of the lecture notebook. Each sub-topic lists what MUST be covered, example code themes, and visual requirements.

---

## Section 1: Functions (continued) — Функції (продовження)

### 1.1 Lambda expressions (Лямбда-вирази)

**Must cover**:
- Syntax: `lambda args: expression`
- When to use vs when to use `def`
- Common use cases: inline sorting key, simple callbacks

**Code examples**:
- Basic lambda vs equivalent `def`
- Lambda with multiple arguments
- Lambda as argument to `sorted()`

**Visuals**: 2 internet-sourced (lambda syntax diagram, lambda vs def comparison)

### 1.2 Functions as parameters + sorting with `key`

**Must cover**:
- Functions are first-class objects in Python
- Passing functions as arguments
- `sorted()` with `key` parameter
- `sort()` with `key` and `reverse`
- Custom sort examples (sort by length, by second element, by dict field)

**Code examples**:
- Passing a function to another function
- `sorted(students, key=lambda s: s["grade"])`
- Multi-criteria sorting

**Visuals**: 2 internet-sourced (first-class functions concept, sorting with key diagram)

### 1.3 `map`, `filter`, `reduce`

**Must cover**:
- `map(func, iterable)` — apply function to each element
- `filter(func, iterable)` — keep elements where func returns True
- `functools.reduce(func, iterable)` — accumulate to single value
- Comparison: map/filter vs comprehensions (when to use which)

**Code examples**:
- map: convert list of strings to lengths
- filter: keep only positive numbers
- reduce: compute product of list
- Equivalent comprehension for each

**Visuals**: 2 internet-sourced (map/filter/reduce flow diagram, comparison with comprehensions)

### 1.4 Iterators and generators

**Must cover**:
- Iterator protocol: `__iter__()` and `__next__()`
- `range()` as a lazy iterator (connect to Lecture 2)
- Generator functions with `yield`
- Generator expressions `(x**2 for x in range(10))`
- Memory efficiency: generator vs list for large data
- `next()` built-in

**Code examples**:
- Manual iteration with `iter()` and `next()`
- Simple generator function (e.g., countdown, fibonacci)
- Generator expression vs list comprehension memory comparison
- Chaining generators

**Visuals**: 2 internet-sourced (generator yield flow, iterator protocol diagram)

### 1.5 Scope: LEGB rule, closures

**Must cover**:
- LEGB: Local → Enclosing → Global → Built-in
- `global` keyword
- `nonlocal` keyword
- What closures are and why they matter
- Closure examples (counter factory, configuration)

**Code examples**:
- LEGB demonstration with same-named variables at each level
- Closure: function that "remembers" enclosing scope
- Practical closure: `make_multiplier(n)` returns function

**Visuals**: 2 internet-sourced (LEGB diagram, closure visualization) + 1 meme (scope confusion meme)

### 1.6 Decorators intro

**Must cover**:
- What a decorator is (function that wraps another function)
- `@decorator` syntax as syntactic sugar
- Simple timing decorator example
- Brief mention: will go deeper in later lectures

**Code examples**:
- Manual wrapping: `func = decorator(func)`
- Same with `@decorator` syntax
- Timing decorator

**Visuals**: 2 internet-sourced (decorator pattern diagram, @syntax explanation)

### 1.7 Type hints intro

**Must cover**:
- Why type hints: readability, IDE support, tools like mypy
- Basic syntax: `def func(x: int) -> str:`
- Common types: `list[int]`, `dict[str, int]`, `tuple[int, ...]`
- `Optional[X]` (= `X | None` in 3.10+)
- Type hints don't enforce at runtime

**Code examples**:
- Function with type hints
- Variable annotations
- `Optional` / `X | None`

**Visuals**: 2 internet-sourced (type hints syntax, mypy workflow or IDE tooltip)

### 1.8 Docstrings / PEP 257

**Must cover**:
- Single-line vs multi-line docstrings
- PEP 257 conventions
- `help()` and `__doc__` attribute
- Brief mention of Google/NumPy docstring styles

**Code examples**:
- Function with proper multi-line docstring
- Accessing docstrings programmatically

**Visuals**: 2 internet-sourced (docstring format examples, PEP 257 reference)

---

## Section 2: Modules & Imports — Модулі та імпорти

### 2.1 Import mechanisms

**Must cover**:
- `import module`
- `from module import name`
- `from module import *` (and why to avoid)
- `import module as alias`
- Import order conventions (PEP 8)

**Code examples**:
- Different import styles
- Aliasing (`import datetime as dt`)

**Visuals**: 2 internet-sourced (import mechanism diagram, import styles comparison)

### 2.2 Standard library overview

**Must cover**:
- `os` / `os.path` — file system
- `sys` — system info
- `math` — mathematical functions
- `datetime` — dates and times
- `random` — random numbers
- `json` — JSON parsing
- `collections` — Counter, defaultdict, namedtuple (preview)
- `pathlib` — modern path handling (brief)

**Code examples**:
- Quick demo of 3–4 modules (math, datetime, random, json)
- `collections.Counter` example

**Visuals**: 2 internet-sourced (Python standard library map/overview, module categories)

### 2.3 Creating custom modules + `__name__`

**Must cover**:
- Creating a `.py` file as a module
- `if __name__ == "__main__":` pattern and why it matters
- Building `utils/validators.py` (constitution requirement)

**Code examples**:
- Simulated module creation (using `%%writefile` magic or showing file content)
- `__name__` behavior when imported vs run directly
- Practical: validators module

**Visuals**: 2 internet-sourced (__name__ == __main__ diagram, module import flow)

### 2.4 Package structure basics

**Must cover**:
- What a package is (directory with `__init__.py`)
- Simple package layout
- Relative imports (brief)
- Real-world project structure preview

**Code examples**:
- Package directory tree (markdown diagram)
- Import from package

**Visuals**: 2 internet-sourced (package structure diagram, __init__.py role)

---

## Section 3: Error Handling — Обробка помилок

### 3.1 Exception types and hierarchy

**Must cover**:
- Common exceptions: `ValueError`, `TypeError`, `KeyError`, `IndexError`, `FileNotFoundError`, `ZeroDivisionError`
- Exception hierarchy: `BaseException` → `Exception` → specific
- `isinstance()` check for exceptions

**Code examples**:
- Triggering different exception types
- Printing exception hierarchy

**Visuals**: 2 internet-sourced (Python exception hierarchy tree, common exceptions cheat sheet)

### 3.2 `try`/`except`/`else`/`finally`

**Must cover**:
- Basic `try`/`except`
- Catching specific exceptions
- Multiple `except` blocks
- `else` block (runs when no exception)
- `finally` block (always runs)
- `except Exception as e` — accessing exception details

**Code examples**:
- Basic try/except
- Multiple except blocks
- Full try/except/else/finally example
- Practical: safe division function

**Visuals**: 2 internet-sourced (try/except flow chart, else/finally behavior diagram)

### 3.3 `raise` + custom exceptions

**Must cover**:
- `raise ValueError("message")`
- Re-raising exceptions (`raise` without argument)
- Defining custom exception classes
- Exception chaining (`raise ... from ...`)

**Code examples**:
- Raising a built-in exception
- Custom `ValidationError` class
- Exception chaining example

**Visuals**: 2 internet-sourced (raise flow, custom exception pattern)

### 3.4 Best practices

**Must cover**:
- Catch specific exceptions, not bare `except:`
- EAFP vs LBYL (Easier to Ask Forgiveness vs Look Before You Leap)
- Don't silence exceptions
- Logging exceptions

**Code examples**:
- Bad vs good exception handling comparison
- EAFP vs LBYL example

**Visuals**: 2 internet-sourced (EAFP vs LBYL comparison, exception anti-patterns)

---

## Section 4: Debugging & Logging — Відлагодження та логування

### 4.1 `breakpoint()` and pdb basics

**Must cover**:
- `breakpoint()` function
- Basic pdb commands: `n` (next), `s` (step), `c` (continue), `p` (print), `q` (quit)
- When to use debugger vs print statements

**Code examples**:
- Function with `breakpoint()` (explain but don't run in notebook — pdb is interactive)
- Show pdb session output as markdown

**Visuals**: 2 internet-sourced (pdb commands cheat sheet, debugger workflow)

### 4.2 `logging` module basics

**Must cover**:
- Logging levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
- `logging.basicConfig()`
- Creating a logger
- When to use logging vs print()

**Code examples**:
- Basic logging setup
- Different logging levels
- Logging with format string

**Visuals**: 2 internet-sourced (logging levels pyramid, logging vs print comparison)

---

## Section 5: Intro to OOP — Вступ до ООП

### 5.1 Why OOP? Motivation

**Must cover**:
- Problem: managing related data and functions together
- From dicts/functions to classes: natural progression
- 4 pillars overview: encapsulation, inheritance, polymorphism, abstraction

**Code examples**:
- "Before OOP": dict + standalone functions
- "After OOP": class encapsulating data + behavior

**Visuals**: 2 internet-sourced (4 OOP pillars diagram, procedural vs OOP comparison)

### 5.2 Classes, objects, `__init__`, `self`

**Must cover**:
- `class` keyword
- `__init__` as constructor
- `self` parameter
- Creating instances (objects)
- Terminology: class = blueprint, object = instance

**Code examples**:
- Simple `Student` class
- Creating multiple instances
- Accessing attributes

**Visuals**: 2 internet-sourced (class vs object/blueprint vs house analogy, __init__ and self diagram)

### 5.3 Instance vs class attributes + methods

**Must cover**:
- Instance attributes (set in `__init__`)
- Class attributes (shared across instances)
- Instance methods
- `@classmethod` and `@staticmethod` (brief intro)

**Code examples**:
- Class with both instance and class attributes
- Method that modifies instance state
- Brief classmethod example

**Visuals**: 2 internet-sourced (instance vs class attributes diagram, method types comparison)

### 5.4 Encapsulation (`_` and `__` conventions)

**Must cover**:
- Public attributes
- `_protected` convention
- `__private` name mangling
- Properties (`@property`) — brief intro
- Python philosophy: "We're all consenting adults"

**Code examples**:
- Class with public, _protected, __private attributes
- Name mangling demonstration
- Simple @property example

**Visuals**: 2 internet-sourced (encapsulation levels diagram, Python naming conventions)

### 5.5 Inheritance basics

**Must cover**:
- Parent/child class relationship
- `super().__init__()`
- Method inheritance and overriding
- `isinstance()` and `issubclass()`

**Code examples**:
- `Animal` → `Dog`/`Cat` inheritance
- Method overriding
- `super()` usage

**Visuals**: 2 internet-sourced (inheritance hierarchy diagram, super() flow)

### 5.6 Polymorphism (method overriding)

**Must cover**:
- Same method name, different behavior
- Duck typing in Python
- Practical example with different shapes or animals

**Code examples**:
- Different classes with same `.speak()` or `.area()` method
- Loop calling same method on different objects

**Visuals**: 2 internet-sourced (polymorphism diagram, duck typing meme/illustration)

### 5.7 Abstraction concept

**Must cover**:
- Hiding complexity behind simple interfaces
- Brief mention of `abc.ABC` and `@abstractmethod`
- Real-world analogy (car dashboard hides engine complexity)

**Code examples**:
- Conceptual only (or very brief ABC example)

**Visuals**: 2 internet-sourced (abstraction analogy diagram, abstraction layers)

### 5.8 Python OOP vs C#/Java/C++

**Must cover**:
- No access modifiers (public/private/protected keywords) — conventions instead
- No interfaces — duck typing + ABC
- No method overloading — use default arguments
- Multiple inheritance support
- Everything is an object
- Simpler syntax, fewer boilerplate

**Code examples**:
- Side-by-side Python vs pseudo-Java/C# comparison (markdown table)

**Visuals**: 2 internet-sourced (Python vs Java OOP comparison, Python simplicity meme)

---

## Closing Sections

### Exercises (3 + 1 bonus)

Each exercise: markdown problem statement → empty code cell → `<details>` solution

### Mini-Project: Student Grade Manager

Integrates: OOP (Student class) + Functions (lambda/map/filter/sorted) + Errors (validation) + optionally Modules

### Summary + What's Next + Homework + References

Standard closing following Lectures 1–3 format.
