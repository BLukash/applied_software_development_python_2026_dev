# Tasks: Lecture 4 Refinement — Remove OOP & Fix Images

**Input**: Design documents from `/specs/007-lecture4-refinement/`
**Prerequisites**: plan.md (required), spec.md (required), research.md, data-model.md, contracts/modifications.md, quickstart.md

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Notebook**: `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`
- **Assets**: `lectures/04-functions-modules-errors-oop/assets/diagrams/`
- **Memes**: `lectures/04-functions-modules-errors-oop/assets/memes/`
- **Design docs**: `specs/007-lecture4-refinement/`

---

## Phase 1: Setup

**Purpose**: Verify current state before making changes

- [x] T001 Read and analyze the current notebook structure in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: count total cells, identify exact cell indices for OOP Section 5 (cells 54–69), Exercise 4 (cells 79–81), mini-project (cells 82–87), and all cells with OOP references (cells 0, 1, 3, 38, 88, 89, 90). Verify these indices match `contracts/modifications.md`. Reference: data-model.md Cell Map

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Delete OOP asset files and temporary scripts BEFORE modifying the notebook, to avoid referencing deleted content.

- [x] T002 [P] Delete all 14 OOP-related image files from `lectures/04-functions-modules-errors-oop/assets/diagrams/`: `39-4-pillars-of-oop.gif`, `45-encapsulation.webp`, `46-access-modifiers.webp`, `47-inheritance.png`, `49-polymorphism.webp`, `programiz-inheritance2.png`, `programiz-polymorphism.png`, `scaler-abstraction.webp`, `scaler-encapsulation.webp`, `scaler-init.webp`, `scaler-oop.webp`, `scaler-polymorphism.webp`, `scaler-self.webp`, `scaler-super.webp`. Reference: data-model.md Files to DELETE (OOP-related)

- [x] T003 [P] Delete temporary generation files: `lectures/04-functions-modules-errors-oop/download_images.py` and `lectures/04-functions-modules-errors-oop/image_mapping.json`. Reference: data-model.md Files to DELETE (temporary)

**Checkpoint**: OOP assets and temp files removed. Notebook modifications can now begin.

---

## Phase 3: User Story 1 — Remove All OOP Content (Priority: P1)

**Goal**: Remove all OOP content from the notebook. Zero OOP references remain except in "What's Next" section.

**Independent Test**: Search notebook for "ООП", "OOP", "наслідування", "інкапсуляція", "поліморфізм", "абстракція" — no matches except in "What's Next" cell.

### Implementation for User Story 1

- [x] T004 [US1] Delete cells 54–69 (Section 5: all 16 OOP cells) from `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`. These cover sub-topics 5.1 through 5.8 (Why OOP, Classes/__init__/self, Instance vs class attributes, Encapsulation, Inheritance, Polymorphism, Abstraction, Python OOP vs C#/Java/C++). Reference: contracts/modifications.md DELETE Cells 54–69

- [x] T005 [US1] Delete cells 79–81 (Exercise 4: OOP bonus exercise — problem statement, empty code cell, solution `<details>` block) from `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`. After deletion, only 3 exercises remain (Functions, Modules, Errors). Reference: contracts/modifications.md DELETE Cells 79–81

- [x] T006 [US1] Modify cell 0 (Title) in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: Change title from "Лекція 4: Функції (продовження) + Модулі + Помилки + Вступ до ООП" to "Лекція 4: Функції (продовження) + Модулі + Помилки". Remove any other OOP mentions in the title cell. Reference: contracts/modifications.md MODIFY Cell 0

- [x] T007 [US1] Modify cell 1 (Learning Objectives) in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: Remove objective #5 about creating classes, encapsulation, OOP. Keep objectives 1–4 covering lambda/map/filter, modules/imports, exceptions/try-except, and debugging/logging. Renumber if needed. Reference: contracts/modifications.md MODIFY Cell 1

- [x] T008 [US1] Modify cell 3 (Introduction) in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: Remove the line "Вступ до ООП — від функцій до класів" (or similar) from the lecture preview list. Keep all other non-OOP preview items. Reference: contracts/modifications.md MODIFY Cell 3

- [x] T009 [US1] Modify cell 38 (Package structure code example) in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: Replace the `student.py  # class Student` line in the project structure diagram with a non-OOP example like `validators.py  # validation functions`. Reference: contracts/modifications.md MODIFY Cell 38, research.md R1

- [x] T010 [US1] Rewrite the mini-project section (cells 82–87 post-deletion, adjust indices after earlier deletions) in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: Replace "Менеджер оцінок студентів" (Student Grade Manager) with "Конвеєр обробки даних студентів" (Student Data Processing Pipeline). Rewrite all steps: Step 1 — define validation functions (not class), Step 2 — data processing with map/filter/sorted/lambda, Step 3 — error handling with try/except, Step 4 — combine into pipeline. Rewrite the `<details>` solution using only functions + error handling, NO `class` keyword (except `class ValidationError(Exception)`). Reference: contracts/modifications.md REWRITE Cells 82–87, research.md R3

- [x] T011 [US1] Modify the Summary cell in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: Remove all OOP-related takeaways (classes, encapsulation, inheritance, polymorphism, abstraction). Keep takeaways for Functions, Modules, Errors, and Debugging only. Reference: contracts/modifications.md MODIFY Cell 88

- [x] T012 [US1] Modify the "What's Next" cell in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: Update to clearly state that Lecture 5 will cover OOP (об'єктно-орієнтоване програмування) as the primary topic, along with files/JSON/CSV. This is the ONLY cell allowed to mention OOP. Reference: contracts/modifications.md MODIFY Cell 89

- [x] T013 [US1] Modify the References cell in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: Remove all OOP-specific references (Python classes docs, OOP tutorials, inheritance/polymorphism articles). Keep references for functions, modules, exceptions, and debugging. Reference: contracts/modifications.md MODIFY Cell 90

- [x] T014 [US1] Fix section numbering in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: After deleting Section 5 (OOP), verify remaining sections are numbered 1–4 (1. Functions, 2. Modules, 3. Errors, 4. Debugging). Verify exercises section header says "Практичні вправи" with exercises numbered 1–3. Verify mini-project section numbering is correct. Reference: spec.md FR-014

- [x] T015 [US1] Run OOP-reference audit on `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: Search entire notebook for "ООП", "OOP", "наслідування", "інкапсуляція", "поліморфізм", "абстракція", "class " (with space, excluding `class ValidationError` and `first-class`). Verify zero matches outside the "What's Next" cell. Fix any remaining references found. Reference: spec.md SC-001, quickstart.md Step 1

**Checkpoint**: All OOP content removed. Notebook covers only Functions + Modules + Errors + Debugging. Exercises are 1–3. Mini-project uses functions only.

---

## Phase 4: User Story 2 — Fix All Broken Image URLs (Priority: P1)

**Goal**: Every image in the notebook uses a local file path and renders correctly. No remote URLs remain.

**Independent Test**: Run image validation script from quickstart.md Step 2 — zero broken images, zero remote URLs.

### Implementation for User Story 2

- [x] T016 [US2] Audit all remaining image references in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb` after OOP removal: extract every `![alt](url)`, classify each as (a) already has local file in `assets/diagrams/`, (b) needs new download, or (c) needs text-diagram fallback. Document the mapping of each image slot to its local file. Reference: research.md R2

- [x] T017 [US2] Search and download replacement images for the ~20 missing non-OOP image slots. Use Scaler Topics, Programiz, EmbeddedInventor, TutorialsPoint, W3Schools, or Wikimedia Commons. Save to `lectures/04-functions-modules-errors-oop/assets/diagrams/` with descriptive filenames. Priority topics: S1.5 closures, S1.7 type hints (2), S1.8 docstrings, S2.1–S2.4 modules/imports/packages (8), S3.2–S3.4 errors (5), S4.1–S4.2 debugging/logging (2). Reference: research.md R2 coverage gaps

- [x] T018 [US2] For any sub-topics where no downloadable image was found in T017, create inline text-based markdown diagrams (tables, ASCII art, formatted code blocks) directly in the markdown cells of `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`. Each sub-topic MUST have at least 2 visuals (image or text diagram). Reference: research.md R2 strategy item 4, spec.md FR-007

- [x] T019 [US2] Find or create 2 memes for `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: (1) a programming/functions meme for the Introduction cell (cell 3), (2) a scope/closure meme for the LEGB section (cell 18). Download to `lectures/04-functions-modules-errors-oop/assets/memes/` or `assets/diagrams/`. Verify at least 2 memes total exist in the notebook. Reference: contracts/modifications.md Meme Requirements, spec.md FR-008

- [x] T020 [US2] Replace ALL remote image URLs in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb` with local relative paths. Every `![alt](https://...)` becomes `![alt](assets/diagrams/filename.ext)` or `![alt](assets/memes/filename.ext)`. Ensure attribution captions (`*Джерело: [Site](URL)*`) remain with source name. Reference: spec.md FR-006, contracts/modifications.md Image Modifications

- [x] T021 [US2] Validate all image paths in `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: run the validation script from quickstart.md Step 2 to confirm (1) zero remote URLs, (2) all local paths point to existing files, (3) each sub-topic has at least 2 visuals. Reference: quickstart.md Step 2, spec.md SC-002, SC-003

**Checkpoint**: All images render locally. Zero remote URLs. Every sub-topic has 2+ visuals. 2+ memes present.

---

## Phase 5: User Story 3 — Clean Up & Validate (Priority: P2)

**Goal**: No orphaned assets, no temp files, consistent formatting, all cells execute cleanly.

**Independent Test**: Run quickstart.md Steps 3–5. Zero errors, zero orphaned files, constitution compliance confirmed.

### Implementation for User Story 3

- [x] T022 [US3] Verify no orphaned image files remain in `lectures/04-functions-modules-errors-oop/assets/diagrams/`: cross-reference every file in the directory against image references in the notebook. Delete any files not referenced by any cell. Reference: spec.md FR-009

- [x] T023 [US3] Verify `lectures/04-functions-modules-errors-oop/assets/memes/` directory exists and contains at least the meme files referenced in the notebook. Create the directory if it doesn't exist. Reference: plan.md Project Structure

- [x] T024 [US3] Review the complete notebook `lectures/04-functions-modules-errors-oop/lecture-04.ipynb` for consistency: (1) section numbering is sequential (1–4), (2) Ukrainian text uses consistent terminology matching Lectures 1–3, (3) English technical terms appear in parentheses on first use, (4) no excessive icons/emojis (1-2 per section max), (5) `<details>` solution blocks work correctly for all 3 exercises and mini-project. Reference: spec.md FR-014, FR-015, quickstart.md Step 5

- [x] T025 [US3] Final validation of `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`: (1) verify all code cells can execute without errors using only standard library, (2) run the OOP-reference audit one final time (quickstart.md Step 1), (3) run the image validation check (quickstart.md Step 2), (4) verify total cell count is ~70 (91 - 16 OOP - 3 Exercise 4 = 72), (5) count visuals per sub-topic (min 2 each), (6) verify 2+ memes. Reference: quickstart.md Steps 1–5, spec.md SC-001 through SC-006

**Checkpoint**: Notebook is production-ready. All success criteria met.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately
- **Foundational (Phase 2)**: Depends on T001 (state verification) — DELETE OOP assets + temp files
- **US1 — OOP Removal (Phase 3)**: Depends on Phase 2 — modify notebook cells
- **US2 — Image Fixing (Phase 4)**: Depends on Phase 3 — must know final cell structure after OOP removal
- **US3 — Cleanup (Phase 5)**: Depends on Phases 3 and 4 — validate final state

### Within Each User Story

- **US1**: T004 (delete OOP section) → T005 (delete exercise) → T006–T013 (modify individual cells) → T014 (fix numbering) → T015 (audit)
- **US2**: T016 (audit images) → T017 (download) → T018 (text diagrams) → T019 (memes) → T020 (replace URLs) → T021 (validate)
- **US3**: T022 (orphan check) → T023 (memes dir) → T024 (review) → T025 (final validation)

### Parallel Opportunities

- T002 and T003 can run in parallel (different files/directories)
- T006 through T013 modify different cells but same file — run sequentially
- T022 and T023 can run in parallel (different directories)

---

## Implementation Strategy

### MVP First (US1 Only)

1. Complete Phase 1: Verify state
2. Complete Phase 2: Delete OOP assets + temp files
3. Complete Phase 3: Remove all OOP content
4. **STOP and VALIDATE**: Search for OOP references
5. Notebook is usable (no OOP) but images still broken

### Full Delivery

1. Setup + Foundational → Assets cleaned
2. US1 (OOP removal) → Notebook structure finalized
3. US2 (Image fixing) → All visuals working
4. US3 (Cleanup + validation) → Production-ready

---

## Notes

- All tasks modify the same file: `lectures/04-functions-modules-errors-oop/lecture-04.ipynb`
- Cell indices in T004, T005 refer to the ORIGINAL notebook (91 cells). After T004 deletes 16 cells, subsequent cell indices shift. The implementation must account for this by either: (a) deleting from bottom to top, or (b) re-reading cell indices after each deletion.
- `class ValidationError(Exception)` in error handling cells is NOT OOP — it's exception handling syntax. Do not remove.
- "first-class objects" in cell 7 is about first-class functions, NOT OOP. Do not modify.
- Directory name `04-functions-modules-errors-oop` is kept as-is to avoid breaking existing references.
- Total estimated tasks: 25
- Commit after each completed phase
