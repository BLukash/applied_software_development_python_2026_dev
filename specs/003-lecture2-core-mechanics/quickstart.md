# Quickstart: Lecture 2 - Core Language Mechanics

**Date**: 2026-01-31
**Status**: Complete

## Prerequisites

Before working with this lecture, ensure:

1. **Lecture 1 completed** - Students should have finished Lecture 1 (Python Intro)
2. **Python 3.11+ installed** - Required for match statement and modern features
3. **Jupyter environment ready** - Notebook, JupyterLab, or Colab

## File Locations

```
lectures/
└── 02-core-mechanics/
    ├── lecture-02.ipynb     # Main lecture notebook
    └── assets/
        ├── diagrams/        # Visual aids
        │   ├── names-objects.png
        │   ├── memory-model.png
        │   └── ...
        └── memes/
            ├── mutability-bug.png
            └── timing-meme.png
```

## Running the Lecture

### Option 1: Local Jupyter

```bash
# Navigate to lectures directory
cd lectures/02-core-mechanics

# Start Jupyter
jupyter notebook lecture-02.ipynb
# or
jupyter lab
```

### Option 2: VS Code

1. Open `lecture-02.ipynb` in VS Code
2. Select Python 3.11+ kernel
3. Run cells with Shift+Enter

### Option 3: Google Colab

1. Upload `lecture-02.ipynb` to Colab
2. Upload `assets/` folder contents if using local images
3. Or update image paths to use URLs

## Development Workflow

### Creating the Lecture

1. **Read the spec** - `specs/003-lecture2-core-mechanics/spec.md`
2. **Review Lecture 1** - Maintain tone consistency (constitution requirement)
3. **Follow data-model.md** - Section structure and content outline
4. **Check research.md** - Use identified diagram sources and patterns

### Content Guidelines

From constitution:

| Requirement | Implementation |
|-------------|----------------|
| Language | Ukrainian text, English terms in parentheses |
| Examples | 5+ runnable code examples with outputs |
| Exercises | 2+ with solutions |
| Memes | 2 per lecture |
| Diagrams | 3+ (internet or matplotlib) |
| Duration | 1.5 hours |

### Avoiding Repetition (Constitution Requirement)

**DO NOT repeat from Lecture 1:**
- Bytecode/PVM execution model
- GIL explanation
- Duck typing with quack() example
- Dynamic vs static typing matrix
- Basic types with type() function

**DO reference Lecture 1:**
- "Як ми бачили у Лекції 1..."
- "Пам'ятаєте з попередньої лекції..."

## Testing the Lecture

### Before Finalizing

1. **Clean kernel restart** - Kernel > Restart & Run All
2. **Verify all cells execute** - No errors in code cells
3. **Check timing** - Content fits 1.5 hours
4. **Review assets** - All images load correctly
5. **Spell check** - Ukrainian text is correct

### Validation Checklist

- [ ] All code cells run without errors
- [ ] Outputs are visible and correct
- [ ] Images load from assets folder
- [ ] No content repeated from Lecture 1
- [ ] Cross-references to Lecture 1 are present
- [ ] 2 memes included
- [ ] 3+ diagrams included
- [ ] 5+ code examples with outputs
- [ ] 2+ exercises with solutions
- [ ] Summary section complete
- [ ] What's Next section complete
- [ ] References section with links

## Troubleshooting

### Image Not Loading

```python
# Use relative path from notebook location
![Diagram](assets/diagrams/names-objects.png)

# Or absolute path for debugging
![Diagram](/full/path/to/assets/diagrams/names-objects.png)
```

### Match Statement Not Working

```python
import sys
print(sys.version)  # Must be 3.10+
```

### Timing Results Vary

This is expected. Show students that:
- Results vary between runs
- Relative comparison is what matters
- Use multiple runs for more accuracy

## Related Documents

- [spec.md](spec.md) - Feature specification
- [plan.md](plan.md) - Implementation plan
- [research.md](research.md) - Research findings
- [data-model.md](data-model.md) - Lecture structure

## Contact

For issues with this lecture, check:
1. GitHub Issues
2. Course repository README
3. Constitution at `.specify/memory/constitution.md`
