# Data Model: Lecture 11 — pandas Deep Dive on the Stack Overflow Developer Survey

**Feature**: 016-lecture11-pandas-analytics
**Date**: 2026-04-23

This lecture has no persisted entities. The "data model" here is (a) the schema of the Survey DataFrame after each cleaning stage, and (b) the notebook section map.

## DataFrame Schemas (Transformation Stages)

### Stage 0 — Raw Load (`pd.read_csv` with `usecols=`)

Columns loaded from `data/survey_results_public.csv`:

| Column | Raw dtype | Notes |
|---|---|---|
| `ResponseId` | int64 | Row identifier |
| `MainBranch` | object | Categorical text ("I am a developer by profession", "I am learning to code", …) |
| `Country` | object | Free-text country name ("Ukraine", "United States of America", …) |
| `EdLevel` | object | Educational attainment (ordered: primary school → master's → doctorate) |
| `YearsCode` | float64 | In 2025 Survey pre-cleaned to numeric (historical pre-2025 versions had "Less than 1 year" / "More than 50 years" sentinels — the lecture still teaches the `pd.to_numeric` technique on an inline synthetic example) |
| `WorkExp` | float64 | Years of professional work experience — replaces the pre-2025 `YearsCodePro` column, which was dropped in 2025 |
| `DevType` | object | Semicolon-separated multi-value (depending on 2025 schema — may be single-value) |
| `LanguageHaveWorkedWith` | object | Semicolon-separated multi-value |
| `LanguageWantToWorkWith` | object | Semicolon-separated multi-value |
| `DatabaseHaveWorkedWith` | object | Semicolon-separated multi-value |
| `ConvertedCompYearly` | float64 | Annual compensation in USD; heavy tail + many NaN |
| `RemoteWork` | object | Categorical text |

**Exact column names pending verification against the 2025 CSV at notebook authoring time (R4).**

### Stage 1 — After Cleaning (FR-010)

Applied transformations (2025 Survey is already well-curated, so these are idempotent / no-op on the real columns; the section's pedagogical value comes from an inline synthetic messy Series demonstrating the technique):

| Column | New dtype | Transformation |
|---|---|---|
| `YearsCode` | float64 | Idempotent `pd.to_numeric(errors="coerce")` — 2025 values already clean numeric |
| `WorkExp` | float64 | Idempotent `pd.to_numeric(errors="coerce")` — 2025 values already clean numeric |
| `ConvertedCompYearly` | float64 | Kept; `NaN` rows flagged but not dropped globally |
| `EdLevel` | object | Unchanged at this stage (promoted to ordered `Categorical` in FR-034 section) |

Other columns unchanged. `.isna().sum()` shown as the final cell of the cleaning section.

### Stage 2 — After `.explode()` (FR-012)

A *derived* long-format DataFrame `languages_long` is created for the multi-value section:

```text
languages_long columns:
  ResponseId  Country  Language
  67890       Ukraine  Python
  67890       Ukraine  JavaScript
  67890       Ukraine  Go
  67891       USA      Python
  ...
```

Construction:

```python
languages_long = (
    df.assign(LanguageList=df["LanguageHaveWorkedWith"].str.split(";"))
      .explode("LanguageList")
      .rename(columns={"LanguageList": "Language"})
      [["ResponseId", "Country", "Language"]]
      .dropna(subset=["Language"])
)
```

Used in `.explode()` demo and as the left side of the FR-014 merge demo.

### Stage 3 — Categorical Optimization (FR-034)

Applied transformations produce `df_opt` (kept as a named copy so students can compare):

| Column | New dtype | Notes |
|---|---|---|
| `Country` | category | Unordered |
| `DevType` | category | Unordered |
| `EdLevel` | CategoricalDtype(ordered=True) | Order defined explicitly (2025 values use curly apostrophe `’`): primary → secondary → bachelor's → master's → professional. Comparisons use position-based `cat.codes >= master_pos` pattern for pandas-2.3 compatibility rather than direct `>=` on a string literal. |

Side-by-side memory comparison: `df.memory_usage(deep=True).sum()` vs `df_opt.memory_usage(deep=True).sum()`.

### Stage 4 — Aggregation outputs (FR-013, FR-017)

The groupby / aggregation section produces several small result frames:

| Output | Shape (approx) | Source |
|---|---|---|
| `top_languages` | (N≈20, 2) with `Language`, `count` | `languages_long.groupby("Language").size().nlargest(20)` |
| `median_comp_by_country` | (N≈20, 2) with `Country`, `median_usd` | `df.groupby("Country")["ConvertedCompYearly"].median().nlargest(20)` |
| `rust_want_by_devtype` | (N rows, %) | `pd.crosstab(df["DevType"], df["LanguageWantToWorkWith"].str.contains("Rust", na=False), normalize="index")` |
| `ua_vs_global_median_years_pro` | (2 rows) | `df.groupby(df["Country"].eq("Ukraine").map({True: "UA", False: "Global"}))["WorkExp"].median()` |

## Notebook Section Map

| # | Section (Ukrainian title) | FR coverage | Ukraine anchor? |
|---|---|---|---|
| 0 | Header + Prerequisites | FR-002 | — |
| 1 | Цілі заняття (Learning Objectives) | FR-001 | — |
| 2 | Вступ: що таке pandas і коли він потрібен | FR-007 | — |
| 3 | Series vs DataFrame | FR-008 | — |
| 4 | Завантаження даних: pd.read_csv на Stack Overflow Survey 2025 | FR-009, FR-024 | no (global dataset) |
| 5 | Чистка даних: типи, пропущені значення, "Less than 1 year" | FR-010 | no |
| 6 | Індексація та вибірка: .loc, .iloc, boolean masks, .query() | FR-011 | no |
| 7 | Багатозначні стовпці та .explode(): топ мов програмування | FR-012 | no |
| 8 | Groupby та агрегації | FR-013 | **YES** — Ukraine anchor |
| 9 | Merge / join: статистика по мовах, приєднана до респондентів | FR-014 | no |
| 10 | Pivot tables та crosstab | FR-015 | no |
| 11 | Сортування, ранжування, top-N | FR-016 | no |
| 12 | Method chaining: .pipe та .assign | FR-032 | no |
| 13 | .apply та .map: власні функції + швидкодія | FR-033 | no |
| 14 | Categorical dtype: пам'ять та впорядковані категорії | FR-034 | **YES** — Ukraine anchor on filtered Categorical |
| 15 | Практичний блок: top languages / median comp by country / Rust uptake | FR-017 | no |
| 16 | Коли pandas не підходить: DuckDB та Polars | FR-018 | — |
| 17 | Міні-проєкт "Developer Survey Insights" (3-parts) | FR-019, FR-035 | **YES** — Part 1 anchor |
| 18 | Підсумок (Summary) | FR-003 | — |
| 19 | Джерела (References) | FR-024, FR-026 | — |
| 20 | Що далі? (Preview of L12, L13) | FR-003 | — |

## Mini-Project Structure (FR-019)

| Part | When | Time | Task | Hidden solution? |
|---|---|---|---|---|
| 1 | In-class | ~10–15 min | Median `WorkExp` for Ukrainian respondents vs global median | Hidden solution cell |
| 2 | In-class | ~10–15 min | Top 10 languages among "Learning to code" respondents via `.explode()` | Hidden solution cell |
| 3 | Homework | ~30–60 min | Pick one country → compare median comp across its 3 most-common `DevType` values; must use `Categorical`; produce tidy DataFrame + 3–5 sentence UA commentary | Reference solution collapsed at end; grading rubric (3 pts correctness, 2 pts clean pipeline, 1 pt commentary) |

## Asset Inventory

| Asset | Path | Source | Licensing |
|---|---|---|---|
| Survey CSV | `lectures/11-pandas-analytics/data/survey_results_public.csv` | Student download from survey.stackoverflow.co | ODbL (not committed to repo) |
| Meme 1 | `lectures/11-pandas-analytics/assets/memes/first-time.png` | Generic "first time?" template | Public-domain meme template |
| Meme 2 | `lectures/11-pandas-analytics/assets/memes/merge-explode.png` | Generic | Public-domain meme template |
| Diagram | `lectures/11-pandas-analytics/assets/diagrams/explode-schematic.png` | Generated via matplotlib table rendering OR draw.io export | Original work for this lecture |

## File Change Map

| File | Action |
|---|---|
| `lectures/11-pandas-analytics/lecture-11.ipynb` | CREATE |
| `lectures/11-pandas-analytics/README.md` | CREATE (one-page setup: install pandas, download Survey ZIP, path) |
| `lectures/11-pandas-analytics/data/.gitkeep` | CREATE |
| `lectures/11-pandas-analytics/assets/memes/*` | CREATE (≥2 files) |
| `lectures/11-pandas-analytics/assets/diagrams/explode-schematic.png` | CREATE |
| `.gitignore` | MODIFY (append `lectures/11-pandas-analytics/data/*.csv`) |

No changes to `project/notes-api/` per FR-028 / FR-029.
