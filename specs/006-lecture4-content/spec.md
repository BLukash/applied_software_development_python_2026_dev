# Feature Specification: Lecture 4 — Functions (continue) + Modules + Errors + Intro to OOP

**Feature Branch**: `006-lecture4-content`
**Created**: 2026-02-18
**Status**: Draft
**Input**: User description: "Implement Lecture 4 (Functions (continue) + modules + errors + intro to OOP). Make sure to enhance lecture with primarily internet found visuals (min 2 per each sub topic), not your own generated. This seems to have better impact"

## User Scenarios & Testing *(mandatory)*

### User Story 1 — Student Learns Advanced Function Concepts (Priority: P1)

A student who completed Lectures 1–3 opens the Lecture 4 Jupyter Notebook and works through the section on advanced functions. They learn about lambda expressions, higher-order functions (passing functions as arguments), `map`/`filter`/`reduce`, scope rules (local/global/enclosing), closures, decorators (intro-level), and type hints. Each concept is illustrated with runnable code cells and at least 2 internet-sourced visuals (diagrams, infographics, or illustrations).

**Why this priority**: Functions are the foundation for all subsequent topics (modules, error handling, OOP). Students must solidify function mastery before moving on.

**Independent Test**: Can be tested by opening the notebook and running all code cells in the "Functions (continued)" section; every cell executes without errors, and visuals render correctly.

**Acceptance Scenarios**:

1. **Given** a student has completed Lecture 3, **When** they open the Lecture 4 notebook, **Then** they see a structured section on advanced function concepts with explanations in Ukrainian, runnable code examples, and at least 2 internet-sourced visuals per sub-topic (lambda, higher-order functions/map/filter, scope/closures, decorators intro, type hints).
2. **Given** a student runs all code cells in the functions section, **When** cells execute, **Then** all cells produce correct output without errors.
3. **Given** a student reads the functions section, **When** they look for visuals, **Then** each sub-topic contains at least 2 embedded images sourced from the internet (with attribution/source URLs) rather than custom-generated diagrams.

---

### User Story 2 — Student Learns Modules and Imports (Priority: P1)

A student works through the modules section of the notebook. They learn about importing modules (`import`, `from ... import`, `as` aliases), the standard library (key modules like `os`, `sys`, `math`, `datetime`, `random`, `json`, `collections`), creating their own modules, the `__name__ == "__main__"` pattern, and package structure basics. Each sub-topic includes at least 2 internet-sourced visuals.

**Why this priority**: Understanding modules is essential for organizing code and is a prerequisite for real-world Python development.

**Independent Test**: Can be tested by running all code cells in the "Modules" section; all imports resolve, code executes correctly, and visuals render.

**Acceptance Scenarios**:

1. **Given** a student reaches the modules section, **When** they read through it, **Then** they find clear explanations of import mechanisms, standard library overview, custom modules, `__name__` guard, and package structure — each with at least 2 internet-sourced visuals.
2. **Given** a student runs all code cells in the modules section, **When** cells execute, **Then** all cells produce correct output without errors and only use standard library modules (no external pip packages required).

---

### User Story 3 — Student Learns Error Handling (Priority: P1)

A student works through the error handling section. They learn about exception types and hierarchy, `try`/`except`/`else`/`finally` blocks, raising exceptions with `raise`, creating custom exceptions, and best practices for error handling. Each sub-topic includes at least 2 internet-sourced visuals (e.g., exception hierarchy diagrams, try/except flow charts).

**Why this priority**: Error handling is a core skill. Students need this to write robust code and understand Python's exception model before OOP.

**Independent Test**: Can be tested by running all code cells in the "Errors" section; deliberate exceptions are caught and demonstrated, all cells execute as expected.

**Acceptance Scenarios**:

1. **Given** a student reaches the error handling section, **When** they read through it, **Then** they find explanations of exception types, try/except/else/finally, raising exceptions, custom exceptions, and best practices — each sub-topic with at least 2 internet-sourced visuals.
2. **Given** a student runs code cells demonstrating exceptions, **When** cells with intentional errors execute, **Then** exceptions are properly caught and the notebook continues without crashing.

---

### User Story 4 — Student Gets Introduction to OOP (Priority: P2)

A student works through the intro to OOP section. They learn about the motivation for OOP (why classes?), defining classes and creating objects, the `__init__` method and `self`, instance attributes and methods, and a brief preview of what comes in Lecture 5 (inheritance, magic methods, etc.). Each sub-topic includes at least 2 internet-sourced visuals.

**Why this priority**: OOP intro sets the stage for deeper coverage in Lecture 5. It should be substantial enough to convey core concepts but leave advanced topics for later.

**Independent Test**: Can be tested by running all code cells in the "Intro to OOP" section; all class definitions, instantiations, and method calls work correctly.

**Acceptance Scenarios**:

1. **Given** a student reaches the OOP intro section, **When** they read through it, **Then** they find explanations of classes, objects, `__init__`, `self`, attributes, and methods — each sub-topic with at least 2 internet-sourced visuals.
2. **Given** a student runs all OOP code cells, **When** cells execute, **Then** all class examples work without errors and output matches expectations.

---

### User Story 5 — Student Completes Practical Exercises and Mini-Project (Priority: P2)

A student works through end-of-lecture exercises that integrate functions, modules, error handling, and OOP basics. Exercises include empty code cells with TODO comments and hidden solutions (in collapsible `<details>` blocks). A mini-project ties together at least 3 of the 4 major topics.

**Why this priority**: Practice exercises reinforce learning and provide hands-on experience combining all lecture topics.

**Independent Test**: Can be tested by verifying exercise cells have TODO placeholders, solution blocks exist, and solutions execute correctly when revealed.

**Acceptance Scenarios**:

1. **Given** a student reaches the exercises section, **When** they look at each exercise, **Then** they see a clear problem statement, empty code cells with TODO comments, and collapsible solution blocks.
2. **Given** a student reveals and runs a solution, **When** the solution code executes, **Then** it produces the expected output without errors.

---

### Edge Cases

- What happens when a student runs the notebook without having completed Lecture 3 prerequisites? — A "Prerequisites" section at the top clearly states required prior knowledge.
- What happens when internet-sourced images become unavailable (broken links)? — Each image includes alt-text describing the visual and a source URL for maintenance and replacement purposes. Stable sources (official docs, well-known educational sites) are preferred.
- What happens when students try exercises without looking at solutions? — Exercise cells have clear TODO markers and are independently functional for student code.
- What happens when a student runs cells out of order? — Each section is as self-contained as possible; dependencies on earlier cells are minimized and documented where they exist.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Lecture MUST be delivered as a Jupyter Notebook file (`lecture-04.ipynb`) in the `lectures/04-functions-modules-errors-oop/` directory, following the naming and structure conventions of Lectures 1–3.
- **FR-002**: Lecture content MUST be written in Ukrainian, consistent with Lectures 1–3.
- **FR-003**: Lecture MUST contain the following major sections in order: (1) Learning Objectives, (2) Prerequisites, (3) Functions (continued), (4) Modules and Imports, (5) Error Handling, (6) Intro to OOP, (7) Practical Exercises, (8) Mini-Project, (9) Summary, (10) What's Next, (11) References.
- **FR-004**: Each sub-topic within a major section MUST include at least 2 visuals sourced from the internet (not custom-generated), embedded as markdown images with source attribution.
- **FR-005**: All code examples MUST be compatible with Python 3.11+ and executable in Jupyter Notebook without external pip dependencies.
- **FR-006**: The "Functions (continued)" section MUST cover: lambda expressions, higher-order functions (functions as arguments/return values), `map`/`filter`/`reduce`, scope rules (local/global/enclosing/LEGB), closures, a brief intro to decorators, and type hints.
- **FR-007**: The "Modules and Imports" section MUST cover: import statements (`import`, `from ... import`, `as`), key standard library modules overview, creating custom modules, the `__name__ == "__main__"` pattern, and package structure basics.
- **FR-008**: The "Error Handling" section MUST cover: common exception types, the exception hierarchy, `try`/`except`/`else`/`finally` blocks, catching specific vs broad exceptions, `raise` statement, creating custom exceptions, and error handling best practices.
- **FR-009**: The "Intro to OOP" section MUST cover: motivation for OOP, defining classes and creating objects, the `__init__` method and `self`, instance attributes and methods, and a preview of Lecture 5 topics.
- **FR-010**: Practical exercises MUST include at least 3 exercises covering functions, modules, and error handling, with empty code cells (TODO markers) and collapsible solution blocks (`<details>` tags).
- **FR-011**: A mini-project MUST integrate concepts from at least 3 of the 4 major topics (functions, modules, errors, OOP) into a single practical scenario.
- **FR-012**: The lecture MUST include a "Summary" section listing key takeaways and a "What's Next" section previewing Lecture 5 topics.
- **FR-013**: The lecture MUST include a "References" section with links to official Python documentation and reputable educational resources.
- **FR-014**: All internet-sourced visuals MUST include alt-text and a source URL comment or caption for attribution and maintenance purposes.

### Key Entities

- **Lecture Notebook**: The primary Jupyter Notebook file containing all lecture content, code cells, and embedded visuals.
- **Visual Asset**: An internet-sourced image (diagram, infographic, illustration) embedded via markdown image syntax with attribution.
- **Exercise**: A structured practice problem with problem statement, empty code cell, and collapsible solution.
- **Mini-Project**: A capstone exercise integrating multiple lecture topics.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: All code cells in the notebook (estimated 40–60 cells) execute without errors when run sequentially from top to bottom.
- **SC-002**: Each of the 4 major topic sections (Functions continued, Modules, Errors, OOP intro) contains at least 2 internet-sourced visuals per sub-topic (estimated 8–12 sub-topics total, minimum ~20 visuals across the lecture).
- **SC-003**: At least 3 practical exercises and 1 mini-project are included, each with problem statements, TODO code cells, and working collapsible solutions.
- **SC-004**: The lecture follows the same language (Ukrainian), formatting style, and structural conventions as Lectures 1–3.
- **SC-005**: Students who completed Lectures 1–3 can work through Lecture 4 independently, understanding all concepts with the provided explanations and visuals.
- **SC-006**: No external pip packages are required — all code examples use only the Python standard library.

## Assumptions

- The lecture language is Ukrainian, consistent with Lectures 1–3.
- The lecture follows the folder naming convention: `lectures/04-functions-modules-errors-oop/`.
- Internet-sourced visuals are preferred over custom matplotlib-generated diagrams, as specified by the user. Visuals should come from stable, reputable sources (official docs, Real Python, educational sites, well-known blog posts).
- The OOP introduction is intentionally kept at an introductory level; deeper OOP topics (inheritance, polymorphism, magic methods, dataclasses) are deferred to Lecture 5.
- Decorators are covered at an introductory level only (basic syntax and one practical example), with deeper coverage planned for later lectures.
- The `reduce` function from `functools` is the only standard library function imported beyond built-ins for the functions section.
