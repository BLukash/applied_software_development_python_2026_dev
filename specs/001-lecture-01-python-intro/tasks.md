# Tasks: Лекція 1 — Вступ до Python

**Input**: Design documents from `/specs/001-lecture-01-python-intro/`
**Prerequisites**: plan.md, spec.md, lecture-structure.md, research.md, quickstart.md

**Tests**: Not applicable for educational content. Validation is done via notebook execution and content review.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story's content.

## Format: `[ID] [P?] [Story?] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

```text
lectures/01-python-intro/
├── lecture-01.ipynb         # Main notebook
├── assets/
│   ├── memes/               # Meme images
│   └── diagrams/            # Visual aids
├── exercises/               # Exercise starter files
└── solutions/               # Exercise solutions
```

---

## Phase 1: Setup (Directory Structure)

**Purpose**: Create lecture folder structure and initialize notebook

- [x] T001 Create directory structure in lectures/01-python-intro/ (lecture-01.ipynb, assets/memes/, assets/diagrams/, exercises/, solutions/)
- [x] T002 Initialize empty Jupyter notebook at lectures/01-python-intro/lecture-01.ipynb
- [x] T003 [P] Create placeholder files for exercises (exercises/exercise-01.py, exercises/exercise-02.py)
- [x] T004 [P] Create placeholder files for solutions (solutions/solution-01.py, solutions/solution-02.py)

**Checkpoint**: Directory structure ready, empty notebook created

---

## Phase 2: Foundational (Notebook Header & Structure)

**Purpose**: Create notebook skeleton with all required sections

**⚠️ CRITICAL**: Must complete before adding content to any section

- [x] T005 Add Cell 1: Header markdown (lecture title, course, date, duration) in lectures/01-python-intro/lecture-01.ipynb
- [x] T006 Add Cell 2: Learning Objectives markdown (5 objectives as per lecture-structure.md) in lectures/01-python-intro/lecture-01.ipynb
- [x] T007 Add Cell 3: Prerequisites markdown in lectures/01-python-intro/lecture-01.ipynb
- [x] T008 Add section headers for all 8 sections (What is Python, Environment Setup, Running Code, venv & pip, Basic Syntax, Exercises, Summary, References) in lectures/01-python-intro/lecture-01.ipynb

**Checkpoint**: Notebook skeleton with all section markers ready

---

## Phase 3: User Story 2 - Python Ecosystem Understanding (Priority: P2)

**Goal**: Student understands Python history, philosophy, and use cases

**Independent Test**: Student can explain 3 key Python features and name 3 use cases

### Visual Assets for US2

- [x] T009 [P] [US2] Create or source meme for Python naming (Monty Python vs snake) and save to lectures/01-python-intro/assets/memes/python-naming.png
- [x] T010 [P] [US2] Create history timeline table as image in lectures/01-python-intro/assets/diagrams/python-timeline.png

### Content for US2

- [x] T011 [US2] Add Cell 4: "Що таке Python?" introduction with meme reference in lectures/01-python-intro/lecture-01.ipynb
- [x] T012 [US2] Add Cell 5: Python history table (1991-2024) in lectures/01-python-intro/lecture-01.ipynb
- [x] T013 [US2] Add Cell 6: "Де використовується Python?" with use cases table in lectures/01-python-intro/lecture-01.ipynb
- [x] T014 [US2] Add Cell 7: Code cell with `import this` (Zen of Python) in lectures/01-python-intro/lecture-01.ipynb

**Checkpoint**: Section 1 complete - student can learn about Python ecosystem

---

## Phase 4: User Story 1 - Environment Setup (Priority: P1) 🎯 MVP

**Goal**: Student can install Python, set up IDE, create venv, and run first script

**Independent Test**: Student installs Python, creates venv, runs print("Hello, World!")

### Visual Assets for US1

- [x] T015 [P] [US1] Create or source meme for venv ("Works on my machine" theme) and save to lectures/01-python-intro/assets/memes/works-on-my-machine.png

### Section 2: Environment Setup

- [x] T016 [US1] Add Cell 8: Installation guide for Windows, macOS, Linux in lectures/01-python-intro/lecture-01.ipynb
- [x] T017 [US1] Add Cell 9: IDE setup guide (VS Code, PyCharm) with extensions list in lectures/01-python-intro/lecture-01.ipynb

### Section 3: Running Code

- [x] T018 [US1] Add Cell 10: Comparison table (REPL vs Script vs Notebook) in lectures/01-python-intro/lecture-01.ipynb
- [x] T019 [US1] Add Cell 11: REPL introduction markdown in lectures/01-python-intro/lecture-01.ipynb
- [x] T020 [US1] Add Cell 12: REPL example code cell in lectures/01-python-intro/lecture-01.ipynb
- [x] T021 [US1] Add Cell 13-14: Script demo (markdown + code) in lectures/01-python-intro/lecture-01.ipynb
- [x] T022 [US1] Add Cell 15: Notebook explanation markdown in lectures/01-python-intro/lecture-01.ipynb

### Section 4: venv & pip

- [x] T023 [US1] Add Cell 16: Why venv? explanation with meme reference in lectures/01-python-intro/lecture-01.ipynb
- [x] T024 [US1] Add Cell 17: venv commands for all platforms (create, activate, deactivate) in lectures/01-python-intro/lecture-01.ipynb
- [x] T025 [US1] Add Cell 18: pip commands (install, list, freeze, requirements.txt) in lectures/01-python-intro/lecture-01.ipynb

**Checkpoint**: Sections 2-4 complete - student can set up full environment

---

## Phase 5: User Story 3 - Basic Syntax (Priority: P1)

**Goal**: Student learns variables, types, operators, and f-strings through examples

**Independent Test**: Student writes script with input(), print(), and f-strings

### Section 5: Basic Syntax Content

- [x] T026 [US3] Add Cell 19: First program introduction markdown in lectures/01-python-intro/lecture-01.ipynb
- [x] T027 [US3] Add Cell 20: Hello World code example (print Ukrainian and English) in lectures/01-python-intro/lecture-01.ipynb
- [x] T028 [US3] Add Cell 21: Variables introduction markdown in lectures/01-python-intro/lecture-01.ipynb
- [x] T029 [US3] Add Cell 22: Variables example code (str, float, int, bool, None with type()) in lectures/01-python-intro/lecture-01.ipynb
- [x] T030 [US3] Add Cell 23: Data types comparison table (int, float, str, bool, None) in lectures/01-python-intro/lecture-01.ipynb
- [x] T031 [US3] Add Cell 24-25: Input/Output section (markdown + input() example) in lectures/01-python-intro/lecture-01.ipynb
- [x] T032 [US3] Add Cell 26-27: Operators section (markdown + arithmetic operators example) in lectures/01-python-intro/lecture-01.ipynb
- [x] T033 [US3] Add Cell 28-29: F-strings section (markdown + formatting examples) in lectures/01-python-intro/lecture-01.ipynb

**Checkpoint**: Section 5 complete - student understands basic syntax

---

## Phase 6: Exercises (All Stories)

**Goal**: Practical exercises that test all three user stories

### Exercise 1: Greeting Program (tests US1 + US3)

- [x] T034 [P] Add Cell 30: Exercise 1 instructions markdown in lectures/01-python-intro/lecture-01.ipynb
- [x] T035 [P] Add Cell 31: Exercise 1 starter code cell in lectures/01-python-intro/lecture-01.ipynb
- [x] T036 Add Cell 32: Exercise 1 solution (hidden cell) in lectures/01-python-intro/lecture-01.ipynb
- [x] T037 [P] Create exercises/exercise-01.py with starter code and instructions in lectures/01-python-intro/exercises/exercise-01.py
- [x] T038 [P] Create solutions/solution-01.py with complete solution in lectures/01-python-intro/solutions/solution-01.py

### Exercise 2: Simple Calculator (tests US3)

- [x] T039 [P] Add Cell 33: Exercise 2 instructions markdown in lectures/01-python-intro/lecture-01.ipynb
- [x] T040 [P] Add Cell 34: Exercise 2 starter code cell in lectures/01-python-intro/lecture-01.ipynb
- [x] T041 Add Cell 35: Exercise 2 solution (hidden cell) in lectures/01-python-intro/lecture-01.ipynb
- [x] T042 [P] Create exercises/exercise-02.py with starter code and instructions in lectures/01-python-intro/exercises/exercise-02.py
- [x] T043 [P] Create solutions/solution-02.py with complete solution in lectures/01-python-intro/solutions/solution-02.py

**Checkpoint**: Section 6 complete - students can practice independently

---

## Phase 7: Polish & Finalization

**Purpose**: Complete remaining sections and validate all content

### Summary & References

- [x] T044 Add Cell 36: Summary section with checkmarks for all topics in lectures/01-python-intro/lecture-01.ipynb
- [x] T045 Add Cell 37: "What's Next" preview of Lecture 2 + homework in lectures/01-python-intro/lecture-01.ipynb
- [x] T046 Add Cell 38: References section with all links (official docs, Real Python, Corey Schafer) in lectures/01-python-intro/lecture-01.ipynb

### Validation

- [x] T047 Run all code cells in notebook to verify they execute without errors in lectures/01-python-intro/lecture-01.ipynb
- [x] T048 Verify all meme images display correctly in notebook
- [x] T049 Test all links in References section work
- [x] T050 Review Ukrainian text for grammar and terminology consistency
- [x] T051 Verify notebook loads and runs in clean Python 3.11+ environment

**Checkpoint**: Lecture complete and validated

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Phase 1 completion
- **User Stories (Phase 3-5)**: All depend on Phase 2 completion
  - US2 (Python ecosystem) can run in parallel with US1/US3
  - US1 (Environment setup) should complete before exercises
  - US3 (Basic syntax) should complete before exercises
- **Exercises (Phase 6)**: Depends on US1 and US3 completion
- **Polish (Phase 7)**: Depends on all content phases being complete

### User Story Dependencies

- **User Story 2 (P2)**: Independent - can start after Phase 2
- **User Story 1 (P1)**: Independent - can start after Phase 2
- **User Story 3 (P1)**: Independent - can start after Phase 2
- **Exercises**: Depend on US1 and US3 content being complete

### Within Each Phase

- Markdown cells before related code cells
- Visual assets can be created in parallel with content
- Solutions depend on exercise starters being defined

### Parallel Opportunities

- T003, T004: Exercise and solution placeholders (parallel)
- T009, T010: US2 visual assets (parallel)
- T034, T035, T037, T038: Exercise 1 components (parallel)
- T039, T040, T042, T043: Exercise 2 components (parallel)

---

## Parallel Example: Phase 6 Exercises

```bash
# Launch all Exercise 1 tasks together:
Task: "Add Cell 30: Exercise 1 instructions"
Task: "Add Cell 31: Exercise 1 starter code"
Task: "Create exercises/exercise-01.py"
Task: "Create solutions/solution-01.py"

# Launch all Exercise 2 tasks together:
Task: "Add Cell 33: Exercise 2 instructions"
Task: "Add Cell 34: Exercise 2 starter code"
Task: "Create exercises/exercise-02.py"
Task: "Create solutions/solution-02.py"
```

---

## Implementation Strategy

### MVP First (Environment Setup - US1)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational
3. Complete Phase 4: User Story 1 (Environment Setup)
4. **STOP and VALIDATE**: Test environment setup instructions work
5. Student can install Python and run first script

### Incremental Delivery

1. Setup + Foundational → Notebook skeleton ready
2. Add US1 (Environment Setup) → Students can set up Python
3. Add US2 (Python Ecosystem) → Students understand context
4. Add US3 (Basic Syntax) → Students learn fundamentals
5. Add Exercises → Students can practice
6. Add Polish → Lecture complete

### Content Creation Strategy

For each section:
1. Create markdown cells first (explanations)
2. Add code cells with examples
3. Test code cells execute correctly
4. Add visual elements (memes, diagrams)
5. Review Ukrainian text quality

---

## Notes

- [P] tasks = different files or independent cells, no dependencies
- [Story] label maps content to user story for traceability
- All code examples from lecture-structure.md - copy verbatim
- Memes should be educational-appropriate and relevant
- Test notebook in clean environment before marking complete
- Commit after each phase completion
