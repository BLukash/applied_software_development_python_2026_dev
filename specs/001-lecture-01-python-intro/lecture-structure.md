# Lecture Structure: Лекція 1 — Вступ до Python

**Date**: 2026-01-24
**Status**: Complete

## Notebook Structure Overview

```
lecture-01.ipynb
├── Cell 1: Header (markdown)
├── Cell 2: Learning Objectives (markdown)
├── Cell 3: Prerequisites (markdown)
├── Cells 4-10: Section 1 - What is Python (markdown + code)
├── Cells 11-18: Section 2 - Environment Setup (markdown)
├── Cells 19-25: Section 3 - Running Code (markdown + code)
├── Cells 26-35: Section 4 - venv & pip (markdown + code)
├── Cells 36-50: Section 5 - Basic Syntax (markdown + code)
├── Cells 51-58: Section 6 - Exercises (markdown + code)
├── Cell 59: Summary (markdown)
├── Cell 60: What's Next (markdown)
└── Cell 61: References (markdown)
```

---

## Section 1: Header & Introduction (~5 хв)

### Cell 1: Header (markdown)
```markdown
# Лекція 1: Вступ до Python

**Курс**: Прикладна розробка програмного забезпечення (Python)
**Дата**: [DATE]
**Тривалість**: 1.5 години

---
```

### Cell 2: Learning Objectives (markdown)
```markdown
## Цілі лекції (Learning Objectives)

Після цієї лекції ви зможете:

1. Пояснити, що таке Python та де він використовується
2. Встановити Python 3.11+ та налаштувати середовище розробки
3. Створити та активувати віртуальне середовище (virtual environment)
4. Написати та запустити свою першу Python-програму
5. Використовувати змінні, базові типи даних та f-strings
```

### Cell 3: Prerequisites (markdown)
```markdown
## Передумови (Prerequisites)

Для цієї лекції вам потрібно:
- Базові знання програмування (змінні, цикли, функції — будь-яка мова)
- Комп'ютер з Windows 10+, macOS 10.15+ або Linux
- Доступ до інтернету для завантаження Python
- Бажання вчитися! 🐍
```

---

## Section 2: What is Python (~15 хв)

### Cell 4: Introduction with Meme (markdown)
```markdown
## 1. Що таке Python?

[MEME: Python naming - Monty Python vs Snake]

Python — це високорівнева, інтерпретована (interpreted), динамічно типізована (dynamically typed) мова програмування з автоматичним керуванням пам'яттю.

**Ключові особливості:**
- 🔤 Читабельний синтаксис (readable syntax)
- 🔋 "Batteries included" — багата стандартна бібліотека
- 🌍 Кросплатформеність (cross-platform)
- 🚀 Швидка розробка (rapid development)
```

### Cell 5: History (markdown)
```markdown
### Коротка історія

| Рік | Подія |
|-----|-------|
| 1991 | Guido van Rossum випускає Python 0.9.0 |
| 2000 | Python 2.0 — list comprehensions, garbage collection |
| 2008 | Python 3.0 — несумісний з Python 2 |
| 2020 | Кінець підтримки Python 2 (End of Life) |
| 2024 | Python 3.12+ — найновіша стабільна версія |

> 💡 Назва походить від британського комедійного шоу "Monty Python's Flying Circus", а не від змії!
```

### Cell 6: Where Python is Used (markdown)
```markdown
### Де використовується Python?

| Сфера | Приклади |
|-------|----------|
| **Веб-розробка** | Django, FastAPI, Flask |
| **Data Science & ML** | pandas, NumPy, TensorFlow, PyTorch |
| **Автоматизація** | Скрипти, DevOps, тестування |
| **Наукові обчислення** | SciPy, Jupyter |
| **Ігри** | Pygame, Godot (scripting) |
| **Десктоп-додатки** | PyQt, Tkinter |

> 🏆 Python — #1 за популярністю на TIOBE Index та Stack Overflow Survey
```

### Cell 7: The Zen of Python (code)
```python
# Давайте подивимось на філософію Python
import this
```

---

## Section 3: Environment Setup (~20 хв)

### Cell 8: Installation Guide (markdown)
```markdown
## 2. Встановлення Python

### Windows

1. Завантажте Python з [python.org/downloads](https://www.python.org/downloads/)
2. **ВАЖЛИВО**: Поставте галочку ✅ "Add Python to PATH"
3. Натисніть "Install Now"
4. Перевірте в терміналі:

```cmd
python --version
# або
py --version
```

### macOS

```bash
# Через Homebrew (рекомендовано)
brew install python@3.12

# Перевірка
python3 --version
```

### Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install python3 python3-pip python3-venv

# Перевірка
python3 --version
```
```

### Cell 9: IDE Setup (markdown)
```markdown
### Налаштування IDE

#### VS Code (рекомендовано) ⭐

1. Завантажте з [code.visualstudio.com](https://code.visualstudio.com/)
2. Встановіть розширення:
   - **Python** (Microsoft) — обов'язково
   - **Pylance** — підказки та автодоповнення
   - **Jupyter** — для ноутбуків

#### PyCharm

1. Завантажте Community Edition (безкоштовно) з [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. Створіть новий проект
3. PyCharm автоматично налаштує віртуальне середовище
```

---

## Section 4: Running Code (~10 хв)

### Cell 10: Three Ways to Run (markdown)
```markdown
## 3. Способи запуску коду

| Спосіб | Опис | Коли використовувати |
|--------|------|---------------------|
| **REPL** | Інтерактивний режим | Експерименти, швидкі тести |
| **Script (.py)** | Файл з кодом | Програми, автоматизація |
| **Notebook (.ipynb)** | Jupyter notebook | Аналіз даних, навчання |
```

### Cell 11: REPL Demo (markdown + code example)
```markdown
### REPL (Read-Eval-Print Loop)

Запустіть `python` або `python3` в терміналі:
```

### Cell 12: REPL Example (code)
```python
# Це працює в REPL — спробуйте в терміналі!
2 + 2
"Hello" * 3
```

### Cell 13: Script Demo (markdown)
```markdown
### Script (.py файл)

Створіть файл `hello.py`:
```

### Cell 14: Script Example (code)
```python
# hello.py
print("Привіт з Python-скрипта!")
```

### Cell 15: Notebook Explanation (markdown)
```markdown
### Jupyter Notebook

Ви зараз читаєте Jupyter Notebook! 📓

- Комбінує код, текст та візуалізації
- Чудово для навчання та data science
- Виконуйте комірки за допомогою `Shift + Enter`
```

---

## Section 5: Virtual Environments & pip (~15 хв)

### Cell 16: Why venv (markdown)
```markdown
## 4. Віртуальні середовища (Virtual Environments)

[MEME: "Works on my machine" - Docker/venv meme]

### Навіщо потрібні?

- 🔒 Ізоляція залежностей проекту
- 🔄 Різні версії пакетів для різних проектів
- 🧹 Чистота глобального Python
- 📦 Легке відтворення середовища
```

### Cell 17: venv Commands (markdown)
```markdown
### Створення та використання venv

```bash
# Створення (виконайте в терміналі)
python -m venv .venv

# Активація (Windows cmd)
.venv\Scripts\activate.bat

# Активація (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Активація (macOS/Linux)
source .venv/bin/activate

# Ви побачите (.venv) на початку командного рядка!

# Деактивація
deactivate
```
```

### Cell 18: pip Commands (markdown)
```markdown
### pip — менеджер пакетів

```bash
# Встановлення пакету
pip install requests

# Перегляд встановлених
pip list

# Експорт залежностей
pip freeze > requirements.txt

# Встановлення з файлу
pip install -r requirements.txt
```
```

---

## Section 6: Basic Syntax (~25 хв)

### Cell 19: First Program (markdown)
```markdown
## 5. Перша програма

Класика програмування — "Hello, World!":
```

### Cell 20: Hello World (code)
```python
print("Hello, World!")
print("Привіт, Світе!")
```

### Cell 21: Variables Introduction (markdown)
```markdown
### Змінні (Variables)

В Python не потрібно оголошувати тип — він визначається автоматично:
```

### Cell 22: Variables Example (code)
```python
# Створення змінних
name = "Python"           # str (рядок)
version = 3.12           # float (число з плаваючою точкою)
year = 1991              # int (ціле число)
is_awesome = True        # bool (булевий тип)
nothing = None           # NoneType (відсутність значення)

# Перевірка типів
print(f"name: {name}, тип: {type(name)}")
print(f"version: {version}, тип: {type(version)}")
print(f"year: {year}, тип: {type(year)}")
print(f"is_awesome: {is_awesome}, тип: {type(is_awesome)}")
```

### Cell 23: Data Types Table (markdown)
```markdown
### Базові типи даних

| Тип | Опис | Приклад |
|-----|------|---------|
| `int` | Ціле число | `42`, `-7`, `0` |
| `float` | Дробове число | `3.14`, `-0.5` |
| `str` | Рядок (текст) | `"Hello"`, `'Python'` |
| `bool` | Логічний тип | `True`, `False` |
| `None` | Відсутність значення | `None` |
```

### Cell 24: Input/Output (markdown)
```markdown
### Введення та виведення (I/O)
```

### Cell 25: Input Example (code)
```python
# input() завжди повертає рядок!
name = input("Як тебе звати? ")
print(f"Привіт, {name}! Радий знайомству!")
```

### Cell 26: Operators (markdown)
```markdown
### Оператори (Operators)
```

### Cell 27: Operators Example (code)
```python
a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"a + b = {a + b}")    # Додавання
print(f"a - b = {a - b}")    # Віднімання
print(f"a * b = {a * b}")    # Множення
print(f"a / b = {a / b}")    # Ділення (float)
print(f"a // b = {a // b}")  # Цілочисельне ділення
print(f"a % b = {a % b}")    # Остача від ділення
print(f"a ** b = {a ** b}")  # Піднесення до степеня
```

### Cell 28: F-strings (markdown)
```markdown
### F-strings (форматовані рядки)

F-strings — найзручніший спосіб форматування в Python 3.6+:
```

### Cell 29: F-strings Example (code)
```python
product = "Кава"
price = 45.50
quantity = 3
total = price * quantity

# Базове використання
print(f"Товар: {product}")

# Форматування чисел
print(f"Ціна: {price:.2f} грн")
print(f"Всього: {total:.2f} грн")

# Вирази всередині f-string
print(f"3 × 45.50 = {3 * 45.50:.2f} грн")

# Вирівнювання
print(f"{'Товар':<15}: {product}")
print(f"{'Ціна':<15}: {price:.2f} грн")
```

---

## Section 7: Exercises (~15 хв)

### Cell 30: Exercise 1 (markdown)
```markdown
## 6. Практичні вправи

### Вправа 1: Програма-привітання

Напишіть програму, яка:
1. Запитує ім'я користувача
2. Запитує рік народження
3. Виводить привітання та вік користувача

**Приклад виводу:**
```
Як тебе звати? Олексій
Який рік твого народження? 2000
Привіт, Олексій! Тобі 26 років.
```
```

### Cell 31: Exercise 1 Starter (code)
```python
# Вправа 1: Напишіть ваш код тут
# Підказка: рік можна отримати через: from datetime import datetime; datetime.now().year

```

### Cell 32: Exercise 1 Solution (code - hidden)
```python
# Рішення вправи 1
from datetime import datetime

name = input("Як тебе звати? ")
birth_year = int(input("Який рік твого народження? "))
current_year = datetime.now().year
age = current_year - birth_year

print(f"Привіт, {name}! Тобі {age} років.")
```

### Cell 33: Exercise 2 (markdown)
```markdown
### Вправа 2: Простий калькулятор

Напишіть програму, яка:
1. Запитує два числа
2. Виводить результати всіх арифметичних операцій

**Приклад виводу:**
```
Введіть перше число: 10
Введіть друге число: 3
10 + 3 = 13
10 - 3 = 7
10 × 3 = 30
10 ÷ 3 = 3.33
```
```

### Cell 34: Exercise 2 Starter (code)
```python
# Вправа 2: Напишіть ваш код тут
# Підказка: використовуйте int() або float() для конвертації input()

```

### Cell 35: Exercise 2 Solution (code - hidden)
```python
# Рішення вправи 2
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} × {b} = {a * b}")
print(f"{a} ÷ {b} = {a / b:.2f}")
```

---

## Section 8: Summary & Next (~5 хв)

### Cell 36: Summary (markdown)
```markdown
## Підсумок (Summary)

### Що ми вивчили сьогодні:

✅ **Python** — інтерпретована, динамічно типізована мова з багатою екосистемою

✅ **Встановлення** — python.org, не забудьте додати до PATH!

✅ **IDE** — VS Code + Python extension або PyCharm

✅ **Запуск коду** — REPL, скрипти (.py), notebooks (.ipynb)

✅ **venv** — ізоляція залежностей проекту

✅ **pip** — встановлення пакетів

✅ **Базовий синтаксис** — змінні, типи, оператори, f-strings

✅ **I/O** — print() та input()
```

### Cell 37: What's Next (markdown)
```markdown
## Що далі? (What's Next)

### Лекція 2: Механіка Python

- Імена vs значення, посилання, мутабельність
- Модель пам'яті: list vs tuple
- Умовні оператори: if/elif/else
- Цикли: for, while
- Практичні патерни

### Домашнє завдання

1. Встановіть Python та IDE на свій комп'ютер
2. Створіть віртуальне середовище
3. Виконайте обидві вправи з лекції
4. Поекспериментуйте з REPL
```

### Cell 38: References (markdown)
```markdown
## Додаткові матеріали (References)

### Офіційна документація
- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Standard Library](https://docs.python.org/3/library/)
- [PEP 8 — Style Guide](https://peps.python.org/pep-0008/)

### Корисні ресурси
- [Real Python](https://realpython.com/) — туторіали та статті
- [VS Code Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial)
- [Corey Schafer YouTube](https://www.youtube.com/c/Coreyms) — відео-уроки

---

*Створено для курсу "Прикладна розробка програмного забезпечення (Python)" 2026*
```
