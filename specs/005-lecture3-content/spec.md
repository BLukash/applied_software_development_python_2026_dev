# Feature Specification: Lecture 3 — Data Structures + Pythonic Patterns + Functions

**Feature Branch**: `005-lecture3-content`
**Created**: 2026-02-12
**Status**: Draft
**Input**: User description: "Implement Lecture 3"

## Contextual Analysis (Constitution Requirement)

**Previous Lecture Analysis (Lectures 1 & 2):**

Content already covered that MUST NOT be repeated:
- Basic types (int, float, str, bool, None) with `type()` examples — Lecture 1
- How Python executes code (bytecode, PVM, parsing) — Lecture 1
- Duck typing with `quack()` example — Lecture 1
- Dynamic vs static typing matrix — Lecture 1
- Names vs objects, references, `id()`, assignment as binding — Lecture 2
- Memory model intuition (PyObject, reference diagrams) — Lecture 2
- Mutability principle (mutable vs immutable, mutable default argument bug, shared references) — Lecture 2
- Identity vs equality (`is` vs `==`), integer caching, string interning — Lecture 2
- Truthiness and comparisons (falsy values, short-circuit, chaining) — Lecture 2
- Control flow: if/elif/else, match, for, while, break/continue, for...else — Lecture 2
- Practical patterns: counting, searching, early exit, accumulation — Lecture 2
- Basic timing with `time.perf_counter()` — Lecture 2
- Brief introduction to complex data types (list, dict, set, tuple) — Lecture 2 (brief preview only)

Tone patterns to maintain:
- Ukrainian text with English terms in parentheses on first use: "зрізи (slices)"
- Historical/philosophical context for design decisions where relevant
- Memes at natural breakpoints (2 per lecture as per constitution)
- Tables for comparisons, code with actual outputs shown
- Direct address: "ви", "тобі"

Cross-references to use:
- "У Лекції 2 ми коротко познайомились зі списками, словниками, множинами та кортежами. Тепер пора зануритись глибше..."
- "Пам'ятаєте мутабельність з Лекції 2? Тепер побачимо, як це впливає на роботу з колекціями..."
- "Як ми бачили у Лекції 2, Python-цикли можуть бути повільними — тому зараз вивчимо comprehensions..."

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Collections Deep Dive (Priority: P1)

A student gains comprehensive, hands-on understanding of Python's four core collection types (list, tuple, dict, set) — their creation, common methods, pitfalls, and when to use each. Building on the brief preview from Lecture 2, students now learn indexing, slicing, membership checks, nested structures, and the most-used methods with their gotchas.

**Why this priority**: Collections are the backbone of Python programming. Without fluency in lists, dicts, sets, and tuples, students cannot write meaningful programs. Every future lecture depends on this.

**Independent Test**: Can be fully tested by giving students a dataset and asking them to store, retrieve, slice, and transform data using each collection type.

**Acceptance Scenarios**:

1. **Given** a student who saw the brief collection preview in Lecture 2, **When** they work through the deep-dive section, **Then** they can create, index, slice, and modify lists with confidence.

2. **Given** examples of dict methods (`.get()`, `.pop()`, `.items()`, `.update()`), **When** a student needs to access or modify key-value data, **Then** they choose the correct method and handle missing keys gracefully.

3. **Given** a comparison table of collection types (ordered/unordered, mutable/immutable, duplicates allowed), **When** a student needs to pick a data structure for a task, **Then** they can justify their choice.

4. **Given** examples of common pitfalls (`.append()` vs `.extend()`, modifying a list while iterating, dict key requirements), **When** a student encounters these patterns, **Then** they can identify and avoid the bug.

---

### User Story 2 - Comprehensions and Iteration Patterns (Priority: P1)

A student learns Pythonic iteration patterns (enumerate, zip) and comprehensions (list, dict, set) as concise, readable alternatives to verbose loops. They understand when comprehensions improve code and when they hurt readability.

**Why this priority**: Comprehensions are a signature Python feature and appear in virtually all professional Python code. enumerate and zip are essential for idiomatic iteration.

**Independent Test**: Can be tested by providing loop-based code and asking students to rewrite using comprehensions, and vice versa for overly complex comprehensions.

**Acceptance Scenarios**:

1. **Given** a for loop that builds a new list, **When** a student rewrites it as a list comprehension, **Then** the result is equivalent and more readable.

2. **Given** `enumerate()` and `zip()` examples, **When** a student needs index+value or parallel iteration, **Then** they use these patterns instead of manual indexing.

3. **Given** a dict comprehension example, **When** a student needs to transform or filter a dictionary, **Then** they can write a dict comprehension with conditions.

4. **Given** an overly nested or complex comprehension, **When** a student evaluates readability, **Then** they recognize when a regular loop is preferable.

---

### User Story 3 - Introduction to Functions (Priority: P1)

A student learns to define and call functions with parameters, return values, default arguments, and `*args`/`**kwargs`. They understand functions as a tool for organizing code, avoiding repetition, and building reusable logic.

**Why this priority**: Functions are fundamental to all structured programming. Students need them for every future lecture, mini-projects, and the course capstone.

**Independent Test**: Can be tested by asking students to refactor repeated code into functions, write functions with various parameter types, and predict return values.

**Acceptance Scenarios**:

1. **Given** examples of function definitions with `def`, **When** a student needs to encapsulate logic, **Then** they create a function with appropriate parameters and return value.

2. **Given** default argument examples, **When** a student writes a function with optional parameters, **Then** they correctly use defaults and understand evaluation order.

3. **Given** `*args` and `**kwargs` examples, **When** a student sees flexible parameter passing, **Then** they understand when and how to use variadic arguments.

4. **Given** a block of repeated code, **When** a student refactors it into a function, **Then** the original behavior is preserved and the code is DRY.

---

### User Story 4 - Memory Representation of Collections (Priority: P2)

A student understands how lists, tuples, dicts, and sets are stored in memory through visual diagrams sourced from the internet (with attribution). This deepens the memory model understanding from Lecture 2 with collection-specific details.

**Why this priority**: Visual understanding of memory layout reinforces why certain operations are fast or slow and why tuples are more memory-efficient than lists.

**Independent Test**: Can be tested by asking students to draw simplified memory diagrams for a list of lists vs a tuple of tuples.

**Acceptance Scenarios**:

1. **Given** a diagram showing how a list stores an array of pointers to objects, **When** a student sees `.append()` causing reallocation, **Then** they understand list over-allocation strategy.

2. **Given** a diagram comparing list vs tuple internal structure, **When** a student compares memory usage, **Then** they understand why tuples are lighter.

3. **Given** a hash table diagram for dict/set, **When** a student sees how keys are hashed to slots, **Then** they connect this to O(1) lookup speed.

---

### User Story 5 - Complexity Intuition (Priority: P2)

A student develops intuition about why dict/set lookups are fast (O(1) average) compared to list scans (O(n)), and can use this knowledge to choose appropriate data structures for performance-sensitive tasks.

**Why this priority**: Understanding when to use a set or dict for fast lookups vs a list is a critical skill that prevents performance bugs. Builds on the timing motivation from Lecture 2.

**Independent Test**: Can be tested by timing dict vs list membership checks on large datasets and asking students to predict which is faster and why.

**Acceptance Scenarios**:

1. **Given** a membership check on a list vs a set with 100,000 elements, **When** a student times both, **Then** they observe the dramatic speed difference.

2. **Given** explanation of hash tables (conceptual, not implementation), **When** a student hears "dict/set use hashing for O(1) lookup", **Then** they can explain why `x in my_set` is faster than `x in my_list`.

3. **Given** a real scenario (e.g., "check if username already exists"), **When** a student chooses between a list and a set, **Then** they select set/dict and explain the performance rationale.

---

### User Story 6 - Mini Parsing Task (Priority: P2)

A student completes a practical mini-project that integrates collections, iteration patterns, comprehensions, and functions. The task involves parsing structured text data (e.g., log files or CSV-like input) and computing a frequency table or summary statistics.

**Why this priority**: This is the synthesis exercise that proves students can combine all concepts from this lecture into a working solution.

**Independent Test**: Can be tested by providing sample log/data input and verifying the student's output matches expected frequency counts or statistics.

**Acceptance Scenarios**:

1. **Given** a multi-line string of log entries, **When** a student writes a parsing function, **Then** it correctly extracts relevant fields using string methods and slicing.

2. **Given** parsed data, **When** a student computes a frequency table using a dict, **Then** the counts match expected values.

3. **Given** the frequency table, **When** a student sorts results by count (descending), **Then** they use appropriate sorting with `sorted()` and a key function.

4. **Given** the complete solution, **When** reviewed, **Then** it uses at least one comprehension, one iteration pattern (enumerate or zip), and at least one custom function.

---

### Edge Cases

- What happens when slicing with indices beyond the sequence length?
- How does `dict.get(key, default)` differ from `dict[key]` for missing keys?
- What happens when modifying a list while iterating over it?
- How do nested comprehensions handle readability (when to stop nesting)?
- What happens when a mutable object is used as a dict key?
- How does `*args` interact with positional arguments? What about ordering of `*args` and `**kwargs`?
- What happens with empty collections passed to `zip()`?

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Lecture MUST cover list operations in depth: creation, indexing (positive/negative), slicing (start:stop:step), common methods (`.append()`, `.extend()`, `.insert()`, `.pop()`, `.remove()`, `.sort()`, `.reverse()`, `.copy()`)
- **FR-002**: Lecture MUST cover tuple operations: creation (with and without parentheses), unpacking, single-element tuple syntax `(x,)`, immutability enforcement, `namedtuple` mention as preview
- **FR-003**: Lecture MUST cover dict operations: creation (literal, `dict()`), accessing (`.get()`, bracket notation), modification (`.update()`, `.pop()`, `.setdefault()`), iteration (`.keys()`, `.values()`, `.items()`), key requirements (hashable)
- **FR-004**: Lecture MUST cover set operations: creation (`set()`, `{}`), add/remove (`.add()`, `.discard()`, `.remove()`), set operations (union `|`, intersection `&`, difference `-`, symmetric difference `^`), membership check performance
- **FR-005**: Lecture MUST include a comparison table showing properties of all four collection types (ordered, mutable, duplicates, use case)
- **FR-006**: Lecture MUST cover indexing and slicing with at least 5 examples including negative indices and step values
- **FR-007**: Lecture MUST cover nested structures (list of dicts, dict of lists) with practical examples
- **FR-008**: Lecture MUST cover common pitfalls: `.append()` vs `.extend()`, modifying list while iterating, mutable dict keys, `{}` creates empty dict not empty set
- **FR-009**: Lecture MUST cover `enumerate()` with at least 2 examples showing index+value iteration
- **FR-010**: Lecture MUST cover `zip()` with at least 2 examples including parallel iteration and dict creation
- **FR-011**: Lecture MUST cover list comprehensions with filtering (`if` clause) and transformation
- **FR-012**: Lecture MUST cover dict comprehensions with at least 1 example
- **FR-013**: Lecture MUST cover set comprehensions with at least 1 example
- **FR-014**: Lecture MUST present comprehension readability guidelines (when to use vs when a loop is clearer)
- **FR-015**: Lecture MUST demonstrate complexity difference between `in` on list vs set/dict with timed comparison
- **FR-016**: Lecture MUST explain hash table concept at an intuitive level (without implementation details) to motivate O(1) lookup
- **FR-017**: Lecture MUST include at least 3 diagrams showing collection memory representation (sourced from the internet with attribution, or generated via matplotlib if unavailable)
- **FR-018**: Lecture MUST introduce functions: `def`, parameters, `return`, docstrings (brief)
- **FR-019**: Lecture MUST cover default arguments with correct usage patterns
- **FR-020**: Lecture MUST cover `*args` and `**kwargs` with practical examples
- **FR-021**: Lecture MUST include a mini parsing task as a practical exercise combining collections, iteration, comprehensions, and functions
- **FR-022**: Lecture MUST include at least 2 practical exercises with solutions (hidden cells)
- **FR-023**: All code examples MUST work in Python 3.11+
- **FR-024**: Lecture MUST follow constitution requirements: Ukrainian text, English terms in parentheses, 2 memes, learning objectives (3-5), summary, "What's Next" section, references
- **FR-025**: Lecture MUST NOT repeat content already covered in Lectures 1-2 (basic types, names vs objects, mutability principle, control flow, truthiness, timing basics) — may reference briefly
- **FR-026**: Lecture MUST cross-reference Lecture 2's brief collection introduction as a starting point
- **FR-027**: Lecture MUST include membership checks (`in` operator) for all collection types

### Key Entities

- **List**: Ordered, mutable sequence — the most versatile Python collection
- **Tuple**: Ordered, immutable sequence — used for fixed data and unpacking
- **Dict**: Key-value mapping with O(1) lookup — Python's primary associative data structure
- **Set**: Unordered collection of unique hashable elements with O(1) membership check
- **Function**: Named, reusable block of code with parameters and return value
- **Comprehension**: Concise syntax for creating collections from iterables with optional filtering
- **Frequency Table**: Dict mapping items to their counts — the mini-project output

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 90% of students can correctly slice a list using positive indices, negative indices, and step values
- **SC-002**: 85% of students can choose the appropriate collection type (list, tuple, dict, set) for a given scenario and justify their choice
- **SC-003**: Students can rewrite a loop-based list construction as a list comprehension and vice versa
- **SC-004**: 90% of students can use `enumerate()` and `zip()` correctly in iteration tasks
- **SC-005**: Students can explain why `x in my_set` is faster than `x in my_list` for large collections
- **SC-006**: Students can define functions with default parameters and `*args`/`**kwargs`
- **SC-007**: 85% of students successfully complete the mini parsing task producing correct frequency counts
- **SC-008**: Lecture content fits within 1.5 hours including exercises
- **SC-009**: All code examples run successfully in Python 3.11+
- **SC-010**: At least 5 runnable code examples with visible outputs as per constitution

---

## Assumptions

- Students have completed Lectures 1-2 and understand basic types, names vs objects, mutability, control flow, and basic loop patterns
- Students have Python 3.11+ installed and can run Jupyter notebooks
- Internet-sourced diagrams will have appropriate Creative Commons or educational use licenses
- matplotlib is available for generating custom diagrams if internet sources are unavailable
- The brief collection preview in Lecture 2 provided enough familiarity that this lecture can go deep immediately
- Functions coverage is introductory — deep dive (lambdas, closures, decorators, generators) is deferred to Lecture 4
- The mini parsing task can be completed in 20-30 minutes of in-class time

## Out of Scope

- Lambda functions (Lecture 4)
- Closures, decorators, generators, iterators (Lecture 4)
- Scope rules (local/global/nonlocal) (Lecture 4)
- Exception handling (Lecture 4)
- File I/O for reading actual log files (Lecture 5) — mini-project uses hardcoded multi-line strings
- Type hints (Lecture 4)
- `collections` module advanced types (Counter, defaultdict, OrderedDict) — may mention briefly as "what's next"
