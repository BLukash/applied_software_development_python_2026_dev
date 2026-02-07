# Feature Specification: Lecture 2 Content Restructuring

**Feature Branch**: `004-lecture2-restructure`
**Created**: 2026-02-06
**Status**: Draft
**Input**: User description: "Enhance Lecture 2 by restructuring content flow: move Memory Representation after Names and Objects, add identity vs equality examples on simple types, introduce complex data types, then mutability, then identity vs equality on lists"

## Contextual Analysis (Constitution Requirement)

**Restructuring Rationale:**

The current Lecture 2 structure separates conceptually connected topics. This enhancement reorganizes the flow to build knowledge progressively:

1. Names and Objects (existing) - foundation
2. Memory Representation - immediately shows HOW names/objects work in memory (natural connection)
3. Identity vs Equality on simple types - students see `is` vs `==` on types they already know
4. Complex data types introduction - prepare students for mutability examples
5. Mutability principle - now students have all context needed
6. Identity vs Equality on lists - apply concepts to mutable types
7. Remaining topics unchanged - truthiness, control flow, timing

**Cross-Reference to Lecture 3:**
Complex data types section explicitly states "will be covered in depth in Lecture 3" to set expectations.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Progressive Learning Flow (Priority: P1)

A student follows a logical progression from basic concepts to advanced ones. After learning about names and objects, they immediately see memory representation which visualizes what they just learned. This creates a strong mental model before introducing complexity.

**Why this priority**: The entire restructuring goal is to improve learning flow. If this doesn't work, the enhancement fails.

**Independent Test**: Can be fully tested by having students follow the restructured lecture and checking comprehension at each transition point.

**Acceptance Scenarios**:

1. **Given** a student who just completed Section 1 (Names and Objects), **When** they read the Memory Representation section immediately after, **Then** they report the transition feels natural and reinforces what they learned.

2. **Given** students who understand memory representation, **When** they see identity vs equality on simple types, **Then** they can connect `id()` output to the memory diagrams they just saw.

3. **Given** students who have seen simple type examples, **When** complex types are introduced, **Then** they understand these as "building blocks" without feeling overwhelmed.

---

### User Story 2 - Simple Types Identity vs Equality (Priority: P1)

A student learns `is` vs `==` first on simple/immutable types (int, str, bool) before encountering the complexity of mutable types. This builds intuition with predictable behavior before introducing edge cases.

**Why this priority**: Understanding identity vs equality on simple types first reduces cognitive load when later seeing mutable type examples.

**Independent Test**: Can be tested with code prediction exercises using only simple types.

**Acceptance Scenarios**:

1. **Given** examples comparing integers with `is` and `==`, **When** a student sees `a = 100; b = 100; a is b`, **Then** they understand this returns True due to integer caching.

2. **Given** string interning examples, **When** a student sees `s1 = "hello"; s2 = "hello"; s1 is s2`, **Then** they understand interning and when it applies.

3. **Given** the `is None` pattern on simple types, **When** students compare to `== None`, **Then** they establish the habit of using `is None` before seeing mutable type complications.

---

### User Story 3 - Complex Data Types Introduction (Priority: P1)

A student receives a preview of complex data types (list, dict, set, tuple) with enough detail to understand mutability examples, knowing that Lecture 3 will cover them in depth.

**Why this priority**: Students need to understand what lists and dicts ARE before they can understand mutability behavior on them.

**Independent Test**: Can be tested by asking students to create simple lists/dicts and explain their basic purpose.

**Acceptance Scenarios**:

1. **Given** a brief introduction to lists, **When** a student sees `items = [1, 2, 3]`, **Then** they understand it's an ordered, modifiable collection.

2. **Given** a brief introduction to dicts, **When** a student sees `person = {"name": "Ivan", "age": 25}`, **Then** they understand it's a key-value mapping.

3. **Given** explicit statement "details in Lecture 3", **When** students wonder about advanced features, **Then** they know more is coming and don't feel incomplete.

---

### User Story 4 - Mutability After Data Type Knowledge (Priority: P1)

A student learns the mutability principle AFTER they understand all relevant data types. This ensures examples using lists and dicts are meaningful because students know what these types are.

**Why this priority**: The restructuring specifically places mutability after data type introduction for this reason.

**Independent Test**: Can be tested by presenting mutability examples and checking if students can follow without asking "what is a list?"

**Acceptance Scenarios**:

1. **Given** a student who just learned about lists, **When** they see `a = [1,2,3]; b = a; b.append(4)`, **Then** they understand this modifies both references because they know what lists are.

2. **Given** comparison of immutable (tuple) vs mutable (list), **When** students see modification attempts, **Then** they can predict which will fail vs succeed.

3. **Given** the mutable default argument bug, **When** students see `def add_item(item, items=[]):`, **Then** they understand why this is problematic because they understand list mutability.

---

### User Story 5 - Identity vs Equality on Lists (Priority: P2)

A student applies identity vs equality concepts to lists after understanding both concepts separately. This synthesis section demonstrates how simple type rules apply (or differ) for mutable types.

**Why this priority**: This is the culmination of the restructured flow - applying simple concepts to complex types.

**Independent Test**: Can be tested with list comparison exercises using `is` vs `==`.

**Acceptance Scenarios**:

1. **Given** students who understand `is` vs `==` on simple types, **When** they see `a = [1,2]; b = [1,2]; a == b` (True) and `a is b` (False), **Then** they understand equality checks content while identity checks reference.

2. **Given** the aliasing example `a = [1,2]; b = a`, **When** students check `a is b`, **Then** they connect this to the memory diagrams and understand both names point to the same object.

3. **Given** copy operations `b = a.copy()`, **When** students compare `a is b` vs `a == b`, **Then** they understand the difference between copying and aliasing.

---

### User Story 6 - Remaining Topics Unchanged (Priority: P2)

A student continues through truthiness, control flow, and timing sections exactly as in the original lecture. These sections remain in their existing form and position.

**Why this priority**: User explicitly requested no changes to these sections.

**Independent Test**: Can be verified by comparing content with original spec - should be identical.

**Acceptance Scenarios**:

1. **Given** the truthiness section from original spec, **When** reviewing restructured lecture, **Then** the content is unchanged.

2. **Given** control flow sections (if/elif/else, match, loops), **When** reviewing restructured lecture, **Then** all examples and explanations remain as specified.

3. **Given** timing section at the end, **When** reviewing restructured lecture, **Then** the performance intuition content is preserved.

---

### Edge Cases

- What if students skip the complex data types section and jump to mutability?
- How do we handle students who already know lists/dicts from other languages?
- What happens if a student doesn't understand memory representation before moving to identity?
- How do we ensure the complex types preview doesn't duplicate Lecture 3 content?

---

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Lecture MUST present sections in this order: (1) Names & Objects, (2) Memory Representation, (3) Identity vs Equality on Simple Types, (4) Complex Data Types Introduction, (5) Mutability, (6) Identity vs Equality on Lists, (7) Truthiness, (8) Control Flow, (9) Timing
- **FR-002**: Memory Representation section MUST immediately follow Names & Objects section
- **FR-003**: Identity vs Equality MUST be split into two sections: simple types first, lists/complex types after mutability
- **FR-004**: Complex Data Types introduction MUST cover: list, dict, set, and tuple with basic syntax and purpose
- **FR-005**: Complex Data Types section MUST explicitly state that detailed coverage is in Lecture 3
- **FR-006**: Simple types identity examples MUST include: integers (with caching), strings (with interning), and None checks
- **FR-007**: List identity examples MUST include: aliasing (`b = a`), equality vs identity (`==` vs `is`), and copying (`a.copy()`)
- **FR-008**: Mutability section MUST come AFTER complex data types introduction
- **FR-009**: Mutability section MUST reference the data types just introduced for all examples
- **FR-010**: Truthiness, Control Flow, and Timing sections MUST remain unchanged from original specification (003-lecture2-core-mechanics)
- **FR-011**: All transitions between sections MUST include a connecting sentence explaining why this topic follows the previous
- **FR-012**: Lecture MUST maintain constitution requirements: Ukrainian text, English terms in parentheses, 2 memes, visual diagrams
- **FR-013**: All code examples MUST work in Python 3.11+
- **FR-014**: Lecture MUST NOT duplicate Lecture 3's detailed coverage of complex data types

### Key Entities

- **Section Order**: The sequence of topics defining the learning path
- **Simple Types**: int, float, str, bool, None (immutable types for initial examples)
- **Complex Types**: list, dict, set, tuple (types requiring introduction before mutability)
- **Transition**: Connecting text between sections that maintains flow

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 90% of students report the Names → Memory → Identity flow feels logical and connected
- **SC-002**: Students can explain identity vs equality on simple types before encountering list examples
- **SC-003**: Students can create basic lists and dicts after the Complex Types Introduction section
- **SC-004**: 85% of students correctly predict list mutation behavior after completing the restructured flow
- **SC-005**: Zero "what is a list?" questions during the mutability section (because it's introduced earlier)
- **SC-006**: Complex Types Introduction section is under 10 minutes of lecture time (brief preview, not deep dive)
- **SC-007**: No content duplication with Lecture 3 in the Complex Types Introduction section
- **SC-008**: All transitions between sections include explicit connecting language
- **SC-009**: Truthiness, Control Flow, and Timing content matches original spec exactly
- **SC-010**: Lecture fits within 1.5 hours including the restructured content

---

## Assumptions

- Original Lecture 2 spec (003-lecture2-core-mechanics) provides the baseline content for unchanged sections
- Students have completed Lecture 1 and understand basic types and REPL usage
- Lecture 3 will cover complex data types in detail; this lecture only introduces them
- The restructuring improves learning outcomes without significantly increasing lecture duration
- Memory representation diagrams already exist in the original spec and can be repositioned
