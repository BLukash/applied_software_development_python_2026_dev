# Feature Specification: Lecture 2 - Core Language Mechanics

**Feature Branch**: `003-lecture2-core-mechanics`
**Created**: 2026-01-31
**Status**: Draft
**Input**: User description: "Lecture 2 implementation explaining how Python executes and represents values: the object model in CPython, names vs objects, mutability, and the difference between identity (is) and equality (==), so students can reason about bugs and performance later, how data types are stored in memory with nice examples, taken from the internet and where not found - drawn by code. It also covers truthiness, core control flow (if/elif/else, match, loops) and introduces lightweight timing to motivate why Python can be slower in raw loops."

## Contextual Analysis (Constitution Requirement)

**Previous Lecture Analysis (Lecture 1):**

Content already covered that MUST NOT be repeated:
- How Python code executes (bytecode, PVM, parsing) - covered with GIF diagram
- GIL explanation with sys._is_gil_enabled() example
- Duck typing with quack() example class hierarchy
- Dynamic vs static typing matrix with comparison table
- Basic types (int, float, str, bool, None) with type() examples
- Dynamic typing concept and "Сильна vs Слабка типізація"

Tone patterns to maintain:
- Ukrainian text with English terms in parentheses on first use: "мутабельність (mutability)"
- Historical/philosophical context for design decisions
- Memes at section starts (2 per lecture as per constitution)
- Tables for comparisons, code with actual outputs shown
- Direct address: "ви", "тобі"

Cross-references to use:
- "Як ми бачили у Лекції 1, Python — динамічно типізована мова..."
- "Пам'ятаєте duck typing з першої лекції? Тепер подивимось глибше..."

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Understanding Python's Object Model (Priority: P1)

A student learns how Python represents all values as objects, how names bind to objects (not values), and how to use `id()` to inspect object identity. This foundational knowledge enables them to predict behavior of variable assignments and avoid common reference-related bugs.

**Why this priority**: This is the conceptual foundation for everything else in Lecture 2. Without understanding names vs objects, students cannot reason about mutability, identity, or performance.

**Independent Test**: Can be fully tested by having students predict outcomes of variable assignment scenarios and verify using `id()` and `is` operators.

**Acceptance Scenarios**:

1. **Given** a student who completed Lecture 1, **When** they read the explanation of names vs objects with memory diagrams, **Then** they can explain why `a = [1,2,3]; b = a; b.append(4)` modifies both `a` and `b`.

2. **Given** visual diagrams showing memory representation, **When** a student examines integer caching vs list behavior, **Then** they can predict when `is` returns True vs False for small integers and lists.

3. **Given** code examples with `id()` output, **When** a student sees object identity in action, **Then** they can verify their predictions about object reuse.

---

### User Story 2 - Mastering Mutability Concepts (Priority: P1)

A student distinguishes mutable from immutable types, understands the implications for function arguments and data sharing, and can choose appropriate types for their use cases.

**Why this priority**: Mutability bugs are among the most common Python gotchas. Critical for writing correct code.

**Independent Test**: Can be tested by presenting code snippets with mutable default arguments or shared references and asking students to predict/fix behavior.

**Acceptance Scenarios**:

1. **Given** examples of mutable (list, dict, set) and immutable (int, str, tuple) types, **When** a student modifies them through different references, **Then** they correctly predict which modifications affect the original.

2. **Given** a function with a mutable default argument, **When** a student sees the bug pattern, **Then** they can explain why it happens and how to fix it using `None`.

3. **Given** string operations, **When** a student observes that `.upper()` returns a new string, **Then** they understand strings are immutable and operations create new objects.

---

### User Story 3 - Memory Representation with Visuals (Priority: P2)

A student understands how Python stores different data types in memory through diagrams (sourced from the internet or generated via matplotlib/code). This enables them to reason about memory efficiency and performance.

**Why this priority**: Visual understanding reinforces conceptual learning and helps with performance reasoning in later lectures.

**Independent Test**: Can be tested by asking students to draw simplified memory diagrams for given code snippets.

**Acceptance Scenarios**:

1. **Given** a memory diagram showing PyObject header structure, **When** a student sees int vs list internal representation, **Then** they understand why everything is an "object" with overhead.

2. **Given** internet-sourced diagrams (with attribution) or matplotlib-generated visuals, **When** showing list vs tuple memory layout, **Then** students grasp why tuples are more memory-efficient.

3. **Given** code-generated visualizations using simple matplotlib, **When** demonstrating reference chains, **Then** students can trace object relationships visually.

---

### User Story 4 - Identity vs Equality Mastery (Priority: P2)

A student clearly distinguishes `is` (identity) from `==` (equality), understands when to use each, and avoids common bugs like using `is` with strings or numbers.

**Why this priority**: This is a frequent source of subtle bugs and interview questions. Essential Python knowledge.

**Independent Test**: Can be tested with code examples asking "what does this print?" for various `is` and `==` comparisons.

**Acceptance Scenarios**:

1. **Given** examples comparing `is` and `==` for integers, strings, and lists, **When** a student predicts outcomes, **Then** they correctly identify when identity and equality differ.

2. **Given** the integer caching range (-5 to 256), **When** a student sees `a = 257; b = 257`, **Then** they can explain why `a is b` may be False (outside cache).

3. **Given** the `is None` pattern, **When** comparing to `== None`, **Then** a student knows to always use `is None` for None checks.

---

### User Story 5 - Truthiness and Comparisons (Priority: P2)

A student understands Python's truthiness rules (what evaluates to False), uses them idiomatically, and writes cleaner conditional logic.

**Why this priority**: Pythonic code heavily relies on truthiness. Required for writing idiomatic conditions.

**Independent Test**: Can be tested with "what does this print?" exercises for various truthiness scenarios.

**Acceptance Scenarios**:

1. **Given** the list of falsy values (None, 0, 0.0, "", [], {}, set()), **When** a student writes conditionals, **Then** they use `if items:` instead of `if len(items) > 0:`.

2. **Given** comparison chaining examples (`1 < x < 10`), **When** a student writes range checks, **Then** they use Python's elegant chained comparisons.

3. **Given** short-circuit evaluation examples, **When** `and`/`or` are used, **Then** students understand evaluation stops early and can predict results.

---

### User Story 6 - Control Flow Mastery (Priority: P1)

A student uses if/elif/else, match statements (Python 3.10+), for loops, while loops, break, continue, and range() effectively.

**Why this priority**: Control flow is fundamental to all programming. Students need this for every future lecture.

**Independent Test**: Can be tested with coding exercises requiring specific control flow patterns.

**Acceptance Scenarios**:

1. **Given** if/elif/else examples, **When** a student writes multi-branch logic, **Then** they structure conditions correctly without redundant checks.

2. **Given** match statement examples (structural pattern matching), **When** comparing to C-style switch, **Then** students understand Python's more powerful matching capabilities.

3. **Given** for/while loop examples with break/continue, **When** a student needs early exit or skip, **Then** they apply the correct construct.

4. **Given** range() with various arguments, **When** iterating over sequences, **Then** students correctly use range(n), range(a,b), range(a,b,step).

---

### User Story 7 - Practical Patterns (Priority: P2)

A student applies common loop patterns: counting, searching with early exit, accumulating, and filtering.

**Why this priority**: These patterns appear constantly in real code. Practicing them builds fluency.

**Independent Test**: Can be tested with small coding exercises implementing each pattern.

**Acceptance Scenarios**:

1. **Given** a counting task (count occurrences), **When** a student writes a loop, **Then** they correctly initialize counter and increment.

2. **Given** a search task, **When** a student uses early exit, **Then** they apply break effectively and understand for...else.

3. **Given** an accumulation task, **When** a student builds a result, **Then** they correctly initialize and accumulate in loop.

---

### User Story 8 - Performance Intuition with Timing (Priority: P3)

A student uses basic timing (time module) to measure code execution, understands why Python loops can be slow, and gains motivation to use built-in functions and later optimization techniques.

**Why this priority**: Sets up performance awareness for later lectures on NumPy, pandas, and vectorization.

**Independent Test**: Can be tested by having students time different implementations of the same task.

**Acceptance Scenarios**:

1. **Given** time.perf_counter() or time.time() examples, **When** a student wraps code in timing, **Then** they can measure execution duration.

2. **Given** a comparison of Python loop vs built-in sum(), **When** students see 10x+ difference, **Then** they understand Python loops have overhead.

3. **Given** brief mention of why (interpreter overhead, not compiled), **When** referencing Lecture 1's execution model, **Then** students connect dots to bytecode/PVM.

---

### Edge Cases

- What happens when comparing mutable objects that have the same content but different ids?
- How does string interning affect identity comparisons for short strings?
- What happens with empty collections in truthiness checks?
- How does match statement handle no-match cases (default/wildcard)?
- What happens when break is used in nested loops?
- How do very large integers affect identity (no caching)?

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Lecture MUST explain names vs objects with clear visual diagrams showing reference relationships
- **FR-002**: Lecture MUST demonstrate `id()` function to inspect object identity
- **FR-003**: Lecture MUST cover all mutable types (list, dict, set) and immutable types (int, float, str, tuple, frozenset, bool, None)
- **FR-004**: Lecture MUST include the mutable default argument bug pattern and its solution
- **FR-005**: Lecture MUST distinguish `is` (identity) from `==` (equality) with at least 5 comparison examples
- **FR-006**: Lecture MUST explain integer caching (-5 to 256) and string interning
- **FR-007**: Lecture MUST list all falsy values with examples
- **FR-008**: Lecture MUST cover truthiness idioms (`if items:` pattern)
- **FR-009**: Lecture MUST cover comparison chaining (`a < b < c`) and short-circuit evaluation
- **FR-010**: Lecture MUST include if/elif/else with at least 3 examples of varying complexity
- **FR-011**: Lecture MUST introduce match statement (Python 3.10+) with structural pattern examples
- **FR-012**: Lecture MUST cover for loops with range(), enumerate() (reference from Lecture 1), and iteration over collections
- **FR-013**: Lecture MUST cover while loops with break, continue, and for...else pattern
- **FR-014**: Lecture MUST include at least 3 practical patterns: counting, searching, early exit
- **FR-015**: Lecture MUST introduce basic timing with time.perf_counter() or similar
- **FR-016**: Lecture MUST show timing comparison: Python loop vs built-in function (sum example)
- **FR-017**: Lecture MUST include at least 3 diagrams (can be internet-sourced with attribution or matplotlib-generated)
- **FR-018**: Lecture MUST NOT repeat duck typing explanation from Lecture 1 (may reference briefly)
- **FR-019**: Lecture MUST NOT repeat bytecode/PVM execution model from Lecture 1 (may reference briefly)
- **FR-020**: Lecture MUST follow constitution requirements: 2 memes, Ukrainian text, English terms in parentheses

### Key Entities

- **PyObject**: The base structure for all Python objects (id, type, refcount conceptually)
- **Name**: A reference/binding in a namespace pointing to an object
- **Object**: A typed value in memory with identity, type, and value
- **Namespace**: A mapping from names to objects (local, global, built-in)

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 90% of students can correctly predict the outcome of 5 reference/mutation code snippets after the lecture
- **SC-002**: 85% of students can explain why `a is b` returns True for `a = 100; b = 100` but may return False for `a = 500; b = 500`
- **SC-003**: Students can identify and fix mutable default argument bugs in 2 code examples
- **SC-004**: 90% of students can list at least 5 falsy values from memory
- **SC-005**: Students can write a search loop with early exit in under 3 minutes
- **SC-006**: Students can use match statement for at least 2 different pattern types (literal, sequence)
- **SC-007**: Students can measure execution time of a code block using basic timing
- **SC-008**: Lecture content fits within 1.5 hours including exercises
- **SC-009**: All code examples run successfully in Python 3.11+
- **SC-010**: At least 5 runnable code examples with visible outputs as per constitution

---

## Assumptions

- Students have completed Lecture 1 and understand basic types, variables, and REPL usage
- Students have Python 3.11+ installed and can run Jupyter notebooks
- Internet-sourced diagrams will have appropriate Creative Commons or educational use licenses
- matplotlib is available for generating custom diagrams if needed
- Students are familiar with basic programming concepts (from prerequisites)
