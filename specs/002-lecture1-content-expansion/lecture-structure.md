# Lecture 1 Content Expansion: Cell-by-Cell Structure

**Feature**: 002-lecture1-content-expansion
**Date**: 2026-01-25

This document defines the new and modified cells for Lecture 1 expansion.

---

## Section 1: Що таке Python? (Enhanced)

### NEW CELL: Чому Python виглядає саме так? (After cell-5)

**Type**: Markdown
**Duration**: ~5 min

```markdown
### Чому Python виглядає саме так?

Щоб зрозуміти Python, треба знати його історію. У 1980-х роках Guido van Rossum працював над мовою ABC у дослідницькому центрі CWI в Нідерландах. ABC була навчальною мовою з цікавими ідеями:

**Що Python взяв від ABC:**
- Відступи (indentation) замість фігурних дужок — це було революційно!
- Високорівневі структури даних (списки, словники)
- Простий синтаксис: IF, WHILE, FOR без зайвого "шуму"

**Що Guido змінив:**

> "ABC була монолітною — розробники мови були 'богами', і не було способу її розширити. Це мене фруструвало." — Guido van Rossum

Python став **розширюваним**: маленьке ядро + величезна стандартна бібліотека + легкість написання модулів. Ця філософія зробила Python таким популярним.

**Чому відступи, а не дужки?**

```python
# Python: відступи роблять структуру очевидною
if condition:
    do_something()
    do_more()

# C/Java: дужки можна забути або поставити неправильно
if (condition) {
    do_something();
    do_more();
}
```

Guido вважав, що якщо програмісти і так використовують відступи для читабельності, чому б не зробити їх частиною синтаксису? Менше коду — менше помилок.
```

---

### NEW CELL: Філософія релізів Python (After ABC storytelling)

**Type**: Markdown
**Duration**: ~3 min

```markdown
### Філософія релізів Python

Python має передбачуваний цикл релізів (release cycle):

| Етап | Тривалість | Що відбувається |
|------|------------|-----------------|
| Альфа-версії | 7 місяців | Нові функції, виправлення |
| Бета-версії | 3 місяці | Тільки виправлення, без нових функцій |
| Release candidates | 2 місяці | Фінальне тестування |
| **Реліз** | Жовтень | Нова версія Python X.Y.0 |

**Підтримка версій:**
- 2 роки повної підтримки (full support)
- 3 роки тільки безпекових оновлень (security fixes)
- Всього 5 років підтримки кожної версії

**Для студентів це означає:**
- Завжди використовуйте версію з повною підтримкою (зараз 3.12+)
- Не бійтеся нових версій — deprecation warnings з'являються за 2 роки до видалення
- Слідкуйте за [Python Versions Status](https://devguide.python.org/versions/)
```

---

### NEW CELL: Чому Python крутий + де повільний (After release philosophy)

**Type**: Markdown
**Duration**: ~5 min

```markdown
### Чому Python крутий?

**1. Читабельність — це закон**
```python
# Python: читається як англійська
if user in admin_users and user.is_active:
    grant_access()
```

**2. "Batteries included"**
- HTTP сервер? `python -m http.server`
- JSON? `import json`
- Дати? `from datetime import datetime`
- Тести? `import unittest`

**3. Екосистема**
- PyPI: 500,000+ пакетів
- Спільнота: Stack Overflow, Real Python, YouTube
- Наукова база: NumPy, pandas, TensorFlow

**4. Швидка розробка**
- Прототип за години, не дні
- REPL для експериментів
- Динамічна типізація = менше boilerplate

### Де Python повільний?

**Global Interpreter Lock (GIL)** — механізм CPython, який дозволяє виконувати тільки один потік (thread) Python-коду одночасно.

**Коли це НЕ проблема:**
- Веб-додатки (I/O-bound: чекаємо на мережу/базу)
- Скрипти та автоматизація
- Data science з NumPy/pandas (обчислення в C)

**Коли це проблема:**
- CPU-bound задачі, які потребують паралелізму
- Реальний час з жорсткими вимогами до latency

**Рішення:**
- `multiprocessing` — окремі процеси замість потоків
- NumPy/Cython — обчислення поза GIL
- asyncio — для I/O-bound конкурентності
- Python 3.13+ — експериментальний режим без GIL (PEP 703)

> Не оптимізуйте завчасно! Python достатньо швидкий для більшості задач.
```

---

## Section 4: Virtual Environments (Enhanced)

### MODIFIED CELL: cell-18 (Expanded venv explanation)

**Type**: Markdown
**Duration**: +3 min

```markdown
---

## 4. Віртуальні середовища (Virtual Environments)

![Works on my machine](assets/memes/works-on-my-machine.png)

### Навіщо потрібні?

- Ізоляція залежностей проекту
- Різні версії пакетів для різних проектів
- Чистота глобального Python
- Легке відтворення середовища

### Як venv працює всередині?

Коли ви створюєте venv, Python робить наступне:

```
.venv/
├── pyvenv.cfg          # Конфігурація: шлях до базового Python
├── Scripts/ (Windows)  # або bin/ (Linux/Mac)
│   ├── activate        # Скрипт активації
│   ├── python.exe      # Симлінк на базовий Python
│   └── pip.exe         # pip для цього середовища
└── Lib/
    └── site-packages/  # ← Ваші пакети встановлюються СЮДИ
```

**Що відбувається при активації:**
1. PATH модифікується — `.venv/Scripts` стає першим
2. `sys.prefix` вказує на `.venv` замість глобального Python
3. `pip install` тепер встановлює в `.venv/Lib/site-packages`

Це означає: різні проекти можуть мати різні версії одного пакету!
```

---

### NEW CELL: Розширені команди pip (After cell-20)

**Type**: Markdown
**Duration**: ~3 min

```markdown
### Розширені команди pip

```bash
# Інформація про пакет
pip show requests
# Name: requests
# Version: 2.31.0
# Requires: charset-normalizer, idna, urllib3, certifi

# Перевірка сумісності залежностей
pip check
# No broken requirements found.

# Видалення пакету
pip uninstall requests

# Встановлення конкретної версії
pip install requests==2.28.0

# Оновлення пакету
pip install --upgrade requests

# Встановлення з requirements.txt
pip install -r requirements.txt
```

**Про PyPI (Python Package Index):**
- pypi.org — офіційний репозиторій пакетів
- 500,000+ пакетів
- pip автоматично завантажує звідти
- Перевіряйте популярність та актуальність пакетів перед використанням!
```

---

### NEW CELL: Модулі vs Пакети (After expanded pip)

**Type**: Markdown
**Duration**: ~5 min

```markdown
### Модулі vs Пакети

**Модуль (module)** — це один `.py` файл:
```python
# utils.py — це модуль
def greet(name):
    return f"Hello, {name}!"
```

**Пакет (package)** — це директорія з `__init__.py`:
```
mypackage/
├── __init__.py      # Робить директорію пакетом
├── module1.py       # mypackage.module1
└── module2.py       # mypackage.module2
```

**Як Python шукає імпорти** (`sys.path`):
1. Директорія скрипта (або поточна в REPL)
2. `PYTHONPATH` (змінна середовища)
3. Стандартна бібліотека
4. `site-packages` (встановлені пакети)

![Modules vs Packages](assets/diagrams/modules-packages.png)

**Типова помилка початківців:**
```python
# Файл називається random.py
import random  # Імпортує ВАШ random.py, не стандартний!
```
Не називайте файли так само, як стандартні модулі!
```

---

### NEW CELL: Приклад імпорту (Code cell after modules explanation)

**Type**: Code
**Duration**: ~2 min

```python
# Подивимось, де Python шукає модулі
import sys

print("Python шукає модулі в таких місцях:")
for i, path in enumerate(sys.path[:5], 1):
    print(f"{i}. {path}")

# Перевіримо, звідки взявся модуль os
import os
print(f"\nМодуль os знаходиться: {os.__file__}")
```

---

## Section 5: Типи даних (Enhanced)

### NEW CELL: Duck Typing (After cell-25 - basic types table)

**Type**: Markdown
**Duration**: ~4 min

```markdown
### Динамічна типізація та Duck Typing

Python — це **динамічно типізована** мова. Але що це означає?

**Статична vs Динамічна типізація:**
- **Статична** (Java, C#): тип перевіряється при компіляції
- **Динамічна** (Python): тип перевіряється при виконанні

**Сильна vs Слабка типізація:**
- **Сильна** (Python): `"5" + 5` = помилка!
- **Слабка** (JavaScript): `"5" + 5` = `"55"` (автоматичне перетворення)

| | Сильна | Слабка |
|---|--------|--------|
| **Статична** | Java, C#, Rust | C, C++ |
| **Динамічна** | **Python**, Ruby | JavaScript |

**Python = Динамічна + Сильна типізація**

### Duck Typing

> "Якщо воно ходить як качка і крякає як качка — це качка."

Python не перевіряє ТИП об'єкта — він перевіряє ПОВЕДІНКУ:
```python
# Функція len() працює з будь-чим, що має метод __len__
len("hello")     # str має __len__ → 5
len([1, 2, 3])   # list має __len__ → 3
len({"a": 1})    # dict має __len__ → 1
```

Неважливо, який тип — важливо, чи може об'єкт "крякати"!
```

---

### NEW CELL: Duck Typing Code Example (After explanation)

**Type**: Code
**Duration**: ~3 min

```python
# Duck Typing в дії

class Duck:
    def quack(self):
        return "Кря-кря!"

class Person:
    def quack(self):
        return "Я імітую качку: кря!"

class Robot:
    def quack(self):
        return "QUACK.WAV"

# Функція не перевіряє тип — тільки наявність методу quack()
def make_it_quack(thing):
    print(thing.quack())

# Всі ці об'єкти "крякають" — значить, вони всі "качки"!
make_it_quack(Duck())
make_it_quack(Person())
make_it_quack(Robot())

# Але якщо об'єкт не вміє крякати...
class Cat:
    def meow(self):
        return "Мяу!"

# make_it_quack(Cat())  # AttributeError: 'Cat' object has no attribute 'quack'
```

---

## Section: References (Completely Replaced)

### REPLACED CELL: cell-40 (New structured references)

**Type**: Markdown

```markdown
## Додаткові матеріали (References)

### Офіційна документація
- [Python Tutorial](https://docs.python.org/3/tutorial/) — офіційний підручник для початківців
- [Python Standard Library](https://docs.python.org/3/library/) — довідник стандартної бібліотеки
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/) — стандарт оформлення коду
- [Python Versions Status](https://devguide.python.org/versions/) — статус підтримки версій

### Туторіали та статті
- [Real Python](https://realpython.com/) — якісні туторіали з прикладами (рекомендовано)
  - [Virtual Environments Primer](https://realpython.com/python-virtual-environments-a-primer/) — глибоке пояснення venv
  - [Duck Typing in Python](https://realpython.com/duck-typing-python/) — duck typing з прикладами
  - [Python Modules and Packages](https://realpython.com/python-modules-packages/) — організація коду
- [Python Morsels](https://www.pythonmorsels.com/) — щотижневі вправи (англ.)

### Відеокурси
- [Corey Schafer YouTube](https://www.youtube.com/c/Coreyms) — безкоштовні відео-уроки (англ.)
- [ArjanCodes YouTube](https://www.youtube.com/@ArjanCodes) — архітектура та best practices (англ.)

### Практика
- [Python Data Types Quiz](https://realpython.com/quizzes/python-data-types/) — перевірте свої знання
- [Exercism Python Track](https://exercism.org/tracks/python) — задачі з менторством (безкоштовно)
- [LeetCode](https://leetcode.com/) — алгоритмічні задачі (безкоштовно + платні)

### Рекомендований шлях навчання

**Якщо ви новачок у програмуванні:**
1. Офіційний Python Tutorial
2. Real Python — базові статті
3. Exercism — прості задачі

**Якщо у вас є досвід в інших мовах:**
1. Real Python — специфіка Python (duck typing, venv)
2. PEP 8 — стиль коду
3. Corey Schafer — відео для швидкого огляду

---

*Створено для курсу "Прикладна розробка програмного забезпечення (Python)" 2026*
```

---

## New Diagrams Required

### 1. typing-matrix.png

**Description**: 2x2 matrix showing static/dynamic vs strong/weak typing with language examples
**Style**: Consistent with existing Python blue/yellow color scheme
**Content**:
- Quadrants labeled with language examples
- Python highlighted in "Dynamic + Strong" quadrant

### 2. modules-packages.png

**Description**: Visual showing the difference between module (file) and package (directory)
**Style**: Consistent with existing diagrams
**Content**:
- Single .py file → Module
- Directory with __init__.py → Package
- Import path visualization

---

## Summary: New Cells Count

| Type | Count | Estimated Time |
|------|-------|----------------|
| New Markdown cells | 8 | ~25 min reading |
| New Code cells | 2 | ~5 min execution |
| Modified cells | 1 | — |
| Replaced cells | 1 | — |
| New diagrams | 2 | — |

**Total new content**: ~30 min additional time
**Total lecture time**: ~105 min (within 1.5 hr limit)
