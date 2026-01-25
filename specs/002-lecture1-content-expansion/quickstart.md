# Quickstart: Lecture 1 Content Expansion

**Feature**: 002-lecture1-content-expansion
**Date**: 2026-01-25

## Overview

This guide explains how to implement the Lecture 1 content expansion.

## Prerequisites

- Existing Lecture 1 notebook: `lectures/01-python-intro/lecture-01.ipynb`
- matplotlib installed for diagram generation
- Understanding of [lecture-structure.md](lecture-structure.md) content plan

## Implementation Steps

### Phase 1: Create New Diagrams

1. **typing-matrix.png** - Static/Dynamic vs Strong/Weak typing matrix
   ```bash
   cd lectures/01-python-intro/assets
   python generate_typing_matrix.py
   ```

2. **modules-packages.png** - Module vs Package visualization
   ```bash
   python generate_modules_diagram.py
   ```

### Phase 2: Add New Content Cells

Follow the order in [lecture-structure.md](lecture-structure.md):

1. **After cell-5** (history table):
   - Add: "Чому Python виглядає саме так?" (ABC storytelling)
   - Add: "Філософія релізів Python"
   - Add: "Чому Python крутий + де повільний"

2. **Modify cell-18** (venv section):
   - Expand with "Як venv працює всередині?"

3. **After cell-20** (pip section):
   - Add: "Розширені команди pip"
   - Add: "Модулі vs Пакети" + diagram reference
   - Add: Code cell with `sys.path` example

4. **After cell-25** (data types table):
   - Add: "Динамічна типізація та Duck Typing" + diagram reference
   - Add: Code cell with duck typing example

5. **Replace cell-40** (References):
   - Replace with categorized references from lecture-structure.md

### Phase 3: Validation

1. **Execute all cells** - Ensure no errors
2. **Check diagram display** - All images load correctly
3. **Review timing** - Content should fit ~105 min
4. **Ukrainian text review** - Grammar and terminology check
5. **Icon usage check** - Max 1-2 per section (per constitution v1.0.1)

## File Changes Summary

| File | Action |
|------|--------|
| `lecture-01.ipynb` | Modify (add ~10 cells) |
| `assets/diagrams/typing-matrix.png` | Create |
| `assets/diagrams/modules-packages.png` | Create |
| `assets/generate_typing_matrix.py` | Create |
| `assets/generate_modules_diagram.py` | Create |

## Constitution Compliance

| Requirement | Status |
|-------------|--------|
| Ukrainian text | All new content in Ukrainian |
| English terms in parentheses | Technical terms formatted correctly |
| Code examples executable | All examples tested |
| Icon usage | Sparingly used (1-2 per section) |
| Duration limit | ~105 min total (fits 1.5 hr) |
| Memes | Existing memes retained |

## Testing

Run the notebook in a clean Python 3.11+ environment:

```bash
# Create clean test environment
python -m venv .test-venv
source .test-venv/bin/activate  # or .test-venv\Scripts\activate on Windows
pip install jupyter matplotlib

# Run notebook
jupyter notebook lectures/01-python-intro/lecture-01.ipynb
# Execute all cells (Cell → Run All)
```

## References Used

Key sources incorporated into content:

- [The Making of Python - Artima](https://www.artima.com/articles/the-making-of-python)
- [Duck Typing - Real Python](https://realpython.com/duck-typing-python/)
- [Virtual Environments - Real Python](https://realpython.com/python-virtual-environments-a-primer/)
- [Python Modules - Real Python](https://realpython.com/python-modules-packages/)
- [PEP 602 - Annual Release Cycle](https://peps.python.org/pep-0602/)
- [PEP 703 - Making GIL Optional](https://peps.python.org/pep-0703/)
