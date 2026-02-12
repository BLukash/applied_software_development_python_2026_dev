# Data Model: Lecture 3 — Data Structures + Pythonic Patterns + Functions

**Date**: 2026-02-12
**Status**: Complete

For educational content, the "data model" is the lecture structure and content organization.

## Lecture Structure

### Header Section
- Lecture number: 3
- Title: Структури даних + "Pythonic" патерни + Функції (Data Structures + Pythonic Patterns + Functions)
- Prerequisites: Completion of Lectures 1-2
- Duration target: 1.5 hours

### Learning Objectives (5)

```markdown
Після цієї лекції ви зможете:

1. Впевнено працювати зі списками, кортежами, словниками та множинами — включно з індексацією, зрізами та основними методами
2. Використовувати comprehensions (list/dict/set) та ітераційні патерни (enumerate, zip) для лаконічного та читабельного коду
3. Пояснити, чому пошук у dict/set швидший за list, та обирати відповідну структуру даних для задачі
4. Створювати функції з параметрами, значеннями за замовчуванням та *args/**kwargs
5. Розв'язувати практичні задачі парсингу даних, комбінуючи всі вивчені концепції
```

---

## Content Sections

### Section 1: Колекції — Глибоке занурення (~25 min)

**Subsection 1.1: Списки (Lists) — ~10 min**

**Concepts:**
- List creation (literal, `list()`, `list(range())`)
- Indexing: positive and negative indices
- Slicing: `start:stop:step` with all variations
- Common methods: `.append()`, `.extend()`, `.insert()`, `.pop()`, `.remove()`, `.sort()`, `.reverse()`, `.copy()`
- Pitfalls: `.append()` vs `.extend()`, modifying while iterating

**Code Examples:**
1. Indexing with positive/negative indices
2. Slicing: basic, with step, reversed list via `[::-1]`
3. `.append()` vs `.extend()` comparison
4. Modifying list while iterating — the bug and the fix
5. `.sort()` vs `sorted()` (in-place vs new list)

**Cross-reference:**
- "У Лекції 2 ми коротко познайомились зі списками. Тепер пора зануритись глибше — від індексації до хитрих підводних каменів."

---

**Subsection 1.2: Кортежі (Tuples) — ~5 min**

**Concepts:**
- Tuple creation (with and without parentheses)
- Single-element tuple: `(x,)` vs `(x)`
- Tuple unpacking
- Immutability enforcement
- When to use tuples vs lists
- Brief mention of `namedtuple` as preview for Lecture 5

**Code Examples:**
1. Creation and unpacking
2. Single-element tuple gotcha
3. Tuple as dict key (connects to dict section)

---

**Subsection 1.3: Словники (Dicts) — ~10 min**

**Concepts:**
- Dict creation (literal, `dict()`, from list of tuples)
- Accessing: bracket notation vs `.get()` with default
- Modification: `.update()`, `.pop()`, `.setdefault()`
- Iteration: `.keys()`, `.values()`, `.items()`
- Key requirements: must be hashable (connect to hash table later)
- Pitfall: `{}` creates empty dict, not empty set

**Code Examples:**
1. Creation and access patterns
2. `.get()` with default vs KeyError
3. `.items()` iteration for key-value pairs
4. Dict from `zip()` (preview of zip)

---

**Subsection 1.4: Множини (Sets) — ~5 min**

**Concepts:**
- Set creation: `set()` and `{a, b, c}` (but NOT `{}`)
- Add/remove: `.add()`, `.discard()`, `.remove()`
- Set operations: `|` (union), `&` (intersection), `-` (difference), `^` (symmetric difference)
- Membership check performance (O(1))
- No duplicates guarantee

**Code Examples:**
1. Set creation and deduplication
2. Set operations with `|`, `&`, `-`
3. Membership check: `x in my_set`

---

**Subsection 1.5: Порівняльна таблиця — ~2 min**

**Table:**
| Тип | Впорядкований? | Змінюваний? | Дублікати? | Типове використання |
|-----|----------------|-------------|------------|---------------------|
| list | Так | Так | Так | Колекція елементів у порядку |
| tuple | Так | Ні | Так | Фіксовані дані, ключі dict |
| dict | Так (з 3.7+) | Так | Ключі — ні | Відображення ключ-значення |
| set | Ні | Так | Ні | Унікальні елементи, швидкий пошук |

**Meme 1**: Data structure choice meme (placement here)

---

### Section 2: Як колекції зберігаються в пам'яті (~10 min)

**Concepts:**
- List internal structure: array of pointers with over-allocation
- Tuple internal structure: fixed array of pointers (no over-allocation)
- Dict: hash table (conceptual)
- `sys.getsizeof()` comparison

**Diagrams (3):**
1. List memory diagram (pointer array with capacity > length)
2. Tuple memory diagram (fixed pointer array)
3. Dict hash table concept (keys → hash → slots → values)

**Code Example:**
```python
import sys
print(f"list:  {sys.getsizeof([1, 2, 3])} bytes")
print(f"tuple: {sys.getsizeof((1, 2, 3))} bytes")
print(f"dict:  {sys.getsizeof({'a': 1, 'b': 2, 'c': 3})} bytes")
print(f"set:   {sys.getsizeof({1, 2, 3})} bytes")
```

**Cross-reference:**
- "У Лекції 2 ми бачили, як Python зберігає прості типи в пам'яті. Тепер подивимось на колекції."

---

### Section 3: Індексація, зрізи та вкладені структури (~10 min)

**Concepts:**
- Advanced slicing patterns
- Negative indices deep dive
- Nested structures: list of dicts, dict of lists
- Accessing nested data

**Code Examples:**
1. Slicing with step: `numbers[::2]`, `numbers[::-1]`
2. Slice assignment: `numbers[1:3] = [10, 20, 30]`
3. Nested structure: list of student dicts
4. Accessing nested: `students[0]["name"]`
5. Membership checks: `in` for list, dict (keys), set

---

### Section 4: Ітераційні патерни (~10 min)

**Concepts:**
- `enumerate()` for index + value
- `zip()` for parallel iteration
- `zip()` for dict creation
- When to use which pattern

**Code Examples:**
1. `enumerate()`: numbered list output
2. `enumerate()` with custom start: `enumerate(items, 1)`
3. `zip()`: parallel iteration of two lists
4. `zip()`: creating dict from two lists `dict(zip(keys, values))`
5. Edge case: `zip()` with unequal-length iterables

---

### Section 5: Comprehensions (~15 min)

**Concepts:**
- List comprehension: `[expr for x in iterable]`
- List comprehension with filter: `[expr for x in iterable if condition]`
- Dict comprehension: `{key: value for x in iterable}`
- Set comprehension: `{expr for x in iterable}`
- Readability guidelines: when comprehensions help vs hurt

**Code Examples:**
1. Simple list comprehension: squares
2. Filtered list comprehension: even numbers
3. Transforming list comprehension: uppercase strings
4. Dict comprehension: word lengths
5. Set comprehension: unique first letters
6. Anti-pattern: overly nested comprehension (with loop rewrite)

**Meme 2**: Comprehension readability meme (placement here)

**Teaching note:**
- Show loop version FIRST, then comprehension equivalent
- Emphasize: "Якщо не можете пояснити одним реченням — використовуйте цикл"

---

### Section 6: Складність операцій — Інтуїція (~10 min)

**Concepts:**
- O(1) vs O(n) intuition (no formal Big-O notation)
- Why dict/set lookup is fast (hash table → locker room analogy)
- Why list search is slow (must check every element)
- `hash()` function demonstration
- Practical implications: choosing the right data structure

**Code Examples:**
1. `hash()` on strings and integers
2. Timed comparison: `in` on list vs set (100,000 elements)
3. Real scenario: checking for duplicate usernames

**Cross-reference:**
- "У Лекції 2 ми навчились вимірювати час виконання. Тепер застосуємо це для порівняння структур даних."

---

### Section 7: Вступ до функцій (~15 min)

**Concepts:**
- Why functions: DRY principle, organization, reusability
- `def` statement and basic syntax
- Parameters and return values
- Default arguments
- `*args` for variadic positional arguments
- `**kwargs` for variadic keyword arguments
- Brief docstrings (one-line)
- Returning multiple values via tuple

**Code Examples:**
1. Basic function: `def greet(name): return f"Привіт, {name}!"`
2. Default arguments: `def area(width, height=1): return width * height`
3. Multiple return values: `def min_max(numbers): return min(numbers), max(numbers)`
4. `*args`: `def total(*numbers): return sum(numbers)`
5. `**kwargs`: `def build_profile(**info): return info`
6. Combining: `def log(message, *tags, level="INFO"): ...`

**Cross-reference:**
- "Пам'ятаєте баг з мутабельним аргументом за замовчуванням з Лекції 2? Тепер ми знаємо, як правильно оголошувати функції."

**Note:** Reference mutable default argument from Lecture 2 but do NOT re-explain it.

---

### Section 8: Практичні вправи (~15 min)

#### Exercise 1: Collection Operations
Given a list of student records (dicts), use comprehensions and collection methods to:
- Extract all student names
- Filter students with grades above threshold
- Create a dict of name → grade

**Solution** in hidden cell.

#### Exercise 2: Data Structure Choice
Given scenarios, choose the best data structure and implement:
- Fast membership check on 10,000 items
- Ordered sequence with duplicates
- Key-value mapping with default values

**Solution** in hidden cell.

---

### Section 9: Міні-проєкт — Парсинг логів (~15 min)

**Task**: Parse web server access logs and compute frequency table.

**Input**: Hardcoded multi-line string of log entries (see research.md R6)

**Steps:**
1. Write `parse_log_line()` function
2. Write `count_frequencies()` using dict
3. Sort and display top 5 with `enumerate()`
4. Bonus: count by HTTP method using comprehension

**Solution** in hidden cell with all steps.

**Skills exercised:** string methods, dict, comprehension, enumerate, custom functions, sorted with key.

---

### Section 10: Підсумки + Що далі

**Summary:**

```markdown
### Що ми вивчили сьогодні:

✅ **Колекції** — list, tuple, dict, set з усіма методами та підводними каменями

✅ **Пам'ять** — як колекції зберігаються всередині Python

✅ **Зрізи та вкладені структури** — індексація, slicing, вкладені дані

✅ **enumerate та zip** — ітераційні патерни для чистого коду

✅ **Comprehensions** — лаконічне створення колекцій (і коли їх НЕ використовувати)

✅ **Складність** — чому dict/set швидші за list для пошуку

✅ **Функції** — def, параметри, return, *args, **kwargs
```

**What's Next:**

```markdown
## Що далі? (What's Next)

### Лекція 4: Функції + Модулі + Помилки

- Функції глибше: lambda, функції як параметри, map/filter/reduce
- Області видимості (scope): local/global, замикання (closures)
- Виключення (exceptions): try/except/else/finally
- Модулі та імпорти: структура пакетів
- Підказки типів (type hints)

### Домашнє завдання

1. Пройдіть усі вправи з лекції
2. Напишіть функцію, що приймає текст та повертає словник частот слів
3. Перепишіть 3 цикли з попередніх лекцій у вигляді comprehensions
4. Порівняйте час пошуку в list vs set для різних розмірів (1K, 10K, 100K)
```

---

### References Section

**Official Documentation:**
- [Data Structures Tutorial](https://docs.python.org/3/tutorial/datastructures.html)
- [Built-in Types — Sequence](https://docs.python.org/3/library/stdtypes.html#sequence-types-list-tuple-range)
- [Built-in Types — Mapping](https://docs.python.org/3/library/stdtypes.html#mapping-types-dict)
- [Built-in Types — Set](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Defining Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Time Complexity](https://wiki.python.org/moin/TimeComplexity)

**Tutorials:**
- [Real Python - Python Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)
- [Real Python - Sets](https://realpython.com/python-sets/)
- [Real Python - List Comprehension](https://realpython.com/list-comprehension-python/)
- [Real Python - Defining Your Own Functions](https://realpython.com/defining-your-own-python-function/)

**Deep Dives:**
- [Laurent Luce - Python List Implementation](https://www.laurentluce.com/posts/python-list-implementation/)
- [Real Python - Hash Tables](https://realpython.com/python-hash-table/)

---

## Entity Summary

| Entity | Description | Constitution Requirement |
|--------|-------------|-------------------------|
| List | Ordered, mutable sequence with indexing/slicing | Lecture 3 topics |
| Tuple | Ordered, immutable sequence for fixed data | Lecture 3 topics |
| Dict | Key-value mapping with O(1) lookup | Lecture 3 topics |
| Set | Unordered unique elements with O(1) membership | Lecture 3 topics |
| Comprehension | Concise collection creation from iterables | Lecture 3 topics |
| Function | Named reusable code block with params/return | Lecture 3 topics |
| Frequency Table | Dict mapping items to counts (mini-project) | Lecture 3 topics |

## Time Allocation

| Section | Duration | Type |
|---------|----------|------|
| 1. Collections Deep Dive | ~25 min | Theory + code |
| 2. Memory Representation | ~10 min | Theory + diagrams |
| 3. Indexing/Slicing/Nested | ~10 min | Code-heavy |
| 4. Iteration Patterns | ~10 min | Code-heavy |
| 5. Comprehensions | ~15 min | Theory + code |
| 6. Complexity Intuition | ~10 min | Theory + timing |
| 7. Functions Introduction | ~15 min | Theory + code |
| 8. Exercises | ~15 min | Hands-on |
| 9. Mini Parsing Task | ~15 min | Hands-on |
| 10. Summary + What's Next | ~5 min | Wrap-up |
| **Total** | **~130 min** | **Fits 1.5h with breaks** |

Note: Sections 8-9 can overlap — exercises can be assigned as homework if time is tight.
