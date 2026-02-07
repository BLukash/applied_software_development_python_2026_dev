# Research: Lecture 2 Content Restructuring

**Branch**: `004-lecture2-restructure` | **Date**: 2026-02-06

## Research Tasks Completed

### 1. Lecture 1 Analysis (For Consistency)

**Tone Patterns Identified:**
- Ukrainian text with English terms in parentheses on first use: "інтерпретована (interpreted)", "динамічно типізована (dynamically typed)"
- Direct address using "ви/вам/тобі"
- Historical/philosophical context for design decisions (e.g., ABC language history)
- Tables for comparisons (Release cycle, Typing matrix, Where Python is used)
- Memes at section starts (2 per lecture)
- Code examples with visible outputs shown

**Content Already Covered (MUST NOT repeat):**
- How Python code executes (bytecode, PVM, parsing) - covered with GIF diagram
- GIL explanation with `sys._is_gil_enabled()` example
- Duck typing with `quack()` example class hierarchy
- Dynamic vs static typing matrix with comparison table
- Basic types (`int`, `float`, `str`, `bool`, `None`) with `type()` examples
- Dynamic typing concept and "Сильна vs Слабка типізація"
- Variables, basic operators, f-strings
- venv, pip, modules vs packages

**Cross-References to Use:**
- "Як ми бачили у Лекції 1, Python — динамічно типізована мова..."
- "Пам'ятаєте duck typing з першої лекції? Тепер подивимось глибше..."
- Reference to PVM when explaining timing performance

### 2. Current Lecture 2 Structure Analysis

**Current Cell Mapping:**
| Section | Cells | Content Summary |
|---------|-------|-----------------|
| Header + Objectives | 0-2 | Title, learning objectives, prerequisites |
| Intro | 3 | Cross-ref to Lecture 1, duck typing mention |
| Names & Objects | 4-10 | Concept, id(), aliasing examples (includes list!) |
| Mutability | 11-17 | Concept, table, list alias, string immutable, mutable default bug |
| Memory Representation | 18-21 | PyObject structure, sys.getsizeof(), tuple efficiency |
| Identity vs Equality | 22-29 | is vs ==, int caching, lists, None, string interning, warning |
| Truthiness | 30-35 | Falsy values, idioms, chaining, short-circuit |
| Control Flow | 36-46 | if/elif/else, match (3 examples), for, while, for...else, enumerate |
| Practical Patterns | 47-50 | Counting, search with early exit, accumulation |
| Timing | 51-55 | perf_counter, loop vs builtin comparison, PVM reference |
| Exercises | 56-65 | 3 exercises with solutions |
| Summary | 66-67 | Bullet points, What's Next |
| References | 68 | Documentation links |

### 3. Content to Move/Split Analysis

**Names & Objects Section (cells 4-10):**
- cells 4-5: Concept explanation (KEEP)
- cell 6: Basic id() with int (KEEP)
- cell 7: Empty (SKIP)
- cell 8: [Output] (N/A)
- cells 9-10: List aliasing examples → MOVE to Identity (Lists) section

**Rationale:** The list aliasing example in Names & Objects is premature. Students haven't learned what lists are yet in the new flow.

**Memory Representation (cells 18-21):**
- All cells MOVE immediately after Names & Objects
- Natural connection: "You now know names point to objects. Let's see how those objects are stored in memory."

**Identity vs Equality (cells 22-29):**
- cells 22-23: Concept intro, table (KEEP in Simple Types section)
- cells 24-25: Integer caching (KEEP in Simple Types section)
- cells 26: List comparison → MOVE to Identity (Lists) section
- cells 27: None checking (KEEP in Simple Types section)
- cells 28-29: String interning, warning (KEEP in Simple Types section)

### 4. New Content Requirements

**Complex Data Types Introduction (NEW SECTION):**

**Decision:** Create a brief (~5-7 minute) section introducing:
- `list` - ordered, mutable collection: `[1, 2, 3]`
- `tuple` - ordered, immutable collection: `(1, 2, 3)`
- `dict` - key-value mapping: `{"key": "value"}`
- `set` - unordered, unique elements: `{1, 2, 3}`

**Rationale:** Students need to know WHAT these types are before they can understand mutability examples. Lecture 3 will cover them in depth.

**Content Constraints:**
- No advanced features (comprehensions, methods beyond basics)
- No indexing/slicing (Lecture 3)
- Focus on: syntax, basic purpose, mutable vs immutable preview
- Explicit statement: "Деталі роботи з цими типами — у Лекції 3"

**Code Examples Needed:**
```python
# Brief list introduction
numbers = [1, 2, 3]
print(type(numbers))  # <class 'list'>

# Brief tuple introduction
point = (10, 20)
print(type(point))  # <class 'tuple'>

# Brief dict introduction
person = {"name": "Іван", "age": 25}
print(type(person))  # <class 'dict'>

# Brief set introduction
unique = {1, 2, 3, 2, 1}  # Duplicates removed
print(unique)  # {1, 2, 3}
```

### 5. Transition Text Research

**Best Practices for Section Transitions:**
- Each transition should answer: "Why are we learning this now?"
- Connect to previous concept
- Preview what's coming
- Keep to 1-2 sentences

**Proposed Transitions (in Ukrainian):**

1. **Names → Memory:**
   "Тепер, коли ми розуміємо, що імена — це посилання на об'єкти, подивимося, як ці об'єкти зберігаються в пам'яті."

2. **Memory → Identity (Simple):**
   "Знаючи структуру об'єктів у пам'яті, ми можемо зрозуміти різницю між ідентичністю (identity) та рівністю (equality). Почнемо з простих типів."

3. **Identity (Simple) → Complex Types:**
   "Ми побачили, як `is` та `==` працюють з числами та рядками. Перш ніж йти далі, познайомимося зі складними типами даних."

4. **Complex Types → Mutability:**
   "Тепер, коли ви знаєте, що таке списки, словники та множини, ми можемо поговорити про їх ключову властивість — мутабельність (mutability)."

5. **Mutability → Identity (Lists):**
   "Розуміючи мутабельність, повернемося до порівняння `is` та `==` — цього разу на прикладі списків, де різниця критична."

### 6. Exercises Impact Analysis

**Current Exercises:**
1. Predict list aliasing result → Still valid (after restructure)
2. Fix mutable default argument bug → Still valid
3. Control flow challenge → No changes needed

**Recommendation:** Keep exercises as-is. They work with restructured content since students will have seen all necessary concepts by exercise time.

### 7. Summary Section Updates

**Current Summary Order:**
1. Names & Objects
2. Mutability
3. is vs ==
4. Truthiness
5. Control flow
6. Timing

**New Summary Order:**
1. Names & Objects
2. Memory Representation
3. Identity vs Equality (simple types)
4. Complex Data Types (new)
5. Mutability
6. Identity vs Equality (lists)
7. Truthiness
8. Control flow
9. Timing

## Decisions Made

| Topic | Decision | Rationale |
|-------|----------|-----------|
| List example in Names section | Move to Identity (Lists) | Students need to know lists first |
| Complex Types depth | Brief intro only | Lecture 3 has detailed coverage |
| Meme positions | Keep both existing | mutability-bug and timing are well-placed |
| Exercises | No changes | Already work with restructured flow |
| Duration impact | Minimal (+5 min for Complex Types) | Brief intro, moving content doesn't add time |

## Alternatives Considered

| Alternative | Rejected Because |
|-------------|------------------|
| Keep list example in Names section | Students haven't learned lists yet in new flow |
| Full Complex Types coverage | Would duplicate Lecture 3 content |
| Add new meme for Complex Types | Constitution says 2 memes per lecture (already met) |
| Split lecture into two | Restructure should fit in 1.5 hours |

## Dependencies Identified

1. **Lecture 1**: Must not duplicate basic types explanation
2. **Lecture 3**: Must coordinate - Complex Types intro here, details there
3. **Assets**: No new diagrams needed (existing memory-model.png sufficient)
