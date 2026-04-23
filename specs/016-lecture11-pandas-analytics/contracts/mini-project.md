# Mini-Project Contract: "Developer Survey Insights"

**Feature**: 016-lecture11-pandas-analytics
**Date**: 2026-04-23

This document defines the expected output shapes and grading rubric for the three-part mini-project (FR-019). The notebook's hidden solution cells (Parts 1–2) and the collapsed reference solution (Part 3) MUST conform to these contracts.

## Part 1 — In-class (~10–15 min): Ukrainian vs Global Median `WorkExp`

**Task statement (Ukrainian)**: "Обчисліть медіанне значення `WorkExp` для респондентів з України та порівняйте з глобальною медіаною. Виведіть обидва числа та різницю між ними (у роках)."

**Required techniques from earlier sections**: `df["Country"] == "Ukraine"` boolean mask, `.median()`, numeric comparison.

**Expected output contract**:

```text
Series or scalar triple:
  ua_median_work_exp:     float  (≥ 0; on 2025 data ≈ 6.0)
  global_median_work_exp: float  (≥ 0; on 2025 data ≈ 10.0)
  delta_years:            float  (signed; negative if UA lower; on 2025 data ≈ -4.0)
```

Printed form (exemplar):

```text
Медіана WorkExp:
  Україна:    5.0 років
  Глобальна:  9.0 років
  Різниця:   -4.0 років (Україна нижче)
```

**Acceptance**: Student's answer matches the hidden solution to within 0.5 years on each value. Deviations beyond that indicate either wrong column name, wrong filter, or skipping the cleaning step.

## Part 2 — In-class (~10–15 min): Top 10 Languages Among Learners

**Task statement (Ukrainian)**: "Знайдіть 10 найпопулярніших мов програмування серед респондентів, які обрали `MainBranch == 'I am learning to code'`. Використайте `str.split(';')` + `.explode()`."

**Required techniques from earlier sections**: Boolean mask on `MainBranch`, `str.split(";")`, `.explode()`, `.value_counts()` / `.size()`, `.head(10)` or `.nlargest(10)`.

**Expected output contract**:

```text
Series of length 10:
  Index: Language (str)
  Values: respondent count (int, descending)

Example (illustrative, actual numbers vary with 2025 data):
  Language
  Python        1820
  JavaScript    1432
  HTML/CSS      1280
  SQL           1105
  TypeScript     980
  Java           845
  C++            740
  C#             620
  Bash/Shell     510
  PHP            430
  Name: count, dtype: int64
```

**Acceptance**: Top 5 entries match the hidden solution in ordering. Positions 6–10 may differ by ±1 rank due to tie-breaks; the set of {top 10 language names} must match exactly.

## Part 3 — Homework (~30–60 min): Country × DevType Compensation Study

**Task statement (Ukrainian)**: "Оберіть одну країну. У межах цієї країни знайдіть 3 найпопулярніші `DevType`. Для кожного з них обчисліть медіанну річну компенсацію (`ConvertedCompYearly`). Обов'язково: (a) примусово приведіть `Country` та `DevType` до `Categorical` dtype; (b) виведіть результат як охайний (tidy) DataFrame з колонками `country`, `dev_type`, `n_respondents`, `median_usd`; (c) додайте коментар українською (3–5 речень) про те, що ви побачили."

**Required techniques from earlier sections**: `.value_counts()`, boolean mask by country, `.groupby(["Country", "DevType"])`, `.astype("category")`, named aggregation, `.reset_index()`.

**Expected output contract**:

```text
DataFrame with exactly these columns and types:
  country         category
  dev_type        category
  n_respondents   int64
  median_usd      float64

Exactly 3 rows (one per top-3 DevType within the chosen country).
Rows ordered by n_respondents descending.
```

Plus a text / markdown cell containing a 3–5 sentence Ukrainian-language commentary.

**Reference solution placement**: End of notebook, inside a collapsed cell with a clear header "Еталонне рішення міні-проєкту (Частина 3)". Students are encouraged to attempt the task before expanding.

**Grading rubric (6 points total)**:

| Criterion | Points | What passes |
|---|---|---|
| Correctness of the 3-row DataFrame (right columns, right types, right values) | 3 | Top-3 DevType list matches reference; `median_usd` within ±10% of reference |
| Clean pandas pipeline (method chaining OR clear stepwise; no needless loops; `.apply` only if justified) | 2 | One coherent pipeline; no `for` loop over rows; `.apply` used only for custom formatting, not for what `groupby` does |
| Commentary quality (Ukrainian, 3–5 sentences, references specific numbers) | 1 | Non-trivial observation backed by at least one number from the result |

Passing threshold: ≥ 4 / 6 points.

## Summary

| Part | Duration | Output type | Solution visibility |
|---|---|---|---|
| 1 | In-class 10–15 min | 3-number comparison | Hidden cell below the task |
| 2 | In-class 10–15 min | Series of length 10 | Hidden cell below the task |
| 3 | Homework 30–60 min | 3-row tidy DataFrame + UA commentary | Collapsed reference solution + rubric at notebook end |
