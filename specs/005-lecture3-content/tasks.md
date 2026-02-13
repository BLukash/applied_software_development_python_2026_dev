# Tasks: Lecture 3 — Data Structures + Pythonic Patterns + Functions

**Input**: Design documents from `/specs/005-lecture3-content/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, quickstart.md

**Tests**: Not requested — no test tasks generated. Validation is manual (Kernel > Restart & Run All).

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story. Since this is a single Jupyter notebook, user stories map to lecture sections. Each story adds cells to `lectures/03-data-structures/lecture-03.ipynb`.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

```text
lectures/03-data-structures/
├── lecture-03.ipynb          # Main lecture notebook (all content)
└── assets/
    ├── diagrams/             # Memory layout diagrams
    └── memes/                # Educational humor images
```

---

## Phase 1: Setup

**Purpose**: Create directory structure, notebook skeleton, and perform contextual analysis of previous lectures

- [X] T001 Create directory structure: `lectures/03-data-structures/`, `lectures/03-data-structures/assets/diagrams/`, `lectures/03-data-structures/assets/memes/`
- [X] T002 Read and analyze Lecture 2 in full detail at `lectures/02-core-mechanics/lecture-02.ipynb` — document tone patterns, recurring phrases, analogies used, examples given, and cross-reference opportunities per constitution requirement III
- [X] T003 Briefly review Lecture 1 at `lectures/01-python-intro/lecture-01.ipynb` — skim headings, note content already covered to avoid duplication
- [X] T004 Create notebook skeleton in `lectures/03-data-structures/lecture-03.ipynb` with header cell (Лекція 3, title, date, prerequisites), learning objectives cell (5 objectives from data-model.md), and empty section headers for all 10 sections

**Checkpoint**: Notebook skeleton exists with header, learning objectives, and section placeholders. Contextual analysis complete.

---

## Phase 2: Foundational (Shared Content)

**Purpose**: Prepare assets and cross-cutting content that multiple user stories depend on

- [X] T005 [P] Source or create Meme 1 (data structure choice meme) and save to `lectures/03-data-structures/assets/memes/collections-meme.png` — see research.md R4 for concepts
- [X] T006 [P] Source or create Meme 2 (comprehension readability meme) and save to `lectures/03-data-structures/assets/memes/comprehensions-meme.png` — see research.md R4 for concepts
- [X] T007 [P] Source or create diagram: list internal memory structure (pointer array with over-allocation) and save to `lectures/03-data-structures/assets/diagrams/list-memory.png` — see research.md R1 for sources (Laurent Luce, Real Python); generate with matplotlib if no internet source found
- [X] T008 [P] Source or create diagram: tuple internal memory structure (fixed pointer array) and save to `lectures/03-data-structures/assets/diagrams/tuple-memory.png` — compare with list diagram; generate with matplotlib if needed
- [X] T009 [P] Source or create diagram: dict/set hash table concept (keys → hash → slots → values) and save to `lectures/03-data-structures/assets/diagrams/dict-hashtable.png` — see research.md R1/R2 for approach

**Checkpoint**: All 2 memes and 3+ diagrams ready in assets folder with proper attribution.

---

## Phase 3: User Story 1 — Collections Deep Dive (Priority: P1) MVP

**Goal**: Student gains comprehensive understanding of list, tuple, dict, set — creation, methods, pitfalls, indexing, slicing, nested structures, membership checks, and a comparison table.

**Independent Test**: Give students a dataset and ask them to store, retrieve, slice, and transform data using each collection type.

### Implementation for User Story 1

- [X] T010 [US1] Write Section 1.1 (Списки / Lists) in `lectures/03-data-structures/lecture-03.ipynb` — markdown cell with Ukrainian explanation + English terms in parentheses, followed by code cells: (1) list creation and indexing with positive/negative indices, (2) slicing with start:stop:step variations including [::-1], (3) .append() vs .extend() comparison showing different results, (4) modifying list while iterating — the bug and the fix using copy, (5) .sort() vs sorted() comparison. Include cross-reference to Lecture 2's brief collection introduction. Cover FR-001, FR-006.
- [X] T011 [US1] Write Section 1.2 (Кортежі / Tuples) in `lectures/03-data-structures/lecture-03.ipynb` — markdown + code cells: (1) tuple creation with and without parentheses, (2) single-element tuple gotcha (x,) vs (x), (3) tuple unpacking, (4) immutability enforcement attempt (TypeError), (5) brief namedtuple mention as preview. Cover FR-002.
- [X] T012 [US1] Write Section 1.3 (Словники / Dicts) in `lectures/03-data-structures/lecture-03.ipynb` — markdown + code cells: (1) dict creation (literal, dict(), from zip preview), (2) bracket notation vs .get() with default showing KeyError avoidance, (3) .update(), .pop(), .setdefault() examples, (4) iteration with .keys(), .values(), .items(), (5) key hashability requirement + {} creates empty dict not set pitfall. Cover FR-003.
- [X] T013 [US1] Write Section 1.4 (Множини / Sets) in `lectures/03-data-structures/lecture-03.ipynb` — markdown + code cells: (1) set creation (set() and {a,b,c}), (2) deduplication example, (3) .add(), .discard(), .remove(), (4) set operations: | & - ^ with examples, (5) membership check x in my_set. Cover FR-004.
- [X] T014 [US1] Write Section 1.5 (Порівняльна таблиця) in `lectures/03-data-structures/lecture-03.ipynb` — markdown table comparing all 4 collection types (ordered, mutable, duplicates, use case) per data-model.md. Insert Meme 1 image from assets/memes/collections-meme.png after the table. Cover FR-005.
- [X] T015 [US1] Write Section 3 (Індексація, зрізи та вкладені структури) in `lectures/03-data-structures/lecture-03.ipynb` — markdown + code cells: (1) advanced slicing with step numbers[::2], (2) slice assignment numbers[1:3] = [10, 20, 30], (3) nested structure: list of student dicts, (4) accessing nested: students[0]["name"], (5) membership checks: `in` for list, dict (keys), set. Cover FR-006, FR-007, FR-027.
- [X] T016 [US1] Write common pitfalls subsection within Section 1 in `lectures/03-data-structures/lecture-03.ipynb` — code cells demonstrating: (1) .append() vs .extend() side by side, (2) modifying list during iteration, (3) unhashable dict key attempt (TypeError), (4) {} is empty dict not empty set. Cover FR-008.

**Checkpoint**: Sections 1 and 3 complete. Student can work with all 4 collection types including indexing, slicing, nested structures.

---

## Phase 4: User Story 2 — Comprehensions and Iteration Patterns (Priority: P1)

**Goal**: Student masters enumerate, zip, and list/dict/set comprehensions with readability guidelines.

**Independent Test**: Provide loop-based code and ask students to rewrite using comprehensions, and vice versa.

### Implementation for User Story 2

- [X] T017 [US2] Write Section 4 (Ітераційні патерни) in `lectures/03-data-structures/lecture-03.ipynb` — markdown + code cells: (1) enumerate() with numbered output, (2) enumerate(items, 1) with custom start, (3) zip() for parallel iteration, (4) zip() for dict creation dict(zip(keys, values)), (5) zip() with unequal-length edge case. Cover FR-009, FR-010.
- [X] T018 [US2] Write Section 5 (Comprehensions) in `lectures/03-data-structures/lecture-03.ipynb` — markdown + code cells: (1) simple list comprehension (squares), (2) filtered list comprehension (even numbers), (3) transforming comprehension (uppercase strings), (4) dict comprehension (word lengths), (5) set comprehension (unique first letters), (6) anti-pattern: overly nested comprehension with loop rewrite equivalent. Show loop version FIRST then comprehension. Cover FR-011, FR-012, FR-013.
- [X] T019 [US2] Write comprehension readability guidelines subsection in Section 5 of `lectures/03-data-structures/lecture-03.ipynb` — markdown cell with Ukrainian text explaining when to use comprehensions vs loops using "one sentence rule" from research.md R3. Insert Meme 2 image from assets/memes/comprehensions-meme.png. Cover FR-014.

**Checkpoint**: Sections 4-5 complete. Student can use enumerate, zip, and all comprehension types with readability awareness.

---

## Phase 5: User Story 3 — Introduction to Functions (Priority: P1)

**Goal**: Student can define and call functions with parameters, return values, defaults, *args/**kwargs.

**Independent Test**: Ask students to refactor repeated code into functions and write functions with various parameter types.

### Implementation for User Story 3

- [X] T020 [US3] Write Section 7 (Вступ до функцій) in `lectures/03-data-structures/lecture-03.ipynb` — markdown introducing WHY functions (DRY principle, organization, reusability) + code cells: (1) basic function def greet(name), (2) function with default argument def area(width, height=1), (3) multiple return values via tuple def min_max(numbers), (4) brief docstring example (one-line format). Cross-reference Lecture 2's mutable default argument but do NOT re-explain. Cover FR-018, FR-019.
- [X] T021 [US3] Write *args and **kwargs subsection in Section 7 of `lectures/03-data-structures/lecture-03.ipynb` — code cells: (1) *args example def total(*numbers): return sum(numbers), (2) **kwargs example def build_profile(**info): return info, (3) combining positional + *args + keyword: def log(message, *tags, level="INFO"). Cover FR-020.

**Checkpoint**: Section 7 complete. Student can define and use functions with all parameter types.

---

## Phase 6: User Story 4 — Memory Representation of Collections (Priority: P2)

**Goal**: Student understands how list, tuple, dict, set are stored in memory through diagrams and sys.getsizeof().

**Independent Test**: Ask students to draw simplified memory diagrams for a list vs tuple.

### Implementation for User Story 4

- [X] T022 [US4] Write Section 2 (Як колекції зберігаються в пам'яті) in `lectures/03-data-structures/lecture-03.ipynb` — markdown with Ukrainian explanation + insert 3 diagrams from assets/diagrams/ (list-memory.png, tuple-memory.png, dict-hashtable.png) with attribution. Add code cell with sys.getsizeof() comparison for list, tuple, dict, set. Cross-reference Lecture 2's memory model section. Cover FR-017.

**Checkpoint**: Section 2 complete with all diagrams and memory comparison code.

---

## Phase 7: User Story 5 — Complexity Intuition (Priority: P2)

**Goal**: Student understands why dict/set O(1) lookup is faster than list O(n) scan and can choose data structures accordingly.

**Independent Test**: Time list vs set membership checks on 100K elements; student predicts and explains result.

### Implementation for User Story 5

- [X] T023 [US5] Write Section 6 (Складність операцій — Інтуїція) in `lectures/03-data-structures/lecture-03.ipynb` — markdown with locker room analogy for hash tables (see research.md R2) + code cells: (1) hash() demonstration on strings and integers, (2) timed comparison of `in` on list vs set with 100,000 elements using time.perf_counter() (see research.md R2 for exact code), (3) real scenario: checking duplicate usernames with set. Cross-reference Lecture 2's timing section. Cover FR-015, FR-016.

**Checkpoint**: Section 6 complete. Student can explain O(1) vs O(n) and choose appropriate data structures.

---

## Phase 8: User Story 6 — Mini Parsing Task (Priority: P2)

**Goal**: Student completes a practical exercise combining collections, comprehensions, iteration patterns, and functions to parse log data.

**Independent Test**: Provide sample log input, verify student output matches expected frequency counts.

### Implementation for User Story 6

- [X] T024 [US6] Write Exercise 1 (Collection Operations) in Section 8 of `lectures/03-data-structures/lecture-03.ipynb` — markdown with task description (list of student dicts: extract names, filter by grade, create name→grade dict) + starter code cell + hidden solution cell. Cover FR-022 (exercise 1 of 2).
- [X] T025 [US6] Write Exercise 2 (Data Structure Choice) in Section 8 of `lectures/03-data-structures/lecture-03.ipynb` — markdown with scenarios (fast membership check, ordered sequence, key-value mapping) + starter code cell + hidden solution cell. Cover FR-022 (exercise 2 of 2).
- [X] T026 [US6] Write Section 9 (Міні-проєкт — Парсинг логів) in `lectures/03-data-structures/lecture-03.ipynb` — markdown with task description + hardcoded log data string (from research.md R6) + step-by-step instructions (parse_log_line, count_frequencies, top_requests) + starter code with TODO comments + hidden solution cell using research.md R6 expected solution. Must use at least one comprehension, enumerate, and custom functions. Cover FR-021.

**Checkpoint**: Sections 8-9 complete. All exercises and mini-project have starter code and hidden solutions.

---

## Phase 9: Polish & Cross-Cutting Concerns

**Purpose**: Wrap-up sections, final quality validation, and cross-cutting improvements

- [X] T027 Write Section 10 summary in `lectures/03-data-structures/lecture-03.ipynb` — markdown cell with "Що ми вивчили сьогодні" bullet list (use checkmarks sparingly per constitution) covering all 7 topics from data-model.md summary section
- [X] T028 Write "Що далі?" (What's Next) section in `lectures/03-data-structures/lecture-03.ipynb` — markdown cell previewing Lecture 4 topics (functions deep dive, lambda, scope, exceptions, modules, type hints) + homework assignments (4 items from data-model.md)
- [X] T029 Write References section in `lectures/03-data-structures/lecture-03.ipynb` — markdown cell with categorized links: Official Documentation (6 links), Tutorials (5 Real Python links), Deep Dives (2 links) from data-model.md references. Verify no Russian-language resources per constitution.
- [X] T030 Review entire notebook for content duplication with Lectures 1-2 — verify FR-025 compliance: no re-explanation of basic types, names/objects, mutability principle, control flow, truthiness, timing basics. Ensure only cross-references, not repetitions.
- [X] T031 Verify all cross-references to Lectures 1-2 are present and use consistent notation — check that each section opening connects to previous material per spec contextual analysis and FR-026
- [X] T032 Run full notebook validation: Kernel > Restart & Run All in `lectures/03-data-structures/lecture-03.ipynb` — verify all code cells execute without errors in Python 3.11+ per FR-023
- [X] T033 Verify constitution compliance in `lectures/03-data-structures/lecture-03.ipynb` — checklist: (1) 5 learning objectives at start, (2) 15+ runnable code examples, (3) 2 exercises with hidden solutions, (4) mini parsing task with hidden solution, (5) 2 memes loaded correctly, (6) 3+ diagrams loaded correctly, (7) Ukrainian text with English terms in parentheses, (8) summary section, (9) What's Next section, (10) references section, (11) icons/emojis used sparingly
- [X] T034 Verify timing: estimate lecture content fits within 1.5 hours — review time allocation per data-model.md (~130 min total) and adjust sections if needed per SC-008

**Checkpoint**: Lecture 3 complete, validated, and ready for human review.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on T001 (directory structure) — asset preparation can proceed in parallel with Setup T002-T004
- **US1 Collections (Phase 3)**: Depends on T004 (notebook skeleton) and T005 (Meme 1 for Section 1.5)
- **US2 Comprehensions (Phase 4)**: Depends on T004 (notebook skeleton) and T006 (Meme 2 for Section 5)
- **US3 Functions (Phase 5)**: Depends on T004 (notebook skeleton)
- **US4 Memory (Phase 6)**: Depends on T004 (notebook skeleton) and T007-T009 (diagrams)
- **US5 Complexity (Phase 7)**: Depends on T004 (notebook skeleton)
- **US6 Mini Task (Phase 8)**: Depends on US1, US2, US3 content being complete (exercises reference all prior concepts)
- **Polish (Phase 9)**: Depends on all user story phases complete

### User Story Dependencies

- **US1 (P1)**: Independent — can start after Setup. MVP scope.
- **US2 (P1)**: Independent of US1 — can start in parallel (different notebook sections)
- **US3 (P1)**: Independent of US1/US2 — can start in parallel (different notebook sections)
- **US4 (P2)**: Independent — requires diagrams from Phase 2
- **US5 (P2)**: Independent — can start after Setup
- **US6 (P2)**: Depends on US1 + US2 + US3 being complete (synthesis exercise uses all concepts)

### Within Each User Story

- Markdown explanation cells before code cells
- Code examples in progressive difficulty order
- Cross-references use phrasing from spec contextual analysis
- Memes/diagrams inserted at positions specified in data-model.md

### Parallel Opportunities

- T005, T006, T007, T008, T009 (all asset preparation) can run in parallel
- T010-T016 (US1 sections) are sequential within the notebook but can be drafted in parallel as text
- T017-T019 (US2) can proceed in parallel with T010-T016 (US1) since they target different sections
- T020-T021 (US3) can proceed in parallel with US1 and US2
- T022 (US4) can proceed in parallel with US1-US3 once diagrams are ready
- T023 (US5) can proceed in parallel with US1-US4

---

## Parallel Example: Asset Preparation

```text
# Launch all asset tasks together (Phase 2):
Task: T005 "Source/create collections meme → assets/memes/collections-meme.png"
Task: T006 "Source/create comprehensions meme → assets/memes/comprehensions-meme.png"
Task: T007 "Source/create list memory diagram → assets/diagrams/list-memory.png"
Task: T008 "Source/create tuple memory diagram → assets/diagrams/tuple-memory.png"
Task: T009 "Source/create hash table diagram → assets/diagrams/dict-hashtable.png"
```

## Parallel Example: P1 User Stories

```text
# After notebook skeleton (T004), launch all P1 stories in parallel:
Task: T010-T016 "US1: Collections deep dive sections"
Task: T017-T019 "US2: Iteration patterns + comprehensions sections"
Task: T020-T021 "US3: Functions introduction section"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup (T001-T004)
2. Complete Phase 2: Assets (T005-T009) — at minimum T005 for Meme 1
3. Complete Phase 3: US1 Collections (T010-T016)
4. **STOP and VALIDATE**: Notebook has complete collections coverage with indexing, slicing, methods, pitfalls
5. Can deliver as partial lecture if needed

### Incremental Delivery

1. Setup + Assets → Foundation ready
2. Add US1 (Collections) → Core collections complete (MVP)
3. Add US2 (Comprehensions) → Pythonic patterns added
4. Add US3 (Functions) → Function intro added
5. Add US4 (Memory) → Visual depth added
6. Add US5 (Complexity) → Performance intuition added
7. Add US6 (Mini Task) → Synthesis exercise added
8. Polish → Lecture complete and validated

### Recommended Execution Order (Single Author)

For a single author working sequentially, follow notebook section order for natural flow:

1. T001-T004 (Setup)
2. T005-T009 (Assets — can be deferred if images aren't ready yet)
3. T010-T016 (US1: Sections 1 + 3 — Collections + Indexing/Slicing)
4. T022 (US4: Section 2 — Memory, placed between Sections 1 and 3 in notebook)
5. T017-T019 (US2: Sections 4-5 — Iteration + Comprehensions)
6. T023 (US5: Section 6 — Complexity)
7. T020-T021 (US3: Section 7 — Functions)
8. T024-T026 (US6: Sections 8-9 — Exercises + Mini Task)
9. T027-T034 (Polish)

---

## Notes

- [P] tasks = different files, no dependencies on incomplete tasks
- [Story] label maps task to specific user story for traceability
- All content must be in Ukrainian with English terms in parentheses on first use
- Single notebook file means tasks are logically parallel but physically sequential in the file
- Hidden solution cells use Jupyter cell metadata or collapsible headings
- Commit after completing each user story phase
- Stop at any checkpoint to validate independently
