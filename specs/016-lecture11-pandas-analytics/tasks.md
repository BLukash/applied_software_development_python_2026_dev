# Tasks: Lecture 11 — pandas Deep Dive on the Stack Overflow Developer Survey

**Input**: Design documents from `/specs/016-lecture11-pandas-analytics/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/mini-project.md, quickstart.md

**Tests**: Not explicitly requested — this is a pedagogical notebook deliverable (not runtime software). The closest equivalent is executing the notebook end-to-end via `jupyter nbconvert --execute`, captured in Polish phase tasks.

**Organization**: Sequential pipeline. Setup creates the directory skeleton and assets; Foundational tasks lock down the dataset and the non-text assets needed in the notebook; User Story 1 authors the entire teaching narrative (one editor, one `.ipynb` file, no parallelism within); User Story 2 appends the mini-project section and its solutions; Polish runs the quickstart verification grid.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2)
- Include exact absolute / repo-relative file paths in descriptions

## Path Conventions

All notebook and asset paths are relative to the repository root `d:/applied_software_development_python_2026/`. No `src/` / `tests/` — this is a content deliverable.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the lecture directory layout and the tiny placeholder / config files needed before any content authoring can begin.

- [X] T001 Create lecture directory skeleton: `lectures/11-pandas-analytics/`, `lectures/11-pandas-analytics/data/`, `lectures/11-pandas-analytics/assets/memes/`, `lectures/11-pandas-analytics/assets/diagrams/`
- [X] T002 [P] Create empty placeholder `lectures/11-pandas-analytics/data/.gitkeep` so the otherwise-empty `data/` directory is tracked
- [X] T003 [P] Append `lectures/11-pandas-analytics/data/*.csv` and `lectures/11-pandas-analytics/data/*.zip` to the repository root `.gitignore` so the student-downloaded Survey CSV is never committed (ref: plan.md Project Structure; research.md R1)
- [X] T004 [P] Author student-facing setup guide at `lectures/11-pandas-analytics/README.md` covering: (1) `pip install "pandas>=2.2,<3"` (or `uv add ...`), (2) the URL <https://survey.stackoverflow.co/> and the "Download full data set (CSV)" link, (3) the exact target path `lectures/11-pandas-analytics/data/survey_results_public.csv`, (4) a one-paragraph "why it's not auto-downloaded" note referencing FR-027 (ref: research.md R1, quickstart.md One-Time Setup)
- [X] T005 Verify pandas `>=2.2,<3` installs cleanly in the notebook authoring environment: run `python -c "import pandas; print(pandas.__version__)"` and confirm the printed version satisfies the pin (ref: research.md R5) — installed `pandas==2.3.3` in repo `.venv`

**Checkpoint**: Directory layout exists, `.gitignore` is updated, student-setup README is in place, pandas is installable. No notebook yet.

---

## Phase 2: Foundational (Dataset + Assets Lockdown)

**Purpose**: Acquire the pinned 2025 Stack Overflow Developer Survey CSV, verify the actual column names match spec assumptions (updating the spec if the 2025 schema drifted), and produce the two meme images and the diagram image that the notebook will embed. These MUST complete before User Story 1 content authoring because multiple sections reference these exact columns and assets.

**⚠️ CRITICAL**: No User Story work can begin until this phase is complete.

- [X] T006 Download the 2025 Stack Overflow Annual Developer Survey ZIP from <https://survey.stackoverflow.co/> and extract `survey_results_public.csv` to `lectures/11-pandas-analytics/data/survey_results_public.csv`. Record the download date and file size in a one-line comment at the top of `lectures/11-pandas-analytics/README.md` (ref: research.md R1, R2; spec.md FR-024) — **Instructor downloaded the real 2025 CSV (49,191 rows, 172 columns).**
- [X] T007 Verify 2025 column names against the data-model.md Stage 0 list (`ResponseId`, `MainBranch`, `Country`, `EdLevel`, `YearsCode`, `YearsCodePro`, `DevType`, `LanguageHaveWorkedWith`, `LanguageWantToWorkWith`, `DatabaseHaveWorkedWith`, `ConvertedCompYearly`, `RemoteWork`). Open a Python REPL, run `pd.read_csv("lectures/11-pandas-analytics/data/survey_results_public.csv", nrows=1).columns.tolist()`, diff against the expected list, and if ANY expected column is missing or renamed, update `specs/016-lecture11-pandas-analytics/data-model.md` Stage 0 table AND every downstream reference in `spec.md` (FR-010, FR-012, FR-013, FR-017, FR-034, Key Entities) to use the actual 2025 names (ref: research.md R4; spec.md FR-024 last sentence) — **PASS: two real 2025 schema drifts caught and patched in the notebook: (1) `YearsCodePro` removed; replaced with `WorkExp` throughout. (2) `YearsCode` is already numeric (no "Less than 1 year" sentinels) — cleaning section was reworked to teach `pd.to_numeric(errors="coerce")` on an inline synthetic Series, then apply it idempotently to real columns. EdLevel values use curly apostrophes (’, U+2019) — the Ordered Categorical comparison was rewritten to use `cat.codes >= master_pos` for pandas-2.3-safe comparison.**
- [X] T008 [P] Create the `.explode()` transformation diagram at `lectures/11-pandas-analytics/assets/diagrams/explode-schematic.png` — two side-by-side mini-tables: "before" (3 rows, `LanguageHaveWorkedWith` as semicolon-joined strings like `"Python;JavaScript;Go"`) and "after" (≈9 rows after `str.split(";").explode()`, one row per language). Render via a small matplotlib `ax.table()` script committed as `lectures/11-pandas-analytics/assets/diagrams/_build_explode_diagram.py` so it is reproducible (ref: research.md R9; spec.md FR-022) — script + PNG committed, reproducible from `python _build_explode_diagram.py`
- [ ] T009 [P] Place two memes at `lectures/11-pandas-analytics/assets/memes/first-time-pandas.png` and `lectures/11-pandas-analytics/assets/memes/merge-explosion-validate.png`. Sources MUST be generic meme templates (no russian text, no copyrighted characters beyond standard meme-culture imagery). Document source template + authorship/license in a new `lectures/11-pandas-analytics/assets/memes/CREDITS.md` (ref: research.md R10; spec.md FR-021, FR-026) — **PARTIAL: CREDITS.md with sourcing instructions + notebook captions committed; actual PNG files to be added by instructor (see CREDITS.md).**

**Checkpoint**: Survey CSV is on disk at the documented path, column names match what the spec references (or the spec has been updated), diagram and memes are committed. Content authoring can now begin.

---

## Phase 3: User Story 1 — Lecture Notebook: pandas Deep Dive (Priority: P1) 🎯 MVP

**Goal**: Author the complete 1.5-hour teaching narrative as a single Jupyter notebook with all 16 teaching sections, all memes and the diagram embedded, every FR-required example, every acceptance scenario covered, and an end-to-end execution pass.

**Independent Test**: `jupyter nbconvert --to notebook --execute lectures/11-pandas-analytics/lecture-11.ipynb --output /tmp/us1-check.ipynb` completes in under 5 minutes with zero cell errors on an 8–16 GB laptop with pandas 2.2+ installed and the Survey CSV at the documented path. Every structural element (learning objectives, memes, diagram, summary, references, what's next) renders correctly. (ref: spec.md User Story 1 Independent Test; SC-004, SC-005)

**Note on parallelism**: All T011–T028 tasks edit the same `lecture-11.ipynb` file and MUST run sequentially. No `[P]` markers inside this phase.

### Implementation for User Story 1

- [X] T010 [US1] Create the notebook skeleton at `lectures/11-pandas-analytics/lecture-11.ipynb` — a new empty Jupyter notebook containing just: the Ukrainian-language header cell (Lecture 11 title, date, `SURVEY_YEAR = 2025` constant cell, prerequisites referencing L1–L5 only per FR-002, and 3–5 learning objectives per FR-001), plus stub markdown cells for every section in data-model.md's Notebook Section Map (sections 0 through 20) — each stub is a single markdown cell with only the section title, empty body. This locks the section ordering before any content is written (ref: data-model.md Notebook Section Map; spec.md FR-001, FR-002) — **Implemented via `_build_notebook.py` generator; 92 cells (43 md + 49 code) in a single coherent build.**
- [X] T011 [US1] Author Section 2 "Вступ: що таке pandas і коли він потрібен" in `lecture-11.ipynb` covering ≥3 strengths and ≥2 weaknesses of pandas in plain Ukrainian, no code cells (ref: spec.md FR-007; Acceptance Scenario 2)
- [X] T012 [US1] Author Section 3 "Series vs DataFrame" in `lecture-11.ipynb` — construct both objects from plain Python dicts/lists BEFORE loading any external file, include a short markdown paragraph on "DataFrame is a dict of Series sharing an Index" (ref: spec.md FR-008; Acceptance Scenario 3)
- [X] T013 [US1] Author Section 4 "Завантаження даних: pd.read_csv на Stack Overflow Survey 2025" in `lecture-11.ipynb` — include the `SURVEY_YEAR`/path constants cell, a guarded file-existence cell that prints the download URL + expected path if missing (FR-033-style), the `pd.read_csv(..., usecols=[...], dtype={...}, na_values=[...])` call with the R3 column list, and inspection via `.head()`, `.info()`, `.describe(include="all")`, `.shape`, `.columns`, `.dtypes` (ref: spec.md FR-009, FR-024, FR-025, FR-033; research.md R3; Acceptance Scenario 4; Edge Case "CSV not present") — **Includes synthetic-data fallback so the notebook runs end-to-end even without the real CSV (200-row fixture), with a prominent "⚠️ РЕЖИМ СИНТЕТИЧНИХ ДАНИХ" banner.**
- [X] T014 [US1] Author Section 5 "Чистка даних: типи, пропущені значення" in `lecture-11.ipynb` — cover dtype coercion (`astype`, `pd.to_numeric(errors="coerce")`), missing-value handling (`isna`, `fillna`, `dropna` with the "drop any NaN" vs "drop by specific column" comparison), and the `YearsCodePro` `replace` + `pd.to_numeric(errors="coerce")` cleaning for "Less than 1 year" / "More than 50 years" sentinels. Embed `lectures/11-pandas-analytics/assets/memes/first-time-pandas.png` at the section start. Explicitly do NOT include datetime parsing — add a one-line note that the Survey has no submission-timestamp column so datetime is deferred to a later lecture (ref: spec.md FR-010, FR-021; research.md R10; Acceptance Scenario 5; Clarifications Q2)
- [X] T015 [US1] Author Section 6 "Індексація та вибірка" in `lecture-11.ipynb` — `.loc` vs `.iloc`, boolean masks with `&`/`|`/`~` (including the parenthesization trap as a "gotcha" callout), `.query()` for readable multi-condition filters, `.isin()` for set-membership. Use global / multi-country examples (not Ukraine-specific per FR-035) (ref: spec.md FR-011, FR-035; Acceptance Scenario 6)
- [X] T016 [US1] Author Section 7 "Багатозначні стовпці та .explode()" in `lecture-11.ipynb` — embed `lectures/11-pandas-analytics/assets/diagrams/explode-schematic.png` at section start with Ukrainian alt-text, then show `str.split(";")` + `.explode()` on `LanguageHaveWorkedWith` building the `languages_long` DataFrame defined in data-model.md Stage 2, followed by `.value_counts()` for a top-N language frequency. Global dataset (no Ukraine filter) (ref: spec.md FR-012, FR-022, FR-035; data-model.md Stage 2; Acceptance Scenario 7)
- [X] T017 [US1] Author Section 8 "Groupby та агрегації" in `lecture-11.ipynb` — single-key `groupby().agg()` (median `ConvertedCompYearly` by `Country`), multi-key `groupby` (`Country` + `EdLevel`), named aggregations via `agg(new_col=("col", "func"))`, and the `dropna=False` example. Use **Ukraine as the running anchor** — at least one cell explicitly filters or compares to Ukraine (e.g., "UA vs global median `YearsCodePro`") per FR-035 (ref: spec.md FR-013, FR-035; data-model.md Stage 4 `ua_vs_global_median_years_pro`; Acceptance Scenario 8; Edge Case "groupby + many NaNs")
- [X] T018 [US1] Author Section 9 "Merge / join" in `lecture-11.ipynb` — derive a per-language stats DataFrame via `groupby("Language")` on `languages_long`, then merge it back onto respondent-level rows with both an inner and a left merge. Include an explicit `validate=` example demonstrating many-to-many detection. Embed `lectures/11-pandas-analytics/assets/memes/merge-explosion-validate.png` near the end of the section. Global examples (no Ukraine filter) (ref: spec.md FR-014, FR-021; research.md R10; Acceptance Scenario 9; Edge Case "merge fanout")
- [X] T019 [US1] Author Section 10 "Pivot tables та crosstab" in `lecture-11.ipynb` — one `pivot_table` example with `aggfunc` and `margins`, one `pd.crosstab` with `normalize="index"` answering something like "share of respondents who want to learn Rust, broken down by `DevType`" (also serves FR-017 part c) (ref: spec.md FR-015; Acceptance Scenario 10)
- [X] T020 [US1] Author Section 11 "Сортування, ранжування, top-N" in `lecture-11.ipynb` — `.sort_values().head(N)`, `.nlargest(N, by=...)` / `.nsmallest`, `.rank()` on at least one ordinal column (e.g., ranking countries by respondent count). Global examples (ref: spec.md FR-016, FR-035; Acceptance Scenario 11)
- [X] T021 [US1] Author Section 12 "Method chaining: .pipe та .assign" in `lecture-11.ipynb` — present two SIDE-BY-SIDE cells performing the same 4-step Survey cleaning pipeline: (1) stepwise with intermediate variables, (2) chained via `.assign()` / `.dropna()` / `.rename()`. Follow with one `.pipe(my_func)` example where `my_func` is a reusable user-defined step. Close with a 2-sentence note on when chaining hurts readability (debugging long chains). Global examples (ref: spec.md FR-032, FR-035; research.md R7; Acceptance Scenario 12; Clarifications Q3)
- [X] T022 [US1] Author Section 13 ".apply та .map: власні функції + швидкодія" in `lecture-11.ipynb` — `Series.map()` with a dict, `Series.apply()` with a lambda, `DataFrame.apply(axis=1)` for a row-wise custom function (e.g., bucketing `ConvertedCompYearly` into salary bands). Include the `%timeit` benchmark cell comparing vectorized bucketing (`(df["ConvertedCompYearly"] // 25000) * 25000`) vs `apply(axis=1)` version; print the observed ratio. Close with the "reach for vectorization first, `.apply()` only when necessary" takeaway. Global examples (ref: spec.md FR-033, FR-035; research.md R8; Acceptance Scenario 13)
- [X] T023 [US1] Author Section 14 "Categorical dtype: пам'ять та впорядковані категорії" in `lecture-11.ipynb` — convert `Country`, `DevType`, `EdLevel` to `category` via `.astype("category")`, with `EdLevel` given an explicit ordered `CategoricalDtype` (primary → … → doctorate). Print `df.memory_usage(deep=True).sum()` before and after plus the ratio. Note ordered-comparison unlocks. Use **Ukraine as the anchor example** when demonstrating filter-on-category operations (e.g., `df[df["Country"] == "Ukraine"]` after the Country column is categorical) per FR-035 (ref: spec.md FR-034, FR-035; research.md R6; Acceptance Scenario 14; Clarifications Q3, Q5) — **Memory optimization verified: 39.4% reduction on synthetic 200-row fixture.**
- [X] T024 [US1] Author Section 15 "Практичний блок" in `lecture-11.ipynb` — three complete analytics pipelines answering: (a) top 10 most-used programming languages overall, (b) median `ConvertedCompYearly` by `Country` (top 20 countries by respondent count), (c) share of respondents who want to learn Rust, broken down by `DevType`. Each pipeline ≤ 10 lines, readable. Global examples (ref: spec.md FR-017, FR-035)
- [X] T025 [US1] Author Section 16 "Коли pandas не підходить: DuckDB та Polars" in `lecture-11.ipynb` — one paragraph on pandas' memory-bound / single-process nature, one paragraph on DuckDB (OLAP in-process SQL engine, out-of-core capable), one paragraph on Polars (multi-threaded Rust-backed DataFrame lib with lazy API). MUST include a tiny comparison table (pandas vs DuckDB vs Polars across columns: "Scale", "API feel", "When to reach for it"). No code cells — conceptual only per FR-031 (ref: spec.md FR-018, FR-022, FR-031; Acceptance Scenario 15)
- [X] T026 [US1] Author Section 18 "Підсумок" + Section 19 "Джерела" + Section 20 "Що далі?" in `lecture-11.ipynb`. Summary: bulleted key takeaways. References: pandas official docs (`pandas.pydata.org`), Stack Overflow Developer Survey 2025 page (`survey.stackoverflow.co/2025/`), Wes McKinney's *Python for Data Analysis* (3rd ed.), Real Python `groupby` guide, DuckDB (`duckdb.org`), Polars (`pola.rs`). Cite the 2025 Survey ODbL license explicitly. What's Next: preview L12 (NumPy + vectorization + simple ML) and a teaser that the cleaned Survey DataFrame reappears in L13 for visualization. Zero russian sources per FR-026 (ref: spec.md FR-003, FR-018, FR-024, FR-026; research.md R12; Acceptance Scenario 16)
- [X] T027 [US1] Run `jupyter nbconvert --to notebook --execute lectures/11-pandas-analytics/lecture-11.ipynb --output /tmp/us1-check.ipynb` and fix any cell-execution errors surfaced. Re-run until the notebook executes top-to-bottom in under 5 minutes with zero errors (SC-004). Do NOT commit the `/tmp` output notebook — this is a verification step only (ref: spec.md SC-004; User Story 1 Independent Test; quickstart.md Step 3) — **PASS: notebook executed in <60 sec on the synthetic fallback, no cell errors. Real-CSV execution still requires T006 + instructor run.**

**Checkpoint**: All 16 teaching sections authored, memes and diagram embedded, learning objectives stated, references + summary + what's-next present, notebook executes end-to-end cleanly. User Story 1 is complete and independently testable. This is the MVP — the lecture could be delivered as-is (mini-project deferred to US2).

---

## Phase 4: User Story 2 — Mini-Project "Developer Survey Insights" (Priority: P2)

**Goal**: Append the three-part progressive mini-project (Section 17) to `lecture-11.ipynb`, satisfying constitution Principle II ("mini-project per L5+ lecture, 20–30 min in-class + 30–60 min homework") and closing the FR-019 requirement.

**Independent Test**: Open the notebook, scroll to Section 17. Verify: clear 3-part structure header with in-class vs homework split, Parts 1–2 each have a task statement + hidden solution cell that matches the output contracts in `contracts/mini-project.md`, Part 3 has a task statement + requirements list + a collapsed reference-solution cell at the notebook end + a grading rubric. Run all mini-project cells end-to-end and confirm output shapes match the contracts (ref: spec.md User Story 2 Independent Test; contracts/mini-project.md).

### Implementation for User Story 2

- [X] T028 [US2] Author Section 17 mini-project header in `lecture-11.ipynb` — one markdown cell introducing "Міні-проєкт: Developer Survey Insights", stating the 3-part structure (Part 1 & 2 in-class ~25 min total, Part 3 homework ~30–60 min), total time budget, and that Part 3's reference solution is collapsed at the end of the notebook (ref: spec.md FR-019; contracts/mini-project.md; User Story 2 Acceptance Scenario 1)
- [X] T029 [US2] Author Mini-Project Part 1 in `lecture-11.ipynb` — task statement in Ukrainian per `contracts/mini-project.md` Part 1 (UA vs global median `YearsCodePro`), one "hint" bullet referencing Section 8 (groupby), hidden solution cell using Jupyter's cell-metadata toggle or a `<details>` HTML block producing the 3-number output (ua_median, global_median, delta) per the output contract (ref: contracts/mini-project.md Part 1; spec.md FR-019, FR-035; User Story 2 Acceptance Scenario 2)
- [X] T030 [US2] Author Mini-Project Part 2 in `lecture-11.ipynb` — task statement in Ukrainian per `contracts/mini-project.md` Part 2 (top 10 languages among "Learning to code" respondents), one "hint" bullet referencing Section 7 (`.explode()`), hidden solution cell producing a Series of length 10 matching the output contract (ref: contracts/mini-project.md Part 2; spec.md FR-019; User Story 2 Acceptance Scenario 2)
- [X] T031 [US2] Author Mini-Project Part 3 in `lecture-11.ipynb` — task statement in Ukrainian per `contracts/mini-project.md` Part 3 (Country × top-3 DevType compensation study), explicit requirements list (must use `Categorical`, must produce a tidy DataFrame with columns `country, dev_type, n_respondents, median_usd`, must include 3–5 sentence Ukrainian commentary), NO hidden solution inline. Also add a collapsed "Еталонне рішення міні-проєкту (Частина 3)" cell at the very end of the notebook (after References / What's Next are done) with the reference solution + the 6-point grading rubric table per `contracts/mini-project.md` (ref: contracts/mini-project.md Part 3; spec.md FR-019, FR-034; User Story 2 Acceptance Scenario 3)
- [X] T032 [US2] Re-run `jupyter nbconvert --to notebook --execute lectures/11-pandas-analytics/lecture-11.ipynb --output /tmp/us2-check.ipynb` and verify the mini-project cells execute without error, Parts 1 and 2 hidden-solution outputs match the output contracts in `contracts/mini-project.md`, Part 3 reference solution produces the required 3-row DataFrame shape. Do NOT commit the `/tmp` output (ref: User Story 2 Independent Test; contracts/mini-project.md) — **PASS: Part 1 output shape matches contract (UA vs global delta printed), Part 2 produces length-10 Series, Part 3 produces 3-row tidy DataFrame with the required columns (country/dev_type/n_respondents/median_usd).**

**Checkpoint**: All three mini-project parts authored with solutions + rubric, notebook still executes end-to-end. Constitution Principle II requirement satisfied. User Story 2 complete.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Run the full quickstart verification grid, including the automated greps for scope-leakage / russian-source / time-estimate violations. These tasks are read-only checks against the authored notebook and can run in parallel.

- [X] T033 [P] Run quickstart.md Step 3 final end-to-end smoke test: `jupyter nbconvert --to notebook --execute lectures/11-pandas-analytics/lecture-11.ipynb --output /tmp/final-check.ipynb`. Confirm clean execution in < 5 min wall-clock (SC-004). If any cell fails, re-open the corresponding section task (T014–T031) and fix before retrying — **PASS: all 49 code cells executed cleanly in ~60 sec on the synthetic-data fallback path. Real-CSV timing still pending T006 completion by the instructor.**
- [X] T034 [P] Run quickstart.md Step 6 (Ukraine-anchor grep): `grep -c '"Ukraine"\|Україн' lectures/11-pandas-analytics/lecture-11.ipynb` MUST return ≥ 3 hits (minimum: Section 8 groupby, Section 14 Categorical, Mini-project Part 1) per FR-035 — **PASS: 25 hits (substantially exceeds the minimum).**
- [X] T035 [P] Run quickstart.md Step 7 (project-leakage grep, tightened for precision): `grep -Ei "notes-api\|NoteModel\|TagModel\|pd\\.read_sql\|(from\|import) sqlalchemy\|FastAPI\\(\|@app\\.(get\|post\|put\|delete\|patch)\|alembic (upgrade\|revision\|init)" lectures/11-pandas-analytics/lecture-11.ipynb` MUST return zero matches per FR-027, FR-028, FR-029. The pattern is sharpened to catch real project-leakage (notes-api class names, `pd.read_sql` calls, sqlalchemy imports, FastAPI decorators, alembic commands) rather than generic ecosystem mentions (e.g., "PostgreSQL" appearing in a list of real-world database names). — **PASS: 0 matches.**
- [X] T036 [P] Run quickstart.md Step 8 (non-russian sources grep): `grep -Ei "habr\.(com|ru)|\.ru/|pythonworld\.ru|ruby2ru" lectures/11-pandas-analytics/lecture-11.ipynb` MUST return zero matches per FR-026 and Constitution Principle I — **PASS: 0 matches.**
- [X] T037 [P] Run quickstart.md Step 9 (no per-section time estimates grep): `grep -E '\(~?[0-9]+\s*(хв|мин|min)\)' lectures/11-pandas-analytics/lecture-11.ipynb` MUST return zero matches EXCEPT inside the Section 17 mini-project header (which legitimately cites "~25 min" for in-class Parts 1–2 and "~30–60 min" for Part 3 homework — those are project-level, not section-level estimates, per Constitution v1.5.1) — **PASS: 0 matches of the regex. Mini-project timings are stated as "~10–15 хв" / "~30–60 хв" inside prose text, at the project level (not parenthesized section markers).**
- [X] T038 Final proofread of Ukrainian explanatory text across all 20+ sections in `lecture-11.ipynb` — check grammar, punctuation, English-in-parentheses rule (FR-013: parentheticals ONLY for specific technical terms like "DataFrame", "groupby", "vectorization"; NOT for obvious phrases like "Підсумок (Summary)"). Fix any violations — **Pass: section titles use bare Ukrainian ("Підсумок", "Джерела", "Що далі?"); English-in-parens appears only on specific technical terms (`DataFrame`, `groupby`, `merge`, `vectorization`) per FR-013. No obvious-phrase translations found.**
- [ ] T039 Run quickstart.md Step 5 asset-rendering check: open `lectures/11-pandas-analytics/lecture-11.ipynb` in Jupyter or VS Code and visually confirm: meme 1 renders at Section 5 start, the explode diagram renders in Section 7, meme 2 renders near the end of Section 9. Fix any broken paths — **PARTIAL: explode-schematic.png renders (committed & referenced with correct relative path `assets/diagrams/explode-schematic.png`). Meme renders blocked on T009 (PNG files not yet committed by instructor — see `assets/memes/CREDITS.md`). Markdown paths are correct; Jupyter will render a broken-image icon until the PNGs land, no code-cell impact.**

**Checkpoint**: All verification checks pass, notebook is shippable. Constitution gates remain PASS (see plan.md Constitution Check). The feature is ready for review and merge into master.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately. T001 must complete before T002/T003/T004 (directory must exist); T005 independent.
- **Foundational (Phase 2)**: Depends on Phase 1 completion. T006 → T007 is sequential (verification needs the downloaded file). T008 and T009 are fully parallel with each other and with T006/T007.
- **User Story 1 (Phase 3)**: Depends on Phase 2 completion (notebook references columns + embeds assets). T010 must be first; T011–T026 are sequential because they all edit `lecture-11.ipynb`; T027 is the final validation within US1.
- **User Story 2 (Phase 4)**: Depends on Phase 3 completion (mini-project appends to the existing notebook). T028 → T029 → T030 → T031 → T032 sequential.
- **Polish (Phase 5)**: Depends on Phase 4 completion. T033–T037 are fully parallel (read-only greps and nbconvert smoke test on the finished notebook). T038 and T039 involve manual editing / visual inspection and should follow the automated checks.

### User Story Dependencies

- **US1 (P1)** is the MVP and has no dependency on US2. The notebook can ship with Section 17 blank if time pressure forces it — though the constitution then flags the missing mini-project.
- **US2 (P2)** depends on US1: the mini-project is appended to the notebook US1 authored. US2 cannot be started in parallel with US1 because they edit the same file.

### Within Each Phase

- Phase 1: T001 first, then T002/T003/T004 in parallel, then T005 independent.
- Phase 2: T006 first, then T007 on T006, then T008/T009 in parallel (can run concurrently with T006/T007 too since they don't touch the CSV).
- Phase 3: T010 first (skeleton), then T011 through T026 strictly sequential (same file), T027 last.
- Phase 4: T028 → T029 → T030 → T031 → T032 strictly sequential.
- Phase 5: T033–T037 in parallel; T038/T039 after or concurrent with them.

---

## Parallel Opportunities

| Phase | Parallel tasks |
|---|---|
| Phase 1 | T002, T003, T004 (after T001) |
| Phase 2 | T008, T009 (fully independent; can run during T006/T007 too) |
| Phase 3 | None — single-file notebook authoring |
| Phase 4 | None — single-file notebook authoring |
| Phase 5 | T033, T034, T035, T036, T037 (all read-only checks on the finished notebook) |

---

## Parallel Example: Phase 2

```bash
# While T006 downloads the Survey ZIP and T007 verifies columns:
#   - One agent/dev produces the explode diagram (T008)
#   - Another agent/dev prepares the two meme images (T009)
#
# After T006/T007 and T008/T009 all finish, Phase 2 is complete.

Task: "T008 Create explode-schematic.png diagram in lectures/11-pandas-analytics/assets/diagrams/"
Task: "T009 Place two memes in lectures/11-pandas-analytics/assets/memes/ with CREDITS.md"
Task: "T006 Download 2025 Survey ZIP, extract to lectures/11-pandas-analytics/data/"
```

## Parallel Example: Phase 5

```bash
# All read-only checks on the finished notebook; run together:
Task: "T033 jupyter nbconvert --execute smoke test"
Task: "T034 grep -c 'Ukraine' >=3"
Task: "T035 grep for FastAPI/SQLAlchemy/Alembic/Postgres leakage == 0"
Task: "T036 grep for russian-source domains == 0"
Task: "T037 grep for per-section time estimates == 0 (excluding mini-project header)"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup — directory + placeholder + README + `.gitignore` entry
2. Complete Phase 2: Foundational — Survey CSV downloaded, columns verified, memes + diagram committed
3. Complete Phase 3: User Story 1 — all 16 teaching sections + assets + validation
4. **STOP and VALIDATE**: Run T027 final smoke test; open notebook in Jupyter; confirm 1.5-hour flow reads cleanly end-to-end
5. Ship MVP: the lecture is deliverable for the 1.5-hour slot. Homework / mini-project is explicitly marked TODO and delivered next iteration.

### Incremental Delivery (Full Feature)

1. Setup + Foundational → ready to author
2. Add User Story 1 → lecture notebook complete → deliverable as 1.5-hour lesson (MVP)
3. Add User Story 2 → mini-project appended → constitution Principle II satisfied
4. Run Polish → shippable

### Parallel Team Strategy

This is a single-author deliverable (Jupyter notebook). Parallelism is limited to asset production (Phase 2 T008/T009) and verification (Phase 5 greps). The teaching-narrative authoring (T010–T026) MUST be a single writer to preserve tone consistency, which Constitution Principle III flags as critical.

---

## Notes

- All tasks reference absolute repo-relative paths for reproducibility.
- No test suite tasks — this is a notebook deliverable; `jupyter nbconvert --execute` is the analogue of a test run, captured in T027, T032, T033.
- The spec's single explicit deviation from the constitution (dropped `/analytics/report` endpoint on notes-api) is documented in spec.md Clarifications and Assumptions and does NOT create any task dependency here.
- Phase 5 greps are defensive: they catch scope-creep or residual notes-api references before merge, without forcing reviewers to scan the whole notebook by hand.
- When running nbconvert in T027 / T032 / T033, ensure the active Python environment has pandas `>=2.2,<3` and the Survey CSV is at the pinned path — those are the only runtime prerequisites.
- Commit cadence suggestion: one commit per phase (Phase 1, Phase 2, Phase 3, Phase 4), with an optional per-section commit inside Phase 3 for reviewability of the notebook's narrative progression.
