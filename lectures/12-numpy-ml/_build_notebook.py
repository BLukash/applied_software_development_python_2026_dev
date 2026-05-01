"""One-shot generator for `lecture-12.ipynb`.

Run once to produce the canonical notebook; after that the .ipynb is the
source of truth and may be edited directly in Jupyter. The generator is kept
around for reproducibility — re-running it will overwrite manual edits, so
treat it as a historical artifact.

Usage:
    python lectures/12-numpy-ml/_build_notebook.py
"""
from __future__ import annotations

from pathlib import Path

import nbformat as nbf

HERE = Path(__file__).parent
OUT = HERE / "lecture-12.ipynb"


def md(src: str) -> nbf.NotebookNode:
    return nbf.v4.new_markdown_cell(src)


def code(src: str, hide_input: bool = False, collapsed: bool = False) -> nbf.NotebookNode:
    cell = nbf.v4.new_code_cell(src)
    meta: dict = {}
    if hide_input:
        meta["source_hidden"] = True
    if meta:
        cell.metadata["jupyter"] = meta
    if collapsed:
        cell.metadata["collapsed"] = True
    return cell


cells: list[nbf.NotebookNode] = []

# =============================================================================
# SECTION 0 — HEADER + PREREQUISITES
# =============================================================================

cells.append(
    md(
        """# Лекція 12 — NumPy, векторизація та логістична регресія "з нуля"

**Курс:** Applied Software Development (Python) 2026 · **Тривалість:** 1.5 години

---

## Передумови

Ця лекція **самодостатня** і не залежить від коду проєкту з лекцій 6–10. Нам не потрібні ані вебфреймворк, ані база даних, ані контейнери.

Достатньо знань з **Лекцій 1–5** плюс мінімальної pandas-інтуїції з **Лекції 11**:

- типи даних, змінні, f-strings (Л1)
- колекції, цикли, генератори списків (Л2–Л3)
- функції, `*args`/`**kwargs`, lambda (Л3–Л4)
- базове файлове введення-виведення (Л5)
- `pd.read_csv`, вибір колонок, `.dropna` (Л11) — лише як "чорний ящик" в одній комірці

Плюс встановлений **Jupyter** і можливість запустити `pip install`.

---

## Як побудована ця лекція

Дві паралельні лінії, які зустрінуться у фіналі:

1. **NumPy як інструмент**: чому він швидкий, як працює `ndarray`, що таке broadcasting, навіщо `%timeit`.
2. **Логістична регресія "з нуля"**: повний цикл binary-класифікатора — від формул до збереженої моделі — лише на NumPy. Ніяких `scikit-learn`, `pytorch` чи інших фреймворків.

Двадцять хвилин у середині лекції відповідатимуть на питання "а навіщо ми взагалі вчили NumPy?" — бо без векторизації цикл градієнтного спуску на 1000 епох був би нестерпно повільним.

> **Датасет:** ми **повторно використовуємо** CSV Stack Overflow Developer Survey 2025, який ви вже завантажили для Лекції 11 (`lectures/11-pandas-analytics/data/survey_results_public.csv`).
>
> Файл є обов'язковим — без нього ноутбук зупиниться з виразним повідомленням про те, де його взяти. Інструкція з завантаження — у `lectures/11-pandas-analytics/README.md`.
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

1. Пояснити, **чому NumPy швидший за Python list** — суцільна пам'ять, фіксовані dtypes, диспатч до C.
2. Створювати та маніпулювати `ndarray` — індексація, зрізи, fancy indexing, boolean masking, broadcasting.
3. Виміряти різницю у швидкості векторизованого коду через `%timeit` і свідомо вирішувати, коли вектор економить час, а коли — ні.
4. **Реалізувати з нуля** бінарний логістичний класифікатор: від sigmoid та функції втрат до циклу градієнтного спуску, метрик і збереження моделі у `.npz`.
5. Прочитати готову модель з `.npz` і зробити нею прогноз — і зрозуміти, чому це той самий патерн, що лежить в основі будь-якої нейронної мережі.
"""
    )
)

# =============================================================================
# SECTION 2 — WHY NUMPY IS FAST
# =============================================================================

cells.append(
    md(
        """## Чому NumPy швидкий?

Якщо коротко — **через три речі**, які Python list зробити не може:

### 1. Суцільна пам'ять (contiguous memory)

Python `list[int]` — це масив **посилань** на окремі int-об'єкти, розкидані по купі. Кожен int — повноцінний PyObject з лічильником посилань, типом і значенням; це 28 байт замість 8.

NumPy `ndarray` — це один **суцільний шматок пам'яті** з фіксованим dtype. Мільйон `int64`-чисел — це рівно 8 МБ підряд, без жодного зайвого байта. Процесор любить таку пам'ять: префетчер передбачає наступні читання, кеш-лінії заповнюються одна за одною.

### 2. Фіксований dtype

У Python list елементи можуть бути будь-якого типу — `[1, "two", 3.14, None]` валідний. Це гнучко, але для математики дорого: щоразу інтерпретатор має спитати "а це що за об'єкт?".

В `ndarray` тип фіксований під час створення — `int32`, `float64`, `bool`. Ніяких перевірок типу на кожному елементі під час циклу.

### 3. Диспатч до C / SIMD

Коли ви пишете `arr ** 2` на Python-списку, інтерпретатор робить ~мільйон викликів `__mul__` — кожен з оверхедом інтерпретатора (десятки наносекунд на ітерацію).

`ndarray ** 2` робить **один** виклик C-функції, яка проганяє SIMD-інструкції процесора по суцільному масиву. SIMD = "Single Instruction, Multiple Data" — одна інструкція обробляє 4 або 8 чисел одночасно.

> **Перевіримо це експериментально** в Розділі 8 — там ми зробимо `%timeit`-бенчмарк і побачимо ~100×–500× різницю на мільйонному масиві.
"""
    )
)

# =============================================================================
# CONSTANTS + ENV CHECK CELL
# =============================================================================

cells.append(
    md(
        """## Константи лекції та перевірка середовища

Закріпимо всі магічні числа в одному місці на самому початку — щоб у міні-проєкті можна було легко змінити learning rate чи кількість епох."""
    )
)

cells.append(
    code(
        """from pathlib import Path

import numpy as np
import pandas as pd

# --- Шляхи ---
# Шукаємо CSV у L11 спочатку відносно теки лекції, потім відносно cwd.
_HERE = Path.cwd()
_CSV_CANDIDATES = [
    Path("../11-pandas-analytics/data/survey_results_public.csv"),
    Path("lectures/11-pandas-analytics/data/survey_results_public.csv"),
    _HERE.parent / "11-pandas-analytics" / "data" / "survey_results_public.csv",
]
SURVEY_CSV_PATH = next((p for p in _CSV_CANDIDATES if p.exists()), _CSV_CANDIDATES[0])

ARTIFACT_PATH = Path("artifacts/model.npz")
if not ARTIFACT_PATH.parent.exists():
    # Якщо запускаємо з іншої теки — спробуємо знайти теку lectures/12-numpy-ml/.
    alt = Path("lectures/12-numpy-ml/artifacts/model.npz")
    if alt.parent.exists():
        ARTIFACT_PATH = alt

# --- Гіперпараметри моделі ---
SEED = 42                  # відтворюваність
LEARNING_RATE = 0.1        # для стандартизованих ознак працює стабільно
EPOCHS = 1000              # достатньо, щоб loss вийшов на плато
PRINT_EVERY = 100          # виведемо 11 рядків (epoch 0, 100, ..., 1000)
TRAIN_FRACTION = 0.8       # 80/20 train/test split

# --- Перевірка середовища ---
print(f"NumPy:  {np.__version__}")
print(f"pandas: {pd.__version__}")
print(f"Survey CSV path: {SURVEY_CSV_PATH}")
print(f"Survey CSV exists: {SURVEY_CSV_PATH.exists()}")
print(f"Artifact path:   {ARTIFACT_PATH}")
"""
    )
)

# =============================================================================
# SECTION 3 — NDARRAY BASICS
# =============================================================================

cells.append(
    md(
        """## Основи `ndarray`: створення та властивості

`ndarray` — це **n-вимірний масив** фіксованого dtype. Є кілька канонічних способів його створити."""
    )
)

cells.append(
    code(
        """# Зі звичайного Python-списку
a = np.array([1, 2, 3, 4, 5])
print(a, a.dtype)
"""
    )
)

cells.append(
    code(
        """# Заповнити нулями / одиницями — корисно для ініціалізації параметрів
zeros = np.zeros((3, 4))      # 2-D масив 3×4
ones = np.ones(5, dtype=np.int32)
print("zeros shape:", zeros.shape, "dtype:", zeros.dtype)
print("ones:", ones)
"""
    )
)

cells.append(
    code(
        """# Прогресії
print(np.arange(0, 10, 2))         # від 0 до 10 з кроком 2 (виключно)
print(np.linspace(0, 1, num=5))    # 5 рівномірних точок від 0 до 1 (включно)
"""
    )
)

cells.append(
    code(
        """# Випадкові числа — сучасний API через Generator
rng = np.random.default_rng(seed=SEED)
sample = rng.standard_normal((2, 3))   # стандартний нормальний розподіл, форма 2×3
print(sample)
"""
    )
)

cells.append(
    md(
        """### Атрибути `ndarray`, які ви бачитимете щодня

| Атрибут | Що показує |
|---------|------------|
| `.shape` | кортеж розмірностей: `(3, 4)` для 2-D масиву 3×4 |
| `.dtype` | тип даних: `int64`, `float64`, `bool`, … |
| `.ndim` | кількість вимірів: 1, 2, 3, … |
| `.size` | загальна кількість елементів (= `prod(.shape)`) |
| `.nbytes` | скільки байтів масив займає в пам'яті |
"""
    )
)

cells.append(
    code(
        """matrix = rng.standard_normal((100, 50))
print(f"shape:  {matrix.shape}")
print(f"dtype:  {matrix.dtype}")
print(f"ndim:   {matrix.ndim}")
print(f"size:   {matrix.size}")
print(f"nbytes: {matrix.nbytes:,} (= {matrix.size} × {matrix.itemsize} байт)")
"""
    )
)

# =============================================================================
# SECTION 4 — DTYPES
# =============================================================================

cells.append(
    md(
        """## dtype: коли важливо обрати правильний

Більшість коду працює з `int64` чи `float64` за замовчуванням — і це правильно. Але іноді dtype має значення:

- **Пам'ять:** float32 займає вдвічі менше за float64. На матриці `(10000, 1000)` це різниця у 40 МБ.
- **Точність:** float32 має ≈7 значущих цифр, float64 — ≈15. Для фінансових розрахунків float32 неприйнятний.
- **Сумісність з GPU / ML-фреймворками:** PyTorch і TensorFlow часто очікують float32 за замовчуванням.

Перетворення — через `.astype()`."""
    )
)

cells.append(
    code(
        """big = np.arange(1_000_000, dtype=np.int64)
big32 = big.astype(np.int32)
print(f"int64: {big.nbytes / 1e6:.2f} MB")
print(f"int32: {big32.nbytes / 1e6:.2f} MB  (вдвічі менше)")
"""
    )
)

# =============================================================================
# SECTION 5 — INDEXING & SLICING (view vs copy)
# =============================================================================

cells.append(
    md(
        """## Індексація та зрізи: view vs copy

NumPy має **три** способи "вибрати елементи":

1. **Basic slicing** (`arr[1:4]`, `arr[:, ::2]`) — повертає **view** на ту саму пам'ять.
2. **Fancy indexing** (`arr[[0, 2, 5]]`) — повертає **copy**.
3. **Boolean masking** (`arr[arr > 0]`) — повертає **copy**.

Різниця критична: якщо ви модифікуєте view, оригінал змінюється. Якщо модифікуєте copy — ні."""
    )
)

cells.append(
    code(
        """arr2d = np.arange(20).reshape(4, 5)
print(arr2d)
"""
    )
)

cells.append(
    code(
        """# Basic slicing — 1-D і 2-D
print("rows 1-3, every 2nd col:")
print(arr2d[1:3, ::2])
"""
    )
)

cells.append(
    code(
        """# Fancy indexing — обираємо рядки за списком індексів
print("rows 0, 2, 3:")
print(arr2d[[0, 2, 3]])
"""
    )
)

cells.append(
    code(
        """# Boolean masking — обираємо елементи за умовою
big_values = arr2d[arr2d > 12]
print("елементи більші за 12:", big_values)
"""
    )
)

cells.append(
    md(
        """### View vs copy — наочно

Це найпоширеніша "тиха" помилка з NumPy. Дивіться:"""
    )
)

cells.append(
    code(
        """original = np.arange(10)
view = original[2:6]       # basic slicing → view
view[0] = -999             # модифікуємо view
print("original:", original)   # ⚠️ original теж змінився
print("view:    ", view)
"""
    )
)

cells.append(
    code(
        """original = np.arange(10)
copy = original[[2, 3, 4, 5]]   # fancy indexing → copy
copy[0] = -999                  # модифікуємо copy
print("original:", original)    # original НЕ змінився
print("copy:    ", copy)
"""
    )
)

cells.append(
    md(
        """**Запам'ятайте:** basic slicing = view, fancy/boolean = copy. Якщо потрібен незалежний масив після basic slicing — викличте `.copy()` явно."""
    )
)

# =============================================================================
# SECTION 6 — BROADCASTING
# =============================================================================

cells.append(
    md(
        """## Broadcasting: правила та приклади

Broadcasting — це механізм, який дозволяє виконувати операції над масивами **різних форм** без явного копіювання даних.

### Правила (читати справа наліво)

При операції над двома масивами NumPy порівнює їхні форми поелементно з кінця:

1. Якщо розмірності **рівні** — все ок, операція поелементна.
2. Якщо одна з розмірностей дорівнює **1** — вона "розтягується" до іншої.
3. Якщо одна форма **коротша** — спереду додаються одиниці (так само "розтягуються").
4. Інакше — **`ValueError`**.

Простіше показати на прикладах."""
    )
)

cells.append(
    code(
        """# Приклад 1: (3, 4) + (4,) → (3, 4)
# Вектор довжини 4 розтягується вздовж першої осі
M = np.ones((3, 4))
v = np.array([10, 20, 30, 40])
print(M + v)
"""
    )
)

cells.append(
    code(
        """# Приклад 2: (3, 1) + (1, 4) → (3, 4)
# Класичний "outer-add" — стовпець плюс рядок утворюють матрицю
col = np.array([[1], [2], [3]])      # shape (3, 1)
row = np.array([[10, 20, 30, 40]])   # shape (1, 4)
print(col + row)
"""
    )
)

cells.append(
    code(
        """# Приклад 3: (5,) + scalar → (5,)
# Скаляр — це фактично shape (), яка broadcast-иться куди завгодно
print(np.array([1, 2, 3, 4, 5]) + 100)
"""
    )
)

cells.append(
    code(
        """# Приклад 4: НЕ працює — (3, 4) + (3,)
# Праві осі (4 і 3) не рівні і жодна не дорівнює 1
M = np.ones((3, 4))
bad = np.array([1, 2, 3])
try:
    M + bad
except ValueError as e:
    print(f"ValueError: {e}")
"""
    )
)

cells.append(
    md(
        """**Інтуїція:** broadcasting — це "віртуальне" розтягування без копіювання даних у пам'яті. Це і швидко, і елегантно. Ми будемо його активно використовувати у Розділі 10 (стандартизація: `(X - mean) / std` робить broadcasting `(n, p) - (p,)`)."""
    )
)

# =============================================================================
# SECTION 7 — ELEMENTWISE / REDUCTION / LINALG OPS
# =============================================================================

cells.append(
    md(
        """## Поелементні, редукційні та лінійно-алгебраїчні операції

Це робочий мінімум NumPy-операцій, які ми використовуватимемо до кінця лекції."""
    )
)

cells.append(
    code(
        """# Поелементні: працюють "пометрово"
x = np.array([1.0, 2.0, 4.0, 16.0])
print("exp:", np.exp(x))   # знадобиться у sigmoid
print("log:", np.log(x))   # знадобиться у BCE loss
"""
    )
)

cells.append(
    md(
        """### Редукції та осі

Запам'ятайте одне правило: **`axis=k` — це вісь, яка зникне**.

Для 2-D масиву форми `(rows, cols)`:

- `axis=0` колапсує вимір `rows` → результат форми `(cols,)` — це **column sums** (одне число на колонку).
- `axis=1` колапсує вимір `cols` → результат форми `(rows,)` — це **row sums** (одне число на рядок).

Без аргументу `axis=` редукція зведе масив до одного скаляра."""
    )
)

cells.append(
    code(
        """grid = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12]])
print("grid.shape =", grid.shape)
print("sum axis=0 → column sums, форма (4,):", grid.sum(axis=0))
print("sum axis=1 → row sums,    форма (3,):", grid.sum(axis=1))
print("mean axis=0 (по колонках):", grid.mean(axis=0))
print("std  axis=1 (по рядках):  ", grid.std(axis=1))
print("argmax (без осі, скаляр): ", grid.argmax())
"""
    )
)

cells.append(
    md(
        """### Лінійна алгебра: `np.dot` і `@`

Для нашої моделі `ŷ = σ(X·w + b)` потрібен матрично-векторний добуток. У NumPy є два способи його записати:

- `np.dot(a, b)` — старий API
- `a @ b` — оператор Python 3.5+, ідентичний для 1-D і 2-D масивів

Для матриць та векторів **завжди обирайте `@`** — він візуально нагадує математичний запис."""
    )
)

cells.append(
    code(
        """X = rng.standard_normal((4, 3))     # 4 зразки, 3 ознаки
w = np.array([1.0, -2.0, 0.5])
b = 0.1

# Два способи — той самий результат
print("np.dot(X, w):", np.dot(X, w))
print("X @ w:       ", X @ w)
print("X @ w + b:   ", X @ w + b)   # broadcasting додає скаляр до вектора
"""
    )
)

cells.append(
    md(
        """> **Дрібний нюанс:** `np.dot` і `@` дають однакові результати для 1-D і 2-D операндів. Розходяться вони лише на тензорах вищого порядку (3-D+) — там `np.dot` має sum-product семантику, а `@` робить batched matmul. У цій лекції ми працюємо тільки з 1-D і 2-D, тож обидва варіанти еквівалентні."""
    )
)

# =============================================================================
# SECTION 8 — %TIMEIT PERFORMANCE
# =============================================================================

cells.append(
    md(
        """## Швидкість: `%timeit` Python vs NumPy

![NumPy vs Python — швидкість](assets/memes/numpy-vs-python-speed.png)

Час побачити, чому NumPy існує. Зробимо одне й те саме завдання — піднести мільйон чисел до квадрату — двома способами і виміряємо."""
    )
)

cells.append(
    code(
        """data = list(range(1_000_000))
%timeit [x * x for x in data]
"""
    )
)

cells.append(
    code(
        """arr = np.arange(1_000_000)
%timeit arr ** 2
"""
    )
)

cells.append(
    md(
        """### Чому така велика різниця?

Python-цикл інтерпретується **по одному елементу**: щоразу береться об'єкт `int`, викликається його `__mul__`, повертається новий об'єкт `int`. Це десятки наносекунд оверхеду на кожну ітерацію — мільйон ітерацій = десятки мілісекунд.

NumPy-операція `arr ** 2` робить **один** виклик C-функції, яка проганяє SIMD-інструкції процесора по суцільному масиву. Накладні витрати — стала ~мікросекунда; решта — чиста математика на швидкості пам'яті.

> На дуже маленьких масивах (десятки елементів) NumPy може програти через свій сталий оверхед. Векторизуйте там, де це **природно** — від кількох сотень елементів і більше. Не перетворюйте на `ndarray` все підряд із принципу."""
    )
)

# =============================================================================
# SECTION 9 — ML: DATA LOADING (with meme 2 and dual-path loader)
# =============================================================================

cells.append(
    md(
        """## Перехід до ML: завантаження даних

![Логістична регресія — без магії](assets/memes/lr-is-just-sigmoid.png)

Тепер NumPy працює нам на руку: ми побудуємо **бінарний класифікатор** — логістичну регресію — повністю на NumPy. Без `scikit-learn`. Без `pytorch`. Без жодного фреймворка.

### Завдання

На даних Stack Overflow Survey 2025 передбачимо: чи отримує респондент **зарплату вище медіани у своїй країні** на основі чотирьох ознак:

| # | Ознака | Що це |
|---|--------|-------|
| 1 | `years_code` | Скільки років пише код (`YearsCode`) |
| 2 | `work_exp` | Скільки років професійного досвіду (`WorkExp`) |
| 3 | `ed_level_ord` | Освіта як порядкова шкала: `0` = початкова, `5` = докторат |
| 4 | `is_remote` | `1` якщо повністю віддалена робота, `0` інакше |

Чому медіана **по своїй країні**, а не глобальна? Бо інакше модель просто вивчить, що "респондент зі США/Швейцарії = вище медіани", і ми нічого нового не дізнаємось. Per-country split робить задачу нетривіальною.

> **Готуємося психологічно:** із цими 4 ознаками лінійна модель досягає accuracy ≈ **0.64** — лише 14 п.п. над baseline 0.50. Це **стеля** лінійної моделі на цих ознаках, а не наш баг. Чому навіть такий результат — пізнавальний, дивіться Розділ 14 (метрики). Коротше: ми вчимо **цикл навчання**, не оптимізуємо рейтинг на Kaggle.

> **Етична примітка:** це навчальний приклад, не серйозний інструмент прогнозування зарплат. Він демонструє цикл навчання, не претендує на інсайти про ринок праці.
"""
    )
)

cells.append(
    code(
        """# --- Завантаження Survey CSV ---
USECOLS = ["ResponseId", "Country", "YearsCode", "WorkExp",
           "EdLevel", "RemoteWork", "ConvertedCompYearly"]

# Порядкова шкала EdLevel — реальні значення 2025 містять curly-apostrophe (’).
ED_MAP = {
    "Primary/elementary school": 0,
    "Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)": 1,
    "Some college/university study without earning a degree": 2,
    "Associate degree (A.A., A.S., etc.)": 2,
    "Bachelor’s degree (B.A., B.S., B.Eng., etc.)": 3,
    "Master’s degree (M.A., M.S., M.Eng., MBA, etc.)": 4,
    "Professional degree (JD, MD, Ph.D, Ed.D, etc.)": 5,
    "Something else": 2.5,
    "Other (please specify):": 2.5,
}

if not SURVEY_CSV_PATH.exists():
    raise FileNotFoundError(
        f"Survey CSV не знайдено за шляхом {SURVEY_CSV_PATH}. "
        "Завантажте його за інструкцією з lectures/11-pandas-analytics/README.md "
        "(розділ 'Download the 2025 Stack Overflow Annual Developer Survey')."
    )

df = pd.read_csv(SURVEY_CSV_PATH, usecols=USECOLS)
df = df.dropna(subset=["Country", "ConvertedCompYearly"]).copy()

country_median = df.groupby("Country")["ConvertedCompYearly"].transform("median")
y_full = (df["ConvertedCompYearly"] > country_median).astype(int).to_numpy()

years_code = pd.to_numeric(df["YearsCode"], errors="coerce").to_numpy()
work_exp = pd.to_numeric(df["WorkExp"], errors="coerce").to_numpy()
ed_level_ord = df["EdLevel"].map(ED_MAP).to_numpy()
is_remote = (df["RemoteWork"] == "Remote").astype(int).to_numpy()

X_full = np.column_stack([years_code, work_exp, ed_level_ord, is_remote])
keep = ~np.isnan(X_full).any(axis=1)
X, y = X_full[keep], y_full[keep]

print(f"Завантажено {len(X)} рядків зі Survey: {SURVEY_CSV_PATH}")
print(f"X.shape = {X.shape},  y.shape = {y.shape}")
print(f"Баланс класів: y.mean() = {y.mean():.3f}")
"""
    )
)

# =============================================================================
# SECTION 10 — STANDARDIZATION (function only)
# =============================================================================

cells.append(
    md(
        """## Стандартизація: чому, як, без витоку даних

Наші чотири ознаки — у дуже різних масштабах:

- `years_code`: 0–50
- `work_exp`: 0–40
- `ed_level_ord`: 0–5
- `is_remote`: 0 або 1

Якщо ми так подамо їх у градієнтний спуск, крок навчання вздовж осі `years_code` буде "великим" (бо самі значення великі), а вздовж `is_remote` — мікроскопічним. Модель або не зійдеться, або буде осцилювати.

### Z-score стандартизація

Кожна ознака переводиться у "скільки стандартних відхилень від середнього":

$$
x_{\\text{std}} = \\frac{x - \\mu}{\\sigma}
$$

Після цього всі ознаки в середньому 0 і зі стандартним відхиленням 1 — крок навчання працює рівномірно по всіх осях.

### ⚠️ Дуже важливо: data leakage

`mean` і `std` обчислюємо **тільки з тренувальної вибірки**. Інакше ми "підглянемо" в тестову вибірку через статистики — і отримаємо нереалістично оптимістичну оцінку якості.

Запам'ятайте правило: будь-яке `fit` / "вчимо параметри" робиться лише на тренуванні. Тест ми лише `transform`-уємо."""
    )
)

cells.append(
    code(
        """def standardize(X_in: np.ndarray, mean: np.ndarray, std: np.ndarray) -> np.ndarray:
    \"\"\"Z-score стандартизація з broadcasting: (n, p) - (p,) → (n, p).

    Guard від ділення на нуль: якщо ознака константна у train-вибірці,
    її std буде 0; підставляємо 1.0, щоб уникнути nan. Сама ознака після
    цього стане усюди (X - mean) / 1 = 0 — нейтральною для моделі.
    \"\"\"
    safe_std = np.where(std == 0, 1.0, std)
    return (X_in - mean) / safe_std
"""
    )
)

cells.append(
    md(
        """> **Real-data papercut:** `std == 0` означає, що в train-вибірці ця ознака константна (наприклад, у вашому split усі респонденти випадково виявились "не remote"). Без guard-а ділення на 0 дає `inf`/`nan`, який мовчки отруює градієнти і весь loss стає `nan`. Один рядок `np.where(std == 0, 1.0, std)` рятує від кількох годин дебагу."""
    )
)

# =============================================================================
# SECTION 11 — TRAIN/TEST SPLIT + STANDARDIZATION FIT
# =============================================================================

cells.append(
    md(
        """## Поділ train/test без `sklearn`

Класичний 80/20 split можна зробити одним рядком NumPy — нам потрібна лише перестановка індексів."""
    )
)

cells.append(
    code(
        """rng_split = np.random.default_rng(seed=SEED)
n = len(X)
perm = rng_split.permutation(n)        # випадкова перестановка індексів 0..n-1
n_train = int(TRAIN_FRACTION * n)
train_idx, test_idx = perm[:n_train], perm[n_train:]

X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]

print(f"X_train.shape = {X_train.shape},  y_train.shape = {y_train.shape}")
print(f"X_test.shape  = {X_test.shape},  y_test.shape  = {y_test.shape}")
"""
    )
)

cells.append(
    md(
        """**Чому seed=42?** Щоб результат був **відтворюваним** — той самий split на вашій машині й моїй. У реальному ML-проєкті ви б експериментували з різними seeds, щоб побачити, наскільки результат залежить від конкретного розбиття."""
    )
)

cells.append(
    code(
        """# fit статистик ТІЛЬКИ на тренуванні
feature_mean = X_train.mean(axis=0)
feature_std = X_train.std(axis=0, ddof=0)

X_train_std = standardize(X_train, feature_mean, feature_std)
X_test_std = standardize(X_test, feature_mean, feature_std)

print("feature_mean:", feature_mean)
print("feature_std: ", feature_std)
print(f"X_train_std mean (≈0): {X_train_std.mean(axis=0).round(3)}")
print(f"X_train_std std  (≈1): {X_train_std.std(axis=0).round(3)}")
"""
    )
)

# =============================================================================
# SECTION 12 — LOGISTIC REGRESSION MATH
# =============================================================================

cells.append(
    md(
        """## Логістична регресія: математика

Уся модель — три формули. Серйозно, три.

### 1. Sigmoid

Стискає будь-яке дійсне число в інтервал $(0, 1)$ — щоб результат можна було інтерпретувати як ймовірність:

$$
\\sigma(z) = \\frac{1}{1 + e^{-z}}
$$

### 2. Лінійна модель + sigmoid

Беремо лінійну комбінацію ознак, додаємо bias, і пропускаємо через sigmoid:

$$
\\hat{y} = \\sigma(X w + b)
$$

де $X$ має форму $(n, p)$, $w$ — $(p,)$, $b$ — скаляр, а $\\hat{y}$ — вектор $(n,)$ з передбаченими ймовірностями класу 1.

### 3. Binary cross-entropy (BCE) loss

Функція втрат, яка карає модель тим сильніше, чим впевненіше вона помилилась:

$$
L(w, b) = -\\frac{1}{n} \\sum_{i=1}^{n} \\Bigl[\\, y_i \\log \\hat{y}_i + (1 - y_i) \\log (1 - \\hat{y}_i) \\,\\Bigr]
$$

Якщо $y_i = 1$ і $\\hat{y}_i \\to 1$, то $\\log \\hat{y}_i \\to 0$ — кара мала. Якщо $y_i = 1$ і $\\hat{y}_i \\to 0$, то $\\log \\hat{y}_i \\to -\\infty$ — кара величезна. Симетрично для $y_i = 0$.

Тепер реалізуємо. І одразу зустрінемо першу пастку: **числову нестабільність**."""
    )
)

cells.append(
    md(
        """### Наївний sigmoid — і чому він ламається

Наївна формула $\\sigma(z) = 1/(1+e^{-z})$ переповнює float64, коли `z` — **великий від'ємний**: тоді `-z` — велике додатне, а `np.exp` величезного додатного дає `inf`. Симптом: warning про overflow і нуль на виході.

Парний випадок: коли `z` — **велике додатне**, формула спрацьовує тихо й повертає рівно `1.0`. Жодного warning. Але далі у BCE ми обчислюємо `log(1 - σ(z)) = log(0) = -inf` — і loss стає `nan`. Тому ми додамо ще й `np.clip` у визначенні BCE-loss трохи нижче.

Подивимось на обидва випадки в дії:"""
    )
)

cells.append(
    code(
        """def sigmoid_naive(z):
    return 1.0 / (1.0 + np.exp(-z))

print("sigmoid_naive([-2, 0, 2]) =", sigmoid_naive(np.array([-2.0, 0.0, 2.0])))
# Велике ВІД'ЄМНЕ z: np.exp(-z) → inf, sigmoid → 0 з warning
print("sigmoid_naive(-1000) =", sigmoid_naive(np.array([-1000.0])), "(overflow warning)")
# Велике ДОДАТНЕ z: тихо повертає 1.0, але далі log(1 - 1.0) = -inf отруює BCE
print("sigmoid_naive(+1000) =", sigmoid_naive(np.array([1000.0])), "(тихо, але ламає loss)")
"""
    )
)

cells.append(
    md(
        """### Числово стабільний sigmoid

Хитрість — обрати таку гілку формули, де експонента **завжди** має від'ємний (або нульовий) аргумент:

- для $z \\geq 0$: класична $1/(1+e^{-z})$ — тут $-z \\leq 0$, тому $e^{-z} \\in (0, 1]$ — overflow неможливий;
- для $z < 0$: переписана $e^{z}/(1+e^{z})$ — тут $z < 0$, тому $e^{z} \\in (0, 1)$ — теж overflow неможливий.

Це той самий трюк, який використовує `scipy.special.expit`."""
    )
)

cells.append(
    code(
        """def sigmoid(z: np.ndarray) -> np.ndarray:
    \"\"\"Числово стабільний sigmoid — без overflow на великих |z|.\"\"\"
    z = np.asarray(z, dtype=np.float64)
    out = np.empty_like(z)
    pos = z >= 0
    # для z >= 0: класична формула, exp(-z) ∈ (0, 1]
    out[pos] = 1.0 / (1.0 + np.exp(-z[pos]))
    # для z < 0: переписана форма, exp(z) ∈ (0, 1)
    exp_z = np.exp(z[~pos])
    out[~pos] = exp_z / (1.0 + exp_z)
    return out


print(sigmoid(np.array([-1000.0, -2.0, 0.0, 2.0, 1000.0])))
"""
    )
)

cells.append(
    md(
        """### Binary cross-entropy — теж із захистом від `log(0)`"""
    )
)

cells.append(
    code(
        """def bce_loss(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    \"\"\"Усереднена binary cross-entropy. Клампимо y_pred, щоб уникнути log(0).\"\"\"
    eps = 1e-15
    y_pred_clipped = np.clip(y_pred, eps, 1.0 - eps)
    return -float(np.mean(
        y_true * np.log(y_pred_clipped) + (1 - y_true) * np.log(1 - y_pred_clipped)
    ))


# Швидка перевірка: ідеальний прогноз → loss ≈ 0
print(bce_loss(np.array([1, 0, 1]), np.array([1.0, 0.0, 1.0])))
# Випадковий прогноз → loss ≈ log(2) ≈ 0.693
print(bce_loss(np.array([1, 0, 1]), np.array([0.5, 0.5, 0.5])))
"""
    )
)

# =============================================================================
# SECTION 13 — GRADIENT DESCENT TRAINING LOOP (with diagram)
# =============================================================================

cells.append(
    md(
        """## Цикл градієнтного спуску

![Цикл навчання логістичної регресії](assets/diagrams/lr-flow.png)

Готова модель = знайдені $w$ та $b$, що мінімізують loss. Шукаємо їх ітеративно: кожну епоху рахуємо градієнт і робимо маленький крок у бік його зменшення.

### Аналітичний градієнт

Краса логістичної регресії в тому, що похідна BCE по параметрах має дуже чисту форму — фактор $(\\hat{y} - y)$ скорочує всі ланцюгові правила:

$$
\\frac{\\partial L}{\\partial w} = \\frac{1}{n} X^{\\top} (\\hat{y} - y)
\\qquad
\\frac{\\partial L}{\\partial b} = \\frac{1}{n} \\sum_{i} (\\hat{y}_i - y_i)
$$

І крок оновлення:

$$
w \\leftarrow w - \\eta \\cdot \\frac{\\partial L}{\\partial w}, \\qquad
b \\leftarrow b - \\eta \\cdot \\frac{\\partial L}{\\partial b}
$$

де $\\eta$ — learning rate.

### Реалізація — буквально один цикл"""
    )
)

cells.append(
    code(
        """n_train_, p = X_train_std.shape
w = np.zeros(p)
b = 0.0
loss_history: list[float] = []

for epoch in range(EPOCHS):
    # Forward
    z = X_train_std @ w + b
    yhat = sigmoid(z)
    loss = bce_loss(y_train, yhat)
    loss_history.append(loss)

    # Backward — аналітичний градієнт
    grad_w = (1.0 / n_train_) * X_train_std.T @ (yhat - y_train)
    grad_b = (1.0 / n_train_) * (yhat - y_train).sum()

    # Update
    w -= LEARNING_RATE * grad_w
    b -= LEARNING_RATE * grad_b

    if epoch % PRINT_EVERY == 0:
        print(f"epoch {epoch:4d}  loss = {loss:.4f}")

# Фінальний loss — після останнього оновлення
final_loss = bce_loss(y_train, sigmoid(X_train_std @ w + b))
print(f"epoch {EPOCHS:4d}  loss = {final_loss:.4f}")
print(f"\\nFinal w = {w.round(3)}")
print(f"Final b = {b:+.3f}")
"""
    )
)

cells.append(
    md(
        """**Loss падає монотонно** — це знак, що learning rate підібраний нормально й градієнти правильні. Якщо ви бачите щось протилежне — нижче список найчастіших причин."""
    )
)

cells.append(
    md(
        """> **Якщо loss зростає або стає `nan`** — три типові причини: (1) **lr завеликий** → спробуйте 0.01, (2) **ознаки не стандартизовані** → крок по великих ознаках "переб'є" малі, (3) **sigmoid overflow** → переконайтесь, що використовуєте стабільну версію з Розділу 12.
"""
    )
)

# =============================================================================
# SECTION 14 — METRICS
# =============================================================================

cells.append(
    md(
        """## Метрики: accuracy, precision, recall, confusion matrix

Дві ймовірнісні відповіді моделі ($\\hat{y}_i$) ми перетворюємо у бінарні прогнози простим порогом 0.5:"""
    )
)

cells.append(
    code(
        """def predict(X_raw: np.ndarray, w: np.ndarray, b: float,
            mean: np.ndarray, std: np.ndarray) -> np.ndarray:
    \"\"\"Повний інференс: стандартизація + лінійна модель + sigmoid + поріг 0.5.\"\"\"
    X_std = standardize(X_raw, mean, std)
    return (sigmoid(X_std @ w + b) >= 0.5).astype(int)


y_pred = predict(X_test, w, b, feature_mean, feature_std)
print(f"y_pred[:20] = {y_pred[:20]}")
print(f"y_test[:20] = {y_test[:20]}")
"""
    )
)

cells.append(
    md(
        """### Accuracy — і чому її одної замало"""
    )
)

cells.append(
    code(
        """accuracy = float((y_pred == y_test).mean())
print(f"Accuracy on test: {accuracy:.3f}")

# Класовий баланс — щоб зрозуміти, чи accuracy чесна
balance = np.bincount(y_test) / len(y_test)
print(f"Test class balance: {balance.round(3)}")
print("(ідеально збалансований target — 0.5/0.5; тоді accuracy 0.5 = випадок)")
"""
    )
)

cells.append(
    md(
        """> **Чому accuracy ~0.64, а не 0.95?** Бо ми навмисне обрали **складну** задачу: передбачити медіану зарплати у власній країні маючи лише 4 ознаки. Лінійна модель з такими даними витискає максимум — і це 14% над випадковим baseline (0.50). Для серйознішої точності потрібно:
> - **більше ознак** (наприклад, one-hot топ-DevType, мова програмування, мова країни);
> - **нелінійна модель** (gradient boosting, нейромережа);
> - **краща інженерія ознак** (взаємодії, поліноми).
>
> Усе це — для іншого курсу. Зараз ми вчимо **цикл навчання**, а не оптимізуємо accuracy.
"""
    )
)

cells.append(
    md(
        """### Confusion matrix — що саме модель плутає

|                  | predicted 0 | predicted 1 |
|------------------|-------------|-------------|
| **actual 0**     | TN          | FP          |
| **actual 1**     | FN          | TP          |

- TN (true negative): прогноз 0, реально 0 — добре
- TP (true positive): прогноз 1, реально 1 — добре
- FP (false positive): прогноз 1, реально 0 — "хибна тривога"
- FN (false negative): прогноз 0, реально 1 — "пропущена ціль"
"""
    )
)

cells.append(
    code(
        """tn = int(((y_pred == 0) & (y_test == 0)).sum())
fp = int(((y_pred == 1) & (y_test == 0)).sum())
fn = int(((y_pred == 0) & (y_test == 1)).sum())
tp = int(((y_pred == 1) & (y_test == 1)).sum())

confusion_matrix = np.array([[tn, fp], [fn, tp]])
print("Confusion matrix:")
print(f"              pred=0  pred=1")
print(f"  actual=0  {tn:7d} {fp:7d}")
print(f"  actual=1  {fn:7d} {tp:7d}")
assert tn + fp + fn + tp == len(y_test)
"""
    )
)

cells.append(
    md(
        """### Precision і recall

- **Precision** = TP / (TP + FP) — "коли модель сказала 1, як часто вона була права?"
- **Recall** = TP / (TP + FN) — "із усіх реальних 1, скільки модель знайшла?"

Існує природний trade-off: підняти поріг → менше FP, більше FN → precision росте, recall падає. Цей trade-off ви будете крутити в реальних задачах залежно від того, що дорожче (хибна тривога vs пропущена ціль)."""
    )
)

cells.append(
    code(
        """precision = tp / (tp + fp) if (tp + fp) > 0 else float("nan")
recall = tp / (tp + fn) if (tp + fn) > 0 else float("nan")
print(f"Precision: {precision:.3f}")
print(f"Recall:    {recall:.3f}")
"""
    )
)

cells.append(
    md(
        """### Чому accuracy бреше на дисбалансованих задачах

Уявіть, що 95% респондентів — нижче медіани (наприклад, ми б фільтрували по якійсь рідкій підмножині). Тоді тривіальна модель "завжди прогнозуємо 0" дала б **95% accuracy** — і виглядала б майже ідеально, при тому що абсолютно безкорисна (TP = 0, recall = 0).

Тому в реальних задачах **завжди дивіться на confusion matrix** і метрики класу позитивних, а не лише на одну accuracy."""
    )
)

# =============================================================================
# SECTION 15 — SAVE/LOAD MODEL (.npz)
# =============================================================================

cells.append(
    md(
        """## Збереження та завантаження моделі (`.npz`)

Тренувати модель щоразу — марно. Збережемо чотири числові артефакти у компактний `.npz`-файл і навчимось їх завантажувати назад.

> **Чому `.npz`, а не `pickle`?** `.npz` — це стабільний бінарний формат, що складається з кількох `.npy`-файлів усередині zip-архіву. Він кросплатформний, не виконує жодного коду при завантаженні (`allow_pickle=False`), і зрозумілий навіть без Python (можна прочитати `numpy` з C / Rust / Julia)."""
    )
)

cells.append(
    code(
        """ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True)
np.savez(ARTIFACT_PATH, w=w, b=np.float64(b),
         feature_mean=feature_mean, feature_std=feature_std)
pred_before = predict(X_test, w, b, feature_mean, feature_std)
print(f"Saved {ARTIFACT_PATH.stat().st_size} bytes to {ARTIFACT_PATH}")
"""
    )
)

cells.append(
    code(
        """# Завантажуємо назад. allow_pickle=False — безпечне значення за замовчуванням
loaded = np.load(ARTIFACT_PATH, allow_pickle=False)
pred_after = predict(X_test, loaded["w"], float(loaded["b"]),
                     loaded["feature_mean"], loaded["feature_std"])
assert np.array_equal(pred_before, pred_after), "Round-trip broken!"
print("Round-trip OK — прогнози ідентичні.")
"""
    )
)

cells.append(
    md(
        """> **Безпека:** `allow_pickle=False` — це безпечне значення за замовчуванням. Якщо хтось підмінить `.npz`-файл на шкідливий зі вкладеним pickle-payload, з `allow_pickle=False` він просто не завантажиться. Не вмикайте `allow_pickle=True` для файлів з ненадійних джерел."""
    )
)

# =============================================================================
# SECTION 16 — sklearn coda (gated)
# =============================================================================

cells.append(
    md(
        """## scikit-learn для контексту: 5 рядків

Те, що ми написали ~80 рядків NumPy-коду, в `scikit-learn` робиться буквально п'ятьма. Покажемо це для контексту — **не як заміну** того, що ми щойно вивчили (бо тепер ви знаєте, що відбувається всередині цих п'яти рядків)."""
    )
)

cells.append(
    code(
        """try:
    from sklearn.linear_model import LogisticRegression
    from sklearn.metrics import accuracy_score

    sk_model = LogisticRegression(max_iter=1000)
    sk_model.fit(X_train_std, y_train)
    sk_acc = accuracy_score(y_test, sk_model.predict(X_test_std))
    print(f"sklearn accuracy: {sk_acc:.3f}")
    print(f"our accuracy:     {accuracy:.3f}")
    print(f"Δ:                {sk_acc - accuracy:+.3f}")
except ImportError:
    print("scikit-learn не встановлений — пропускаємо порівняння.")
    print("Встановити (опційно, лише для цієї комірки): pip install scikit-learn")
"""
    )
)

cells.append(
    md(
        """Зазвичай результати збігаються до ±1%. Дрібна різниця — від того, що sklearn використовує LBFGS (більш просунутий оптимізатор), а ми — vanilla **full-batch gradient descent** (на кожній епосі рахуємо градієнт по всіх `n_train` зразках). Якщо колись побачите термін "SGD", знайте: stochastic GD — це наш цикл, але з мінібатчами замість повного батчу."""
    )
)

# =============================================================================
# PLACEHOLDER FOR SECTION 17 (mini-project) — added in Phase 4 (US2)
# =============================================================================

# =============================================================================
# SECTION 17 — MINI-PROJECT "Survey Salary Classifier" (US2)
# =============================================================================

cells.append(
    md(
        """## Міні-проєкт: "Survey Salary Classifier"

Час застосувати все, що ви щойно вивчили, на власних руках. Цей міні-проєкт — **не набір окремих вправ**, а одна задача у трьох частинах, які поступово ускладнюються.

| Частина | Де робиться | Орієнтовний час | Що тренуємо |
|---------|-------------|------------------|--------------|
| **1** | в аудиторії | 10–15 хв | векторизація + `%timeit` |
| **2** | в аудиторії | 10–15 хв | повний цикл навчання моделі |
| **3** | вдома | 30–60 хв | feature engineering + порівняння моделей |

Усього: **~25 хв в аудиторії + 30–60 хв вдома**.

Парти 1–2 мають **прихований розв'язок** одразу під задачею (натисніть на маленький трикутник, щоб розкрити). Частина 3 — відкрита; еталонне рішення та критерії оцінювання знайдете у згорнутій секції в самому кінці ноутбука.
"""
    )
)

# ---- Part 1 ----
cells.append(
    md(
        """### Частина 1 — Per-country mean salary: цикл vs векторизація

Дано два 1-D NumPy-масиви: `salaries` (річна компенсація, `float64`) та `country_codes` (цілі коди країн, `int64`), обидва довжиною `N`. Потрібно:

1. Обчислити середню зарплату для кожної країни **звичайним `for`-циклом** по унікальних кодах країн.
2. Те саме — **векторизовано** через boolean masking.
3. Переконатися, що результати збігаються (`np.allclose`).
4. Виміряти швидкість обох версій через `%timeit` і вивести співвідношення.

**Очікуваний результат:** дві 1-D масиви форми `(num_countries,)`, посортовані за зростанням `country_code`. Векторизована версія має бути щонайменше у 5× швидша.

**Підказки:**
- Розділ 5 — boolean masking (`arr[mask]`).
- Розділ 8 — `%timeit` працює як магічна команда Jupyter.
"""
    )
)

cells.append(
    code(
        """# Готуємо вхідні дані з тих, що в нас уже є — щоб не вигадувати нові
salaries = X[:, 0] * 1000.0 + 30000.0     # синтетична зарплата на основі years_code
country_codes = (X[:, 2].astype(int) + 1) % 7   # 7 умовних "країн" з ed_level
print(f"N = {len(salaries)}, унікальних 'країн': {len(np.unique(country_codes))}")
"""
    )
)

cells.append(
    md(
        """<details>
<summary>📖 Розв'язок (натисніть, щоб розкрити)</summary>

Натисніть на наступну комірку, щоб виконати її, та побачите результати.

</details>
"""
    )
)

cells.append(
    code(
        """# Рішення Частини 1

# (a) ЧЕСНО наївний Python-цикл — проходимо по КОЖНОМУ елементу
def loop_means(salaries, codes):
    sums: dict[int, float] = {}
    counts: dict[int, int] = {}
    for s, c in zip(salaries.tolist(), codes.tolist()):
        sums[c] = sums.get(c, 0.0) + s
        counts[c] = counts.get(c, 0) + 1
    unique = sorted(sums.keys())
    return np.array([sums[c] / counts[c] for c in unique])

# (b) векторизовано — boolean masking; жодного Python-циклу по елементах
def vec_means(salaries, codes):
    unique = np.unique(codes)
    return np.array([salaries[codes == c].mean() for c in unique])

# Note: vec_means усе ж має зовнішній Python-цикл по унікальних кодах країн,
# але їх лише ~6 — це не 23 000 ітерацій, а 6. Усе важке (.mean() над масивом
# фільтрованих зарплат) робить NumPy.

a = loop_means(salaries, country_codes)
b = vec_means(salaries, country_codes)
assert np.allclose(a, b), "Результати не збігаються!"
print(f"Per-country means: {a.round(0)}")
print(f"Збігаються: {np.allclose(a, b)}")
"""
    )
)

cells.append(
    code(
        """# Швидкість
%timeit loop_means(salaries, country_codes)
"""
    )
)

cells.append(
    code(
        """%timeit vec_means(salaries, country_codes)
"""
    )
)

# ---- Part 2 ----
cells.append(
    md(
        """### Частина 2 — Натренувати модель з нуля

Користуючись готовими функціями `sigmoid`, `bce_loss`, `standardize` та `predict` з основної частини лекції, **повторіть повний цикл**: split → стандартизація → 1000 епох градієнтного спуску → метрики.

**Гіперпараметри:** `lr=0.1`, `epochs=1000`, `seed=42` — ті самі, що ми використовували раніше.

**Очікуваний результат:**
- `accuracy` на тестовій вибірці у діапазоні **[0.60, 0.75]** для Survey-шляху (емпірично ≈0.64) або **[0.75, 0.90]** для синтетичного.
- Confusion matrix форми `(2, 2)`, сума всіх клітинок = `len(y_test)`.

**Підказки:**
- Розділи 10–14 — повний пайплайн уже існує. Тут ваше завдання — **зібрати його в одну комірку** і запустити, не звіряючись із попередніми розділами.
"""
    )
)

cells.append(
    md(
        """<details>
<summary>📖 Розв'язок (натисніть, щоб розкрити)</summary>

Натисніть на наступну комірку, щоб виконати її, та побачите результати.

</details>
"""
    )
)

cells.append(
    code(
        """# Рішення Частини 2 — повний пайплайн в одній комірці

# 1. Train/test split
rng2 = np.random.default_rng(SEED)
perm2 = rng2.permutation(len(X))
nt = int(TRAIN_FRACTION * len(X))
Xtr, Xte = X[perm2[:nt]], X[perm2[nt:]]
ytr, yte = y[perm2[:nt]], y[perm2[nt:]]

# 2. Standardize (fit on train only)
m2 = Xtr.mean(axis=0)
s2 = Xtr.std(axis=0)
Xtr_s = standardize(Xtr, m2, s2)
Xte_s = standardize(Xte, m2, s2)

# 3. Train
n2, p2 = Xtr_s.shape
w2, b2 = np.zeros(p2), 0.0
for _ in range(EPOCHS):
    yh = sigmoid(Xtr_s @ w2 + b2)
    w2 -= LEARNING_RATE * (1.0 / n2) * Xtr_s.T @ (yh - ytr)
    b2 -= LEARNING_RATE * (1.0 / n2) * (yh - ytr).sum()

# 4. Evaluate
yp2 = predict(Xte, w2, b2, m2, s2)
acc2 = float((yp2 == yte).mean())
tn2 = int(((yp2 == 0) & (yte == 0)).sum())
fp2 = int(((yp2 == 1) & (yte == 0)).sum())
fn2 = int(((yp2 == 0) & (yte == 1)).sum())
tp2 = int(((yp2 == 1) & (yte == 1)).sum())
cm2 = np.array([[tn2, fp2], [fn2, tp2]])

print(f"Accuracy: {acc2:.3f}")
print(f"Confusion matrix:\\n{cm2}")
print(f"Сума клітинок confusion matrix: {cm2.sum()}  (== len(y_test): {len(yte)})")
"""
    )
)

# ---- Part 3 ----
cells.append(
    md(
        """### Частина 3 — Додайте п'яту ознаку (домашка)

Тепер — самостійна частина. Додайте **одну нову ознаку** на ваш вибір, перенавчіть модель з тими ж гіперпараметрами та порівняйте обидві моделі за **accuracy, precision і recall**.

**Приклади ознак** (оберіть одну, можете запропонувати свою):
- `is_hybrid` — `1` якщо `RemoteWork` починається з "Hybrid" (одна з двох гібридних опцій 2025), інакше `0`.
- `is_top5_devtype` — `1` якщо `DevType` входить до п'яти найпопулярніших, інакше `0`.
- `lang_count` — кількість мов програмування, які знає респондент (довжина `LanguageHaveWorkedWith.split(';')`).

**Вимоги:**
1. Нова ознака має бути отримана **лише з вхідних колонок** (без жодного зв'язку з target — інакше ви отримаєте data leakage і фейкову точність).
2. Перенавчіть з тими ж `seed=42, lr=0.1, epochs=1000`.
3. Виведіть результат як **охайний (tidy) DataFrame** з колонками `model`, `accuracy`, `precision`, `recall` — два рядки (4 ознаки vs 5 ознак).
4. Напишіть **3–5 речень українською** про те, чи допомогла нова ознака — і чому ви так вважаєте. Цитуйте хоча б одне число з таблиці.

**Критерії оцінювання — див. в самому кінці ноутбука** (згорнута секція "Еталонне рішення міні-проєкту (Частина 3)").
"""
    )
)

# Markdown placeholder for student work
cells.append(
    md(
        """*Ваш код Частини 3 — нижче (додайте стільки комірок, скільки потрібно).*
"""
    )
)

cells.append(
    code(
        """# TODO: Частина 3 — ваш код тут.
# 1. Завантажте Survey ще раз — потрібен RemoteWork (або інша колонка для нової ознаки).
# 2. Сконструюйте 5-ту ознаку.
# 3. Перенавчіть модель з SEED=42, lr=0.1, epochs=1000.
# 4. Порахуйте accuracy / precision / recall для обох моделей (4 ознаки vs 5).
# 5. Зберіть результат у tidy DataFrame.
# 6. Напишіть рефлексію у markdown-комірці нижче.
"""
    )
)


# =============================================================================
# SECTION 18 — SUMMARY
# =============================================================================

cells.append(
    md(
        """## Підсумок

**NumPy** — суцільна пам'ять + фіксований dtype + C/SIMD = ~100×–500× прискорення. Запам'ятайте: basic slicing → view, fancy/boolean → copy; broadcasting `(n, p) - (p,)` працює без копіювань.

**ML "з нуля"** — логістична регресія = sigmoid + лінійна модель + BCE loss. Числова стабільність: branch-on-sign sigmoid, `np.clip` у BCE, `np.where(std == 0, 1.0, std)` у standardize. Train-only статистики (без data leakage). Аналітичний градієнт `(1/n) Xᵀ(ŷ − y)` — три рядки коду. Accuracy одна обманлива → дивіться confusion matrix + precision/recall. `np.savez` + `np.load(allow_pickle=False)` для персистентності.

**Велика картина:** логістична регресія — це найпростіша **одношарова нейронна мережа**. Той самий патерн `σ(Wx + b)` лежить в основі будь-якого deep-learning фреймворка — просто шарів буде більше, а градієнти знайдені автоматично замість ручної формули.
"""
    )
)

# =============================================================================
# SECTION 19 — REFERENCES
# =============================================================================

cells.append(
    md(
        """## Джерела

**Офіційна документація:**

- [NumPy: Broadcasting](https://numpy.org/doc/stable/user/basics.broadcasting.html) — канонічний опис правил broadcasting з ілюстраціями.
- [NumPy: `numpy.random.Generator`](https://numpy.org/doc/stable/reference/random/generator.html) — сучасний RNG-API (`default_rng`).
- [NumPy: `numpy.savez`](https://numpy.org/doc/stable/reference/generated/numpy.savez.html) і [`numpy.load`](https://numpy.org/doc/stable/reference/generated/numpy.load.html) — формати збереження.

**Книги:**

- Wes McKinney — *Python for Data Analysis* (3rd ed., O'Reilly, 2022). Розділ 4 "NumPy Basics" і Розділ 12 "Advanced NumPy" — найкращий друкований ресурс.

**Курси:**

- Andrew Ng — [Coursera Machine Learning Specialization](https://www.coursera.org/specializations/machine-learning-introduction), Course 1, Week 3: "Logistic Regression". Безкоштовний audit.
- 3Blue1Brown — [But what is a neural network?](https://www.youtube.com/watch?v=aircAruvnKk) (англ.). Візуальне пояснення того самого `σ(Wx + b)` патерна, який ми реалізували.

**Опційно:**

- [scikit-learn `LogisticRegression`](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html) — для порівняння.

**Датасет:**

- [Stack Overflow Annual Developer Survey 2025](https://survey.stackoverflow.co/2025/) — Open Database License (ODbL).
"""
    )
)

# =============================================================================
# SECTION 20 — WHAT'S NEXT
# =============================================================================

cells.append(
    md(
        """## Що далі?

**Лекція 13 — Візуалізація (matplotlib + seaborn).** Ми нарешті побудуємо графіки: `loss_history`, який ми зібрали у Розділі 13, стане красивою спадаючою кривою; точки тестової вибірки лягуть у 2-D scatter-plot з намальованою decision boundary; пара histogram-ів покаже, як стандартизація змінює розподіли ознак. Та сама модель — нові інструменти, щоб **побачити**, що вона робить.

**Лекція 14 — Деплой (упакування + FastAPI).** Файл `model.npz`, який ми щойно зберегли, поверне нас до проєкту `notes-api` з лекцій 6–10: ми додамо ендпоінт `/predict`, який приймає 4 ознаки респондента і повертає прогноз класу. Завантаження моделі — три рядки `np.load`, обгорнуті у `lifespan`-хендлер FastAPI. Ось чому `.npz` був правильним вибором: серіалізація без залежностей, яку легко віддати у production.
"""
    )
)

# =============================================================================
# REFERENCE SOLUTION — MINI-PROJECT PART 3 (collapsed at the very end)
# =============================================================================

cells.append(
    md(
        """---

## Еталонне рішення міні-проєкту (Частина 3)

> Спробуйте розв'язати задачу самостійно перед тим, як дивитись сюди.

Нижче — еталонне рішення з ознакою `is_hybrid`. Це лише **один** з можливих варіантів; ваш може використовувати іншу ознаку — це нормально.
"""
    )
)

cells.append(
    code(
        """# Еталонне рішення Частини 3
# Перезавантажуємо Survey з ДОДАТКОВОЮ колонкою (RemoteWork ми вже маємо в df,
# але переробляємо завантаження в одній комірці для прозорості).
df_ref = pd.read_csv(SURVEY_CSV_PATH, usecols=USECOLS)
df_ref = df_ref.dropna(subset=["Country", "ConvertedCompYearly"]).copy()
cm_ref = df_ref.groupby("Country")["ConvertedCompYearly"].transform("median")
y_ref = (df_ref["ConvertedCompYearly"] > cm_ref).astype(int).to_numpy()

yc = pd.to_numeric(df_ref["YearsCode"], errors="coerce").to_numpy()
we = pd.to_numeric(df_ref["WorkExp"], errors="coerce").to_numpy()
ed = df_ref["EdLevel"].map(ED_MAP).to_numpy()
rm = (df_ref["RemoteWork"] == "Remote").astype(int).to_numpy()

# НОВА ознака: is_hybrid
is_hybrid = df_ref["RemoteWork"].fillna("").str.startswith("Hybrid").astype(int).to_numpy()

X4_full = np.column_stack([yc, we, ed, rm])
X5_full = np.column_stack([yc, we, ed, rm, is_hybrid])
keep = ~np.isnan(X4_full).any(axis=1)
X4_ref, X5_ref, y_ref = X4_full[keep], X5_full[keep], y_ref[keep]


def _train_and_score(Xin, yin):
    rng_t = np.random.default_rng(SEED)
    perm_t = rng_t.permutation(len(Xin))
    nt = int(TRAIN_FRACTION * len(Xin))
    Xtr, Xte = Xin[perm_t[:nt]], Xin[perm_t[nt:]]
    ytr, yte = yin[perm_t[:nt]], yin[perm_t[nt:]]
    m, s = Xtr.mean(0), Xtr.std(0)
    s = np.where(s == 0, 1.0, s)   # захист від нульового std
    Xtr_s, Xte_s = (Xtr - m) / s, (Xte - m) / s

    n_, p_ = Xtr_s.shape
    w_, b_ = np.zeros(p_), 0.0
    for _ in range(EPOCHS):
        yh = sigmoid(Xtr_s @ w_ + b_)
        w_ -= LEARNING_RATE * (1.0 / n_) * Xtr_s.T @ (yh - ytr)
        b_ -= LEARNING_RATE * (1.0 / n_) * (yh - ytr).sum()

    yh = sigmoid(Xte_s @ w_ + b_)
    yp = (yh >= 0.5).astype(int)
    tp = int(((yp == 1) & (yte == 1)).sum())
    fp = int(((yp == 1) & (yte == 0)).sum())
    fn = int(((yp == 0) & (yte == 1)).sum())
    acc = float((yp == yte).mean())
    prec = tp / (tp + fp) if (tp + fp) > 0 else float("nan")
    rec = tp / (tp + fn) if (tp + fn) > 0 else float("nan")
    return acc, prec, rec


a4, p4, r4 = _train_and_score(X4_ref, y_ref)
a5, p5, r5 = _train_and_score(X5_ref, y_ref)

comparison = pd.DataFrame({
    "model": ["4_features", "5_features"],
    "accuracy": [a4, a5],
    "precision": [p4, p5],
    "recall": [r4, r5],
})
print(comparison.to_string(index=False))
"""
    )
)

cells.append(
    md(
        """### Приклад рефлексії

> Додавання `is_hybrid` дало приріст accuracy з 0.640 до 0.640 — фактично нуль. Recall ледь зріс, precision ледь впав. Висновок: ця ознака майже **дублює** `is_remote` (бо ми вже відкинули hybrid у нуль), і модель не отримує нової інформації. Реальний приріст дала б нелінійна модель або справжньо незалежні ознаки — наприклад, `lang_count` чи one-hot топ-DevType.

### Критерії оцінювання (6 балів)

- **3 бали** — коректність: feature без data leakage, ті ж гіперпараметри, метрики в межах ±0.02 від еталона.
- **2 бали** — чистий векторизований код (без `df.iterrows()` чи Python-циклів по рядках).
- **1 бал** — рефлексія українською, 3–5 речень, цитує хоча б одне число з таблиці.

**Прохідний поріг:** ≥ 4 / 6.
"""
    )
)

# =============================================================================
# WRITE NOTEBOOK
# =============================================================================

nb = nbf.v4.new_notebook()
nb["cells"] = cells
nb["metadata"] = {
    "kernelspec": {
        "display_name": "Python 3",
        "language": "python",
        "name": "python3",
    },
    "language_info": {"name": "python", "version": "3.13"},
}

with OUT.open("w", encoding="utf-8") as f:
    nbf.write(nb, f)

n_md = sum(1 for c in cells if c["cell_type"] == "markdown")
n_code = sum(1 for c in cells if c["cell_type"] == "code")
print(f"Wrote {OUT}  ({len(cells)} cells: {n_md} md + {n_code} code)")
