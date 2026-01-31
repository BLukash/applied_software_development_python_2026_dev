# Data Model: Lecture 2 - Core Language Mechanics

**Date**: 2026-01-31
**Status**: Complete

For educational content, the "data model" is the lecture structure and content organization.

## Lecture Structure

### Header Section
- Lecture number: 2
- Title: Механіка Python (Core Language Mechanics)
- Prerequisites: Completion of Lecture 1
- Duration target: 1.5 hours

### Learning Objectives (5)

```markdown
Після цієї лекції ви зможете:

1. Пояснити різницю між іменами (names) та об'єктами (objects) у Python
2. Розрізняти мутабельні (mutable) та немутабельні (immutable) типи даних
3. Правильно використовувати `is` (ідентичність) та `==` (рівність)
4. Застосовувати конструкції керування потоком: if/elif/else, match, for, while
5. Вимірювати час виконання коду для порівняння продуктивності
```

---

## Content Sections

### Section 1: Імена та Об'єкти (~20 min)

**Concepts:**
- Everything in Python is an object
- Names are references to objects, not containers
- `id()` function reveals object identity
- Assignment creates bindings, not copies

**Code Examples:**
1. `id()` demonstration with integers
2. Same object, multiple names (aliasing)
3. Reassignment creates new binding

**Diagram:**
- Box-and-arrow: names pointing to objects in memory

**Cross-reference:**
- "Як ми бачили у Лекції 1, Python — динамічно типізована мова. Тепер подивимось глибше на те, як це працює всередині."

---

### Section 2: Мутабельність (Mutability) (~20 min)

**Concepts:**
- Mutable types: list, dict, set
- Immutable types: int, float, str, tuple, frozenset, bool, None
- Implications for shared references
- The mutable default argument trap

**Code Examples:**
1. Modifying list through alias
2. String immutability (`.upper()` returns new string)
3. Mutable default argument bug and fix

**Meme:**
- "First time?" or Drake meme for mutable default argument

**Table:**
| Тип | Мутабельний? | Приклад |
|-----|--------------|---------|
| list | Так | `[1, 2, 3]` |
| dict | Так | `{"a": 1}` |
| set | Так | `{1, 2, 3}` |
| int | Ні | `42` |
| str | Ні | `"hello"` |
| tuple | Ні | `(1, 2, 3)` |

---

### Section 3: Представлення в Пам'яті (~15 min)

**Concepts:**
- PyObject structure (conceptual)
- Object overhead (type, refcount)
- List vs tuple memory layout
- Why tuples are more efficient

**Diagram:**
- Memory layout comparison: list vs tuple
- Object header visualization

**Code Example:**
```python
import sys
print(sys.getsizeof([1, 2, 3]))  # List size
print(sys.getsizeof((1, 2, 3)))  # Tuple size
```

---

### Section 4: Ідентичність vs Рівність (~15 min)

**Concepts:**
- `is` checks identity (same object in memory)
- `==` checks equality (same value)
- Integer caching (-5 to 256)
- String interning
- When to use which (always `is None`, usually `==` otherwise)

**Code Examples:**
1. `is` vs `==` with small integers (cached)
2. `is` vs `==` with large integers (not cached)
3. `is` vs `==` with lists
4. `is None` pattern
5. String interning behavior

**Important warning:**
- Integer caching is CPython implementation detail
- Never use `is` for value comparison

---

### Section 5: Істинність (Truthiness) (~10 min)

**Concepts:**
- Falsy values: None, 0, 0.0, "", [], {}, set()
- Everything else is truthy
- Pythonic conditionals: `if items:` not `if len(items) > 0:`
- Short-circuit evaluation

**Code Examples:**
1. All falsy values demonstration
2. Idiomatic truthiness check
3. Short-circuit with `and`/`or`

**Comparison chaining:**
```python
# Pythonic
if 0 < x < 10:
    print("x is between 0 and 10")

# Less readable equivalent
if x > 0 and x < 10:
    print("x is between 0 and 10")
```

---

### Section 6: Керування Потоком (Control Flow) (~25 min)

#### 6.1 Умовні Оператори

**if/elif/else:**
```python
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"
```

**match (Python 3.10+):**
- Simple literal matching
- Sequence unpacking
- Guard clauses

**Code Examples:**
1. Grade calculation with if/elif/else
2. HTTP status with match
3. Command parsing with match and unpacking

#### 6.2 Цикли

**for loop:**
- Iteration over sequences
- `range()` variations: `range(n)`, `range(a,b)`, `range(a,b,step)`
- Reference to `enumerate()` from Lecture 1

**while loop:**
- Condition-based iteration
- `break` and `continue`
- `for...else` pattern

**Code Examples:**
1. for with range variations
2. while with break
3. for...else search pattern

---

### Section 7: Практичні Патерни (~10 min)

**Patterns:**
1. Counting occurrences
2. Search with early exit
3. Accumulation pattern

**Code Examples:**
```python
# Counting
count = 0
for item in items:
    if condition(item):
        count += 1

# Search with early exit
for item in items:
    if target(item):
        found = item
        break
else:
    found = None  # for...else: executed if no break

# Accumulation
result = []
for item in items:
    result.append(transform(item))
```

---

### Section 8: Вимірювання Часу (~10 min)

**Concepts:**
- Why measure performance
- `time.perf_counter()` for timing
- Loop overhead demonstration
- Motivation for built-in functions and later optimization

**Meme:**
- Performance comparison meme

**Code Example:**
```python
import time

# Slow: Python loop
start = time.perf_counter()
total = 0
for i in range(1_000_000):
    total += i
loop_time = time.perf_counter() - start

# Fast: Built-in
start = time.perf_counter()
total = sum(range(1_000_000))
builtin_time = time.perf_counter() - start

print(f"Loop: {loop_time:.4f}s")
print(f"sum(): {builtin_time:.4f}s")
print(f"Builtin {loop_time/builtin_time:.1f}x faster!")
```

**Cross-reference:**
- "Пам'ятаєте з Лекції 1, як Python виконує байткод у віртуальній машині? Тому прості цикли повільніші, ніж вбудовані функції, написані на C."

---

### Exercises Section

#### Exercise 1: Predict the Output
Given code snippets, predict what they will print (mutability, identity).

#### Exercise 2: Fix the Bug
Fix the mutable default argument bug in provided function.

#### Exercise 3: Control Flow Challenge
Implement a simple loop pattern (counting or searching).

---

### Summary Section

```markdown
### Що ми вивчили сьогодні:

✅ **Імена та об'єкти** — імена є посиланнями на об'єкти, не контейнерами

✅ **Мутабельність** — list/dict/set можна змінювати, str/int/tuple — ні

✅ **is vs ==** — ідентичність проти рівності (завжди `is None`!)

✅ **Truthiness** — falsy значення та ідіоматичні перевірки

✅ **Control flow** — if/elif/else, match, for, while, break/continue

✅ **Вимірювання часу** — time.perf_counter() для бенчмарків
```

---

### What's Next Section

```markdown
## Що далі? (What's Next)

### Лекція 3: Структури Даних + "Pythonic" Патерни

- Колекції: list, tuple, dict, set (глибше)
- Індексація, зрізи (slicing)
- Comprehensions: list/dict/set
- Складність операцій (O(1) vs O(n))

### Домашнє завдання

1. Пройдіть усі вправи з лекції
2. Поекспериментуйте з id() для різних типів
3. Напишіть функцію з правильною обробкою мутабельних аргументів
4. Виміряйте час виконання 3 різних способів підрахунку елементів
```

---

### References Section

**Official Documentation:**
- [Python Data Model](https://docs.python.org/3/reference/datamodel.html)
- [PEP 636 - Pattern Matching Tutorial](https://peps.python.org/pep-0636/)
- [timeit module](https://docs.python.org/3/library/timeit.html)

**Tutorials:**
- [Real Python - Python Timer Functions](https://realpython.com/python-timer/)
- [Real Python - Structural Pattern Matching](https://realpython.com/structural-pattern-matching/)
- [Real Python - Small Integer Caching](https://realpython.com/lessons/small-integer-caching/)

**Deep Dives:**
- [Super Fast Python - perf_counter vs time](https://superfastpython.com/time-time-vs-time-perf_counter/)
- [Better Stack - Pattern Matching Guide](https://betterstack.com/community/guides/scaling-python/python-pattern-matching/)

---

## Entity Summary

| Entity | Description | Constitution Requirement |
|--------|-------------|-------------------------|
| Names | References/bindings to objects | Lecture 2 topics |
| Objects | Typed values in memory | Lecture 2 topics |
| Mutable types | list, dict, set | Lecture 2 topics |
| Immutable types | int, str, tuple, etc. | Lecture 2 topics |
| Control flow | if/elif/else, match, for, while | Lecture 2 topics |
| Timing | time.perf_counter() | Lecture 2 topics |
