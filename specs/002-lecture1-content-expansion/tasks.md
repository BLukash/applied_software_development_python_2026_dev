# Tasks: Lecture 1 Content Expansion

**Feature**: 002-lecture1-content-expansion
**Generated**: 2026-01-25
**Source**: [spec.md](spec.md), [plan.md](plan.md), [lecture-structure.md](lecture-structure.md)

---

## Phase 1: Setup — Diagram Generation Infrastructure

### TASK-001: Create typing matrix diagram generator script
**Priority**: P1 | **Estimate**: S | **Dependencies**: None

Create `lectures/01-python-intro/assets/generate_typing_matrix.py` script that generates a 2x2 matrix diagram showing:
- X-axis: Strong vs Weak typing
- Y-axis: Static vs Dynamic typing
- Quadrants with language examples (Python highlighted in Dynamic+Strong)
- Consistent color scheme with existing diagrams (Python blue/yellow)

**Acceptance**:
- [X] Script runs without errors: `python generate_typing_matrix.py`
- [X] Output file created: `assets/diagrams/typing-matrix.png`
- [X] Python is clearly highlighted in the Dynamic+Strong quadrant
- [X] Colors consistent with existing python-timeline.png

**Files**:
- Create: `lectures/01-python-intro/assets/generate_typing_matrix.py`
- Create: `lectures/01-python-intro/assets/diagrams/typing-matrix.png`

---

### TASK-002: Create modules vs packages diagram generator script
**Priority**: P2 | **Estimate**: S | **Dependencies**: None

Create `lectures/01-python-intro/assets/generate_modules_diagram.py` script that visualizes:
- Single .py file → Module
- Directory with __init__.py → Package
- Import path flow visualization
- Clear visual distinction between file and folder

**Acceptance**:
- [X] Script runs without errors: `python generate_modules_diagram.py`
- [X] Output file created: `assets/diagrams/modules-packages.png`
- [X] Diagram clearly distinguishes module (file) from package (directory)
- [X] Shows __init__.py role

**Files**:
- Create: `lectures/01-python-intro/assets/generate_modules_diagram.py`
- Create: `lectures/01-python-intro/assets/diagrams/modules-packages.png`

---

## Phase 2: US1 — Python Design Philosophy Storytelling (P1)

### TASK-003: Add ABC language storytelling cell
**Priority**: P1 | **Estimate**: S | **Dependencies**: None

Add new markdown cell after cell-5 (history table) with content from lecture-structure.md "Чому Python виглядає саме так?" section:
- ABC language history at CWI Netherlands
- What Python inherited from ABC (indentation, data types)
- What Guido changed (extensibility, lowercase)
- Key quote from Guido van Rossum
- Code comparison: Python vs C/Java indentation

**Acceptance**:
- [X] Cell appears after the Python history table
- [X] Contains ABC → Python narrative
- [X] Includes Guido quote about extensibility
- [X] Code comparison shows indentation vs braces
- [X] Ukrainian text with English terms in parentheses (English in parentheses only for specific terms that are used typically in English)

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-001, FR-002, FR-005

---

### TASK-004: Add Python release philosophy cell
**Priority**: P1 | **Estimate**: S | **Dependencies**: TASK-003

Add new markdown cell after ABC storytelling with content from lecture-structure.md "Філософія релізів Python" section:
- Annual release cycle table (Alpha → Beta → RC → Release)
- Support timeline (2 years full + 3 years security)
- Guidance for students on version selection
- Link to Python Versions Status page

**Acceptance**:
- [X] Cell appears after ABC storytelling
- [X] Contains release cycle table
- [X] Explains 5-year support window
- [X] Student guidance included
- [X] Ukrainian text

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-006

---

### TASK-005: Add "Why Python awesome + where slow" cell
**Priority**: P1 | **Estimate**: M | **Dependencies**: TASK-004

Add new markdown cell after release philosophy with content from lecture-structure.md "Чому Python крутий + де повільний" section:
- Why Python is awesome (readability, batteries included, ecosystem, fast development)
- GIL explanation in simple terms
- When GIL doesn't matter (I/O-bound, web apps, NumPy)
- When GIL is a problem (CPU-bound parallelism)
- Solutions (multiprocessing, NumPy, asyncio, Python 3.13+)
- Conclusion: don't optimize prematurely

**Acceptance**:
- [X] Cell appears after release philosophy
- [X] "Why awesome" section with 4 key points
- [X] GIL explained in beginner-friendly terms
- [X] When-it-matters vs when-it-doesn't clearly distinguished
- [X] Solutions listed with brief explanation
- [X] Ukrainian text with English terms

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-003, FR-004

---

## Phase 3: US2 — Duck Typing Understanding (P1)

### TASK-006: Add duck typing explanation cell
**Priority**: P1 | **Estimate**: M | **Dependencies**: TASK-001 (for diagram)

Add new markdown cell after cell-25 (data types table) with content from lecture-structure.md "Динамічна типізація та Duck Typing" section:
- Static vs Dynamic typing explanation
- Strong vs Weak typing explanation
- 2x2 matrix table with language examples
- Reference to typing-matrix.png diagram
- Duck typing explanation with "walks like a duck" quote
- len() example showing duck typing behavior

**Acceptance**:
- [X] Cell appears after basic data types table
- [X] Contains typing matrix table
- [X] References typing-matrix.png diagram
- [X] Duck typing quote included
- [X] len() example shows behavior-based typing
- [X] Ukrainian text

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-007, FR-009, FR-010, FR-011, FR-012

---

### TASK-007: Add duck typing code example cell
**Priority**: P1 | **Estimate**: S | **Dependencies**: TASK-006

Add new code cell after duck typing explanation with executable duck typing example:
- Duck, Person, Robot classes with quack() method
- make_it_quack() function demonstrating duck typing
- Cat class without quack() showing what happens when interface missing
- Commented-out error case for demonstration

**Acceptance**:
- [X] Code cell executes without errors
- [X] Demonstrates duck typing with multiple classes
- [X] Shows behavior-based compatibility
- [X] Commented line shows what would fail
- [X] Output clearly shows the concept

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-008

---

## Phase 4: US3 — Modules and Packages Deep Understanding (P2)

### TASK-008: Expand venv explanation in cell-18
**Priority**: P2 | **Estimate**: M | **Dependencies**: None

Modify cell-18 (venv section) to add content from lecture-structure.md "Як venv працює всередині?" section:
- Keep existing venv basics
- Add directory structure visualization (.venv/ tree)
- Explain pyvenv.cfg purpose
- Explain Scripts/ vs bin/ directories
- Explain what happens at activation (PATH, sys.prefix)
- Show site-packages isolation

**Acceptance**:
- [X] Existing venv content preserved
- [X] Directory tree structure added
- [X] Activation process explained
- [X] sys.prefix change mentioned
- [X] site-packages isolation clear
- [X] Ukrainian text

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-016

---

### TASK-009: Add expanded pip commands cell
**Priority**: P2 | **Estimate**: S | **Dependencies**: TASK-008

Add new markdown cell after cell-20 (pip section) with content from lecture-structure.md "Розширені команди pip" section:
- pip show example with output
- pip check command
- pip uninstall command
- pip install with specific version
- pip install --upgrade
- pip install -r requirements.txt
- PyPI explanation (500,000+ packages)

**Acceptance**:
- [X] Cell appears after basic pip section
- [X] All pip commands shown with examples
- [X] PyPI explained
- [X] Advice about checking package popularity
- [X] Ukrainian text

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-015

---

### TASK-010: Add modules vs packages explanation cell
**Priority**: P2 | **Estimate**: M | **Dependencies**: TASK-002, TASK-009

Add new markdown cell after expanded pip section with content from lecture-structure.md "Модулі vs Пакети" section:
- Module definition (single .py file) with example
- Package definition (directory with __init__.py) with structure
- sys.path search order (4 locations)
- Reference to modules-packages.png diagram
- Common mistake warning (naming files same as stdlib modules)

**Acceptance**:
- [X] Module vs package clearly distinguished
- [X] Package directory structure shown
- [X] sys.path search order explained
- [X] Diagram reference included
- [X] Common mistake warning included
- [X] Ukrainian text

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-013, FR-014, FR-017

---

### TASK-011: Add sys.path code example cell
**Priority**: P2 | **Estimate**: S | **Dependencies**: TASK-010

Add new code cell after modules vs packages explanation with sys.path demonstration:
- Print first 5 entries of sys.path
- Show where os module is located (os.__file__)
- Numbered output for clarity

**Acceptance**:
- [X] Code cell executes without errors
- [X] Shows sys.path entries
- [X] Demonstrates module location discovery
- [X] Output is clear and educational

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-014

---

## Phase 5: US4 — Student-Friendly References (P3)

### TASK-012: Replace references section (cell-40)
**Priority**: P3 | **Estimate**: M | **Dependencies**: None

Replace content of cell-40 with structured references from lecture-structure.md:
- Official documentation category (Python Tutorial, Standard Library, PEP 8, Versions Status)
- Tutorials category (Real Python with specific article links)
- Video courses category (Corey Schafer, ArjanCodes)
- Practice category (quizzes, Exercism, LeetCode)
- Recommended learning path for beginners vs experienced programmers
- Course footer

**Acceptance**:
- [X] References categorized by type
- [X] Each reference has brief description
- [X] Difficulty/audience indicated where applicable
- [X] Free vs paid clearly marked
- [X] Learning path recommendations included
- [X] All URLs are valid
- [X] Ukrainian text

**Files**:
- Modify: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: FR-018, FR-019, FR-020, FR-021, FR-022

---

## Phase 6: Validation

### TASK-013: Execute all notebook cells and verify
**Priority**: P1 | **Estimate**: S | **Dependencies**: TASK-003 through TASK-012

Run all cells in the notebook and verify:
- All code cells execute without errors
- All images/diagrams load correctly
- No broken references or missing assets

**Acceptance**:
- [X] All cells execute successfully (Cell → Run All)
- [X] typing-matrix.png displays correctly
- [X] modules-packages.png displays correctly
- [X] No ModuleNotFoundError or FileNotFoundError
- [X] Code outputs match expectations

**Files**:
- Verify: `lectures/01-python-intro/lecture-01.ipynb`

---

### TASK-014: Review content for constitution compliance
**Priority**: P1 | **Estimate**: S | **Dependencies**: TASK-013

Review all new content against constitution v1.0.1 requirements:
- Ukrainian text quality (grammar, terminology)
- English terms in parentheses for technical concepts
- Icon usage (max 1-2 per section)
- Total duration estimate (~105 min target)

**Acceptance**:
- [X] Ukrainian grammar checked
- [X] Technical terms formatted correctly
- [X] Icons used sparingly (count per section)
- [X] Content fits 1.5-hour limit
- [X] Memes retained from original

**Files**:
- Review: `lectures/01-python-intro/lecture-01.ipynb`

**Satisfies**: SC-005, SC-007

---

## Summary

| Phase | Tasks | Priority | Estimated Time |
|-------|-------|----------|----------------|
| Phase 1: Setup | TASK-001, TASK-002 | P1-P2 | 2 tasks |
| Phase 2: US1 Storytelling | TASK-003, TASK-004, TASK-005 | P1 | 3 tasks |
| Phase 3: US2 Duck Typing | TASK-006, TASK-007 | P1 | 2 tasks |
| Phase 4: US3 Modules/Packages | TASK-008, TASK-009, TASK-010, TASK-011 | P2 | 4 tasks |
| Phase 5: US4 References | TASK-012 | P3 | 1 task |
| Phase 6: Validation | TASK-013, TASK-014 | P1 | 2 tasks |

**Total**: 14 tasks

### Dependency Graph

```
TASK-001 ─────────────────────────────┐
                                      ├──→ TASK-006 → TASK-007
TASK-002 ─────────────────────────────┤
                                      │
TASK-003 → TASK-004 → TASK-005 ───────┤
                                      │
TASK-008 → TASK-009 → TASK-010 ───────┤
                          │           │
                    TASK-002 ─────────┤
                          ↓           │
                    TASK-011 ─────────┤
                                      │
TASK-012 ─────────────────────────────┤
                                      ↓
                              TASK-013 → TASK-014
```

### Critical Path

P1 tasks that block validation:
1. TASK-001 (typing diagram) → TASK-006 (duck typing cell)
2. TASK-003 → TASK-004 → TASK-005 (storytelling chain)
3. TASK-006 → TASK-007 (duck typing + example)
