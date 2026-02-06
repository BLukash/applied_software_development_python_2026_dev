# Diagrams for Lecture 2

This folder should contain the following diagrams:

## Required Diagrams

### 1. names-objects.png
**Concept**: Names as references to objects
**Description**: Box-and-arrow diagram showing:
- Variables (names) as labels/tags
- Objects in memory as boxes
- Arrows showing references from names to objects
- Example: `a = [1,2,3]` and `b = a` pointing to the same list object

**Sources to consider**:
- Real Python OOP tutorials
- Python documentation
- Or generate with matplotlib

### 2. memory-model.png
**Concept**: Python object memory layout
**Description**: Diagram showing:
- PyObject structure (refcount, type pointer, data)
- Comparison of list vs tuple memory layout
- Why tuples are more memory-efficient

**Sources to consider**:
- Python internals documentation
- CPython source code visualizations
- Or generate with matplotlib

## Generating with Matplotlib

If suitable diagrams are not available, they can be generated using matplotlib:

```python
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Example code for names-objects diagram
fig, ax = plt.subplots(figsize=(10, 6))
# ... drawing code ...
plt.savefig('names-objects.png', dpi=150, bbox_inches='tight')
```
