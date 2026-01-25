# Feature Specification: Lecture 1 Content Expansion

**Feature Branch**: `002-lecture1-content-expansion`
**Created**: 2026-01-25
**Status**: Draft
**Input**: User description: "Improve Lecture 1 notebook by: adding storytelling ('on the history of why Python looks like it looks', 'why Python is awesome + where it's slow'), expanding pip/venv + modules/packages, how packages and modules in Python work, when talking about data types explain that dynamic in Python means duck typing and its explanation, upgrading References section (student-friendly + structured)"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Python Design Philosophy Storytelling (Priority: P1)

A student reading Lecture 1 wants to understand WHY Python was designed the way it was, not just WHAT features it has. Through engaging storytelling about Guido van Rossum's decisions and Python's evolution, the student gains deeper appreciation for Python's design principles and remembers concepts better through narrative context.

**Why this priority**: Storytelling creates emotional connection to material and improves retention. Understanding "why" before "what" aligns with constitution's Student-Centered Design principle.

**Independent Test**: Student can explain to a peer why Python uses indentation for blocks, why it emphasizes readability, and can articulate Python's strengths and weaknesses in different contexts.

**Acceptance Scenarios**:

1. **Given** a student reading the "What is Python" section, **When** they encounter the history narrative, **Then** they understand the connection between ABC language problems and Python's design decisions
2. **Given** a student completing the lecture, **When** asked "Why does Python look different from C/Java?", **Then** they can explain the readability philosophy with concrete examples
3. **Given** a student reading about Python's performance, **When** they learn where Python is slow, **Then** they understand the trade-offs and when to use Python vs alternatives

---

### User Story 2 - Duck Typing Understanding (Priority: P1)

A student learning about Python's dynamic typing wants to understand what "dynamic" actually means in practice. Through the duck typing concept explanation with practical examples, the student understands how Python determines object compatibility at runtime rather than through declared types.

**Why this priority**: Duck typing is fundamental to understanding Python's flexibility and common patterns. Misconceptions here cause confusion in later lectures.

**Independent Test**: Student can predict the behavior of code that relies on duck typing and explain why it works without explicit type declarations.

**Acceptance Scenarios**:

1. **Given** a student reading the data types section, **When** they encounter the duck typing explanation, **Then** they understand "If it walks like a duck and quacks like a duck, it's a duck"
2. **Given** a student seeing a function that accepts multiple object types, **When** asked how Python handles this, **Then** they can explain method resolution at runtime
3. **Given** a student comparing Python to statically-typed languages, **When** asked about trade-offs, **Then** they can articulate benefits (flexibility) and costs (runtime errors)

---

### User Story 3 - Modules and Packages Deep Understanding (Priority: P2)

A student setting up their Python environment wants to understand the difference between modules and packages, how Python finds imports, and how pip/venv work together. This knowledge prevents common "ModuleNotFoundError" frustrations and prepares them for project organization in later lectures.

**Why this priority**: Environment and import issues are the #1 source of beginner frustration. Clear understanding here prevents hours of debugging later.

**Independent Test**: Student can create a simple package structure, import from it correctly, and troubleshoot basic import errors.

**Acceptance Scenarios**:

1. **Given** a student learning about imports, **When** they read the modules vs packages section, **Then** they understand a module is a .py file and a package is a directory with __init__.py
2. **Given** a student reading about pip, **When** they learn about PyPI and package installation, **Then** they understand how pip resolves dependencies and where packages are installed
3. **Given** a student using venv, **When** they read the expanded venv section, **Then** they understand how venv isolates site-packages and why this matters for reproducibility

---

### User Story 4 - Student-Friendly References (Priority: P3)

A student finishing the lecture wants to continue learning independently. The upgraded References section provides categorized resources (official docs, tutorials, video courses, practice platforms) with brief descriptions of what each offers and recommended learning paths.

**Why this priority**: Self-directed learning resources extend lecture value beyond class time. Good references reduce dependency on instructor.

**Independent Test**: Student can identify the most appropriate resource for their specific learning goal (quick reference vs deep dive vs hands-on practice).

**Acceptance Scenarios**:

1. **Given** a student wanting quick syntax reference, **When** they check the References section, **Then** they find categorized resources with clear descriptions
2. **Given** a student preferring video learning, **When** they look for video resources, **Then** they find recommended YouTube channels/courses with brief descriptions
3. **Given** a student wanting hands-on practice, **When** they seek practice platforms, **Then** they find interactive coding sites with difficulty levels indicated

---

### Edge Cases

- What happens when a student has prior programming experience in statically-typed languages? Content includes comparison points to C++/Java/C# for context
- How does content handle students who already know some Python basics? Sections provide depth beyond surface explanations for advanced readers
- What if references become outdated? Primary sources are version-agnostic official documentation

## Requirements *(mandatory)*

### Functional Requirements

**Storytelling & Philosophy**
- **FR-001**: Lecture MUST include a narrative section explaining ABC language's influence on Python's design
- **FR-002**: Lecture MUST explain why Python chose indentation over braces with historical context
- **FR-003**: Lecture MUST include "Why Python is awesome" section covering: readability, standard library, community, cross-platform
- **FR-004**: Lecture MUST include "Where Python is slow" section covering: GIL, interpreted nature, when to consider alternatives
- **FR-005**: Storytelling sections MUST use engaging narrative style, not just bullet points
- **FR-006**: Lecture must include Python release and changes philosophy

**Duck Typing & Dynamic Typing**
- **FR-007**: Lecture MUST define duck typing with the canonical "walks like a duck" explanation
- **FR-008**: Lecture MUST include runnable code example demonstrating duck typing behavior
- **FR-009**: Lecture MUST contrast duck typing with static typing using concrete examples
- **FR-010**: Lecture MUST explain runtime method resolution in simple terms
- **FR-011**: Lecture MUST acknowledge trade-offs: flexibility vs potential runtime errors
- **FR-012**: Lecture MUST include explanation why there is separation into static/dynamic and strong/weak typing and where Python fits here

**Modules & Packages**
- **FR-013**: Lecture MUST clearly distinguish between module (single .py file) and package (directory with __init__.py)
- **FR-014**: Lecture MUST explain Python's import search path (PYTHONPATH, site-packages, current directory)
- **FR-015**: Lecture MUST expand pip section to cover: PyPI, dependency resolution, pip show, pip uninstall
- **FR-016**: Lecture MUST explain how venv creates isolated site-packages directory
- **FR-017**: Lecture MUST include visual diagram showing module/package relationship

**References Section**
- **FR-018**: References MUST be categorized by type: Official Documentation, Tutorials, Video Courses, Practice Platforms, Books
- **FR-019**: Each reference MUST include 1-sentence description of what it offers
- **FR-020**: References MUST indicate difficulty level or target audience where applicable
- **FR-021**: References MUST prioritize free resources, marking paid ones clearly
- **FR-022**: References section MUST include "Recommended Learning Path" for different student backgrounds

### Key Entities

- **Lecture Content Sections**: Discrete content blocks that can be added/modified independently
- **Code Examples**: Runnable Python code demonstrating concepts (duck typing, imports)
- **Visual Diagrams**: Module/package structure diagram, import path visualization
- **Reference Categories**: Organized groups of external learning resources

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Students can correctly explain Python's design philosophy (indentation choice, readability focus) after reading the storytelling section
- **SC-002**: Students can predict duck typing behavior in code examples with 90% accuracy
- **SC-003**: Students can create a simple package with two modules and import between them without errors
- **SC-004**: Students can identify the appropriate reference resource for their learning goal within 30 seconds
- **SC-005**: Lecture content fits within the 1.5-hour target duration with new additions
- **SC-006**: All code examples execute successfully in Python 3.11+ environment
- **SC-007**: Content adheres to constitution's icon usage guideline (sparingly, max 1-2 per section)

## Assumptions

- Students have access to the existing Lecture 1 notebook as baseline
- New content will be integrated into existing notebook structure, not replace it
- All additions follow constitution's Ukrainian language with English technical terms in parentheses only if this is some programming-specific or science-specific concept htat is mostly used in English
- Visual diagrams will be generated programmatically (matplotlib) consistent with existing assets or downloaded from the internet if this is more relevant
- Reference URLs will be validated for accessibility before inclusion

## Dependencies

- Existing Lecture 1 notebook (`lectures/01-python-intro/lecture-01.ipynb`)
- Constitution content standards (v1.0.1)
- Asset generation scripts (`lectures/01-python-intro/assets/`)

## Out of Scope

- Changes to exercise content (exercises remain as-is)
- Changes to existing memes/images (unless directly related to new content)
- Addition of new exercises (this focuses on explanatory content)
- Changes to other lectures
