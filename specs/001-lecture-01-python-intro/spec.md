# Feature Specification: Лекція 1 — Вступ до Python: середовище, інструменти, основи мови

**Feature Branch**: `001-lecture-01-python-intro`
**Created**: 2026-01-24
**Status**: Draft
**Input**: Create first lecture based on constitution plan

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Студент вперше знайомиться з Python (Priority: P1)

Студент, який ніколи не працював з Python (але має базові знання програмування), відкриває лекцію та крок за кроком налаштовує своє середовище розробки, запускає перший скрипт і розуміє базові концепції мови.

**Why this priority**: Це фундаментальний сценарій — без успішного налаштування середовища студент не зможе продовжити курс.

**Independent Test**: Студент може самостійно встановити Python, створити віртуальне середовище, написати та запустити скрипт з print() та input().

**Acceptance Scenarios**:

1. **Given** студент без встановленого Python, **When** він слідує інструкціям лекції, **Then** він успішно встановлює Python 3.11+ та перевіряє версію в терміналі
2. **Given** встановлений Python, **When** студент створює venv та активує його, **Then** він бачить (venv) у командному рядку
3. **Given** активоване середовище, **When** студент запускає print("Hello, World!"), **Then** він бачить вивід у консолі

---

### User Story 2 - Студент розуміє екосистему Python (Priority: P2)

Студент отримує загальне уявлення про мову Python: її історію, філософію, сфери застосування та чому вона популярна.

**Why this priority**: Контекст допомагає мотивувати вивчення, але не блокує практичну роботу.

**Independent Test**: Студент може пояснити 3 ключові особливості Python та назвати 3 сфери його застосування.

**Acceptance Scenarios**:

1. **Given** студент читає вступну частину, **When** він завершує секцію "Що таке Python", **Then** він може пояснити що означає "інтерпретована", "динамічна" мова
2. **Given** студент переглянув приклади застосування, **When** його запитують про сфери використання, **Then** він називає мінімум 3 (веб, аналіз даних, автоматизація, ML)

---

### User Story 3 - Студент опановує базовий синтаксис (Priority: P1)

Студент вивчає змінні, базові типи даних, оператори та форматування рядків через практичні приклади.

**Why this priority**: Базовий синтаксис необхідний для всіх наступних лекцій.

**Independent Test**: Студент може написати скрипт, який запитує ім'я та вік користувача і виводить привітання з використанням f-string.

**Acceptance Scenarios**:

1. **Given** студент вивчив типи даних, **When** він створює змінні різних типів, **Then** він може перевірити їх тип через type()
2. **Given** студент розуміє f-strings, **When** він пише форматований вивід, **Then** результат коректно підставляє значення змінних
3. **Given** студент знає про input(), **When** він пише інтерактивну програму, **Then** програма коректно зчитує та обробляє ввід

---

### Edge Cases

- Що робити, якщо студент має стару версію Python (2.x або 3.9)?
- Як вирішити проблеми з PATH на Windows?
- Що робити, якщо venv не активується (різні shell: cmd, PowerShell, bash)?
- Як працювати, якщо немає прав адміністратора для встановлення?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: Лекція MUST містити чіткі learning objectives на початку (3-5 пунктів)
- **FR-002**: Лекція MUST включати покрокові інструкції встановлення Python 3.11+ для Windows, macOS та Linux
- **FR-003**: Лекція MUST демонструвати різницю між REPL, скриптом та notebook з прикладами коли використовувати кожен
- **FR-004**: Лекція MUST містити мінімум 5 runnable code examples з поясненнями
- **FR-005**: Лекція MUST включати 2 практичні вправи з рішеннями
- **FR-006**: Лекція MUST містити мінімум 2 мемів для полегшення сприйняття матеріалу
- **FR-007**: Лекція MUST включати діаграму або таблицю (наприклад, порівняння типів даних)
- **FR-008**: Лекція MUST бути написана українською мовою з англійськими термінами в дужках при першому вживанні
- **FR-009**: Лекція MUST містити секцію "Prerequisites" (для Lecture 1: базові знання програмування)
- **FR-010**: Лекція MUST завершуватись секціями "Підсумок" та "Що далі"
- **FR-011**: Лекція MUST містити посилання на офіційну документацію та додаткові матеріали (не російськомовні)

### Content Structure Requirements

- **FR-012**: Lecture MUST follow Jupyter Notebook format (.ipynb) with markdown and code cells
- **FR-013**: Content MUST fit within 1.5-hour lecture duration
- **FR-014**: Code comments MAY be in English for industry-standard terminology

### Topics Coverage (per Constitution)

- **FR-015**: MUST cover: What Python is (interpreted, dynamic, batteries-included) + where it's used
- **FR-016**: MUST cover: Installing Python 3.11+, checking versions, PATH
- **FR-017**: MUST cover: IDE choice (VS Code / PyCharm) + recommended extensions
- **FR-018**: MUST cover: Running code: REPL vs script vs notebook (when to use what)
- **FR-019**: MUST cover: venv basics: create/activate/deactivate
- **FR-020**: MUST cover: pip basics: install/list/freeze, requirements.txt
- **FR-021**: MUST cover: First program + simple I/O: print(), input()
- **FR-022**: MUST cover: Variables, basic types (int, float, str, bool, None)
- **FR-023**: MUST cover: Basic operators, formatting (f-strings)

### Key Entities

- **Lecture Notebook**: Jupyter notebook (.ipynb) containing all lecture content
- **Code Examples**: Minimum 5 executable Python code snippets
- **Exercises**: 2 practical tasks with solutions in hidden cells
- **Visual Elements**: Memes (2+), diagrams/tables (1+)
- **References**: Links to official Python documentation and tutorials

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: 90% студентів успішно встановлюють Python та запускають перший скрипт до кінця лекції
- **SC-002**: Студенти можуть створити та активувати віртуальне середовище без допомоги викладача
- **SC-003**: Студенти можуть написати програму з використанням print(), input() та f-strings
- **SC-004**: Час проходження лекції не перевищує 1.5 години
- **SC-005**: Всі 5+ code examples успішно виконуються в чистому Python середовищі
- **SC-006**: Студенти можуть пояснити різницю між REPL, скриптом та notebook

## Assumptions

- Студенти мають базові знання програмування (змінні, цикли, функції в будь-якій мові)
- Студенти мають доступ до комп'ютера з можливістю встановлення програм
- Студенти мають стабільний інтернет для завантаження Python та пакетів
- Лекція буде проводитись очно з можливістю запитань
- Студенти мають операційну систему Windows 10+, macOS 10.15+ або сучасний Linux

## Proposed Time Allocation

| Секція | Орієнтовний час |
|--------|-----------------|
| Вступ + Learning Objectives | 5 хв |
| Що таке Python (історія, особливості, застосування) | 15 хв |
| Встановлення та налаштування середовища | 20 хв |
| REPL vs Script vs Notebook | 10 хв |
| venv та pip basics | 15 хв |
| Змінні та типи даних | 15 хв |
| Оператори та f-strings | 10 хв |
| Практичні вправи | 15 хв |
| Підсумок та Q&A | 5 хв |
| **Всього** | **~90 хв (1.5 год)** |
