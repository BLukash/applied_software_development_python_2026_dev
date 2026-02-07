# Section Contracts: Lecture 2 Restructuring

**Branch**: `004-lecture2-restructure` | **Date**: 2026-02-06

This document specifies the exact content and structure for each modified or new section.

---

## Section 4: Complex Data Types (NEW)

### Contract

**Purpose:** Brief introduction to complex types so students can understand mutability examples.

**Duration:** 7 minutes maximum

**MUST include:**
- list, tuple, dict, set syntax and basic purpose
- Type preview table (mutable/immutable hint)
- Explicit reference to Lecture 3

**MUST NOT include:**
- Indexing/slicing
- Methods beyond basic creation
- Comprehensions
- Iteration patterns
- Performance characteristics (beyond tuple efficiency already covered)

### Content Specification

#### Markdown Introduction
```markdown
---

# 4. Складні Типи Даних (Complex Data Types)

Ми побачили, як `is` та `==` працюють з числами та рядками. Перш ніж йти далі, познайомимося зі складними типами даних.

> 💡 Детальне вивчення цих типів — у Лекції 3. Тут ми лише познайомимося з ними.

### Огляд типів

| Тип | Опис | Приклад | Мутабельний? |
|-----|------|---------|--------------|
| `list` | Впорядкована колекція | `[1, 2, 3]` | Так |
| `tuple` | Впорядкована незмінна колекція | `(1, 2, 3)` | Ні |
| `dict` | Пари ключ-значення | `{"a": 1}` | Так |
| `set` | Унікальні елементи | `{1, 2, 3}` | Так |
```

#### Code Cell 1: List and Tuple
```python
# Список (list) — впорядкована, змінювана колекція
numbers = [1, 2, 3, 4, 5]
print(f"Список: {numbers}, тип: {type(numbers)}")

# Кортеж (tuple) — впорядкована, НЕЗМІНЮВАНА колекція
point = (10, 20)
print(f"Кортеж: {point}, тип: {type(point)}")
```

#### Code Cell 2: Dict and Set
```python
# Словник (dict) — пари "ключ: значення"
person = {"name": "Іван", "age": 25, "city": "Київ"}
print(f"Словник: {person}, тип: {type(person)}")

# Множина (set) — унікальні елементи (дублікати видаляються)
unique = {1, 2, 3, 2, 1}  # Дублікати автоматично видалено
print(f"Множина: {unique}, тип: {type(unique)}")
```

#### Markdown Conclusion
```markdown
### Чому це важливо зараз?

У наступному розділі ми поговоримо про **мутабельність** — здатність об'єкта змінюватися. Це критично важливо розуміти для:
- `list`, `dict`, `set` — можна змінювати "на місці"
- `tuple` — не можна змінювати після створення

Ви побачите, як ця різниця впливає на поведінку коду.
```

---

## Section 1: Names & Objects (MODIFIED)

### Contract

**Changes:** Remove list aliasing examples (cells 9-10). These move to Section 6.

**Current content to KEEP:**
- cells 4-5: Concept explanation with balloon analogy
- cell 6: Basic `id()` with integer
- cell 7-8: (empty/output - skip)

**Current content to REMOVE/MOVE:**
- cells 9-10: List aliasing (`a = [1,2,3]; b = a`) → Move to Section 6

### Modified Code Cell (Replace cell 9-10 content)

Instead of list aliasing, show simple integer rebinding:
```python
# Перепривласнення створює нове посилання
a = 42
print(f"Початкове id(a): {id(a)}")

a = 100  # a тепер посилається на НОВИЙ об'єкт
print(f"Нове id(a): {id(a)}")

# Старий об'єкт 42 все ще існує, якщо хтось на нього посилається
```

---

## Section 3: Identity vs Equality (Simple Types) (SPLIT)

### Contract

**Keep from original Section 4:**
- cells 22-23: is vs == concept and table
- cells 24-25: Integer caching examples
- cell 27: None checking (`is None`)
- cells 28-29: String interning, warning

**Move to Section 6:**
- cell 26: List comparison (`list1 == list2`, `list1 is list2`)

### Section Header (Replace)
```markdown
---

# 3. Ідентичність vs Рівність: Прості Типи (Identity vs Equality: Simple Types)

Знаючи структуру об'єктів у пам'яті, ми можемо зрозуміти різницю між ідентичністю (identity) та рівністю (equality). Почнемо з простих типів.
```

---

## Section 6: Identity vs Equality (Lists) (NEW SPLIT)

### Contract

**Purpose:** Apply identity/equality concepts to mutable types after students understand mutability.

**Content sources:**
- From Names section (cells 9-10): List aliasing
- From Identity section (cell 26): List is vs ==
- New: Copy example

### Content Specification

#### Markdown Introduction
```markdown
---

# 6. Ідентичність vs Рівність: Списки (Identity vs Equality: Lists)

Розуміючи мутабельність, повернемося до порівняння `is` та `==` — цього разу на прикладі списків, де різниця критична.
```

#### Code Cell 1: Aliasing (moved from Section 1)
```python
# Один об'єкт, кілька імен (aliasing)
a = [1, 2, 3]
b = a  # b тепер посилається на ТОЙ САМИЙ об'єкт

print(f"a = {a}")
print(f"b = {b}")
print(f"id(a) = {id(a)}")
print(f"id(b) = {id(b)}")
print(f"a is b: {a is b}")  # True - це один і той самий об'єкт!

# Зміна через b змінює і a!
b.append(4)
print(f"\nПісля b.append(4):")
print(f"a = {a}")  # [1, 2, 3, 4] - змінився теж!
```

#### Code Cell 2: Equality vs Identity (moved from Section 4)
```python
# is vs == зі списками
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print("list1 = [1, 2, 3]")
print("list2 = [1, 2, 3]")
print("list3 = list1")
print()
print(f"list1 == list2: {list1 == list2}")  # True - однакові значення
print(f"list1 is list2: {list1 is list2}")  # False - різні об'єкти
print(f"list1 is list3: {list1 is list3}")  # True - той самий об'єкт
```

#### Code Cell 3: Copy (NEW)
```python
# Копіювання створює НОВИЙ об'єкт
original = [1, 2, 3]
copy = original.copy()  # або list(original), або original[:]

print(f"original: {original}")
print(f"copy: {copy}")
print(f"original == copy: {original == copy}")  # True - однакові значення
print(f"original is copy: {original is copy}")  # False - різні об'єкти

# Тепер зміни copy НЕ впливають на original
copy.append(4)
print(f"\nПісля copy.append(4):")
print(f"original: {original}")  # [1, 2, 3] - не змінився
print(f"copy: {copy}")          # [1, 2, 3, 4]
```

#### Markdown Summary
```markdown
### Підсумок: коли використовувати is vs ==

| Ситуація | Оператор | Чому |
|----------|----------|------|
| Порівняння значень | `==` | Перевіряє вміст |
| Перевірка на `None` | `is None` | `None` — синглтон |
| Перевірка, чи той самий об'єкт | `is` | Рідко потрібно |

> ⚠️ **Правило**: завжди використовуйте `==` для порівняння значень. `is` — тільки для `None`, `True`, `False`.
```

---

## Summary Section (UPDATED)

### Contract

Update the summary bullet points to reflect new order:

```markdown
---

# Підсумок (Summary)

### Що ми вивчили сьогодні:

- **Імена та об'єкти** — імена є посиланнями на об'єкти, не контейнерами

- **Представлення в пам'яті** — PyObject структура, overhead кожного об'єкта

- **is vs == (прості типи)** — ідентичність проти рівності; кешування цілих чисел; завжди `is None`

- **Складні типи даних** — list, tuple, dict, set (детально у Лекції 3)

- **Мутабельність** — `list`/`dict`/`set` можна змінювати, `str`/`int`/`tuple` — ні

- **is vs == (списки)** — критична різниця для мутабельних типів

- **Truthiness** — falsy значення та ідіоматичні перевірки

- **Control flow** — `if/elif/else`, `match`, `for`, `while`, `break`/`continue`

- **Вимірювання часу** — `time.perf_counter()` для бенчмарків
```

---

## Cell Movement Summary

| Original Cell | Original Section | New Section | Action |
|---------------|------------------|-------------|--------|
| 4-8 | Names & Objects | Section 1 | KEEP |
| 9-10 | Names & Objects | Section 6 | MOVE |
| 11-17 | Mutability | Section 5 | MOVE (renumber) |
| 18-21 | Memory | Section 2 | MOVE |
| 22-25 | Identity | Section 3 | KEEP (subset) |
| 26 | Identity | Section 6 | MOVE |
| 27-29 | Identity | Section 3 | KEEP |
| 30-35 | Truthiness | Section 7 | KEEP (renumber) |
| 36-46 | Control Flow | Section 8 | KEEP (renumber) |
| 47-50 | Patterns | Section 9 | KEEP (renumber) |
| 51-55 | Timing | Section 10 | KEEP (renumber) |
| NEW | - | Section 4 | ADD |
