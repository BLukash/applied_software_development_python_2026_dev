"""One-shot generator for `lecture-11.ipynb`.

Run once to produce the canonical notebook; after that the .ipynb is the
source of truth and may be edited directly in Jupyter. The generator is kept
around for reproducibility — re-running it will overwrite manual edits, so
treat it as a historical artifact.

Usage:
    python lectures/11-pandas-analytics/_build_notebook.py
"""
from __future__ import annotations

from pathlib import Path

import nbformat as nbf

HERE = Path(__file__).parent
OUT = HERE / "lecture-11.ipynb"


def md(src: str) -> nbf.NotebookNode:
    return nbf.v4.new_markdown_cell(src)


def code(src: str, hide_input: bool = False) -> nbf.NotebookNode:
    cell = nbf.v4.new_code_cell(src)
    if hide_input:
        cell.metadata["jupyter"] = {"source_hidden": True}
    return cell


cells: list[nbf.NotebookNode] = []

# =============================================================================
# SECTION 0 — HEADER + PREREQUISITES
# =============================================================================

cells.append(
    md(
        """# Лекція 11 — pandas глибоке занурення на Stack Overflow Developer Survey 2025

**Курс:** Applied Software Development (Python) 2026 · **Тривалість:** 1.5 години

---

## Передумови (Prerequisites)

Ця лекція **повністю самодостатня**: жодної залежності від проєктного коду з лекцій 6–10. Нам не потрібні ані вебфреймворк, ані база даних, ані контейнери — лише Python, Jupyter та один CSV.

Достатньо знань з **Лекцій 1–5**:

- типи даних, змінні, f-strings (Л1)
- колекції: `list`, `dict`, `tuple`, `set` (Л2–Л3)
- генератори списків / словників (Л3)
- функції, `*args`/`**kwargs`, lambda (Л3–Л4)
- базове файлове введення-виведення (Л5)

Плюс встановлений **Jupyter** (notebook, lab або VS Code) і можливість запустити `pip install`.

---

## Датасет, на якому все побудовано

Один CSV — **Stack Overflow Annual Developer Survey 2025** (~49 000 респондентів, 177 країн). Ми завантажимо його з офіційного джерела під ліцензією **ODbL**, почистимо, поріжемо, згрупуємо, з'єднаємо — і побачимо, як виглядає світ розробників у цифрах.

> **Важливо:** CSV-файл **не** вкомітчений у репозиторій (він завеликий). Ви завантажуєте його самі — див. `README.md` у теці цієї лекції.
"""
    )
)

# =============================================================================
# SECTION 1 — LEARNING OBJECTIVES
# =============================================================================

cells.append(
    md(
        """## Цілі заняття

Після цієї лекції ви зможете:

1. Пояснити, **коли pandas — правильний інструмент**, а коли варто дивитися в бік DuckDB чи Polars.
2. Розрізнити `Series` та `DataFrame` і будувати їх з чистого Python (без зовнішніх файлів).
3. Завантажити справжній CSV з `pd.read_csv` та вивчити його: типи, пропущені значення, примусове приведення типів (`pd.to_numeric(errors="coerce")`).
4. Впевнено користуватися `.loc`, `.iloc`, булевими масками, `.query()`, `.isin()`, `.explode()`, `groupby().agg()`, `merge()`, `pivot_table` та `crosstab`.
5. Застосовувати інтермедіат-патерни: method chaining (`.pipe`, `.assign`), `.apply` / `.map`, та `Categorical` dtype з реальним порівнянням використання пам'яті.
6. Написати та захистити міні-проєкт **"Developer Survey Insights"** — три частини, від простого фільтру до повноцінної аналітичної історії.

> **Поза межами цієї лекції:** розбір дати/часу (у Survey нема колонки з часом відповіді — перенесено на пізніше), NumPy-внутрішнощі (Л12), візуалізація (Л13), machine learning (Л12), MultiIndex, віконні функції (`rolling`, `resample`), Arrow-бекенд та copy-on-write.
"""
    )
)

# =============================================================================
# SECTION 2 — WHAT PANDAS IS GOOD FOR (AND NOT)  [FR-007]
# =============================================================================

cells.append(
    md(
        """## 1. Для чого pandas — і для чого ні

**pandas** — це Python-бібліотека для роботи з табличними даними. Синтаксично схожа на Excel, але в сто разів швидша і в тисячу разів програмованіша.

### Сильні сторони

- **Векторизовані операції над колонками (vectorization).** `df["a"] + df["b"]` — один виклик у C під капотом, а не Python-цикл. Це зазвичай у 10–1000 разів швидше, ніж `for row in df: ...`.
- **Багатий API для злиття, групування, перетворень.** `groupby`, `merge`, `pivot_table`, `rolling`, `resample` — все вбудовано і добре документовано.
- **Екосистема.** pandas легко інтегрується з matplotlib, seaborn, scikit-learn, Jupyter, Parquet, Excel, різними SQL-базами — одним словом, з усім.

### Слабкі сторони

- **Все в пам'яті, один процес.** Якщо датасет не вміщується в RAM — pandas зламається. Жодних out-of-core чи паралельних обчислень (крім зовнішніх костилів).
- **"Магія" індексів.** `.loc` vs `.iloc`, `SettingWithCopyWarning`, view vs copy — pandas має свою філософію, яку треба опанувати, і яка регулярно кусає новачків.

**Правило великого пальця:** якщо ваш датасет вміщується в пам'ять (≤ кілька GB) і ви робите з ним переважно **агрегації, перетворення та поєднання** — pandas ідеальний. Якщо ні — дивіться в бік DuckDB чи Polars (Секція 16).
"""
    )
)

# =============================================================================
# SECTION 3 — SERIES VS DATAFRAME  [FR-008]
# =============================================================================

cells.append(
    md(
        """## 2. Series vs DataFrame

Перш ніж завантажити справжні дані, збудуємо обидва основні об'єкти pandas **з чистого Python**, щоб побачити їхню природу.

**Ментальна модель:**

- `Series` — одновимірний масив значень з **індексом** (ярликами).
- `DataFrame` — словник `Series`-ів, які **ділять між собою один Index**.

Тобто `DataFrame` — це таблиця, яку можна подивитися як "набір колонок" (кожна колонка — `Series`).
"""
    )
)

cells.append(
    code(
        """import pandas as pd

# Серія з чистого Python-списку — pandas сам створить цілочисловий Index 0..N-1
temps = pd.Series([18.5, 21.0, 19.8, 22.3], name="temperature_c")
print(temps)
print("---")
print(f"dtype: {temps.dtype}")
print(f"name:  {temps.name}")
print(f"index: {list(temps.index)}")"""
    )
)

cells.append(
    code(
        """# Серія з ярликами: явно задаємо Index
rating = pd.Series(
    data=[4.7, 4.5, 4.9, 4.2],
    index=["Python", "JavaScript", "Rust", "PHP"],
    name="developer_love",
)
print(rating)
print("---")
# Доступ за ярликом, не за позицією
print("Rust:", rating["Rust"])"""
    )
)

cells.append(
    code(
        """# DataFrame = dict of Series з одним спільним Index
devs = pd.DataFrame(
    {
        "country": ["Ukraine", "USA", "Poland", "Germany"],
        "years_pro": [5, 9, 4, 12],
        "uses_python": [True, True, False, True],
    }
)
print(devs)
print("---")
# Кожна колонка — Series; індекс 0..3 спільний для всіх колонок
print(type(devs["country"]))
print(devs["country"])"""
    )
)

cells.append(
    md(
        """**Ключова ідея:** коли ми потім напишемо `df["Country"]` над справжнім CSV — повернеться саме `Series`. Коли ми напишемо `df[["Country", "DevType"]]` (зверніть увагу, подвійні дужки) — повернеться `DataFrame` з підмножиною колонок."""
    )
)

# =============================================================================
# SECTION 4 — LOADING DATA  [FR-009, FR-024]
# =============================================================================

cells.append(
    md(
        """## 3. Завантаження даних: pd.read_csv на Stack Overflow Survey 2025

Тепер — до справжнього датасету. Pinуємо версію зверху, щоб лекція була детерміністичною:
"""
    )
)

cells.append(
    code(
        """from pathlib import Path

# Пінимо рік Survey, щоб лекція була детерміністичною.
# Схеми колонок дрейфують рік за роком — якщо перейдете на новіший Survey,
# перевірте df.columns.tolist() і оновіть список нижче.
SURVEY_YEAR = 2025
SURVEY_PATH = Path("data") / "survey_results_public.csv"

print(f"Survey рік: {SURVEY_YEAR}")
print(f"Очікуваний шлях: {SURVEY_PATH.resolve()}")
print(f"Файл існує: {SURVEY_PATH.exists()}")"""
    )
)

cells.append(
    md(
        """### Якщо CSV відсутній

Якщо `data/survey_results_public.csv` ще не на місці — ноутбук зупиниться на наступній клітинці з ясним повідомленням. Щоб це виправити:

1. Відкрийте <https://survey.stackoverflow.co/> і знайдіть посилання **"Download the full data set (CSV)"**.
2. Розпакуйте ZIP-архів.
3. Покладіть `survey_results_public.csv` за шляхом `lectures/11-pandas-analytics/data/survey_results_public.csv`.
4. Перезапустіть ноутбук з початку.

> **Без реального CSV лекція не запрацює** — і це свідомо: вся цінність у тому, що ми працюємо зі справжніми даними 49 000 розробників, а не з іграшковими фіктивними записами.
"""
    )
)

cells.append(
    code(
        """# Колонки, які нам знадобляться протягом лекції.
# Повний CSV 2025 Survey має 172 колонки; завантажимо лише потрібні для швидкості.
USECOLS = [
    "ResponseId",
    "MainBranch",
    "Country",
    "EdLevel",
    "YearsCode",         # загальний стаж коду (вже числовий у 2025)
    "WorkExp",           # років професійного досвіду (замінює історичний YearsCodePro)
    "DevType",
    "LanguageHaveWorkedWith",
    "LanguageWantToWorkWith",
    "DatabaseHaveWorkedWith",
    "ConvertedCompYearly",
    "RemoteWork",
]

if not SURVEY_PATH.exists():
    raise FileNotFoundError(
        f"Не знайдено {SURVEY_PATH.resolve()}.\\n"
        f"Завантажте ZIP з https://survey.stackoverflow.co/, розпакуйте, "
        f"і покладіть survey_results_public.csv у теку lectures/11-pandas-analytics/data/. "
        f"Деталі — у README.md."
    )

df = pd.read_csv(
    SURVEY_PATH,
    usecols=USECOLS,
    na_values=["NA", "N/A", ""],
    low_memory=False,
)
print(f"✅ Завантажено Survey {SURVEY_YEAR}: {len(df):,} рядків × {df.shape[1]} колонок")
"""
    )
)

cells.append(
    code(
        """# Базова "розвідка" датасету
df.head()"""
    )
)

cells.append(
    code(
        """df.info()"""
    )
)

cells.append(
    code(
        """df.describe(include="all").T.head(15)"""
    )
)

cells.append(
    code(
        """# Розмір, колонки, типи
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print("---")
print(df.dtypes)"""
    )
)

# =============================================================================
# SECTION 5 — CLEANING  [FR-010]  + MEME 1
# =============================================================================

cells.append(
    md(
        """## 4. Чистка даних: типи та пропущені значення

![pandas: first time?](assets/memes/first-time-pandas.png)

*(Якщо картинка не відображається — це нормально, мем — педагогічний гарнір. Головне — код нижче.)*

У справжніх CSV завжди дві проблеми:

1. **Пропущені значення (NaN).** Респонденти не зобов'язані відповідати на кожне питання.
2. **Неправильні типи.** Колонка, яку ми очікуємо числовою, інколи приїжджає як `object` (рядок), бо в ній сидять "граничні маркери" типу `"Less than 1 year"`, `"More than 50 years"` або просто сторонній текст.

> **Увага:** 2025 Survey **уже добре причесаний** — `YearsCode` і `WorkExp` приїжджають як `float64`. У попередніх роках Survey (2023, 2024) ті самі колонки були `object` з рядковими граничними маркерами. Техніку `pd.to_numeric(errors="coerce")` ви все одно мусите знати — ви зустрінете її в інших CSV щотижня.

> **Примітка про дати:** у 2025 Survey нема колонки з датою/часом відповіді, тож `pd.to_datetime` тут не показуємо — повернемося до нього в лекції, де є справжні часові ряди.

### 4.1. Скільки NaN у кожній колонці?
"""
    )
)

cells.append(
    code(
        """df.isna().sum().sort_values(ascending=False)"""
    )
)

cells.append(
    md(
        """### 4.2. `pd.to_numeric(errors="coerce")` — на прикладі "брудної" Series

Показуємо техніку на невеличкій **синтетичній** Series, щоб ви її впізнали, коли зустрінете в іншому CSV. У нашому 2025 Survey ця техніка — no-op (бо числа вже є), але запустити її безпечно в будь-якому разі.
"""
    )
)

cells.append(
    code(
        """# Демонстраційна Series із рядковими "граничними" маркерами
# (саме такий вигляд мав YearsCodePro в Survey 2023/2024)
messy = pd.Series(["1", "5", "Less than 1 year", "20", "More than 50 years",
                   None, "не знаю", "10"])
print("ДО: dtype =", messy.dtype)
print(messy.tolist())
print()

# Крок 1: replace — підміняємо відомі рядкові маркери на числа
replacements = {"Less than 1 year": 0.5, "More than 50 years": 51.0}
# Крок 2: to_numeric із errors="coerce" — решту нерозпізнаного перетворює на NaN
cleaned = pd.to_numeric(messy.replace(replacements), errors="coerce")

print("ПІСЛЯ: dtype =", cleaned.dtype)
print(cleaned.tolist())"""
    )
)

cells.append(
    md(
        """Принципово: `errors="coerce"` — **не** викидає виняток на незрозумілому значенні, а перетворює його на `NaN`. Це дає вам шанс побачити проблемні рядки (`cleaned.isna()`) і вирішити, що з ними робити, замість того щоб зупинити весь pipeline.

### 4.3. Перевіримо на реальних даних 2025 Survey
"""
    )
)

cells.append(
    code(
        """# У 2025 ці колонки вже числові — виклик безпечний (no-op для вже-числових)
df["YearsCode"] = pd.to_numeric(df["YearsCode"], errors="coerce")
df["WorkExp"] = pd.to_numeric(df["WorkExp"], errors="coerce")

print(df[["YearsCode", "WorkExp"]].dtypes)
df[["YearsCode", "WorkExp"]].describe()"""
    )
)

cells.append(
    md(
        """### 4.3. Що робити з NaN: dropna vs fillna

Два підходи, і вибір залежить від питання:

- `dropna(subset=[...])` — "мене цікавлять лише респонденти, які відповіли на конкретне питання".
- `fillna(value)` — "відсутня відповідь насправді означає щось відоме, і я хочу це кодувати".
"""
    )
)

cells.append(
    code(
        """# Drop будь-які рядки, де нема WorkExp — бо для наших агрегацій потрібен стаж
n_before = len(df)
df_with_pro = df.dropna(subset=["WorkExp"])
n_after = len(df_with_pro)
print(f"dropna(subset=['WorkExp']): {n_before:,} → {n_after:,} рядків "
      f"(викинули {n_before - n_after:,})")"""
    )
)

cells.append(
    code(
        """# Fillna: для зручного звіту замінимо відсутній DevType на явну мітку
dev_type_filled = df["DevType"].fillna("— не вказано —")
dev_type_filled.value_counts().head(10)"""
    )
)

# =============================================================================
# SECTION 6 — INDEXING / SELECTION  [FR-011]
# =============================================================================

cells.append(
    md(
        """## 5. Індексація та вибірка

Чотири інструменти, які закривають 95% випадків:

- **`.loc[rows, cols]`** — за ярликами (label-based).
- **`.iloc[rows, cols]`** — за позиціями (positional).
- **Булеві маски** — `df[df["Country"] == "Ukraine"]`.
- **`.query("Country == 'Ukraine'")`** — читабельна версія булевої маски, добре комбінується.

### 5.1. .loc і .iloc
"""
    )
)

cells.append(
    code(
        """# .loc — за ярликами (індекс + імена колонок)
# Перші 3 рядки (індекси 0, 1, 2) і дві конкретні колонки
df.loc[0:2, ["Country", "WorkExp"]]"""
    )
)

cells.append(
    code(
        """# .iloc — за позиціями (0-based, як Python-списки)
# Перші 3 рядки і колонки 0, 2, 4
df.iloc[0:3, [0, 2, 4]]"""
    )
)

cells.append(
    md(
        """### 5.2. Булеві маски + пастка з дужками

Комбінувати маски потрібно через `&`, `|`, `~` (не `and`/`or`/`not`!) — **і кожну маску загортати в дужки**. Це класична помилка-новачка.
"""
    )
)

cells.append(
    code(
        """# ПРАВИЛЬНО: дужки навколо кожної маски
mask = (df["WorkExp"] >= 5) & (df["ConvertedCompYearly"].notna())
n = mask.sum()
print(f"Респондентів з ≥5 років стажу і вказаною компенсацією: {n:,}")"""
    )
)

cells.append(
    code(
        """# ТА САМА вибірка через .query() — зазвичай читабельніше
subset = df.query("WorkExp >= 5 and ConvertedCompYearly.notna()")
print(f".query() дає той самий результат: {len(subset):,} рядків")
subset.head(3)"""
    )
)

cells.append(
    code(
        """# .isin() — перевірка належності до множини
top5_countries = ["Ukraine", "United States of America", "Germany", "India", "United Kingdom"]
df_top5 = df[df["Country"].isin(top5_countries)]
df_top5["Country"].value_counts()"""
    )
)

# =============================================================================
# SECTION 7 — EXPLODE  [FR-012]  + DIAGRAM
# =============================================================================

cells.append(
    md(
        """## 6. Багатозначні стовпці та `.explode()`

Survey любить зберігати кілька значень в одній клітинці через крапку з комою:

```text
LanguageHaveWorkedWith:  "Python;JavaScript;Go"
```

Щоб порахувати, скільки респондентів використовують кожну мову, треба **розгорнути** це в довгу форму — один рядок на одну мову.

![explode-schematic](assets/diagrams/explode-schematic.png)

Два кроки:

1. `str.split(";")` — перетворює рядок на список.
2. `.explode(col)` — розгортає кожен елемент списку в окремий рядок.
"""
    )
)

cells.append(
    code(
        """# Будуємо "довгу" таблицю: один рядок = один респондент × одна мова
languages_long = (
    df.assign(LanguageList=df["LanguageHaveWorkedWith"].str.split(";"))
      .explode("LanguageList")
      .rename(columns={"LanguageList": "Language"})
      [["ResponseId", "Country", "Language"]]
      .dropna(subset=["Language"])
)

print(f"df: {len(df):,} рядків")
print(f"languages_long: {len(languages_long):,} рядків (один респондент → кілька)")
languages_long.head(10)"""
    )
)

cells.append(
    code(
        """# Топ-15 мов серед усіх респондентів
top_langs = languages_long["Language"].value_counts().head(15)
top_langs"""
    )
)

# =============================================================================
# SECTION 8 — GROUPBY  [FR-013, FR-035 UKRAINE ANCHOR]
# =============================================================================

cells.append(
    md(
        """## 7. Groupby та агрегації — де ми в цифрах?

`groupby` — найчастіше вживаний інструмент pandas. Патерн завжди один:

```text
df.groupby(<ключ>)[<колонки>].<агрегація>()
```

**У цьому розділі ми використовуємо Україну як наскрізний якір** — побачимо, як наша країна виглядає на глобальному тлі.

### 7.1. Медіанна компенсація — Україна vs Global
"""
    )
)

cells.append(
    code(
        """# Цікавий патерн: згрупувати за булевим, що перетворюється на легку мітку
ua_mask = df["Country"] == "Ukraine"
ua_vs_global = (
    df.groupby(ua_mask.map({True: "Україна", False: "Глобально"}))
      ["WorkExp"]
      .median()
)
ua_vs_global"""
    )
)

cells.append(
    md(
        """### 7.2. Один ключ: медіанна компенсація за країною (топ-20)"""
    )
)

cells.append(
    code(
        """median_comp_by_country = (
    df.dropna(subset=["ConvertedCompYearly"])
      .groupby("Country")["ConvertedCompYearly"]
      .median()
      .sort_values(ascending=False)
      .head(20)
)
median_comp_by_country"""
    )
)

cells.append(
    md(
        """### 7.3. Два ключі + named aggregation

`agg(new_col=("col", "func"))` — синтаксис, який робить вивід охайним і самодокументованим.
"""
    )
)

cells.append(
    code(
        """# Медіанна компенсація та кількість респондентів — по країні + рівню освіти
# Обмежимося країнами з достатньою вибіркою, щоб числа щось значили
big_countries = df["Country"].value_counts().head(10).index.tolist()

summary = (
    df[df["Country"].isin(big_countries)]
      .dropna(subset=["ConvertedCompYearly", "EdLevel"])
      .groupby(["Country", "EdLevel"])
      .agg(
          n=("ResponseId", "size"),
          median_usd=("ConvertedCompYearly", "median"),
      )
      .reset_index()
)
summary.head(15)"""
    )
)

cells.append(
    md(
        """### 7.4. dropna=False — коли NaN як окрема група

За замовчуванням `groupby` **викидає NaN ключі**. Якщо для вас "не вказано" — самостійна група, передайте `dropna=False`.
"""
    )
)

cells.append(
    code(
        """# Скільки респондентів у кожній категорії DevType, включно з NaN
df.groupby("DevType", dropna=False)["ResponseId"].count().head(10)"""
    )
)

# =============================================================================
# SECTION 9 — MERGE  [FR-014]  + MEME 2
# =============================================================================

cells.append(
    md(
        """## 8. Merge / join — зливаємо дві таблиці

Часто треба приєднати результат групування назад до рядків-респондентів ("для кожного респондента покажи, яка середня компенсація у його країні"). Саме для цього `merge`.

Ключові параметри:

- `how=` — `"inner"` (за замовчуванням), `"left"`, `"right"`, `"outer"`.
- `on=` / `left_on=` / `right_on=` — за якою колонкою з'єднуємо.
- `validate=` — перевірка форми з'єднання. Врятує вас від випадкового `many-to-many`, який несподівано перетворює 50 000 рядків на 500 000.

![merge explosion validate](assets/memes/merge-explosion-validate.png)

### 8.1. Inner join: мови → статистика → назад до респондентів
"""
    )
)

cells.append(
    code(
        """# Крок 1 — побудувати per-language агрегати
lang_stats = (
    languages_long.groupby("Language")
                  .agg(n_users=("ResponseId", "nunique"))
                  .reset_index()
                  .sort_values("n_users", ascending=False)
)
lang_stats.head(10)"""
    )
)

cells.append(
    code(
        """# Крок 2 — приєднати ці агрегати до кожного рядка languages_long
# Inner merge: тільки збіги (що у нас і є, бо lang_stats побудовано з languages_long)
enriched = languages_long.merge(
    lang_stats,
    on="Language",
    how="inner",
    validate="many_to_one",  # ← КЛЮЧОВА перевірка: одна мова → одна статистика
)
print(f"До merge: {len(languages_long):,} рядків")
print(f"Після merge: {len(enriched):,} рядків (те саме число — bo many_to_one)")
enriched.head(5)"""
    )
)

cells.append(
    md(
        """### 8.2. Left join: зберегти всіх, навіть тих, кому пари нема"""
    )
)

cells.append(
    code(
        """# Невелика допоміжна таблиця: "рекомендації" для мов (синтетичне, для демо)
recs = pd.DataFrame({
    "Language": ["Python", "JavaScript", "Rust"],
    "Recommendation": ["✓ solid", "✓ essential", "★ growing"],
})

with_recs = lang_stats.head(10).merge(
    recs, on="Language", how="left", validate="one_to_one",
)
with_recs"""
    )
)

cells.append(
    md(
        """**Дивіться на NaN у колонці `Recommendation`:** це саме те, що робить `how="left"` — зберігає всі рядки з лівої таблиці, а праві колонки заповнює `NaN`, де пари нема. Якби ми поставили `how="inner"`, ці рядки просто зникли б.

### 8.3. Коли `validate=` рятує життя

Якщо ви забудете `validate="many_to_one"` і випадково зіллєте два `languages_long`-подібні фрейми (де одна мова має багато записів з **обох** сторін) — ви отримаєте many-to-many і рядки буквально перемножаться. `validate=` кидає виняток одразу, замість того щоб тиша + 10 мільйонів рядків.
"""
    )
)

# =============================================================================
# SECTION 10 — PIVOT / CROSSTAB  [FR-015]
# =============================================================================

cells.append(
    md(
        """## 9. Pivot tables та crosstab

`pivot_table` — "що показати в клітинках таблиці, де рядки — одне, а колонки — інше?".

`crosstab` — частковий випадок `pivot_table` з лічильниками; зручно з `normalize=` для часток.
"""
    )
)

cells.append(
    code(
        """# Pivot: медіанна компенсація, рядки = Country, колонки = RemoteWork
pivot = df.pivot_table(
    index="Country",
    columns="RemoteWork",
    values="ConvertedCompYearly",
    aggfunc="median",
    margins=True,          # додає рядок/колонку "All"
    margins_name="Усі",
)
# Обмежимо вивід кількома країнами, щоб було компактно
shown = ["Ukraine", "United States of America", "Germany", "India", "Усі"]
pivot.loc[[c for c in shown if c in pivot.index]]"""
    )
)

cells.append(
    code(
        """# Crosstab з normalize="index": "яка частка мов 'хочу вивчити' у кожному DevType?"
# Спершу збудуємо довгу таблицю для "хочу вивчити"
want_long = (
    df.assign(WantList=df["LanguageWantToWorkWith"].str.split(";"))
      .explode("WantList")
      .rename(columns={"WantList": "WantLanguage"})
      .dropna(subset=["WantLanguage", "DevType"])
)

# Фокус: частка тих, хто хоче Rust, за DevType
want_long["wants_rust"] = want_long["WantLanguage"] == "Rust"
rust_share = pd.crosstab(
    want_long["DevType"],
    want_long["wants_rust"],
    normalize="index",
).rename(columns={True: "Хоче Rust", False: "Не хоче Rust"})
rust_share.sort_values("Хоче Rust", ascending=False).head(10)"""
    )
)

# =============================================================================
# SECTION 11 — SORT / RANK / TOP-N  [FR-016]
# =============================================================================

cells.append(
    md(
        """## 10. Сортування, ранжування, top-N

Три патерни:

- `.sort_values(by=[...], ascending=[...])` — класичне сортування.
- `.nlargest(N, by=...)` / `.nsmallest(N, by=...)` — швидший і чистіший спосіб взяти top-N, ніж `sort + head`.
- `.rank()` — коли треба впорядкувати та зберегти номер позиції (а не просто відсіяти).
"""
    )
)

cells.append(
    code(
        """# Топ-10 країн за кількістю респондентів
country_counts = df["Country"].value_counts()
country_counts.nlargest(10)"""
    )
)

cells.append(
    code(
        """# Те саме, але через sort_values — еквівалентно, але nlargest зазвичай швидший
country_counts.sort_values(ascending=False).head(10)"""
    )
)

cells.append(
    code(
        """# Рангування: хто в топ-5, топ-10, топ-20 країн за кількістю респондентів?
ranked = country_counts.rank(method="min", ascending=False).astype(int)
ranked.head(5)"""
    )
)

# =============================================================================
# SECTION 12 — METHOD CHAINING  [FR-032]
# =============================================================================

cells.append(
    md(
        """## 11. Method chaining: `.pipe` та `.assign`

Коли pipeline виростає — стиль із проміжними змінними (`df1 = ...; df2 = ...; df3 = ...`) створює смислові "острівці", які легко сплутати. **Method chaining** (ланцюжок викликів) робить pipeline одним логічним блоком.

### 11.1. Stepwise vs chained — той самий pipeline

**Завдання:** з основного DataFrame взяти респондентів-розробників за професією з відомою компенсацією, додати бакет `comp_band` кожної тисячі доларів, вибрати кілька колонок.
"""
    )
)

cells.append(
    code(
        """# Варіант А — stepwise, з проміжними змінними
step1 = df[df["MainBranch"] == "I am a developer by profession"]
step2 = step1.dropna(subset=["ConvertedCompYearly"])
step3 = step2.assign(comp_band=(step2["ConvertedCompYearly"] // 25_000) * 25_000)
step4 = step3[["Country", "DevType", "WorkExp", "comp_band"]]

print(step4.shape)
step4.head(5)"""
    )
)

cells.append(
    code(
        """# Варіант Б — chained, один блок. Ідентичний результат.
chained = (
    df.loc[df["MainBranch"] == "I am a developer by profession"]
      .dropna(subset=["ConvertedCompYearly"])
      .assign(comp_band=lambda d: (d["ConvertedCompYearly"] // 25_000) * 25_000)
      [["Country", "DevType", "WorkExp", "comp_band"]]
)

print(chained.shape)
chained.head(5)"""
    )
)

cells.append(
    md(
        """**Спостереження.** Обидва варіанти дають той самий результат. Chained-варіант:

- не "протікає" проміжними змінними у namespace;
- читається зверху вниз як послідовність кроків;
- дешевше рефакторити (вставити / прибрати крок = змінити один рядок).

**Коли chaining шкодить:** коли ланцюжок стає > 10 кроків, або коли треба дебажити конкретний проміжний результат. Тоді розбивайте назад на stepwise. Або використайте `.pipe(print)` / `.pipe(lambda d: (display(d.head()), d)[1])` як "дебаг-пробник" усередині ланцюжка.

### 11.2. `.pipe(func)` — коли маєте власну функцію-крок
"""
    )
)

cells.append(
    code(
        """def drop_outlier_comp(d: pd.DataFrame, lo: float = 1_000, hi: float = 500_000) -> pd.DataFrame:
    \"\"\"Викинути екстремальні викиди компенсації.\"\"\"
    return d[(d["ConvertedCompYearly"] >= lo) & (d["ConvertedCompYearly"] <= hi)]


cleaned = (
    df.dropna(subset=["ConvertedCompYearly"])
      .pipe(drop_outlier_comp)
      .assign(comp_band=lambda d: (d["ConvertedCompYearly"] // 25_000) * 25_000)
)
print(f"До: {df.dropna(subset=['ConvertedCompYearly']).shape[0]:,}")
print(f"Після drop_outlier_comp: {cleaned.shape[0]:,}")"""
    )
)

# =============================================================================
# SECTION 13 — APPLY / MAP  [FR-033]
# =============================================================================

cells.append(
    md(
        """## 12. `.apply` та `.map` — власні функції

Коли pandas не має "готової" операції — пишемо свою.

- **`Series.map(dict_or_func)`** — поелементно; найшвидший варіант з тих трьох.
- **`Series.apply(func)`** — поелементно, але приймає функцію; трохи повільніший.
- **`DataFrame.apply(func, axis=0|1)`** — `axis=0` працює по колонках, `axis=1` — по рядках (**найповільніший**).

> **Золоте правило:** перед тим, як тягнутися до `.apply`, запитайте — "чи можна це зробити векторизовано?". Якщо так — робіть векторизовано, буде в 100–1000 разів швидше.
"""
    )
)

cells.append(
    code(
        """# .map з dict: переклад довгих офіційних міток на коротші
remote_short = df["RemoteWork"].map({
    "Remote": "remote",
    "Hybrid (some remote, some in-person)": "hybrid",
    "In-person": "onsite",
})
remote_short.value_counts(dropna=False)"""
    )
)

cells.append(
    code(
        """# .apply з lambda: бакет стажу в людські категорії
def years_bucket(y):
    if pd.isna(y):
        return "невідомо"
    if y < 2:
        return "junior (<2)"
    if y < 5:
        return "mid (2–5)"
    if y < 10:
        return "senior (5–10)"
    return "staff+ (10+)"


df["years_bucket"] = df["WorkExp"].apply(years_bucket)
df["years_bucket"].value_counts()"""
    )
)

cells.append(
    md(
        """### 12.1. Бенчмарк: векторизовано vs `.apply(axis=1)`

Порахуємо "бакет компенсації $25 000" двома способами і заміряємо час.
"""
    )
)

cells.append(
    code(
        """# Готуємо підмножину, де є компенсація — щоб було що рахувати
comp_df = df.dropna(subset=["ConvertedCompYearly"]).copy()
print(f"Рядків у бенчмарку: {len(comp_df):,}")"""
    )
)

cells.append(
    code(
        """# Варіант А — векторизовано (одним виразом над цілою колонкою)
%timeit (comp_df["ConvertedCompYearly"] // 25_000) * 25_000"""
    )
)

cells.append(
    code(
        """# Варіант Б — через apply(axis=1): проходимося по кожному рядку в Python
%timeit comp_df.apply(lambda row: (row["ConvertedCompYearly"] // 25_000) * 25_000, axis=1)"""
    )
)

cells.append(
    md(
        """**Висновок:** векторизований варіант у десятки чи сотні разів швидший. Саме тому `.apply(axis=1)` — останній притулок, а не перший вибір.
"""
    )
)

# =============================================================================
# SECTION 14 — CATEGORICAL  [FR-034, FR-035 UKRAINE ANCHOR]
# =============================================================================

cells.append(
    md(
        """## 13. `Categorical` dtype — пам'ять та впорядковані категорії

`object` (рядковий) тип у колонках на кшталт `Country` або `EdLevel` марнує купу пам'яті: кожен "Ukraine" зберігається як окремий рядок, хоча значень лише кілька десятків.

**Categorical** зберігає унікальні значення одноразово плюс масив цілочислових індексів — як внутрішня "довідникова" таблиця. Переваги:

1. Часто кратне зменшення пам'яті.
2. `groupby` по categorical — швидший.
3. **Впорядковані категорії** (`ordered=True`) дозволяють порівняння на кшталт `edlevel >= "Master's"`.

### 13.1. Пам'ять: before/after на реальних колонках
"""
    )
)

cells.append(
    code(
        """# Вимірюємо використання пам'яті об'єктних колонок
def memory_mb(frame: pd.DataFrame) -> float:
    return frame.memory_usage(deep=True).sum() / 1024 ** 2


before_mb = memory_mb(df)
print(f"ДО оптимізації: {before_mb:.2f} MB")

df_opt = df.copy()
for col in ["Country", "DevType", "MainBranch", "RemoteWork"]:
    df_opt[col] = df_opt[col].astype("category")

after_mb = memory_mb(df_opt)
print(f"ПІСЛЯ конвертації 4 колонок у Categorical: {after_mb:.2f} MB")
print(f"Виграш: {(1 - after_mb / before_mb) * 100:.1f}%")"""
    )
)

cells.append(
    md(
        """### 13.2. Ordered Categorical: EdLevel як порядкова шкала

`EdLevel` — природна порядкова величина: primary → secondary → bachelor → master → doctorate. Надаючи явний порядок, ми вмикаємо природне порівняння.
"""
    )
)

cells.append(
    code(
        """# Значення у 2025 Survey вживають "кучерявий" апостроф (’, U+2019) замість ASCII (')
# — список нижче точно відображає рядки, які знайде df["EdLevel"].unique().
ed_order = [
    "Primary/elementary school",
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)",
    "Some college/university study without earning a degree",
    "Associate degree (A.A., A.S., etc.)",
    "Bachelor’s degree (B.A., B.S., B.Eng., etc.)",
    "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)",
    "Professional degree (JD, MD, Ph.D, Ed.D, etc.)",
]
# Беремо лише ті значення, які реально є в датасеті (перестраховка, якщо
# Stack Overflow поправить текст у наступному році)
present = [v for v in ed_order if v in df["EdLevel"].dropna().unique()]
ed_dtype = pd.CategoricalDtype(categories=present, ordered=True)

df_opt["EdLevel"] = df["EdLevel"].astype(ed_dtype)
print("Категорії у порядку:")
for i, c in enumerate(df_opt["EdLevel"].cat.categories, 1):
    print(f"  {i}. {c}")
print("---")

# Впорядковане порівняння: беремо позицію Master's у списку категорій
# і зберігаємо рядки, що знаходяться на ній або вище.
master_label = "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)"
master_pos = df_opt["EdLevel"].cat.categories.get_loc(master_label)
has_master_or_higher = df_opt["EdLevel"].cat.codes >= master_pos
# cat.codes повертає -1 для NaN — не рахуємо їх як Master's+
has_master_or_higher &= df_opt["EdLevel"].notna()
print(f"Респондентів з Master's+ ступенем: {has_master_or_higher.sum():,}")"""
    )
)

cells.append(
    md(
        """### 13.3. Україна-якір: фільтр на Categorical

Коли колонка стала Categorical, `df[df["Country"] == "Ukraine"]` працює так само, як і раніше — але під капотом pandas порівнює цілочислові індекси, а не рядки. Швидше та економніше.
"""
    )
)

cells.append(
    code(
        """# Фільтр "лише Україна" на Categorical-колонці
ua_respondents = df_opt[df_opt["Country"] == "Ukraine"]
print(f"Респондентів з України: {len(ua_respondents):,}")

# Скільки з них має Master's+? Використовуємо той самий позиційний прийом,
# що і в попередній клітинці (cat.codes), щоб обійти особливості порівняння
# Categorical × str у сучасному pandas.
ua_pos = ua_respondents["EdLevel"].cat.codes
ua_master_plus_mask = (ua_pos >= master_pos) & ua_respondents["EdLevel"].notna()
print(f"З них з Master's+ ступенем: {ua_master_plus_mask.sum():,}")"""
    )
)

# =============================================================================
# SECTION 15 — PRACTICAL ANALYTICS  [FR-017]
# =============================================================================

cells.append(
    md(
        """## 14. Практичний блок: три запитання — три пайплайни

Сюди стікається все, що ми вивчили. Кожен пайплайн — ≤ 10 рядків, читабельний зверху вниз.

### 14.1. Топ-10 найпопулярніших мов програмування (глобально)
"""
    )
)

cells.append(
    code(
        """top10_langs = (
    df.assign(lang_list=df["LanguageHaveWorkedWith"].str.split(";"))
      .explode("lang_list")
      .rename(columns={"lang_list": "Language"})
      .dropna(subset=["Language"])
      ["Language"]
      .value_counts()
      .head(10)
)
top10_langs"""
    )
)

cells.append(
    md(
        """### 14.2. Медіанна компенсація по країнах (топ-20 за кількістю респондентів)"""
    )
)

cells.append(
    code(
        """top20_by_resp = df["Country"].value_counts().head(20).index

med_comp = (
    df[df["Country"].isin(top20_by_resp)]
      .dropna(subset=["ConvertedCompYearly"])
      .groupby("Country")
      .agg(
          n=("ResponseId", "size"),
          median_usd=("ConvertedCompYearly", "median"),
      )
      .sort_values("median_usd", ascending=False)
)
med_comp"""
    )
)

cells.append(
    md(
        """### 14.3. Хто хоче вивчити Rust — за DevType"""
    )
)

cells.append(
    code(
        """rust_by_dev = (
    df.assign(wants=df["LanguageWantToWorkWith"].str.split(";"))
      .explode("wants")
      .dropna(subset=["wants", "DevType"])
      .assign(wants_rust=lambda d: d["wants"] == "Rust")
      .groupby("DevType")
      .agg(
          n_respondents=("ResponseId", "nunique"),
          rust_share=("wants_rust", "mean"),
      )
      .sort_values("rust_share", ascending=False)
      .head(10)
)
rust_by_dev"""
    )
)

# =============================================================================
# SECTION 16 — WHEN PANDAS BREAKS  [FR-018]
# =============================================================================

cells.append(
    md(
        """## 15. Коли pandas не підходить

pandas блискуче працює, доки **весь датасет вміщується в RAM** і **вам достатньо одного процесу**. Коли ці умови ламаються — час шукати інше.

| Інструмент | Масштаб | Стиль API | Коли варто |
|---|---|---|---|
| **pandas** | GB в RAM | Імперативний, рядок за рядком | Аналітика, dev-data, прототип моделей |
| **DuckDB** | TB на диску | SQL (+ Python-bind) | OLAP-запити, файли Parquet/CSV без pre-import у БД |
| **Polars** | GB–TB | Lazy, columnar, Rust-backed | Багатопотокові трансформації, великі pipeline-и |

**Коротко:**

- **DuckDB** — "SQL-рушій, який живе у вашому Python-процесі". Ідеальний, коли маєте купу Parquet/CSV на диску і хочете робити SQL-агрегації без підняття окремої БД.
- **Polars** — "pandas, але багатопотокова, ледача та rust-backed". API схожий на pandas, але швидший на великих обсягах і краще масштабується.

У цій лекції ми **не** встановлюємо жодний з них — це концептуальна карта "куди дивитися далі", а не туторіал. Якщо колись ваш pandas-pipeline почне гальмувати або лізти за межі пам'яті — тепер ви знаєте, куди зазирнути.
"""
    )
)

# =============================================================================
# SECTION 17 — MINI-PROJECT  [FR-019, US2]
# =============================================================================

cells.append(
    md(
        """## 16. Міні-проєкт: "Developer Survey Insights"

Три частини, які ви робите на цій же таблиці `df`. **Це і є міні-проєкт цієї лекції** — замість розрізнених вправ ви будуєте одну зв'язну аналітичну історію.

- **Частина 1 — в аудиторії (~10–15 хв):** простий фільтр + агрегація.
- **Частина 2 — в аудиторії (~10–15 хв):** `.explode()` + `value_counts`.
- **Частина 3 — домашнє завдання (~30–60 хв):** відкрите дослідження з обов'язковим `Categorical` + коментар українською.

Тобто ~25 хв в аудиторії + 30–60 хв удома. Відповідь на Частину 3 — еталонне рішення згорнуте в кінці цього ноутбука.
"""
    )
)

# ---- Part 1 ----
cells.append(
    md(
        """### Частина 1 — Медіанний `WorkExp`: Україна vs Глобально

Порахуйте медіанне значення `WorkExp` для респондентів з України та порівняйте з глобальною медіаною. Виведіть обидва числа та різницю (у роках).

**Підказка:** Секція 7.1 — `groupby` з булевим ключем.

*Спершу спробуйте самі, потім розгорніть розв'язок нижче.*
"""
    )
)

# Hidden solution — use source_hidden
cells.append(
    code(
        """# ==== РОЗВ'ЯЗОК ЧАСТИНИ 1 ====
ua_median_years_pro = df.loc[df["Country"] == "Ukraine", "WorkExp"].median()
global_median_years_pro = df["WorkExp"].median()
delta_years = ua_median_years_pro - global_median_years_pro

print("Медіана WorkExp:")
print(f"  Україна:    {ua_median_years_pro:.1f} років")
print(f"  Глобальна:  {global_median_years_pro:.1f} років")
print(f"  Різниця:   {delta_years:+.1f} років "
      f"({'Україна нижче' if delta_years < 0 else 'Україна вище'})")""",
        hide_input=True,
    )
)

# ---- Part 2 ----
cells.append(
    md(
        """### Частина 2 — Топ-10 мов серед тих, хто "вчиться кодити"

Знайдіть 10 найпопулярніших мов програмування серед респондентів з `MainBranch == "I am learning to code"`. Використайте `str.split(";")` + `.explode()`.

**Підказка:** Секція 6 (`.explode`) + Секція 11 (`.nlargest` / `.value_counts`).

*Спершу спробуйте самі, потім розгорніть розв'язок нижче.*
"""
    )
)

cells.append(
    code(
        """# ==== РОЗВ'ЯЗОК ЧАСТИНИ 2 ====
learners_top_langs = (
    df[df["MainBranch"] == "I am learning to code"]
      .assign(lang_list=lambda d: d["LanguageHaveWorkedWith"].str.split(";"))
      .explode("lang_list")
      .rename(columns={"lang_list": "Language"})
      .dropna(subset=["Language"])
      ["Language"]
      .value_counts()
      .head(10)
)
learners_top_langs""",
        hide_input=True,
    )
)

# ---- Part 3 ----
cells.append(
    md(
        """### Частина 3 (домашнє завдання) — Країна × DevType × Компенсація

Оберіть **одну країну**. У межах цієї країни знайдіть **3 найпопулярніші `DevType`**. Для кожного з них обчисліть медіанну річну компенсацію (`ConvertedCompYearly`).

**Обов'язкові вимоги:**

1. Примусово приведіть колонки `Country` та `DevType` до `Categorical` dtype.
2. Виведіть результат як **охайний (tidy) DataFrame** з колонками `country, dev_type, n_respondents, median_usd` (саме такі назви).
3. Додайте коментар українською (3–5 речень) про те, що ви побачили. Коментар має посилатися хоча б на одне число з вашого результату.

**Критерії оцінювання (6 балів максимум):**

| Критерій | Бали |
|---|---|
| Правильність 3-рядкового DataFrame (колонки, типи, значення) | 3 |
| Чистий pandas-pipeline (method chaining або ясний stepwise; без зайвих циклів) | 2 |
| Якість коментаря (3–5 речень українською, посилається на конкретне число) | 1 |

Прохідний бал: **≥ 4 / 6**.

**Еталонне рішення** — згорнуте в самому низу цього ноутбука (Секція 21). Відкривайте лише після спроби!
"""
    )
)

# =============================================================================
# SECTION 18 — SUMMARY  [FR-003]
# =============================================================================

cells.append(
    md(
        """## 17. Підсумок

За цю лекцію ми пройшли повний шлях від "чистий Python" до "справжня аналітика на живих даних":

- **Основи:** Series, DataFrame, `pd.read_csv` з `usecols=` та `na_values=`.
- **Чистка:** `pd.to_numeric(errors="coerce")` як безпечний шаблон для приведення типів, `isna`/`fillna`/`dropna` для пропущених значень.
- **Вибірка:** `.loc`, `.iloc`, булеві маски з дужками, `.query()`, `.isin()`.
- **Багатозначні колонки:** `str.split(";")` + `.explode()` — один рядок на одне значення.
- **Агрегації:** `groupby().agg()` з named aggregations, `dropna=False`, multi-key.
- **Об'єднання:** `merge(..., validate=...)` як захист від випадкового many-to-many.
- **Переформатування:** `pivot_table` з `margins`, `crosstab` з `normalize`.
- **Ранжування:** `.nlargest`, `.sort_values`, `.rank`.
- **Інтермедіат-патерни:** method chaining (`.pipe`, `.assign`), `.apply`/`.map` з бенчмарком проти векторизації, `Categorical` dtype з реальним виграшем пам'яті.
- **Кордони:** коли pandas ламається і куди дивитися — DuckDB, Polars.

**Наскрізний якір:** Україна — з'явилася в розділах groupby, Categorical та в Частині 1 міні-проєкту. Ви бачили, як наша країна виглядає на глобальній мапі `WorkExp` та освітнього рівня.
"""
    )
)

# =============================================================================
# SECTION 19 — REFERENCES  [FR-024, FR-026]
# =============================================================================

cells.append(
    md(
        """## 18. Джерела

### Дані

- **Stack Overflow Annual Developer Survey 2025** — офіційна сторінка: <https://survey.stackoverflow.co/2025/>
  Ліцензія: **ODbL** (Open Database License). Атрибуцію збережено в цьому ноутбуці.
- Методологія 2025 Survey: <https://survey.stackoverflow.co/2025/methodology/>

### pandas

- Офіційна документація: <https://pandas.pydata.org/docs/>
- "10 minutes to pandas": <https://pandas.pydata.org/docs/user_guide/10min.html>
- pandas Cookbook: <https://pandas.pydata.org/docs/user_guide/cookbook.html>
- Wes McKinney, *Python for Data Analysis* (3rd edition, O'Reilly, 2022) — книжка автора pandas, чудове друге джерело.

### Ті, що ми лише згадали (Секція 15)

- **DuckDB:** <https://duckdb.org/docs/>
- **Polars:** <https://pola.rs/>

### Додаткове читання українською / англійською

- Real Python, "pandas GroupBy: Your Guide to Grouping Data in Python": <https://realpython.com/pandas-groupby/>
- KDnuggets, "Pandas: Advanced GroupBy Techniques": <https://www.kdnuggets.com/pandas-advanced-groupby-techniques-for-complex-aggregations>

> **Правило курсу:** у цій лекції, як і у всьому курсі, **не** використовуємо джерел російського походження. Всі посилання вище — офіційні або англомовні спільноти.
"""
    )
)

# =============================================================================
# SECTION 20 — WHAT'S NEXT  [FR-003]
# =============================================================================

cells.append(
    md(
        """## 19. Що далі?

**Лекція 12 — NumPy + векторизація + проста ML "з нуля".**

Наступного разу ми:

- зазирнемо під капот pandas — там NumPy-масиви;
- зрозуміємо, чому векторизація швидша за цикли (ви це вже бачили в бенчмарку Секції 12, тепер побачимо **чому**);
- побудуємо простий класифікатор (logistic regression) власними руками, без scikit-learn;
- познайомимося з metrics (accuracy, precision, recall).

**Лекція 13 — Візуалізація.**

Очищений `df` з Survey 2025, який ми тут зробили, **ще повернеться**: у Л13 ми намалюємо з нього графіки matplotlib / seaborn / plotly. Тож саме тепер добре зберегти ваш pipeline чистим — за два тижні ви його переіспользуєте.

Щасливих групувань! 🐼
"""
    )
)

# =============================================================================
# SECTION 21 — PART 3 REFERENCE SOLUTION (COLLAPSED AT END)
# =============================================================================

cells.append(
    md(
        """---

## 20. Еталонне рішення міні-проєкту (Частина 3)

> ⚠️ **Відкривайте лише після самостійної спроби.** Код нижче — один з прийнятних варіантів. Ваш pipeline може виглядати інакше — головне, щоб виходив такий самий tidy DataFrame з 3 рядками.
"""
    )
)

cells.append(
    code(
        """# ==== ЕТАЛОННЕ РІШЕННЯ ЧАСТИНИ 3 ====
# Обираємо країну — тут Україна для ілюстрації, ви можете взяти будь-яку
chosen_country = "Ukraine"

# Переводимо Country і DevType у Categorical (вимога задачі)
df3 = df.copy()
df3["Country"] = df3["Country"].astype("category")
df3["DevType"] = df3["DevType"].astype("category")

# Знаходимо 3 найпопулярніші DevType у цій країні
top3_devtypes = (
    df3.loc[df3["Country"] == chosen_country, "DevType"]
       .value_counts()
       .head(3)
       .index
       .tolist()
)
print(f"Top-3 DevType у {chosen_country}:", top3_devtypes)

# Будуємо охайний (tidy) DataFrame з очікуваними колонками
result_df = (
    df3[(df3["Country"] == chosen_country) & (df3["DevType"].isin(top3_devtypes))]
       .dropna(subset=["ConvertedCompYearly"])
       .groupby("DevType", observed=True)
       .agg(
           n_respondents=("ResponseId", "size"),
           median_usd=("ConvertedCompYearly", "median"),
       )
       .reset_index()
       .assign(country=chosen_country)
       .rename(columns={"DevType": "dev_type"})
       [["country", "dev_type", "n_respondents", "median_usd"]]
       .sort_values("n_respondents", ascending=False)
       .reset_index(drop=True)
)

# Приводимо country до Categorical для повної відповідності вимогам
result_df["country"] = result_df["country"].astype("category")
result_df["dev_type"] = result_df["dev_type"].astype("category")

print(result_df.dtypes)
print("---")
result_df""",
        hide_input=True,
    )
)

cells.append(
    md(
        """**Приклад коментаря (3–5 речень українською):**

> У вибірці з України найпоширеніший DevType — повноcteкові розробники, і саме вони мають найвищу медіанну компенсацію серед трьох провідних категорій. Back-end розробники на другому місці за кількістю респондентів, але медіана їхньої компенсації помітно нижча за full-stack. Цікавим є розрив між full-stack і front-end — хоча обсяги респондентів порівнянні, різниця в компенсаціях на рівні %-десятків вказує на те, що full-stack стек наразі краще оплачується на українському ринку. Варто пам'ятати, що вибірка українських респондентів у Survey невелика, тож на ці числа варто дивитися як на орієнтир, а не як на офіційну статистику.

---

🐼 *Кінець лекції 11.* Побачимося на Л12 — NumPy + vectorization + ML з нуля.
"""
    )
)

# =============================================================================
# BUILD AND SAVE
# =============================================================================

nb = nbf.v4.new_notebook()
nb["cells"] = cells
nb["metadata"] = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    },
    "language_info": {
        "name": "python",
        "version": "3.13",
    },
    "authors": [{"name": "Applied Software Development (Python) 2026"}],
}

OUT.write_text(nbf.writes(nb), encoding="utf-8")
print(f"Wrote {OUT} with {len(cells)} cells "
      f"({sum(1 for c in cells if c['cell_type'] == 'markdown')} markdown, "
      f"{sum(1 for c in cells if c['cell_type'] == 'code')} code).")
