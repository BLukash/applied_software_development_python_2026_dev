# Quickstart: Лекція 1 — Вступ до Python

**Purpose**: Guide for creating, editing, and validating the lecture notebook
**Date**: 2026-01-24

## Prerequisites

Before working on this lecture:

1. **Python 3.11+** installed
2. **Jupyter** installed: `pip install jupyter`
3. **VS Code** with Jupyter extension (or JupyterLab)

## Project Structure

```
lectures/
└── 01-python-intro/
    ├── lecture-01.ipynb     # Main lecture notebook (create this)
    ├── assets/
    │   ├── memes/           # Place 2+ memes here
    │   │   ├── python-naming.png
    │   │   └── works-on-my-machine.png
    │   └── diagrams/        # Any diagrams/tables as images
    ├── exercises/
    │   ├── exercise-01.py   # Greeting program starter
    │   └── exercise-02.py   # Calculator starter
    └── solutions/
        ├── solution-01.py   # Greeting solution
        └── solution-02.py   # Calculator solution
```

## Creating the Lecture

### Step 1: Create Directory Structure

```bash
mkdir -p lectures/01-python-intro/{assets/memes,assets/diagrams,exercises,solutions}
```

### Step 2: Create Notebook

```bash
cd lectures/01-python-intro
jupyter notebook
# Or open in VS Code
```

### Step 3: Follow Structure

Use [lecture-structure.md](lecture-structure.md) as the content blueprint. Copy markdown and code cells as specified.

### Step 4: Add Visual Assets

1. **Memes**: Create or find 2+ relevant memes and save to `assets/memes/`
2. **Diagrams**: Export any tables/diagrams as images to `assets/diagrams/`
3. Reference in notebook: `![Description](assets/memes/filename.png)`

## Content Guidelines

### Language Rules

| Content Type | Language | Example |
|--------------|----------|---------|
| Headings | Ukrainian | `## Що таке Python?` |
| Explanations | Ukrainian | `Python — це мова програмування...` |
| Technical terms | Ukrainian + (English) | `змінні (variables)` |
| Code | English | `print("Hello")` |
| Code comments | English (minimal) | `# Calculate total` |

### Required Elements Checklist

- [ ] Learning objectives (3-5 points)
- [ ] Prerequisites section
- [ ] 5+ runnable code examples
- [ ] 2+ practical exercises with solutions
- [ ] 2+ memes
- [ ] 1+ diagram/table
- [ ] Summary section
- [ ] "What's Next" section
- [ ] References (non-Russian sources only)

## Testing the Notebook

### 1. Clean Kernel Test

```bash
# Restart kernel and run all cells
jupyter nbconvert --execute --to notebook lecture-01.ipynb
```

### 2. Verify All Code Runs

- Open notebook
- Kernel → Restart & Run All
- Check for errors

### 3. Duration Test

- Present the lecture content
- Should complete in ~90 minutes

## Validation Checklist

Before marking complete:

- [ ] All code cells execute without errors
- [ ] Ukrainian text is grammatically correct
- [ ] English technical terms appear in parentheses on first use
- [ ] All images display correctly
- [ ] Links work (test each reference)
- [ ] Exercises have both starter and solution versions
- [ ] Time allocation roughly matches spec (~90 min total)

## Common Issues

### Issue: Kernel not finding Python

```bash
# Ensure you're in the right venv
python -m ipykernel install --user --name=course-venv
```

### Issue: Images not displaying

- Use relative paths: `assets/memes/file.png`
- Check file exists and has correct extension

### Issue: Code cell errors

- Test each cell independently
- Check for typos in Ukrainian strings (encoding)

## Editing Tips

1. **Keep cells focused**: One concept per cell
2. **Test incrementally**: Run each cell as you write
3. **Use markdown preview**: Check formatting before saving
4. **Save often**: Notebooks can lose unsaved work

## Deployment

When lecture is complete:

```bash
# Commit to git
git add lectures/01-python-intro/
git commit -m "feat: add Lecture 1 - Python Introduction"
```

## Related Documents

- [spec.md](spec.md) - Feature specification
- [plan.md](plan.md) - Implementation plan
- [research.md](research.md) - Research findings
- [lecture-structure.md](lecture-structure.md) - Detailed content structure
