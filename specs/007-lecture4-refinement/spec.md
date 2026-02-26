# Feature Specification: Lecture 4 Refinement — Remove OOP & Fix Images

**Feature Branch**: `007-lecture4-refinement`
**Created**: 2026-02-18
**Status**: Draft
**Input**: User description: "Refine lecture 4, delete all related to OOP from the end of it, make sure not to leave any garbage assets or like this, review what is not ready for it and enhance where needed"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Remove All OOP Content from Lecture 4 (Priority: P1)

A course instructor opens Lecture 4 and expects it to cover only Functions (continued), Modules, and Errors/Debugging — with zero OOP references. The title, learning objectives, main content, exercises, mini-project, and summary must all be updated to reflect this narrower scope. OOP is fully deferred to Lecture 5.

**Why this priority**: OOP content must be removed before any other cleanup can proceed — it determines the notebook's final scope, cell count, image count, and exercise list.

**Independent Test**: Open the notebook and search for "ООП", "OOP", "клас", "class ", "наслідування", "інкапсуляція", "поліморфізм", "абстракція". No matches should appear in any markdown or code cell (except brief mentions in the "What's Next" preview of Lecture 5).

**Acceptance Scenarios**:

1. **Given** the current notebook has Section 5 (cells 54–69) covering OOP, **When** the refinement is applied, **Then** all 16 OOP cells are removed
2. **Given** Exercise 4 (cells 79–81) is an OOP bonus exercise, **When** the refinement is applied, **Then** Exercise 4 is removed entirely
3. **Given** the mini-project (cells 82–87) uses a Student class with OOP, **When** the refinement is applied, **Then** the mini-project is rewritten to use only functions, modules, and error handling (no classes)
4. **Given** the title cell says "Вступ до ООП", **When** the refinement is applied, **Then** the title reads "Функції (продовження) + Модулі + Помилки" with no OOP mention
5. **Given** learning objectives mention OOP, **When** the refinement is applied, **Then** objectives cover only functions, modules, errors, and debugging
6. **Given** the summary mentions OOP takeaways, **When** the refinement is applied, **Then** summary lists only non-OOP topics
7. **Given** "What's Next" previews Lecture 5 topics, **When** the refinement is applied, **Then** it clearly states OOP will be introduced in Lecture 5

---

### User Story 2 - Fix All Broken Image URLs with Local Assets (Priority: P1)

A student opens Lecture 4 and expects every visual to render correctly. Currently ~44 out of 54 images are broken (403 Forbidden from Real Python, GeeksforGeeks, etc.). All images must be downloaded locally to `assets/diagrams/` and referenced via local relative paths.

**Why this priority**: Broken images severely degrade the learning experience. This is equally critical as removing OOP since the notebook is currently unusable with most visuals missing.

**Independent Test**: Open the notebook in Jupyter and verify every `![alt](path)` image renders. No remote URLs should remain — all images use local `assets/diagrams/` or `assets/memes/` paths.

**Acceptance Scenarios**:

1. **Given** the notebook currently has 54 remote image URLs, **When** the refinement is applied, **Then** all remaining non-OOP images use local file paths
2. **Given** OOP sections are removed, **When** counting remaining image slots, **Then** each surviving sub-topic has at least 2 visuals
3. **Given** some images cannot be downloaded from their original source, **When** the refinement is applied, **Then** alternative images from open educational sources are found, or text-based markdown diagrams are used as fallback
4. **Given** local images are stored in `assets/diagrams/`, **When** referenced in notebook, **Then** paths use relative format `assets/diagrams/filename.ext`
5. **Given** each image has attribution, **When** the refinement is applied, **Then** attribution captions remain with source site name

---

### User Story 3 - Clean Up Garbage Files and Validate (Priority: P2)

After OOP removal and image fixing, the instructor verifies the notebook is clean: no orphaned assets, no temporary scripts, no broken references, and proper section numbering.

**Why this priority**: Cleanup ensures a professional, production-ready notebook without leftover artifacts from the development process.

**Independent Test**: Run `ls assets/diagrams/` and verify every file is referenced in the notebook. Check that no temporary files (`download_images.py`, `image_mapping.json`, `generate_notebook.py`) remain. Verify section numbering is sequential.

**Acceptance Scenarios**:

1. **Given** OOP images were downloaded to `assets/diagrams/`, **When** OOP content is removed, **Then** unused OOP image files are deleted from the assets directory
2. **Given** temporary scripts exist (`download_images.py`, `image_mapping.json`), **When** the refinement is applied, **Then** these files are removed
3. **Given** sections were numbered 1–5 with Section 5 being OOP, **When** OOP is removed, **Then** remaining sections are renumbered (1. Functions, 2. Modules, 3. Errors, 4. Debugging) followed by Exercises and Mini-Project
4. **Given** the notebook directory name contains "oop" (`04-functions-modules-errors-oop`), **When** the refinement is applied, **Then** the directory name is evaluated for consistency (keep as-is if renaming would break existing references, or rename if clean)

---

### Edge Cases

- What happens if a sub-topic has fewer than 2 downloadable images? Use a text-based markdown diagram as fallback to meet the minimum 2 visuals requirement.
- What happens if some images reference OOP but also relate to general concepts (e.g., "4 Pillars of OOP")? Remove them — they belong to Lecture 5.
- What happens if the mini-project still uses class-like patterns (e.g., dicts acting as objects)? This is acceptable as long as no `class` keyword or OOP terminology is used.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The notebook title MUST NOT reference OOP ("Вступ до ООП" or similar)
- **FR-002**: Learning objectives MUST cover only functions, modules, errors, and debugging (4 topics, no OOP)
- **FR-003**: Section 5 (OOP, cells 54–69) MUST be completely removed
- **FR-004**: Exercise 4 (OOP bonus) MUST be completely removed; remaining exercises renumbered
- **FR-005**: The mini-project MUST be rewritten to integrate functions + modules + errors without using classes or OOP concepts
- **FR-006**: All image references MUST use local relative paths (`assets/diagrams/` or `assets/memes/`)
- **FR-007**: Each non-OOP sub-topic MUST have at least 2 visuals (internet-sourced, downloaded locally)
- **FR-008**: At least 2 memes MUST remain in the notebook (constitution requirement)
- **FR-009**: All unused image files in `assets/diagrams/` MUST be deleted (no orphaned assets)
- **FR-010**: All temporary/generation scripts (`download_images.py`, `image_mapping.json`) MUST be removed
- **FR-011**: The summary section MUST list only non-OOP takeaways
- **FR-012**: The "What's Next" section MUST clearly preview OOP as a Lecture 5 topic
- **FR-013**: All code cells MUST execute without errors using only standard library modules
- **FR-014**: Section numbering MUST be sequential and consistent after OOP removal
- **FR-015**: The notebook MUST maintain Ukrainian-language explanations with English technical terms in parentheses, consistent with Lectures 1–3

### Key Entities

- **Jupyter Notebook**: `lectures/04-functions-modules-errors-oop/lecture-04.ipynb` — the primary artifact being modified
- **Local Image Assets**: `lectures/04-functions-modules-errors-oop/assets/diagrams/` — downloaded educational visuals
- **Meme Assets**: `lectures/04-functions-modules-errors-oop/assets/memes/` — humor visuals for engagement

### Assumptions

- The directory name `04-functions-modules-errors-oop` will be kept as-is to avoid breaking any existing cross-references from specs or other documents
- The mini-project will be refactored to a "Data Processing Pipeline" or similar theme that naturally integrates functions (lambda, map/filter), modules (custom validators), and error handling — without OOP
- Images that cannot be downloaded from any source will be replaced with clean text-based markdown diagrams (tables, ASCII art) as acceptable fallback per research.md R3
- The constitution v1.2.0 changes (OOP moved to Lecture 5) are already in effect

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Zero OOP references remain in the notebook content (excluding "What's Next" Lecture 5 preview)
- **SC-002**: 100% of images in the notebook render correctly using local file paths
- **SC-003**: Every non-OOP sub-topic (18 sub-topics across 4 sections) has at least 2 visuals
- **SC-004**: Zero temporary or orphaned files remain in the lecture directory
- **SC-005**: All code cells execute without errors when run top-to-bottom in a clean kernel
- **SC-006**: The notebook maintains consistent formatting, numbering, and Ukrainian terminology matching Lectures 1–3
