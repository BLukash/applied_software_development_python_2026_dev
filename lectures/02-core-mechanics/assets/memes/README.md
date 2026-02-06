# Memes for Lecture 2

This folder should contain the following memes:

## Required Memes (per constitution: 2 per lecture)

### 1. mutability-bug.png
**Concept**: The mutable default argument trap
**Suggested formats**:
- "First time?" meme - developer discovering list default argument
- Drake meme: rejecting `def f(items=[])`, accepting `def f(items=None)`
- "They're the same picture" meme comparing multiple calls to function with mutable default

### 2. timing-meme.png
**Concept**: Python loop overhead vs built-in functions
**Suggested formats**:
- "Is this performance?" butterfly meme
- Comparison meme showing Python loop vs sum() speed
- "We have X at home" meme: optimized code vs Python for loop

## Usage Notes

- Memes should be appropriate for educational setting
- Should help illustrate the concept being taught
- Consider using free meme generators or CC-licensed images
- Consistent with Lecture 1 style (educational but light-hearted)

## Alternative: ASCII Art or Emoji-based

If image memes are not available, consider using text-based humor in markdown cells:

```markdown
### The Mutable Default Argument Trap

```
def f(items=[]):     # "I'm just declaring a default"
    items.append(1)
    return items

f()  # [1]           # "Seems fine..."
f()  # [1, 1]        # "Wait what??"
f()  # [1, 1, 1]     # "WHAT IS HAPPENING?!"
```
```
