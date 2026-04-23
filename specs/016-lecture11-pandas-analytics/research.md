# Research: Lecture 11 — pandas Deep Dive on the Stack Overflow Developer Survey

**Feature**: 016-lecture11-pandas-analytics
**Date**: 2026-04-23

All NEEDS CLARIFICATION items from the spec were resolved in the 2026-04-23 clarification session and encoded in the spec itself; see `spec.md > ## Clarifications`. This document captures the remaining implementation-level research decisions.

## Research Tasks

### R1: Dataset download mechanism (FR-024, FR-025, FR-027, Edge Case #1)

**Decision**: Students download the 2025 Survey ZIP manually from `https://survey.stackoverflow.co/` (the "Download Full Data Set" link on the methodology page), extract it, and place `survey_results_public.csv` at `lectures/11-pandas-analytics/data/survey_results_public.csv`. The notebook's first cell checks for the file and prints a clear error message with the exact URL and target path if missing. The path is stored in a module-level constant near the top of the notebook so it is easy to retarget. A short `README.md` in the lecture directory documents this step.

**Rationale**: FR-027 forbids network calls during notebook execution, and FR-025 forbids embedding the dataset in the repo. Automating the download would violate FR-027; fetching via `kaggle` CLI would require authentication setup that distracts from pandas. Manual download is the lowest-friction option that stays within the spec's constraints and matches Stack Overflow's own public-access flow.

**Alternatives considered**:
- Script-based auto-download via `requests` on first cell — violates FR-027 (no network calls) and introduces failure modes (firewall, proxy, rate limits) that steal classroom time.
- Bundle a tiny sampled subset in the repo — violates FR-025; also defeats the "real messy data" pedagogical goal since heavy sampling hides the cleaning value.
- Use `pd.read_csv` with a URL pointing at the SO ZIP — still violates FR-027 and breaks in offline-classroom scenarios.

### R2: Pinning SO Developer Survey year (Spec Clarifications Q1)

**Decision**: Use the 2025 Annual Developer Survey (~49K respondents, released late 2025, ODbL license). Pin via `SURVEY_YEAR = 2025` in a top-of-notebook constants cell. Include a one-line comment in the notebook that schemas drift year-to-year; if a student uses a newer release they must re-check column names.

**Rationale**: Encoded directly in the clarification session (Q1, Option A).

**Alternatives considered**: Documented in spec clarifications.

### R3: Column selection strategy for `pd.read_csv`

**Decision**: Use `usecols=[...]` on `pd.read_csv` to load only the columns needed for the lecture's teaching examples, saving memory and making the `.info()` / `.dtypes` output readable on a slide. Target columns (subject to verification against the actual 2025 CSV schema at notebook-authoring time):

| Column | Why needed |
|---|---|
| `ResponseId` | Identifier for join/merge demos; also an integer for `.nlargest` demo |
| `MainBranch` | Categorical: "I am a developer by profession" / "I am learning to code" / ... — good for cleaning + filtering demos |
| `Country` | The running Ukraine anchor; also the primary `groupby` / `Categorical` / `.nlargest` demo column |
| `EdLevel` | Natural example of an **ordered** `Categorical` (primary school → doctorate) |
| `YearsCode`, `YearsCodePro` | Messy numeric-ish columns ("Less than 1 year", "More than 50 years") — the FR-010 cleaning demo |
| `DevType` | Semicolon-separated multi-value in some years; used for mini-project Part 3 and crosstab demos |
| `LanguageHaveWorkedWith`, `LanguageWantToWorkWith` | The semicolon-separated multi-value FR-012 `.explode()` demo |
| `DatabaseHaveWorkedWith` | Secondary multi-value column for the second `.explode()` example and merge demo (language-stats joined onto DB-using respondents) |
| `ConvertedCompYearly` | Numeric with heavy tails + missing values; primary `groupby().agg` and `apply`-based salary-band demo |
| `RemoteWork` / `WorkExp` | Reserves for mini-project Part 3 open-ended exploration |

**Rationale**: Loading all ~90 columns wastes memory (~200 MB expanded) and bloats every `.head()` output with noise. ~12 columns is enough for every pedagogical section. This list must be cross-checked against the actual 2025 schema during notebook authoring (one renaming between years is common — e.g., 2024 `YearsCodePro` stayed the same, but 2025 introduced new AI-focused columns like `AISelect`, `AIBen` that we deliberately skip to stay focused).

**Alternatives considered**:
- Load all columns, rely on `.head()` + `.sample()` for readability — wastes memory, clutters output.
- Preprocess the CSV externally into a slimmer file distributed with the lecture — violates FR-025 (no bundled dataset) and hides the real `read_csv` experience.

### R4: Column renaming / schema drift handling

**Decision**: Do NOT rename Survey columns in the notebook. Use them as they appear in the 2025 CSV. Add one cell right after the load that introspects columns via `df.columns.tolist()` and shows `.dtypes` so students see the real schema. If the instructor encounters a renamed column during authoring (e.g., a column the spec lists under one name that is different in 2025), the instructor updates the spec's column names rather than renaming in code.

**Rationale**: Renaming columns hides the real-world problem ("actual CSVs have whatever names they have; learn to work with them"). The notebook's first cleaning cell demonstrates case-sensitive column access, which reinforces the habit. If 2025 introduced a material rename, the spec is updated; this is a Phase-2 authoring task, not a Phase-1 architecture decision.

### R5: pandas version pin and install command

**Decision**: Require `pandas >= 2.2, < 3.0`. Install command shown in the notebook's first cell and in the lecture `README.md`:

```bash
pip install "pandas>=2.2,<3"
# or, if uv is available in the student's environment:
uv add "pandas>=2.2,<3"
```

**Rationale**: pandas 2.2+ has stable copy-on-write-opt-in, the PyArrow-backed string dtype as a first-class option, and the modern `Categorical` / `.assign` / `.pipe` APIs used in the lecture. The upper bound guards against a future pandas 3.0 making breaking changes; we pin at the minor level.

**Alternatives considered**:
- Pin exactly `pandas==2.2.3` — too rigid, gratuitously breaks as students pick up point releases.
- Leave unbounded (`pandas`) — invites future breakage when the API shifts.

### R6: `Categorical` dtype memory-comparison technique

**Decision**: Use `df.memory_usage(deep=True).sum()` on a copy of the subset DataFrame before/after `.astype("category")` on `Country`, `DevType`, and `EdLevel`. Print both numbers in MB plus the ratio, and render a tiny one-line observation ("знизили використання пам'яті на X%").

**Rationale**: `memory_usage(deep=True)` is the canonical pandas way to count actual bytes of object columns (including the string payloads). `sys.getsizeof` and `pympler.asizeof` are alternatives but add a dependency and aren't pandas-native.

### R7: Method-chaining comparison structure

**Decision**: Present two side-by-side cells performing the same four-step cleaning pipeline on the Survey:
1. **Stepwise version**: `df1 = df[usecols]; df1 = df1.dropna(...); df1 = df1.assign(...); df1 = df1.rename(...)`
2. **Chained version**: `(df[usecols].dropna(...).assign(...).rename(...))`

Then show one `.pipe(my_func)` example where `my_func` is a reusable user-defined step. Close with a short "when chaining hurts" note (debugging long chains; use `.pipe(print)` or intermediate `.pipe(lambda d: (display(d.head()), d)[1])` as probes).

**Rationale**: Side-by-side is the most pedagogically transparent way to show the before/after of method chaining. `.pipe()` justifies itself only once students have a function they want to plug in; artificially contriving a pipeline for it hurts the lesson.

### R8: `apply`/`map` vs vectorization warning

**Decision**: In the FR-033 section, introduce `Series.map()` with a dict first (fastest, most idiomatic), then `Series.apply()` with a lambda, then `DataFrame.apply(axis=1)` for row-wise custom logic. Right before the `axis=1` demo, include a one-cell benchmark comparing a vectorized approach (`(df["ConvertedCompYearly"] // 25000) * 25000` for salary bucketing) vs the `apply(axis=1)` version using `%timeit`. Expected outcome: vectorized ~100x–1000x faster. Print the ratio.

**Rationale**: Students need to *see* the speed difference, not just be told. `%timeit` in Jupyter is one-line, zero-dependency, and gives a concrete number. This directly motivates "reach for vectorization first, `.apply()` only when necessary" without needing to teach NumPy internals (deferred to L12).

### R9: `.explode()` diagram (FR-022)

**Decision**: Produce one image (`assets/diagrams/explode-schematic.png`) showing two small DataFrames side by side — the "before" has a 3-row frame with `LanguageHaveWorkedWith` as semicolon-joined strings; the "after" has ~9 rows after `str.split(";").explode()`. Use matplotlib's table rendering OR a hand-drawn draw.io export. Include alt-text in the notebook markdown cell.

**Rationale**: `.explode()` is visually the most surprising transformation in the lecture — every other operation keeps row-count stable, this one multiplies rows. A diagram locks the mental model in. matplotlib-generated is reproducible in case we need to regenerate.

**Alternatives considered**:
- ASCII-art diagram — harder to read, especially projected on a classroom screen.
- Mermaid diagram — row-multiplication isn't a natural Mermaid motif.

### R10: Meme sources (FR-021)

**Decision**: At least 2 memes, all non-russian-sourced. Candidates:
1. "Pandas: first time?" (classic "first time?" meme template) placed at the start of the cleaning section, riffing on messy real data.
2. "When your `merge` explodes from 50k rows to 500k rows" — riff on `validate=` saving the day. Placed at end of FR-014 merge section.
3. (Backup) "I don't always use `.apply(axis=1)`, but when I do, I regret it" — closing the FR-033 section.

All memes must use generic meme templates (no Ukrainian-context, no russian-context, no copyrighted characters beyond standard meme-culture imagery) and be checked into `lectures/11-pandas-analytics/assets/memes/`.

**Rationale**: Constitution Principle I requires memes for engagement; Principle IV caps at "sparingly, where they add value". 2–3 memes is the sweet spot; the fourth meme slot is reserved in case instructor finds a better one during authoring.

### R11: Notebook execution verification

**Decision**: Provide a quickstart step that runs `jupyter nbconvert --to notebook --execute lectures/11-pandas-analytics/lecture-11.ipynb --output /tmp/out.ipynb` as the "did it work end-to-end?" check. No formal pytest suite for the notebook — this is pedagogical content, not runtime software.

**Rationale**: `nbconvert --execute` is the standard pandas / Jupyter community smoke test for a notebook. It catches cell execution errors, missing dataset, missing dependency issues quickly.

### R12: Non-russian resources verification

**Decision**: References section MUST include only:
- pandas official docs (`pandas.pydata.org`)
- Stack Overflow Developer Survey 2025 official page (`survey.stackoverflow.co/2025/`)
- Wes McKinney's *Python for Data Analysis* (3rd ed., O'Reilly) — book reference, no russian co-author
- Real Python `groupby` guide
- OWID / FiveThirtyEight guides to working with multi-value columns (optional, English-only)
- DuckDB official docs (`duckdb.org`) and Polars official docs (`pola.rs`) for the "When pandas breaks" conceptual section

Explicitly NOT allowed: habr.com, any russian-language tutorials, any translations originating from russian educational platforms.

**Rationale**: Constitution Principle I ("Additional resources should not contain russian ones"). This list satisfies the requirement with redundant English-language material covering every topic in the lecture.

## Summary of Decisions

| # | Decision | Choice |
|---|----------|--------|
| R1 | Dataset download | Manual student download + `data/` placeholder + README.md |
| R2 | Survey year | 2025 (pinned via `SURVEY_YEAR = 2025`) |
| R3 | Columns loaded | ~12 columns via `usecols=` |
| R4 | Schema drift | Use actual 2025 column names; update spec if renamed |
| R5 | pandas version | `>=2.2, <3.0` |
| R6 | Memory comparison | `df.memory_usage(deep=True).sum()` before/after |
| R7 | Chaining demo | Side-by-side stepwise vs chained; one `.pipe` example |
| R8 | apply warning | `%timeit` benchmark vs vectorized salary-bucketing |
| R9 | Diagram | `.explode()` transformation schematic (PNG in assets/diagrams/) |
| R10 | Memes | 2–3 memes, non-russian, all in assets/memes/ |
| R11 | Notebook test | `jupyter nbconvert --execute` smoke test |
| R12 | References | pandas.pydata.org, survey.stackoverflow.co, Real Python, DuckDB, Polars — no russian sources |
