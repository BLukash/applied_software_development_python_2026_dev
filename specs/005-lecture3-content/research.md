# Research: Lecture 3 — Data Structures + Pythonic Patterns + Functions

**Date**: 2026-02-12
**Status**: Complete

## R1: Collection Memory Diagram Sources

### Decision
Use a combination of internet-sourced diagrams (with attribution) and matplotlib-generated visuals for collection internals.

### Sources Identified

1. **Official Python Documentation** - [Data Structures](https://docs.python.org/3/tutorial/datastructures.html)
   - Authoritative reference for all collection operations
   - Text-based, needs supplementary visual diagrams

2. **Real Python** - [Lists and Tuples](https://realpython.com/python-lists-tuples/), [Dictionaries](https://realpython.com/python-dicts/), [Sets](https://realpython.com/python-sets/)
   - High-quality educational articles with diagrams
   - Appropriate for educational use
   - Good memory layout illustrations

3. **Laurent Luce's Blog** - [Python list internals](https://www.laurentluce.com/posts/python-list-implementation/)
   - Detailed C-level list implementation diagrams
   - Shows pointer array, over-allocation strategy
   - Excellent for visual learners

4. **GeeksForGeeks** - Used in previous lectures for consistency
   - Good hash table and dict internal diagrams
   - Consistent with established lecture style

5. **Python Wiki** - [TimeComplexity](https://wiki.python.org/moin/TimeComplexity)
   - Authoritative complexity reference table
   - Can be adapted into comparison table for lecture

### Diagrams Needed

| Diagram | Source Strategy | Purpose |
|---------|----------------|---------|
| List internal structure (pointer array) | Internet: Laurent Luce or Real Python | Show how list stores references |
| List vs tuple memory comparison | Internet or matplotlib | Explain tuple efficiency |
| Dict hash table (conceptual) | Internet: GeeksForGeeks or matplotlib | Motivate O(1) lookup |

### Fallback Strategy
Generate custom diagrams using matplotlib for:
- Simple box-and-arrow list structure
- Side-by-side list vs tuple comparison with `sys.getsizeof()`
- Hash function concept visualization (key → hash → slot)

### Rationale
Reuse proven sources from Lectures 1-2 where possible. Laurent Luce's blog provides excellent CPython internals visuals that match the "memory deep dive" requirement from the constitution.

---

## R2: Hash Table Explanation for Students

### Decision
Use the "locker room" analogy with a simple hash function demonstration, followed by a timed comparison on 100,000 elements.

### Pedagogical Approach

**Analogy**: Locker room / gym locker
- Each item gets a locker number calculated from its name (hash function)
- To find your locker, you don't check every locker (O(n)) — you compute your number and go directly (O(1))
- Collisions = two people assigned the same locker (briefly mention, don't deep-dive)

**Demonstration Strategy**:
1. Show `hash()` function on strings and integers
2. Explain: "dict uses hash to decide WHERE to store the value"
3. Time comparison: `x in my_list` vs `x in my_set` with 100,000 elements
4. Show the dramatic difference (~1000x for worst case)

**Test Size**: 100,000 elements provides clearly visible timing difference without being too slow on modest hardware. For the search, use an element NOT in the collection (worst case for list).

```python
import time

data_list = list(range(100_000))
data_set = set(range(100_000))
target = -1  # Not in collection

start = time.perf_counter()
target in data_list
list_time = time.perf_counter() - start

start = time.perf_counter()
target in data_set
set_time = time.perf_counter() - start

print(f"list: {list_time:.6f}s")
print(f"set:  {set_time:.6f}s")
print(f"set is {list_time/set_time:.0f}x faster!")
```

### Key Teaching Points
- Don't explain hash table implementation in detail
- Focus on "why" (O(1) vs O(n)) not "how" (open addressing, probing)
- Mention that dict keys must be hashable (immutable) — connect to Lecture 2 mutability
- Relate back to Lecture 2's timing introduction

### Rationale
Students at this level benefit more from intuition than implementation details. The locker analogy is concrete and memorable. The timed comparison creates an "aha moment" that motivates choosing the right data structure.

---

## R3: Comprehension Best Practices and Readability

### Decision
Teach comprehensions as "one transformation, optionally filtered" — and show explicit anti-patterns for when loops are better.

### Key Guidelines

**When to use comprehensions:**
- Single transformation: `[x**2 for x in numbers]`
- Simple filtering: `[x for x in numbers if x > 0]`
- Creating a new collection from an existing one
- The logic fits on one line without scrolling

**When to use loops:**
- Multiple operations per iteration
- Side effects needed (printing, modifying external state)
- More than one level of nesting
- Complex conditions that reduce readability

**PEP 8 Guidance** (from [PEP 8 - Programming Recommendations](https://peps.python.org/pep-0008/#programming-recommendations)):
- Comprehensions should be concise and readable
- If a comprehension is too long, break it into a loop
- No official line-length exception for comprehensions

### Anti-Pattern Examples for Teaching

**Bad — too nested:**
```python
# Don't do this
result = [item for sublist in matrix for item in sublist if item > 0 and item % 2 == 0]

# Do this instead
result = []
for sublist in matrix:
    for item in sublist:
        if item > 0 and item % 2 == 0:
            result.append(item)
```

**Bad — side effects:**
```python
# Don't do this
[print(x) for x in items]  # Comprehension for side effects

# Do this instead
for x in items:
    print(x)
```

### Teaching Progression
1. Simple list comprehension (transformation only)
2. List comprehension with filter
3. Dict comprehension
4. Set comprehension
5. Anti-pattern: when NOT to use comprehensions
6. "Rule of thumb: if you can't explain it in one sentence, use a loop"

### Rationale
Students often over-use comprehensions after learning them. Teaching readability boundaries early prevents bad habits. The "one sentence" rule is memorable and practical.

---

## R4: Meme Sources

### Decision
Create or source 2 memes appropriate for educational context, consistent with Lectures 1-2 style.

### Meme 1: Collections / Data Structure Choice

**Concept**: Choosing the wrong data structure
**Options**:
- "Is this a list?" butterfly meme — pointing at a dict when you need key lookup
- Drake meme: rejecting `if x in my_list` (100K items), accepting `if x in my_set`
- "They're the same picture" meme: `.append()` vs `.extend()` results

**Placement**: After the collections comparison table (Section 1), to reinforce "choose the right type"

### Meme 2: Comprehensions

**Concept**: Comprehension readability
**Options**:
- "Galaxy brain" meme: for loop → list comprehension → nested comprehension → "what does this even do?"
- "Two buttons" meme: "Write readable code" vs "One-liner comprehension"
- Expanding brain: simple loop → comprehension → nested comprehension → unreadable one-liner

**Placement**: After comprehension readability section (Section 5), to reinforce "keep it readable"

### Rationale
Memes at these positions create natural breaks in dense material. Collections meme reinforces data structure choice. Comprehension meme reinforces readability boundaries. Both align with key teaching moments.

---

## R5: Function Introduction Scope

### Decision
Cover core function mechanics (def, parameters, return, defaults, *args/**kwargs) at introductory level. Defer advanced topics (lambdas, closures, decorators, scope rules) to Lecture 4 per constitution.

### Scope Boundaries

**Include in Lecture 3 (intro):**
- `def` statement and basic syntax
- Positional parameters and return values
- Default arguments (simple cases, NOT mutable default — already covered in L2)
- Brief mention of docstrings (one-line format only)
- `*args` and `**kwargs` with 1-2 practical examples each
- Return multiple values via tuple
- Functions as organizing tool (DRY principle)

**Defer to Lecture 4 (deep dive):**
- Lambda functions
- Functions as first-class objects (passing functions as arguments)
- `map()`, `filter()`, `reduce()`
- Scope rules (local/global/nonlocal, LEGB)
- Closures
- Decorators
- Generators and iterators
- Type hints on function signatures

### Example Progression

1. **Hello function**: `def greet(name): return f"Привіт, {name}!"`
2. **Calculation**: `def area(width, height=1): return width * height`
3. **Processing**: `def count_words(text): ...` (connects to later parsing task)
4. **Variadic**: `def log(*messages, sep=" "): print(sep.join(messages))`
5. **Kwargs**: `def build_profile(**info): return info`

### Docstring Approach
Brief introduction only — show that docstrings exist and why they matter:
```python
def calculate_average(numbers):
    """Обчислює середнє значення списку чисел."""
    return sum(numbers) / len(numbers)
```
Defer PEP 257 style guide details to Lecture 4.

### Rationale
Functions need to be introduced before the mini parsing task can work (students need to write functions). The scope is intentionally limited — just enough to write useful functions, with Lecture 4 providing the deep dive. Mutable default argument trap is NOT re-explained (covered in Lecture 2) but can be briefly referenced.

---

## R6: Mini Parsing Task Design

### Decision
Web server access log parsing — extract HTTP methods and paths, compute frequency table of most-accessed endpoints.

### Task Specification

**Input Data** (hardcoded multi-line string):
```python
logs = """
2026-02-12 10:15:32 GET /api/users 200
2026-02-12 10:15:33 POST /api/users 201
2026-02-12 10:15:35 GET /api/users/42 200
2026-02-12 10:15:36 GET /api/products 200
2026-02-12 10:15:37 DELETE /api/users/42 204
2026-02-12 10:15:38 GET /api/users 200
2026-02-12 10:15:39 GET /api/products 200
2026-02-12 10:15:40 POST /api/orders 201
2026-02-12 10:15:41 GET /api/users 200
2026-02-12 10:15:42 GET /api/products/7 200
2026-02-12 10:15:43 PUT /api/users/42 200
2026-02-12 10:15:44 GET /api/orders 200
2026-02-12 10:15:45 GET /api/users 200
2026-02-12 10:15:46 POST /api/products 201
2026-02-12 10:15:47 GET /api/orders/1 200
"""
```

**Requirements:**
1. Parse each line to extract: method, path, status code
2. Build frequency table of (method, path) combinations
3. Sort by frequency (descending)
4. Print top 5 most common requests
5. Bonus: count requests by HTTP method

**Skills Exercised:**
- String `.split()` and slicing
- Dict for frequency counting
- Comprehension (at least one)
- `enumerate()` or `zip()` (for numbered output)
- Custom function(s)
- `sorted()` with key parameter

**Expected Solution Structure:**
```python
def parse_log_line(line):
    """Парсить рядок логу, повертає (method, path, status)."""
    parts = line.strip().split()
    return parts[2], parts[3], int(parts[4])

def count_frequencies(logs_text):
    """Підраховує частоту запитів."""
    lines = [line for line in logs_text.strip().split('\n') if line.strip()]
    freq = {}
    for line in lines:
        method, path, _ = parse_log_line(line)
        key = f"{method} {path}"
        freq[key] = freq.get(key, 0) + 1
    return freq

def top_requests(freq, n=5):
    """Повертає топ-N найчастіших запитів."""
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return sorted_freq[:n]

# Usage
frequencies = count_frequencies(logs)
for i, (request, count) in enumerate(top_requests(frequencies), 1):
    print(f"{i}. {request}: {count} разів")
```

**Difficulty Level**: Medium — requires combining 3-4 concepts but each step is straightforward. Students can be given a skeleton with TODO comments.

### Rationale
Web server logs are:
- Relatable (students will build APIs starting in Lecture 6)
- Structured enough to parse with `.split()`
- Simple enough to not require regex or file I/O
- Rich enough to demonstrate dicts, comprehensions, functions, and sorting
- Forward-looking — foreshadows the course's API/web development focus

---

## Summary

| Research Item | Decision | Key Source |
|--------------|----------|------------|
| Memory Diagrams | Internet + matplotlib fallback | Laurent Luce, Real Python, GeeksForGeeks |
| Hash Table Teaching | Locker analogy + 100K timed comparison | Pedagogical best practices |
| Comprehensions | "One sentence rule" + explicit anti-patterns | PEP 8, community best practices |
| Memes | 2: data structure choice + comprehension readability | Custom/sourced |
| Function Scope | Intro only (def, params, return, defaults, *args/**kwargs) | Constitution Lecture 3-4 split |
| Mini Parsing Task | Web server log frequency analysis | Constitution requirement |

All research items resolved. Ready for Phase 1 design artifacts.
