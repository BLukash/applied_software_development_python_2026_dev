# Feature Specification: Lecture 11 — pandas Deep Dive on the Stack Overflow Developer Survey

**Feature Branch**: `016-lecture11-pandas-analytics`
**Created**: 2026-04-21
**Status**: Draft
**Input**: User description: "Implement Lecture 11 specification according to the constitution. For me is very important to use here some interesting dataset to showcase, so make sure to conduct a thoughtful research on this topic"

## Clarifications

### Session 2026-04-23

- Q: Scope boundary — keep the project increment (`/analytics/report` endpoint over notes-api DB) or drop it and make Lecture 11 a standalone pandas deep dive? → A: Drop the project increment entirely. Lecture 11 is isolated — pandas-only deep dive based on the Stack Overflow Annual Developer Survey. No references to the previous notes-api project (Note/Tag models, PostgreSQL, SQLAlchemy engine, `/analytics/report`, or seed scripts).
- Q: Which Stack Overflow Developer Survey year to pin in the notebook? → A: 2025 — use the 2025 Annual Developer Survey (~49K respondents, latest release) as the single pinned dataset. All concrete column references in the notebook MUST match the 2025 schema (including its AI-focused columns); instructor MUST verify the exact column names against the 2025 schema before finalizing notebook cells.
- Q: How to handle datetime-parsing in L11 given the Survey has no response-date column? → A: Drop datetime parsing from Lecture 11 entirely. The Survey CSV does not ship submission timestamps, and the user-scoped constraint is "only the Survey, no secondary datasets". FR-010 is reframed around dtype coercion + missing-value handling only; datetime parsing (`pd.to_datetime`, `errors="coerce"`, `NaT` handling) is deferred to a later lecture where a dataset with authentic datetime columns is in play.
- Q: How deep is the deep dive — what intermediate/advanced pandas topics go in beyond the fundamentals? → A: Intermediate ceiling (Option B). In addition to the fundamentals (loading, cleaning, indexing, `.explode()`, `groupby`, `merge`, pivot, sorting/top-N), the lecture MUST cover: (1) method chaining via `.pipe()` and `.assign()`, (2) `.apply()` and `.map()` for custom per-row / per-element functions, and (3) the `Categorical` dtype applied to high-repeat Survey columns (`Country`, `DevType`, `EdLevel`) with a before/after memory comparison. MultiIndex, rolling/resample window functions, and performance internals (copy-on-write, Arrow backend) are OUT of scope for L11.
- Q: How to satisfy the constitution's "mini-project per lecture" requirement for L11 given the notes-api increment was dropped? → A: Reframe the three exercises as one progressive mini-project, "Developer Survey Insights" (Option B). Parts 1–2 run in-class (20–30 min) and Part 3 is the homework extension (30–60 min). The mini-project stays anchored on the Survey only — no external stack, no secondary dataset. This restores constitutional compliance for Principle II; the only remaining deviation from the constitution's L11 plan is the dropped `/analytics/report` endpoint on the notes-api.
- Q: Use Ukraine as a recurring hook in teaching examples, or keep them globally neutral? → A: Selective Ukraine anchoring (Option B). The `groupby` and `Categorical` teaching sections MUST use Ukraine as the anchor example; the data-loading, cleaning, `.explode()`, `merge`, pivot, sorting, method-chaining, and `apply`/`map` sections MUST use global / multi-country comparisons. The mini-project Part 1 retains its Ukraine filter. Rationale: balances relatability for the Ukrainian cohort with dataset breadth, avoiding repetition.

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Lecture Notebook: pandas Deep Dive on the Stack Overflow Developer Survey (Priority: P1)

A student opens the Lecture 11 Jupyter notebook and follows a 1.5-hour, **standalone** session that takes them from "I've heard of pandas" to "I can load a messy real-world CSV, clean it, and extract meaningful insights." The entire lecture is built on a single interesting real-world dataset — the **Stack Overflow Annual Developer Survey** (latest release available at lecture time) — so students stay anchored in one mental model instead of hopping between toy datasets. They progress through: what pandas is and isn't good for, Series vs DataFrame, loading the Survey CSV, dtype/missing-value/datetime cleaning, indexing and selection, exploding semicolon-separated multi-value columns, `groupby` with single- and multi-key aggregations, `merge`, pivot tables, sorting/ranking, and finish with a conceptual overview of when pandas is the wrong tool (and which tools come next — DuckDB, Polars). The notebook is fully self-contained: it does NOT depend on the notes-api project from L9/L10 and does NOT produce any project increment.

**Why this priority**: The notebook is the sole deliverable for this lecture. It gives students their first real exposure to pandas, the workhorse library for the analytics half of the course, and sets up L12 (NumPy + vectorization) and L13 (visualization) by leaving a cleaned Stack Overflow DataFrame in students' hands.

**Independent Test**: Open the notebook in Jupyter, run every cell top-to-bottom against a clean Python 3.13 environment with pandas installed and the downloaded Stack Overflow Developer Survey CSV at the expected path; verify all cells execute without error, all outputs render, and the structural elements (learning objectives, exercises, memes, diagrams, references, summary, what's next) are present. No database, no FastAPI, no Docker required.

**Acceptance Scenarios**:

1. **Given** a student opening the L11 notebook, **When** they read the header, **Then** they see prerequisites referencing only basic Python (from L1–L5: types, functions, list comprehensions, file I/O) and a working Jupyter environment — NOT L6–L10 topics (FastAPI, Postgres, Alembic, SQLAlchemy).
2. **Given** a student reading the "What pandas is good for (and not)" section, **When** they finish, **Then** they can articulate at least three strengths and two weaknesses of pandas in their own words.
3. **Given** a student reading the "Series vs DataFrame" section, **When** they finish, **Then** they understand that a DataFrame is a dict-of-Series with a shared Index, and they can construct both objects from plain Python dicts/lists.
4. **Given** a student reading the data-loading section, **When** they finish, **Then** they can load the Developer Survey CSV with `pd.read_csv` using `usecols`, `dtype`, and low-memory options, and they can inspect it with `.head()`, `.info()`, `.describe()`, `.shape`, `.columns`, and `.dtypes`.
5. **Given** a student reading the cleaning section, **When** they finish, **Then** they have seen and applied: dtype coercion, handling of `NaN` (`isna`, `fillna`, `dropna`), and coercion of a numeric-like-but-messy column (e.g., `YearsCodePro` which contains the string "Less than 1 year") via `replace` + `pd.to_numeric(errors="coerce")`. Datetime parsing is explicitly out of scope for this lecture.
6. **Given** a student reading the indexing/selection section, **When** they finish, **Then** they can distinguish `.loc` vs `.iloc`, use boolean masks, combine masks with `&`/`|`/`~`, and use `.query()` for readable filters.
7. **Given** a student reading the multi-value-column section, **When** they finish, **Then** they can take a semicolon-separated column like `LanguageHaveWorkedWith` and convert it into long-format rows using `str.split(";")` + `.explode()`, then analyze per-language statistics.
8. **Given** a student reading the `groupby` section, **When** they finish, **Then** they have seen single-key `groupby().agg()` (e.g., median `ConvertedCompYearly` by `Country`), multi-key `groupby` (e.g., median compensation by `Country` + `EdLevel`), and named aggregations via the `agg(new_col=("col", "func"))` syntax.
9. **Given** a student reading the `merge`/join section, **When** they finish, **Then** they have seen at least one inner merge and one left merge between two DataFrames derived from the Survey (e.g., language-level stats joined onto respondent rows), plus a note on `how=`, `on=` / `left_on` / `right_on`, and the `validate=` argument to catch unintended many-to-many fanout.
10. **Given** a student reading the pivot/crosstab section, **When** they finish, **Then** they have seen one `pivot_table` and one `pd.crosstab` example answering questions like "share of respondents who want to learn language X by country".
11. **Given** a student reading the sorting/ranking/top-N section, **When** they finish, **Then** they can produce a top-10 list using `.sort_values()` + `.head()` or `.nlargest()` and explain when each is faster/clearer.
12. **Given** a student reading the method-chaining section, **When** they finish, **Then** they can rewrite a 4-step stepwise cleaning pipeline into a single `.pipe()` / `.assign()` chain and state one situation in which chaining hurts readability.
13. **Given** a student reading the `.apply()` / `.map()` section, **When** they finish, **Then** they can use `Series.map()` with a dict, use `Series.apply()` with a lambda, use `DataFrame.apply(axis=1)` for a row-wise custom function on the Survey, and explain why vectorized operations are preferred over `.apply()` when both are possible.
14. **Given** a student reading the `Categorical` dtype section, **When** they finish, **Then** they can convert a high-repeat Survey column to `"category"` and produce a concrete before/after memory-usage comparison showing the reduction.
15. **Given** a student reading the "When pandas breaks" section, **When** they finish, **Then** they can explain the memory-bound, single-process nature of pandas and name DuckDB and Polars as alternatives with a one-line description of each.
16. **Given** a student finishing the notebook, **When** they read the Summary and "What's Next" section, **Then** they see a preview of L12 (NumPy + vectorization + simple ML from scratch) and a teaser that the cleaned Survey DataFrame will reappear in L13 for visualization.

---

### User Story 2 - Mini-Project: "Developer Survey Insights" (3-Part Progressive) (Priority: P2)

A student completes a single progressive mini-project called **"Developer Survey Insights"**, anchored entirely on the Developer Survey DataFrame. The mini-project has three parts that build on each other:

- **Part 1 — in-class (~10–15 min)**: A simple filter + aggregate question, e.g., "What is the median `YearsCodePro` among Ukrainian respondents, and how does it compare to the global median?"
- **Part 2 — in-class (~10–15 min)**: A multi-value-column question using `.explode()`, e.g., "What are the top 10 most-used programming languages among respondents who identify as 'Learning to code'?"
- **Part 3 — homework extension (~30–60 min)**: An open-ended analytic task, e.g., "Pick one country and compare median compensation across the three most-common `DevType` values in that country. Apply the `Categorical` dtype to at least one string column. Present results as a tidy DataFrame plus a 3–5 sentence Ukrainian-language commentary on what you found."

Each part ships with a hidden solution cell for the in-class portions (Parts 1–2) and a reference solution + grading rubric for Part 3.

**Why this priority**: Satisfies constitution Principle II ("every lecture from L5 onward MUST include at least one runnable mini-project fitting 20–30 min in-class + 30–60 min homework extension") and converts the "watch" experience into guided practice. P2 because the Part 3 homework is an extension beyond the 1.5-hour lecture slot.

**Independent Test**: A student can complete Parts 1 and 2 within ~25 minutes using only knowledge from the notebook's earlier sections; their in-class answers, when revealed, match the hidden solution cells for shape and top-N ordering. Part 3 can be graded against the reference solution + rubric.

**Acceptance Scenarios**:

1. **Given** the notebook, **When** a student reads the mini-project header, **Then** they see a clear statement that this is the lecture's mini-project (not a loose set of exercises), its three-part structure, the in-class vs homework split, and the expected total time (~1 hour total: 25 min in class + 30–60 min homework).
2. **Given** Parts 1 and 2, **When** a student reads each part, **Then** each has a clear problem statement, expected output shape, at least one "hint" bullet that references the earlier notebook section where the relevant technique was introduced, and a hidden solution cell below.
3. **Given** Part 3, **When** a student reads it, **Then** they see: (a) the open-ended task description, (b) explicit requirements (must use `Categorical`, must produce a tidy DataFrame, must include Ukrainian-language commentary), (c) a reference solution revealed only in a collapsed section at the end of the notebook, and (d) a short grading rubric (e.g., "3 points: correctness; 2 points: clean pandas pipeline; 1 point: commentary quality").
4. **Given** Parts 1–2 completed in class, **When** a student starts Part 3 at home, **Then** they can proceed without re-reading earlier sections because Parts 1–2 have already exercised every pandas technique Part 3 requires.

---

### Edge Cases

- **What happens when the Stack Overflow Developer Survey CSV is not present locally?** The notebook MUST provide a clear download link, the expected local path, and a small guarded code cell that either loads the CSV or prints a helpful message pointing at the download step — it MUST NOT silently fail or attempt network fetches without warning.
- **What happens when pandas is not installed in the student's environment?** The notebook's first code cell MUST check for pandas and, if missing, print the exact `pip install` or `uv add` command (no auto-install).
- **What happens when the Stack Overflow dataset column names change between Survey years?** The notebook MUST commit to ONE specific year of the Developer Survey (pinned in a variable at the top) and note that column names differ year over year, so students adapting to a newer release need to check the schema — preventing silent breakage in the classroom.
- **What happens when a `merge` produces unexpected row multiplication (many-to-many fanout)?** The notebook MUST include at least one example showing how to detect this via shape inspection and the `validate=` keyword argument.
- **What happens when `groupby` is combined with a column containing many NaNs?** The notebook MUST show that `groupby` drops NaN keys by default and demonstrate `dropna=False` for cases where NaN itself is a meaningful group.
- **What happens when a student runs the notebook on a laptop with limited RAM?** The notebook MUST demonstrate `usecols=` to load only needed columns and `dtype=` to downcast early, so the full Survey CSV (multi-hundred-MB expanded) stays comfortably in memory.

## Requirements *(mandatory)*

### Functional Requirements

**Notebook Content — Structure:**

- **FR-001**: The notebook MUST state 3–5 learning objectives at the start covering: what pandas is and when to use it, Series vs DataFrame, loading and cleaning real CSV data (dtype coercion + missing values; NOT datetime), indexing and selection, `groupby` + `merge` + pivot, intermediate patterns (method chaining, `apply`/`map`, `Categorical` dtype), and knowing when to reach beyond pandas.
- **FR-002**: The notebook MUST include prerequisites referencing only basic Python (L1–L5): types, collections, comprehensions, functions, and file I/O. It MUST NOT reference L6–L10 content (FastAPI, Postgres, SQLAlchemy, Alembic, Docker).
- **FR-003**: The notebook MUST end with a Summary and "What's Next" section previewing L12 (NumPy + vectorization + simple ML from scratch).
- **FR-004**: The notebook MUST NOT include per-section time estimates in parentheses.
- **FR-005**: The notebook target duration MUST be 1.5 hours of lecture content.
- **FR-006**: All explanatory text MUST be in Ukrainian; English technical terms in parentheses ONLY for specific terms students need to recognize (e.g., "DataFrame", "Series", "groupby", "merge", "vectorization", "pivot table") — NOT for obvious phrases.

**Notebook Content — Pedagogical Sections:**

- **FR-007**: The notebook MUST include a "What pandas is good for (and not)" section with at least three strengths and two weaknesses explained in plain Ukrainian.
- **FR-008**: The notebook MUST include a "Series vs DataFrame" section constructing both from plain Python dicts/lists BEFORE loading any external file, so students build intuition about the core objects before seeing a messy real dataset.
- **FR-009**: The notebook MUST include a data-loading section demonstrating `pd.read_csv` on the Stack Overflow Developer Survey CSV with at least the following keyword arguments shown and explained: `usecols`, `dtype`, `na_values`, and either `low_memory=False` or a targeted `dtype` map. MUST show at least three inspection methods: `.head()`, `.info()`, `.describe(include="all")`, plus `.shape`, `.columns`, `.dtypes`.
- **FR-010**: The notebook MUST include a cleaning section covering: dtype coercion (`astype`, `pd.to_numeric(errors="coerce")`), missing-value handling (`isna`, `fillna`, `dropna` — with the difference between "drop rows with any NaN" vs "drop rows where a specific column is NaN"), and at least one example of coercing a messy numeric-ish column (e.g., `YearsCodePro` with string sentinels like "Less than 1 year" and "More than 50 years"). Datetime parsing is explicitly out of scope — the Survey CSV ships no submission-timestamp column, and the lecture is constrained to a single dataset.
- **FR-011**: The notebook MUST include an indexing/selection section covering: label-based (`.loc`) vs positional (`.iloc`) access, boolean masking with `&` / `|` / `~` (including the parenthesization trap), `.query()` for readable multi-condition filters, and `.isin()` for set-membership checks.
- **FR-012**: The notebook MUST include a multi-value-column section showing how to take a semicolon-separated column from the Survey (e.g., `LanguageHaveWorkedWith`, `DatabaseHaveWorkedWith`) and convert it to long-format rows via `str.split(";")` + `.explode()`, followed by a per-value frequency count (`value_counts()`).
- **FR-013**: The notebook MUST include a `groupby` section covering: single-key `groupby().agg()`, multi-key `groupby`, named aggregations via `agg(new_col=("col", "func"))`, and the `dropna=False` option for keeping NaN keys. This section MUST use Ukraine as its running anchor example (e.g., "how do Ukrainian respondents compare to the global median on X?") per the engagement-hook clarification.
- **FR-014**: The notebook MUST include a `merge` / join section demonstrating at least one inner merge and one left merge between two DataFrames both derived from the Survey (e.g., per-language summary stats merged back onto respondent-level rows), plus the `how=`, `on=` / `left_on` / `right_on`, and `validate=` arguments.
- **FR-015**: The notebook MUST include a pivot / crosstab section showing one `pivot_table` example (with `aggfunc` and `margins`) and one `pd.crosstab` example with normalization.
- **FR-016**: The notebook MUST include a sorting / ranking / top-N section showing `.sort_values()` + `.head(N)`, `.nlargest(N, by=...)` / `.nsmallest`, and `.rank()` on at least one ordinal column.
- **FR-017**: The notebook MUST include a "Practical analytics examples" section showing AT LEAST three complete pipelines answering the following concrete questions on the Survey dataset: (a) top 10 most-used programming languages overall, (b) median `ConvertedCompYearly` by `Country` (top 20 countries by respondent count), (c) share of respondents who want to learn Rust, broken down by main dev role (`DevType`).
- **FR-018**: The notebook MUST include a "When pandas breaks" conceptual section covering the memory-bound / single-process nature of pandas and briefly introducing DuckDB and Polars as alternatives (one paragraph each, no installation required, no code required).

**Notebook Content — Intermediate Topics (the "deep dive"):**

- **FR-032**: The notebook MUST include a method-chaining section showing the `.pipe()` and `.assign()` pattern for composing multi-step transformations into a single readable expression, with a side-by-side comparison of "stepwise intermediate-variable style" vs "chained style" on the same Survey-cleaning pipeline. MUST include one worked example per method, and explicitly discuss when chaining hurts readability (long chains, hard-to-debug failures).
- **FR-033**: The notebook MUST include an `.apply()` / `.map()` section covering: `Series.map()` for element-wise mapping (including mapping via a dict), `Series.apply()` for element-wise functions, `DataFrame.apply()` for column-wise or row-wise functions (`axis=0` vs `axis=1`), and a short warning that `apply` is slower than vectorized operations — so students learn to reach for vectorization first and `apply` only when necessary. MUST include at least one concrete Survey example (e.g., bucketing `ConvertedCompYearly` into salary bands via `.apply()` with a custom function).
- **FR-034**: The notebook MUST include a `Categorical` dtype section showing how to convert high-repeat string columns (`Country`, `DevType`, `EdLevel`) to `pd.Categorical` / `.astype("category")`, with a before/after memory comparison using `df.memory_usage(deep=True)` so students see the concrete payoff. MUST include a brief note that `Categorical` also unlocks ordered comparisons when the category order is meaningful (e.g., ordering `EdLevel` from primary-school to doctorate). This section MUST use Ukraine as its running anchor example when demonstrating filter-on-category operations (e.g., filtering to the Ukraine category on the newly-categorical `Country` column) per the engagement-hook clarification.

**Notebook Content — Exercises & Visual Elements:**

- **FR-019**: The notebook MUST contain a single progressive mini-project titled "Developer Survey Insights", anchored entirely on the Survey dataset, structured as three parts: Part 1 (in-class, filter + aggregate), Part 2 (in-class, multi-value column via `.explode()`), Part 3 (homework extension, open-ended multi-step analysis that MUST require use of the `Categorical` dtype and MUST produce a tidy DataFrame plus a 3–5 sentence Ukrainian-language commentary). Parts 1–2 MUST each have a hidden solution cell; Part 3 MUST have a reference solution revealed only in a collapsed section at the end of the notebook, together with a short grading rubric. Total student time target: ~25 min in-class (Parts 1–2) + 30–60 min homework (Part 3).
- **FR-020**: The notebook MUST contain at least 5 runnable code examples end-to-end in the instructional cells (independent of exercises).
- **FR-021**: The notebook MUST contain at least 2 memes or visual humor elements relevant to the topic.
- **FR-022**: The notebook MUST contain at least 1 diagram (e.g., a comparison table of pandas vs DuckDB vs Polars, a visual depicting how `.explode()` transforms rows, or an Index/Series/DataFrame schematic).
- **FR-023**: The notebook MUST NOT produce heavy visualizations (matplotlib/seaborn plots) beyond what comes for free from `.value_counts().head().plot(kind="bar")` — full visualization is the subject of L13 and MUST NOT be pre-empted here.

**Dataset Selection & Sourcing:**

- **FR-024**: The showcase dataset MUST be the **2025** Stack Overflow Annual Developer Survey (ODbL license). The notebook MUST pin the year in a single top-of-notebook variable (`SURVEY_YEAR = 2025`), link to the official download URL in the References section, and use column names as they appear in the 2025 schema. The notebook MUST include a one-line note that schemas drift year over year, so adapting to a different year requires re-checking column names.
- **FR-025**: The notebook MUST NOT embed the dataset file in the repository; the CSV MUST be downloaded separately by the student, with clear instructions and the expected local path, and handled gracefully if missing (see Edge Cases).
- **FR-026**: No russian-originated datasets, translations, or sources MUST be used, per constitution principle I.
- **FR-027**: The notebook MUST NOT depend on any external service beyond the one locally downloaded CSV — no network calls, no database, no FastAPI app.

**Scope Boundaries (what this lecture explicitly does NOT include):**

- **FR-028**: The notebook MUST NOT reference the notes-api project from L6–L10 (no `Note`/`Tag` models, no `pd.read_sql`, no SQLAlchemy engine, no FastAPI endpoints, no Alembic, no Docker).
- **FR-029**: This lecture MUST NOT add any project increment to the notes-api repository; L11 is a self-contained pandas lesson.
- **FR-030**: This lecture MUST NOT cover NumPy internals (deferred to L12), matplotlib/seaborn visualization (deferred to L13), or ML (deferred to L12). The following pandas topics are also explicitly out of scope for L11: `MultiIndex` (setting/resetting/stack/unstack), window functions (`rolling`, `expanding`, `resample`), and performance internals (copy-on-write, Arrow backend, `.itertuples` vs `iterrows` benchmarking).
- **FR-031**: This lecture MUST NOT install or demonstrate code with DuckDB or Polars — those are conceptual mentions only in the "When pandas breaks" section.

**Engagement & Pedagogy:**

- **FR-035**: The notebook MUST use Ukraine as a recurring anchor example in the `groupby` section (FR-013) and the `Categorical` dtype section (FR-034) — those are the two sections where "how does our country fit?" naturally illustrates the technique. The data-loading, cleaning, `.explode()`, `merge`, pivot/crosstab, sorting/top-N, method-chaining, and `apply`/`map` sections MUST use global or multi-country examples (no Ukraine filter), to preserve dataset breadth and avoid repetition. The mini-project (FR-019) Part 1 additionally keeps its Ukraine filter.

### Key Entities

- **Stack Overflow Developer Survey record** (the only entity in this lecture): One respondent's answers to the survey; a single row in the CSV. Key columns the notebook works with include: `ResponseId`, `MainBranch`, `Country`, `EdLevel`, `YearsCode`, `YearsCodePro`, `DevType`, `LanguageHaveWorkedWith`, `LanguageWantToWorkWith`, `DatabaseHaveWorkedWith`, `ConvertedCompYearly`. Not persisted — only loaded into pandas DataFrames inside the notebook.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: After the lecture, a student can load the Stack Overflow Developer Survey CSV into a DataFrame, clean at least two messy columns (one numeric, one multi-value), and produce a `groupby` result — verified by completing the notebook's exercises independently.
- **SC-002**: A student can explain in one sentence each (a) when pandas is the right tool, (b) when it isn't, and (c) what Series and DataFrame are — verified by short oral or written reflection.
- **SC-003**: A student can take a semicolon-separated Survey column (e.g., `LanguageHaveWorkedWith`) and produce a correct top-N frequency table in under 5 minutes without referring back to the notebook — verified by the exercise timing.
- **SC-004**: The notebook runs end-to-end in a clean Python 3.13 environment with pandas (and its transitive dependencies) as the only new install, in under 5 minutes of wall-clock time (excluding dataset download) on a typical student laptop.
- **SC-005**: The notebook contains all required structural elements: learning objectives, 5+ code examples, the 3-part "Developer Survey Insights" mini-project (Parts 1–2 with hidden solution cells, Part 3 with reference solution + grading rubric), 2+ memes/visuals, 1+ diagram, References (including dataset licensing and official link), Summary, and What's Next — verified by the checklist in `specs/016-lecture11-pandas-analytics/checklists/requirements.md`.
- **SC-006**: After the lecture, a student can name at least two pandas alternatives (DuckDB, Polars) and give one sentence explaining when each is preferable — verified by the "When pandas breaks" reflection.
- **SC-007**: After the lecture, at least 80% of students in an informal show-of-hands poll can correctly answer "what does `.explode()` do?" — verified by the instructor during the session.

### Assumptions

- Students have completed L1–L5 and are comfortable with Python basics: types, collections, comprehensions, functions, basic file I/O. No knowledge of FastAPI, databases, SQLAlchemy, or Docker is assumed or required.
- Students have Python 3.13+ and Jupyter (notebook or lab) working locally; `pandas` is the only new runtime dependency introduced by this lecture.
- The Stack Overflow Annual Developer Survey 2025 CSV is publicly downloadable at lecture time (ODbL license) from the official survey portal; the notebook pins `SURVEY_YEAR = 2025` and notes that column names differ year over year.
- The dataset fits comfortably in memory when loaded with targeted `usecols` / `dtype` on a typical 8–16 GB laptop; no out-of-core techniques are required.
- DuckDB and Polars remain conceptual; they are not installed or run in code during this lecture.
- The cleaned Survey DataFrame produced in this lecture MAY be reused in L13 (visualization) — but L11 does not depend on that reuse and does not produce any artifact that other lectures depend on.
- The lecture is standalone by design: dropping the notes-api project increment is an explicit scope decision recorded in the Clarifications section, deviating from the constitution's suggested L11 `/analytics/report` endpoint. The constitution's course-capstone thread resumes in L12 or later.
- Constitutional compliance for Principle II ("mini-project per L5+ lecture, 20–30 min in-class + 30–60 min homework") is preserved: the "Developer Survey Insights" 3-part mini-project (FR-019, User Story 2) fills that role without depending on any previous project stack.
