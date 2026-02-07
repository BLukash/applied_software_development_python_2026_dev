# Tasks: Lecture 2 Content Restructuring

**Input**: Design documents from `/specs/004-lecture2-restructure/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/sections.md, quickstart.md

**Tests**: Manual validation only (no automated tests required for educational content restructuring)

**Organization**: Tasks are grouped to enable independent implementation of each section change while maintaining notebook integrity.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different cells, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1-US6)
- All paths relative to repository root

## Path Conventions

- **Target file**: `lectures/02-core-mechanics/lecture-02.ipynb`
- **Backup file**: `lectures/02-core-mechanics/lecture-02.backup.ipynb`
- **Design docs**: `specs/004-lecture2-restructure/`

---

## Phase 1: Setup (Preparation)

**Purpose**: Backup and verify current notebook state before restructuring

- [x] T001 Create backup copy of lecture-02.ipynb to lecture-02.backup.ipynb in lectures/02-core-mechanics/
- [x] T002 Open lecture-02.ipynb and run all cells (Kernel → Restart & Run All) to verify current state works
- [x] T003 Fix any errors in current notebook before proceeding (if any found in T002)

**Checkpoint**: Notebook backed up and verified working

---

## Phase 2: Foundational (Section Order Mapping)

**Purpose**: Document current cell positions for restructuring reference

**⚠️ CRITICAL**: Complete cell mapping before any moves to prevent confusion

- [x] T004 Document exact cell IDs for Names & Objects section (cells 4-10) in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T005 [P] Document exact cell IDs for Mutability section (cells 11-17) in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T006 [P] Document exact cell IDs for Memory Representation section (cells 18-21) in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T007 [P] Document exact cell IDs for Identity vs Equality section (cells 22-29) in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: All cell positions documented - restructuring can begin

---

## Phase 3: User Story 3 - Complex Data Types Introduction (Priority: P1) 🎯 MVP

**Goal**: Create new Section 4 introducing list, dict, set, tuple before Mutability

**Independent Test**: Students can create basic lists/dicts and explain their basic purpose after this section

**Why first**: Creating new content is safer than moving existing content. Does not affect other cells.

### Implementation for User Story 3

- [x] T008 [US3] Create markdown cell for Section 4 header with transition text from contracts/sections.md in lectures/02-core-mechanics/lecture-02.ipynb (insert after current Identity section cells)
- [x] T009 [US3] Create markdown cell with type overview table (list, tuple, dict, set) in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T010 [US3] Create code cell demonstrating list and tuple creation with type() output in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T011 [US3] Create code cell demonstrating dict and set creation with type() output in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T012 [US3] Create markdown cell with "Чому це важливо зараз?" conclusion and Lecture 3 reference in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T013 [US3] Run new Section 4 cells to verify code executes correctly in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 4 (Complex Data Types) is complete and runnable

---

## Phase 4: User Story 1 - Progressive Learning Flow - Memory Move (Priority: P1)

**Goal**: Move Memory Representation section immediately after Names & Objects

**Independent Test**: Students report the Names → Memory transition feels natural

### Implementation for User Story 1 (Memory Section)

- [x] T014 [US1] Add transition text markdown cell before Memory Representation section header in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T015 [US1] Cut cells 18-21 (Memory Representation) and paste after Names & Objects section (after cell 10) in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T016 [US1] Update section number from "3" to "2" in Memory Representation header in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T017 [US1] Run moved Memory cells to verify code still executes correctly in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Memory Representation now immediately follows Names & Objects

---

## Phase 5: User Story 2 - Simple Types Identity vs Equality (Priority: P1)

**Goal**: Keep only simple type examples (int, str, None) in Identity section

**Independent Test**: Students can explain `is` vs `==` on simple types before seeing list examples

### Implementation for User Story 2

- [x] T018 [US2] Update Identity section header to "3. Ідентичність vs Рівність: Прості Типи" in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T019 [US2] Add transition text connecting Memory Representation to Identity section in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T020 [US2] Identify cell 26 (list comparison example) for removal/move - do NOT delete yet, mark for Section 6 in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T021 [US2] Verify remaining cells (22-25, 27-29) contain only simple type examples in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T022 [US2] Run Identity (Simple Types) cells to verify code executes correctly in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Identity section now covers only simple types

---

## Phase 6: User Story 4 - Mutability After Data Type Knowledge (Priority: P1)

**Goal**: Move Mutability section after Complex Data Types introduction

**Independent Test**: Students understand mutability examples without asking "what is a list?"

### Implementation for User Story 4

- [x] T023 [US4] Add transition text connecting Complex Data Types to Mutability section in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T024 [US4] Cut cells 11-17 (Mutability) and paste after Section 4 (Complex Data Types) in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T025 [US4] Update section number to "5" in Mutability header in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T026 [US4] Add note "Деталі роботи з цими типами — у Лекції 3" to Mutability section in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T027 [US4] Run moved Mutability cells to verify code executes correctly in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Mutability now follows Complex Data Types

---

## Phase 7: User Story 5 - Identity vs Equality on Lists (Priority: P2)

**Goal**: Create new Section 6 with list identity/equality examples after Mutability

**Independent Test**: Students understand aliasing and copy behavior with `is` vs `==` on lists

### Implementation for User Story 5

- [x] T028 [US5] Create markdown cell for Section 6 header with transition text in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T029 [US5] Move list aliasing example from Names section (cells 9-10) to Section 6 in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T030 [US5] Move list comparison example (cell 26) from old Identity section to Section 6 in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T031 [US5] Create NEW code cell for copy example (original.copy() demonstration) per contracts/sections.md in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T032 [US5] Create markdown summary cell with "when to use is vs ==" table per contracts/sections.md in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T033 [US5] Run all Section 6 cells to verify code executes correctly in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Section 6 (Identity/Lists) is complete with aliasing, comparison, and copy examples

---

## Phase 8: User Story 1 - Names & Objects Modification (Priority: P1)

**Goal**: Remove list aliasing from Names section (now in Section 6), replace with integer rebinding

**Independent Test**: Names section demonstrates core concept without introducing lists prematurely

### Implementation for User Story 1 (Names Section)

- [x] T034 [US1] Delete or modify cells 9-10 (list aliasing now moved to Section 6) in Names section in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T035 [US1] Replace list aliasing with integer rebinding example per contracts/sections.md in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T036 [US1] Run Names & Objects section cells to verify code executes correctly in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Names section no longer introduces lists prematurely

---

## Phase 9: User Story 6 - Remaining Topics Unchanged (Priority: P2)

**Goal**: Renumber sections 7-10 and verify unchanged content

**Independent Test**: Truthiness, Control Flow, Timing content matches original spec exactly

### Implementation for User Story 6

- [x] T037 [P] [US6] Update Truthiness section number to "7" in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T038 [P] [US6] Update Control Flow section number to "8" in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T039 [P] [US6] Update Practical Patterns section number to "9" in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T040 [P] [US6] Update Timing section number to "10" in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T041 [US6] Verify all code in sections 7-10 still executes correctly in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Sections 7-10 renumbered with content unchanged

---

## Phase 10: User Story 1 - Summary and Final Updates (Priority: P1)

**Goal**: Update Summary section to reflect new order and verify complete flow

**Independent Test**: Summary bullet points match restructured section order

### Implementation for User Story 1 (Summary)

- [x] T042 [US1] Update Summary section bullet points to new order per contracts/sections.md in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T043 [US1] Verify Learning Objectives still align with restructured content in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T044 [US1] Update "What's Next" section to mention Lecture 3 detailed complex types coverage in lectures/02-core-mechanics/lecture-02.ipynb

**Checkpoint**: Summary reflects new structure

---

## Phase 11: Polish & Validation

**Purpose**: Final validation across all sections

- [x] T045 Run all cells in notebook (Kernel → Restart & Run All) to verify complete notebook works in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T046 Verify all 5 transition texts are present and read naturally in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T047 Verify 2 memes still present (mutability-bug.png, timing-meme.png) in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T048 Verify Ukrainian text with English terms in parentheses maintained throughout in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T049 Verify no content duplication with Lecture 1 in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T050 Verify Complex Types section has explicit Lecture 3 reference in lectures/02-core-mechanics/lecture-02.ipynb
- [x] T051 Estimate lecture duration (target: ~90 minutes) in lectures/02-core-mechanics/lecture-02.ipynb
- [ ] T052 Delete backup file lecture-02.backup.ipynb after successful validation in lectures/02-core-mechanics/

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - must complete first
- **Foundational (Phase 2)**: Depends on Setup - documents cell positions
- **US3 Complex Types (Phase 3)**: Depends on Foundational - creates new section first
- **US1 Memory Move (Phase 4)**: Depends on Phase 2 - moves existing content
- **US2 Simple Identity (Phase 5)**: Depends on Phase 4 - modifies existing section
- **US4 Mutability (Phase 6)**: Depends on Phase 3 - moves after Complex Types
- **US5 List Identity (Phase 7)**: Depends on Phase 5, Phase 6 - creates new section with moved content
- **US1 Names Modify (Phase 8)**: Depends on Phase 7 - cleans up source section
- **US6 Renumber (Phase 9)**: Depends on Phase 8 - final section numbering
- **US1 Summary (Phase 10)**: Depends on Phase 9 - reflects final structure
- **Polish (Phase 11)**: Depends on all phases - final validation

### User Story Dependencies

| Story | Depends On | Can Parallel With |
|-------|------------|-------------------|
| US3 (Complex Types) | Phase 2 | None (creates new content) |
| US1 (Memory Move) | Phase 2 | US3 |
| US2 (Simple Identity) | US1 Memory | None |
| US4 (Mutability) | US3 | US2 |
| US5 (List Identity) | US2, US4 | None |
| US1 (Names Modify) | US5 | None |
| US6 (Renumber) | US1 Names | None |
| US1 (Summary) | US6 | None |

### Parallel Opportunities

Within Phase 2 (Foundational):
```
T005, T006, T007 can run in parallel - documenting different sections
```

Within Phase 9 (Renumber):
```
T037, T038, T039, T040 can run in parallel - different section headers
```

---

## Implementation Strategy

### MVP First (Progressive Flow)

1. Complete Phase 1-2: Setup and cell mapping
2. Complete Phase 3: Create Complex Data Types section (US3)
3. Complete Phase 4: Move Memory Representation (US1)
4. **STOP and VALIDATE**: Test flow from Names → Memory → Identity

### Incremental Delivery

1. Setup + Foundational → Ready to restructure
2. Add Complex Types → New section exists
3. Move Memory → First restructure complete
4. Split Identity → Simple types isolated
5. Move Mutability → Section order correct
6. Create List Identity → All new sections complete
7. Clean Names section → Source cleaned
8. Renumber + Summary → Complete restructure

---

## Notes

- All tasks modify single file: `lectures/02-core-mechanics/lecture-02.ipynb`
- [P] tasks = can run in parallel (different cells, no dependencies)
- [Story] label maps task to specific user story for traceability
- Create backup FIRST (T001) - enables rollback if needed
- Execute cell moves carefully - Jupyter cell IDs may shift during editing
- Run cells after each section change to catch errors early
- Constitution requirements: Ukrainian text, 2 memes, English terms in parentheses
