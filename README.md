# Прикладне програмне забезпечення (Python) 2026

Матеріали курсу "Прикладне програмне забезпечення (Python)". (в розробці), розрахований на 14 лекцій

## Лекції

Всі наразі готові лекції знаходяться в папці [`lectures/`](lectures/) у форматі Jupyter Notebook:

### [Лекція 1: Вступ до Python](lectures/01-python-intro/lecture-01.ipynb)
- Що таке Python — історія, характеристики, філософія
- Встановлення Python та налаштування IDE (VS Code, PyCharm)
- Способи запуску коду — REPL, скрипти (.py), Jupyter Notebook
- Віртуальні середовища (venv) та pip
- Модулі vs пакети
- Змінні та базові типи даних (int, float, str, bool, None)
- Динамічна типізація та Duck Typing
- Введення/виведення — print() та input()
- Оператори, f-рядки
- Практика: програма-привітання, простий калькулятор

### [Лекція 2: Механіка мови Python](lectures/02-core-mechanics/lecture-02.ipynb)
- Імена та об'єкти — імена як посилання, id()
- Огляд складних типів даних (list, tuple, dict, set)
- Мутабельність — мутабельні vs іммутабельні типи
- Ідентичність vs рівність — is vs ==
- Truthiness — falsy-значення, ідіоматичні перевірки
- Умовні оператори — if/elif/else, match (Python 3.10+)
- Pattern Matching — literal, sequence unpacking, guard clauses
- Цикли — for, while, range(), enumerate(), break/continue
- Патерни циклів — підрахунок, пошук, акумуляція
- Вимірювання продуктивності — time.perf_counter()

### [Лекція 3: Структури даних, «Pythonic» патерни, Функції](lectures/03-data-structures/lecture-03.ipynb)
- Колекції — list, tuple, dict, set (методи, операції)
- Зберігання в пам'яті — over-allocation, hash-таблиці
- Індексація та зрізи (slicing)
- Вкладені структури — списки словників
- enumerate(), zip() — ітераційні патерни
- Comprehensions — list, dict, set; коли НЕ використовувати (ніколи)))
- Big O складність — list O(n) vs dict/set O(1)
- Вступ до функцій — def, параметри, return, docstrings
- Аргументи функцій — default, *args, **kwargs
- Практика: парсинг логів та частотний аналіз

### [Лекція 4: Функції, Модулі, Помилки](lectures/04-functions-modules-errors-oop/lecture-04.ipynb)
- Lambda-вирази та анонімні функції
- Функції як параметри — сортування з key
- map(), filter(), reduce() — функціональне програмування
- Ітератори та генератори
- Scope та замикання — правило LEGB
- Декоратори — обгортання функцій
- Type Hints — базові анотації типів
- Імпорт — import, from...import, import...as
- Стандартна бібліотека та власні модулі
- Структура пакетів — \_\_init\_\_.py
- Винятки — try/except/else/finally, ієрархія винятків
- Модуль logging

### [Лекція 5: ООП в Python та Робота з файлами](lectures/05-oop-files/lecture-05.ipynb)
- Основи ООП — class, \_\_init\_\_, self, атрибути
- Чотири принципи ООП — інкапсуляція, наслідування, поліморфізм, абстракція
- Magic-методи — \_\_str\_\_, \_\_repr\_\_, \_\_eq\_\_ тощо
- Композиція > Наслідування
- Pythonic ООП — @property, @classmethod, @staticmethod, @dataclass, ABC
- Файловий ввід/вивід — open(), контекстні менеджери (with), кодування
- pathlib.Path — сучасний API для роботи з шляхами
- JSON — серіалізація/десеріалізація даних
- CSV — робота з табличними даними
- Міні-проект: книга контактів (ООП + файлова персистенція)

## Експериментальний репозиторій

Цей репозиторій є експериментальним — лекції частково створені за допомогою AI-інструментів (Claude Code, SpecKit).

Якщо знайшли помилку або маєте пропозиції — створюйте Issues та Pull Requests.

## Розробка лекцій (SpecKit)

Для створення або покращення лекцій використовується SpecKit workflow:
(https://github.com/github/spec-kit)

```bash
# 1. Створити специфікацію нової фічі
/speckit.specify

# 2. Спланувати імплементацію
/speckit.plan

# 3. Згенерувати список задач
/speckit.tasks

# 4. Виконати задачі
/speckit.implement
```

Конституція курсу: [`.specify/memory/constitution.md`](.specify/memory/constitution.md)
