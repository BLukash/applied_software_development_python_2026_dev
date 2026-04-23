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

### [Лекція 6: Веб-основи та FastAPI](lectures/06-web-fastapi/lecture-06.ipynb)
- Основи веб-серверів — клієнт-серверна архітектура, запит-відповідь, порти
- HTTP-основи — методи (GET/POST/PUT/DELETE), статус-коди, заголовки, JSON
- Raw HTTP демо — http.server зі стандартної бібліотеки
- REST — ресурси, CRUD-маппінг, ідемпотентність, структура помилок
- FastAPI — app, routers, endpoints, path/query/body параметри
- Pydantic — BaseModel, валідація, request vs response моделі, HTTPException
- OpenAPI/Swagger — автоматична документація, uvicorn
- Бутстрап проєкту — uv init/sync, структура app/routers/schemas/services
- Інструменти якості — ruff + black
- [Проєкт: Notes API](project/notes-api/) — FastAPI stub з GET /health, POST /notes/create, POST /notes/search

### [Лекція 7: Async, HTTPX, Testing та Quality Workflow](lectures/07-async-testing/lecture-07.ipynb)
- Async-основи — інтуїція event loop, async/await, чому це важливо для FastAPI
- HTTP-клієнт httpx — синхронний vs асинхронний, таймаути, обробка помилок
- Конфігурація — .env, змінні оточення, pydantic-settings
- Тестування — pytest, FastAPI TestClient, fixtures, parametrize
- Практика тестування — покриття CRUD-ендпоїнтів тестами
- Quality workflow — lint + format + tests як одна команда (make check)
- Розширення [Notes API](project/notes-api/) — async-виклики, тести, налаштування

### [Лекція 8: MCP — Model Context Protocol](lectures/08-mcp/lecture-08.ipynb)
- Концепція MCP — "USB-C для AI", навіщо потрібні стандартизовані протоколи
- Архітектура — Host, Client, Server (три учасники з діаграмами)
- Три примітиви — Tools, Resources, Prompts: що це й коли що використовувати
- Життєвий цикл — як клієнти запускають та керують серверами (subprocess)
- Транспорти — stdio vs SSE/HTTP, порівняльна таблиця
- Практика — keep-mcp через pipx, Google Master Token auth, конфіг LLM-клієнта
- Live demo — search, create, list нотаток через keep-mcp + LLM
- Безпека — safe/unsafe mode, принцип найменших привілеїв
- Тестування MCP-інтеграцій — monkeypatch, integration-test flag

### [Лекція 9: Docker, PostgreSQL та SQLAlchemy](lectures/09-docker-postgres-sqlalchemy/lecture-09.ipynb)
- Docker як інструмент — контейнери (1-хвилинний recap), docker-compose.yml для FastAPI + Postgres
- Налаштування підключення — connection string з .env, sqlalchemy.create_engine
- SQLAlchemy ORM — концепція (class = table), моделі, Engine, Session, Base.metadata.create_all
- CRUD через ORM — заміна in-memory stubs на справжню БД, транзакції (session.commit)
- Обробка помилок — not found → 404, unique constraint → 409
- Шаровність — repository.py, router → service → repository flow
- Розширення [Notes API](project/notes-api/) — docker compose up, CRUD з PostgreSQL, repository-шар

### [Лекція 10: Міграції, Зв'язки та Цілісність даних](lectures/10-migrations-relationships/lecture-10.ipynb)
- Навіщо міграції — проблема еволюції схеми, що ламається при зміні моделі
- Alembic workflow — init, revision --autogenerate, upgrade/downgrade (один раз end-to-end)
- Зв'язки — one-to-many (Tag → Note), ForeignKey, relationship(), cascade
- Проєктування БД — індекси, обмеження (unique, not null, foreign key), "думай про запити першим"
- Тестування з реальною БД — fixtures створення/руйнування test DB (на контрасті з L7 in-memory)
- psql toolkit — базові команди: \dt, \d table_name, SELECT з JOIN
- Розширення [Notes API](project/notes-api/) — Alembic ініціалізовано, Tag модель, міграції

### [Лекція 11: pandas глибоке занурення на Stack Overflow Developer Survey 2025](lectures/11-pandas-analytics/lecture-11.ipynb)
- Коли pandas — правильний інструмент (та коли ні — DuckDB, Polars)
- Series vs DataFrame з чистого Python — перш ніж торкатися CSV
- pd.read_csv — usecols, dtype, na_values на справжньому 49K-рядковому CSV
- Чистка даних — pd.to_numeric(errors="coerce"), isna/fillna/dropna
- Індексація — .loc, .iloc, boolean masks, .query(), .isin()
- Багатозначні колонки — str.split(";") + .explode()
- groupby з агрегаціями — single/multi-key, named aggregations, dropna=False (з українським якорем)
- merge з validate= — захист від випадкового many-to-many
- pivot_table та crosstab — з margins та normalize
- Сортування та top-N — .nlargest, .sort_values, .rank
- Method chaining — .pipe, .assign, stepwise vs chained
- .apply / .map + %timeit бенчмарк проти векторизації
- Categorical dtype — пам'ять (−36% на реальних даних) + впорядковані категорії
- Коли pandas ламається — концептуальний огляд DuckDB та Polars
- Міні-проєкт "Developer Survey Insights" — 3 частини (25 хв в аудиторії + 30–60 хв вдома)

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
