# Quickstart: Lecture 4 Refinement Validation

**Feature**: 007-lecture4-refinement
**Date**: 2026-02-18

## Step 1: Verify OOP Removal

Open the notebook and search for these terms:
- "ООП" — should appear ONLY in "What's Next" section
- "OOP" — should appear ONLY in "What's Next" section
- "class " (with space) — should appear ONLY in exception definitions (`class ValidationError(Exception)`)
- "наслідування" — should appear NOWHERE
- "інкапсуляція" — should appear NOWHERE
- "поліморфізм" — should appear NOWHERE
- "абстракція" — should appear NOWHERE

**Expected**: Section numbering is 1–4 (no Section 5). Exercises are numbered 1–3 (no Exercise 4).

## Step 2: Verify Images

Run this check:

```python
import json, re, os

with open('lectures/04-functions-modules-errors-oop/lecture-04.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

broken = []
for i, cell in enumerate(nb['cells']):
    src = ''.join(cell['source']) if isinstance(cell['source'], list) else cell['source']
    for m in re.finditer(r'!\[([^\]]*)\]\(([^)]+)\)', src):
        url = m.group(2)
        if url.startswith('http'):
            broken.append((i, m.group(1), url))
        elif not os.path.exists(f'lectures/04-functions-modules-errors-oop/{url}'):
            broken.append((i, m.group(1), f'MISSING: {url}'))

if broken:
    print(f'FAIL: {len(broken)} broken images')
    for cell, alt, url in broken:
        print(f'  Cell {cell}: {alt} -> {url}')
else:
    print('PASS: All images use valid local paths')
```

**Expected**: PASS — zero broken images, zero remote URLs.

## Step 3: Verify Code Execution

1. Open notebook in Jupyter
2. Kernel → Restart & Run All
3. All cells must execute without errors
4. No `ModuleNotFoundError` (only stdlib allowed)

**Expected**: Zero errors. All output cells populated.

## Step 4: Verify Asset Cleanup

```bash
# No orphaned files
ls lectures/04-functions-modules-errors-oop/download_images.py  # should NOT exist
ls lectures/04-functions-modules-errors-oop/image_mapping.json  # should NOT exist

# No OOP images
ls lectures/04-functions-modules-errors-oop/assets/diagrams/ | grep -i -E "oop|pillar|encap|inherit|poly|abstract"
# should return empty
```

**Expected**: No temporary files. No OOP-related images.

## Step 5: Constitution Compliance

| Requirement | Check |
|-------------|-------|
| Ukrainian text | All markdown in Ukrainian |
| English terms in () | Technical terms formatted correctly |
| 2+ memes | Count meme images — at least 2 |
| 2+ exercises | Count exercises — should be 3 |
| Summary section | Present with non-OOP takeaways |
| What's Next section | Present with Lecture 5 OOP preview |
| References section | Present with relevant links |
| Standard library only | No pip install required |
| Duration ~1.5h | Reasonable content volume |
