# Research: Lecture 2 - Core Language Mechanics

**Date**: 2026-01-31
**Status**: Complete

## R1: Memory Diagram Sources

### Decision
Use a combination of internet-sourced diagrams (with attribution) and matplotlib-generated visuals.

### Sources Identified

1. **Official Python Documentation** - [Data Model](https://docs.python.org/3/reference/datamodel.html)
   - Authoritative source for object model concepts
   - Text-based, will need visual diagrams from elsewhere

2. **Real Python** - [OOP in Python](https://realpython.com/python3-object-oriented-programming/)
   - High-quality educational content
   - CC-licensed for educational use
   - Good diagrams for class/object relationships

3. **GeeksForGeeks** - Already used in Lecture 1 for execution model GIF
   - Consistent with existing lecture style
   - Good memory/reference diagrams available

4. **Medium Article by Alexander Obregon** - [Python Object Model for Beginners](https://medium.com/@AlexanderObregon/how-pythons-object-model-works-for-beginners-3b5bd54b0d80)
   - Simple beginner-friendly explanations
   - May have useful visual aids

### Fallback Strategy
Generate custom diagrams using matplotlib for:
- Names pointing to objects (box-and-arrow)
- Mutable vs immutable modification behavior
- List vs tuple internal structure comparison

### Rationale
Internet sources provide polished, tested visuals. Matplotlib fallback ensures we can create exactly what we need if no suitable diagram exists. This approach balances quality with flexibility.

---

## R2: Integer Caching Documentation

### Decision
Document the -5 to 256 caching range with appropriate caveats about implementation-specific behavior.

### Key Findings

1. **Official Documentation**: [Integer Objects - Python C API](https://docs.python.org/3/c-api/long.html)
   - CPython pre-allocates integers from -5 to 256
   - Implementation uses NSMALLPOSINTS=257 and NSMALLNEGINTS=5 macros
   - Total: 262 cached integer objects

2. **Behavior Verification**:
   ```python
   a = 256; b = 256
   a is b  # True - within cache

   a = 257; b = 257
   a is b  # May be False in REPL, True in same code block (compiler optimization)
   ```

3. **Important Caveats** (from [William Vincent](https://wsvincent.com/python-wat-integer-cache/) and [Real Python](https://realpython.com/lessons/small-integer-caching/)):
   - This is CPython-specific, not a language guarantee
   - Behavior may differ in other Python implementations (PyPy, Jython)
   - Compiler may optimize beyond cache range in same code block
   - Never rely on `is` for integer comparison - always use `==`

### Rationale
Students must understand this as an implementation detail, not a feature to depend on. The example demonstrates why `is` and `==` are different, but the teaching point is "always use `==` for value comparison."

---

## R3: Match Statement Examples

### Decision
Include 3-4 progressive examples: simple literal, sequence unpacking, and guard clauses.

### Best Practice Sources

1. **PEP 636** - [Official Tutorial](https://peps.python.org/pep-0636/)
   - Authoritative source for teaching pattern matching
   - Progressive examples from simple to complex

2. **Better Stack Guide** (March 2025) - [Comprehensive Guide](https://betterstack.com/community/guides/scaling-python/python-pattern-matching/)
   - Updated for 2025
   - Good practical examples

3. **Real Python** - [Structural Pattern Matching](https://realpython.com/structural-pattern-matching/)
   - Educational focus
   - Comparison with if/elif chains

### Example Progression for Lecture

**Example 1: Simple literal matching (HTTP status)**
```python
match status:
    case 200:
        return "OK"
    case 404:
        return "Not Found"
    case _:
        return "Unknown"
```

**Example 2: Sequence unpacking**
```python
match command.split():
    case ["quit"]:
        quit_game()
    case ["go", direction]:
        move(direction)
    case ["take", *items]:
        take_items(items)
```

**Example 3: Guards**
```python
match point:
    case (x, y) if x == y:
        print("On diagonal")
    case (x, y):
        print(f"Point at {x}, {y}")
```

### Rationale
Progressive complexity helps students build understanding. The HTTP status example is relatable. Sequence unpacking shows power beyond C-switch. Guards demonstrate conditional matching.

---

## R4: Meme Sources

### Decision
Create or source 2 memes appropriate for educational context.

### Meme 1: Mutability Gotcha

**Concept**: The "mutable default argument" trap
**Options**:
- "First time?" meme with developer discovering list default argument
- "They're the same picture" meme comparing `def f(items=[])` calls
- Drake meme: rejecting `def f(items=[])`, accepting `def f(items=None)`

**Source**: Create using free meme generators or find CC-licensed version

### Meme 2: Performance/Timing

**Concept**: Python loop overhead
**Options**:
- "Is this a butterfly?" meme: "Is this performance?"
- Comparison meme: loop vs sum() speed
- "We have X at home" meme: optimized code vs Python for loop

**Source**: Consistent with Lecture 1 style (educational but light-hearted)

### Rationale
Memes aid memory retention and reduce cognitive load. Constitution requires 2 memes per lecture. Topics chosen align with key learning moments (mutability, performance).

---

## R5: Timing Best Practices

### Decision
Use `time.perf_counter()` for manual timing demonstrations, mention `timeit` briefly for reference.

### Key Findings

1. **time.perf_counter()** - [Real Python Timer Functions](https://realpython.com/python-timer/)
   - High-resolution, monotonic clock
   - Best for benchmarking short durations
   - Simple to understand and demonstrate
   - Default timer used by timeit internally

2. **timeit module** - [Official Documentation](https://docs.python.org/3/library/timeit.html)
   - More sophisticated, runs multiple iterations
   - Better for micro-benchmarks
   - More complex API - save for later lectures

3. **time.time()** - [Super Fast Python](https://superfastpython.com/time-time-vs-time-perf_counter/)
   - Lower resolution
   - Not monotonic (can go backwards on clock adjustments)
   - **Not recommended** for benchmarking

### Teaching Approach

**Introduce (simple):**
```python
import time

start = time.perf_counter()
# code to time
result = sum(range(1_000_000))
end = time.perf_counter()
print(f"Elapsed: {end - start:.4f} seconds")
```

**Compare (loop vs builtin):**
```python
# Loop version
start = time.perf_counter()
total = 0
for i in range(1_000_000):
    total += i
loop_time = time.perf_counter() - start

# Builtin version
start = time.perf_counter()
total = sum(range(1_000_000))
builtin_time = time.perf_counter() - start

print(f"Loop: {loop_time:.4f}s, Builtin: {builtin_time:.4f}s")
print(f"Builtin is {loop_time/builtin_time:.1f}x faster")
```

**Mention but don't deep-dive:**
- `timeit` module exists for more rigorous benchmarking
- `%timeit` magic in Jupyter (brief mention, use later)
- Reference back to Lecture 1: interpreter overhead, bytecode

### Rationale
`time.perf_counter()` is simple, accurate, and teaches the core concept. Students can see timing in action without learning a complex module. This sets up motivation for NumPy/vectorization in later lectures.

---

## Summary

| Research Item | Decision | Key Source |
|--------------|----------|------------|
| Memory Diagrams | Internet + matplotlib fallback | Python docs, Real Python, GeeksForGeeks |
| Integer Caching | -5 to 256, CPython-specific | Python C API docs, Real Python |
| Match Statement | 3 progressive examples | PEP 636, Better Stack Guide |
| Memes | 2 custom/sourced | Mutability trap, timing comparison |
| Timing | time.perf_counter() primary | Real Python, timeit docs |

All research items resolved. Ready for Phase 1 design artifacts.
