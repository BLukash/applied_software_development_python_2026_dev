# Quickstart: Lecture 3 — Data Structures + Pythonic Patterns + Functions

**Date**: 2026-02-12
**Status**: Complete

## Prerequisites

Before working with this lecture, ensure:

1. **Lectures 1-2 completed** - Students should have finished Lectures 1-2
2. **Python 3.11+ installed** - Required for all code examples
3. **Jupyter environment ready** - Notebook, JupyterLab, or Colab

## File Locations

```
lectures/
└── 03-data-structures/
    ├── lecture-03.ipynb     # Main lecture notebook
    └── assets/
        ├── diagrams/        # Memory layout diagrams
        │   ├── list-memory.png
        │   ├── tuple-memory.png
        │   ├── dict-hashtable.png
        │   └── ...
        └── memes/
            ├── collections-meme.png
            └── comprehensions-meme.png
```

## Running the Lecture

### Option 1: Local Jupyter

```bash
# Navigate to lectures directory
cd lectures/03-data-structures

# Start Jupyter
jupyter notebook lecture-03.ipynb
# or
jupyter lab
```

### Option 2: VS Code

1. Open `lecture-03.ipynb` in VS Code
2. Select Python 3.11+ kernel
3. Run cells with Shift+Enter

### Option 3: Google Colab

1. Upload `lecture-03.ipynb` to Colab
2. Upload `assets/` folder contents if using local images
3. Or update image paths to use URLs

## Development Workflow

### Creating the Lecture

1. **Read the spec** - `specs/005-lecture3-content/spec.md`
2. **Review Lectures 1-2** - Maintain tone consistency (constitution requirement)
3. **Follow data-model.md** - Section structure and content outline
4. **Check research.md** - Use identified diagram sources and patterns

### Content Guidelines

From constitution:

| Requirement | Implementation |
|-------------|----------------|
| Language | Ukrainian text, English terms in parentheses |
| Examples | 15+ runnable code examples with outputs |
| Exercises | 2 exercises + 1 mini parsing task with solutions |
| Memes | 2 per lecture (collections, comprehensions) |
| Diagrams | 3+ (internet-sourced or matplotlib) |
| Duration | 1.5 hours |

### Avoiding Repetition (Constitution Requirement)

**DO NOT repeat from Lectures 1-2:**
- Basic types (int, float, str, bool, None)
- Names vs objects, id(), references
- Mutability principle (mutable default argument bug)
- Identity vs equality (is vs ==)
- Truthiness and comparisons
- Control flow (if/elif/else, match, loops)
- Basic timing with time.perf_counter()
- Bytecode/PVM execution model
- GIL explanation
- Duck typing

**DO reference Lectures 1-2:**
- "У Лекції 2 ми коротко познайомились зі списками..."
- "Пам'ятаєте мутабельність з Лекції 2?..."
- "Як ми бачили у Лекції 2, Python-цикли можуть бути повільними..."

### New Content That Builds on Previous

| Previous Concept | How Lecture 3 Extends It |
|-----------------|--------------------------|
| Brief collection preview (L2) | Full deep dive with methods and pitfalls |
| Mutability principle (L2) | Applied to collection operations |
| Basic timing (L2) | Applied to list vs set/dict comparison |
| Memory model (L2) | Extended to collection internals |

## Testing the Lecture

### Before Finalizing

1. **Clean kernel restart** - Kernel > Restart & Run All
2. **Verify all cells execute** - No errors in code cells
3. **Check timing** - Content fits 1.5 hours
4. **Review assets** - All images load correctly
5. **Spell check** - Ukrainian text is correct

### Validation Checklist

- [ ] All code cells run without errors in Python 3.11+
- [ ] Outputs are visible and correct
- [ ] Images load from assets folder
- [ ] No content repeated from Lectures 1-2
- [ ] Cross-references to Lectures 1-2 are present
- [ ] 2 memes included
- [ ] 3+ diagrams included (collection memory representation)
- [ ] 15+ code examples with outputs
- [ ] 2 exercises with solutions in hidden cells
- [ ] Mini parsing task with solution in hidden cell
- [ ] Comparison table of collection types present
- [ ] Timed list vs set comparison present
- [ ] Function examples cover: basic, defaults, *args, **kwargs
- [ ] Comprehension readability anti-pattern included
- [ ] Summary section complete
- [ ] What's Next section references Lecture 4
- [ ] References section with official docs links
- [ ] Learning objectives (5) at start
- [ ] Prerequisites section present

## Troubleshooting

### Image Not Loading

```python
# Use relative path from notebook location
![Diagram](assets/diagrams/list-memory.png)

# Or absolute path for debugging
![Diagram](/full/path/to/assets/diagrams/list-memory.png)
```

### Timing Results Vary

This is expected for the list vs set comparison. Show students:
- Results vary between runs
- Relative comparison is what matters (set should always be dramatically faster)
- Use larger collections (100K+) for more visible differences

### Exercise Solutions Not Hidden

Use Jupyter's "Hide Cell" extension or raw cell with solution markers:
```python
# Solution (toggle visibility in Jupyter)
```

## Related Documents

- [spec.md](spec.md) - Feature specification
- [plan.md](plan.md) - Implementation plan
- [research.md](research.md) - Research findings
- [data-model.md](data-model.md) - Lecture structure
