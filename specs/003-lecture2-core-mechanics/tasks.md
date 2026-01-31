# Tasks: Lecture 2 - Core Language Mechanics

**Input**: Design documents from `/specs/003-lecture2-core-mechanics/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md

**Tests**: Not applicable - educational content validated through manual review per constitution.

**Organization**: Tasks are grouped by user story (lecture sections) to enable independent implementation and incremental delivery. Each section can be written and reviewed independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files/cells, no dependencies)
- **[Story]**: Which user story this task belongs to (US1-US8 mapping to lecture sections)
- Include exact file paths in descriptions

## Path Conventions

```text
lectures/
└── 02-core-mechanics/
    ├── lecture-02.ipynb     # Main lecture notebook
    └── assets/
        ├── diagrams/        # Visual aids
        └── memes/           # Educational humor
```

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create directory structure and notebook skeleton

- [ ] T001 Create directory structure: lectures/02-core-mechanics/assets/diagrams/ and lectures/02-core-mechanics/assets/memes/
- [ ] T002 Create empty Jupyter notebook: lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T003 [P] Source or create meme for mutability section in lectures/02-core-mechanics/assets/memes/mutability-bug.png
- [ ] T004 [P] Source or create meme for timing section in lectures/02-core-mechanics/assets/memes/timing-meme.png

**Checkpoint**: Directory structure ready, assets prepared.

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Create notebook header and structure that all sections depend on

**CRITICAL**: These cells must exist before any content section can be added.

- [ ] T005 Create header cell with lecture number, title, course info in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T006 Create learning objectives cell (5 objectives from data-model.md) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T007 Create prerequisites cell referencing Lecture 1 completion in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T008 Add cross-reference introduction: "Як ми бачили у Лекції 1..." in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Notebook skeleton ready with header, objectives, prerequisites.

---

## Phase 3: User Story 1 - Understanding Python's Object Model (Priority: P1)

**Goal**: Students learn that names are references to objects, not containers, and can use id() to inspect identity.

**Independent Test**: Students can predict outcomes of `a = [1,2,3]; b = a; b.append(4)` scenarios.

### Implementation for User Story 1

- [ ] T009 [US1] Create Section 1 markdown header: "1. Імена та Об'єкти (Names and Objects)" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T010 [US1] Write concept explanation: everything is an object, names are references in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T011 [P] [US1] Source or create names-objects diagram in lectures/02-core-mechanics/assets/diagrams/names-objects.png
- [ ] T012 [US1] Add diagram cell referencing assets/diagrams/names-objects.png in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T013 [US1] Create code cell: id() demonstration with integers in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T014 [US1] Create code cell: same object, multiple names (aliasing) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T015 [US1] Create code cell: reassignment creates new binding in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T016 [US1] Add cross-reference to Lecture 1 dynamic typing in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 1 complete - students understand names vs objects.

---

## Phase 4: User Story 2 - Mastering Mutability Concepts (Priority: P1)

**Goal**: Students distinguish mutable from immutable types and can fix mutable default argument bugs.

**Independent Test**: Students can identify and fix mutable default argument bug patterns.

### Implementation for User Story 2

- [ ] T017 [US2] Create Section 2 markdown header: "2. Мутабельність (Mutability)" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T018 [US2] Add mutability meme cell referencing assets/memes/mutability-bug.png in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T019 [US2] Write concept explanation: mutable vs immutable types in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T020 [US2] Create mutability table (list/dict/set vs int/str/tuple) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T021 [US2] Create code cell: modifying list through alias in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T022 [US2] Create code cell: string immutability (.upper() returns new string) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T023 [US2] Create code cell: mutable default argument bug in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T024 [US2] Create code cell: mutable default argument fix using None in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 2 complete - students understand mutability.

---

## Phase 5: User Story 6 - Control Flow Mastery (Priority: P1)

**Goal**: Students use if/elif/else, match statements, for loops, while loops, break, continue effectively.

**Independent Test**: Students can write multi-branch logic and loop patterns correctly.

### Implementation for User Story 6

- [ ] T025 [US6] Create Section 6 markdown header: "6. Керування Потоком (Control Flow)" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T026 [US6] Write subsection 6.1: "Умовні Оператори" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T027 [US6] Create code cell: if/elif/else grade calculation example in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T028 [US6] Write match statement introduction (Python 3.10+) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T029 [US6] Create code cell: match with HTTP status example in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T030 [US6] Create code cell: match with sequence unpacking example in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T031 [US6] Create code cell: match with guard clauses example in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T032 [US6] Write subsection 6.2: "Цикли" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T033 [US6] Create code cell: for loop with range() variations in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T034 [US6] Create code cell: while loop with break in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T035 [US6] Create code cell: for...else search pattern in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T036 [US6] Add reference to enumerate() from Lecture 1 in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 6 complete - students master control flow.

---

## Phase 6: User Story 3 - Memory Representation with Visuals (Priority: P2)

**Goal**: Students understand how Python stores data types in memory through visual diagrams.

**Independent Test**: Students can draw simplified memory diagrams for code snippets.

### Implementation for User Story 3

- [ ] T037 [US3] Create Section 3 markdown header: "3. Представлення в Пам'яті (Memory Representation)" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T038 [P] [US3] Source or create memory-model diagram in lectures/02-core-mechanics/assets/diagrams/memory-model.png
- [ ] T039 [US3] Write concept explanation: PyObject structure, overhead in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T040 [US3] Add diagram cell referencing assets/diagrams/memory-model.png in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T041 [US3] Create code cell: sys.getsizeof() comparison list vs tuple in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T042 [US3] Write explanation: why tuples are more memory-efficient in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 3 complete - students visualize memory.

---

## Phase 7: User Story 4 - Identity vs Equality Mastery (Priority: P2)

**Goal**: Students clearly distinguish `is` (identity) from `==` (equality).

**Independent Test**: Students correctly predict `is` vs `==` outcomes for various types.

### Implementation for User Story 4

- [ ] T043 [US4] Create Section 4 markdown header: "4. Ідентичність vs Рівність (Identity vs Equality)" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T044 [US4] Write concept explanation: is checks identity, == checks equality in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T045 [US4] Create code cell: is vs == with small integers (cached) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T046 [US4] Create code cell: is vs == with large integers (not cached) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T047 [US4] Create code cell: is vs == with lists in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T048 [US4] Create code cell: is None pattern in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T049 [US4] Create code cell: string interning behavior in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T050 [US4] Add warning box: integer caching is CPython detail, never use is for values in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 4 complete - students master is vs ==.

---

## Phase 8: User Story 5 - Truthiness and Comparisons (Priority: P2)

**Goal**: Students understand Python's truthiness rules and write idiomatic conditionals.

**Independent Test**: Students use `if items:` pattern instead of `if len(items) > 0:`.

### Implementation for User Story 5

- [ ] T051 [US5] Create Section 5 markdown header: "5. Істинність (Truthiness)" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T052 [US5] Write concept explanation: falsy values list in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T053 [US5] Create code cell: all falsy values demonstration in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T054 [US5] Create code cell: idiomatic truthiness check pattern in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T055 [US5] Create code cell: comparison chaining (0 < x < 10) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T056 [US5] Create code cell: short-circuit evaluation with and/or in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 5 complete - students write Pythonic conditions.

---

## Phase 9: User Story 7 - Practical Patterns (Priority: P2)

**Goal**: Students apply common loop patterns: counting, searching, accumulating.

**Independent Test**: Students can write search loop with early exit in under 3 minutes.

### Implementation for User Story 7

- [ ] T057 [US7] Create Section 7 markdown header: "7. Практичні Патерни (Practical Patterns)" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T058 [US7] Write concept explanation: common loop patterns in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T059 [US7] Create code cell: counting pattern in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T060 [US7] Create code cell: search with early exit pattern in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T061 [US7] Create code cell: accumulation pattern in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 7 complete - students know common patterns.

---

## Phase 10: User Story 8 - Performance Intuition with Timing (Priority: P3)

**Goal**: Students use basic timing and understand why Python loops can be slow.

**Independent Test**: Students can measure execution time of code blocks.

### Implementation for User Story 8

- [ ] T062 [US8] Create Section 8 markdown header: "8. Вимірювання Часу (Timing)" in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T063 [US8] Add timing meme cell referencing assets/memes/timing-meme.png in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T064 [US8] Write concept explanation: why measure performance in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T065 [US8] Create code cell: time.perf_counter() basic usage in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T066 [US8] Create code cell: Python loop vs sum() comparison in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T067 [US8] Add cross-reference to Lecture 1 bytecode/PVM in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 8 complete - students understand timing basics.

---

## Phase 11: Exercises & Wrap-Up

**Purpose**: Add exercises, summary, references, and finalize notebook

### Exercises

- [ ] T068 Create Exercise 1: "Predict the Output" (mutability, identity) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T069 Create Exercise 1 solution (hidden cell) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T070 Create Exercise 2: "Fix the Bug" (mutable default argument) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T071 Create Exercise 2 solution (hidden cell) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T072 Create Exercise 3: "Control Flow Challenge" (counting/searching) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T073 Create Exercise 3 solution (hidden cell) in lectures/02-core-mechanics/lecture-02.ipynb

### Summary & References

- [ ] T074 Create Summary section with checkmarks per data-model.md in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T075 Create "What's Next" section previewing Lecture 3 in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T076 Create homework assignment section in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T077 Create References section with links from research.md in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: All content complete.

---

## Phase 12: Polish & Validation

**Purpose**: Final review and quality assurance

- [ ] T078 Reorder sections to match data-model.md flow (1-8) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T079 Run Kernel > Restart & Run All to verify all code cells execute in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T080 Verify all images load correctly from assets/ folder in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T081 Review Ukrainian text for grammar and clarity in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T082 Verify English terms in parentheses on first use in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T083 Check constitution compliance: 2 memes, 3+ diagrams, 5+ examples, 2+ exercises in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T084 Verify no content repeated from Lecture 1 (duck typing, bytecode/PVM) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T085 Estimate lecture duration target: 1.5 hours in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Lecture 2 complete and validated.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Phase 1 (Setup)**: No dependencies - can start immediately
- **Phase 2 (Foundational)**: Depends on Phase 1 - BLOCKS all content sections
- **Phases 3-10 (User Stories)**: All depend on Phase 2 completion
  - P1 stories (US1, US2, US6) should be completed first
  - P2 stories (US3, US4, US5, US7) can follow
  - P3 story (US8) is lowest priority
- **Phase 11 (Exercises)**: Depends on all content sections
- **Phase 12 (Polish)**: Depends on all content and exercises

### User Story Dependencies

| Story | Priority | Section | Dependencies |
|-------|----------|---------|--------------|
| US1 | P1 | 1. Names & Objects | Foundation only |
| US2 | P1 | 2. Mutability | US1 (builds on names/objects) |
| US6 | P1 | 6. Control Flow | Foundation only |
| US3 | P2 | 3. Memory | US1 (builds on objects) |
| US4 | P2 | 4. Identity vs Equality | US1, US2 (builds on both) |
| US5 | P2 | 5. Truthiness | Foundation only |
| US7 | P2 | 7. Practical Patterns | US6 (builds on loops) |
| US8 | P3 | 8. Timing | US6 (uses loops for demo) |

### Parallel Opportunities

Within Setup phase:
- T003, T004 (meme sourcing) can run in parallel

Within content phases:
- T011, T038 (diagram sourcing) can run in parallel
- All [P] marked tasks within same phase can run in parallel

---

## Implementation Strategy

### MVP First (P1 Stories Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (header, objectives)
3. Complete Phase 3: US1 - Names & Objects
4. Complete Phase 4: US2 - Mutability
5. Complete Phase 5: US6 - Control Flow
6. **STOP and VALIDATE**: Core content ready for review

### Incremental Delivery

1. Setup + Foundational → Notebook skeleton
2. Add US1 + US2 → Core concepts ready
3. Add US6 → Control flow complete
4. Add US3-US5, US7 → P2 stories complete
5. Add US8 → Full content
6. Add Exercises → Interactive elements
7. Polish → Final validation

### Section Order in Final Notebook

Per data-model.md, final section order should be:
1. Names & Objects (US1)
2. Mutability (US2)
3. Memory Representation (US3)
4. Identity vs Equality (US4)
5. Truthiness (US5)
6. Control Flow (US6)
7. Practical Patterns (US7)
8. Timing (US8)

---

## Notes

- [P] tasks = different files/cells, no dependencies
- [Story] label maps task to specific user story for traceability
- Each section should be independently reviewable
- Verify code cells run without errors after each section
- Commit after each phase completion
- Use constitution checklist at Phase 12 for final validation
