# Quickstart: Lecture 11 — pandas Deep Dive on the Stack Overflow Developer Survey

**Feature**: 016-lecture11-pandas-analytics
**Date**: 2026-04-23

## Prerequisites

- Python 3.13+
- Jupyter (notebook or lab) installed — either via `pip install jupyter` or the VS Code Jupyter extension
- ~200 MB free disk space for the Survey ZIP + extracted CSV

**No prior project setup required.** This lecture is isolated from the L6–L10 notes-api project (per spec FR-028 / FR-029). No Docker, no PostgreSQL, no FastAPI.

## One-Time Setup

### 1. Install pandas

```bash
pip install "pandas>=2.2,<3"
```

Or with uv:

```bash
uv add "pandas>=2.2,<3"
```

### 2. Download the 2025 Stack Overflow Developer Survey

1. Open <https://survey.stackoverflow.co/>
2. Click **"Download the full data set (CSV)"** (on the 2025 survey page or methodology page)
3. You will receive a ZIP file, typically named `stack-overflow-developer-survey-2025.zip`
4. Extract it. The file you need is `survey_results_public.csv`
5. Place `survey_results_public.csv` at:

   ```text
   lectures/11-pandas-analytics/data/survey_results_public.csv
   ```

The `data/` directory is already present in the repo (tracked via `.gitkeep`) and CSV files inside it are `.gitignore`d, so your local download will not be committed accidentally.

## Verification Steps

### 1. Verify lecture directory structure

```bash
ls lectures/11-pandas-analytics/
# Expected: lecture-11.ipynb  README.md  data/  assets/
```

### 2. Verify CSV is in place

```bash
ls lectures/11-pandas-analytics/data/survey_results_public.csv
# Expected: the file exists (size ~80–120 MB depending on year)
```

### 3. Run the notebook end-to-end

```bash
jupyter nbconvert --to notebook --execute \
    lectures/11-pandas-analytics/lecture-11.ipynb \
    --output /tmp/lecture-11-executed.ipynb
```

This should complete without a cell-execution error in under 5 minutes on a typical 8–16 GB laptop (SC-004).

### 4. Sanity-check the mini-project reference solutions

Open the executed notebook. Verify:

- Part 1 prints three labeled values (UA median, global median, delta).
- Part 2 prints a `Series` of length 10 with `Language` names as the index.
- Part 3 reference solution (collapsed at notebook end) renders a 3-row DataFrame with columns `country`, `dev_type`, `n_respondents`, `median_usd`.

### 5. Verify assets render

In the opened notebook, scroll to:

- Section 5 (cleaning) — meme 1 ("Pandas: first time?") should render
- Section 7 (`.explode`) — the `explode-schematic.png` diagram should render
- Section 9 (merge) — meme 2 ("merge explosion / `validate=`") should render

### 6. Verify Ukraine anchoring

Search the notebook for `"Ukraine"`:

```bash
grep -c '"Ukraine"\|Україн' lectures/11-pandas-analytics/lecture-11.ipynb
```

Expected ≥ 3 occurrences:

- one in the groupby section (FR-013, FR-035)
- one in the Categorical section (FR-034, FR-035)
- one in the mini-project Part 1 (FR-019)

### 7. Verify no notes-api / FastAPI leakage

```bash
grep -i "fastapi\|sqlalchemy\|alembic\|postgres\|notes-api\|read_sql" lectures/11-pandas-analytics/lecture-11.ipynb
```

Expected: no matches. L11 is standalone (FR-027, FR-028, FR-029).

### 8. Verify no russian sources

```bash
grep -i "habr\|\.ru/\|ruby2ru\|pythonworld\.ru" lectures/11-pandas-analytics/lecture-11.ipynb
```

Expected: no matches (Constitution Principle I).

### 9. Verify no per-section time estimates

```bash
grep -E '\(~?[0-9]+\s*(хв|мин|min)\)' lectures/11-pandas-analytics/lecture-11.ipynb
```

Expected: no matches other than the mini-project header (which cites project-level durations, not per-notebook-section). Per Constitution v1.5.1.

### 10. Cleanup

The notebook leaves no persistent state. To clean up the executed copy:

```bash
rm /tmp/lecture-11-executed.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---|---|---|
| `FileNotFoundError: survey_results_public.csv` | CSV not downloaded or placed in wrong path | Re-read Step 2 of One-Time Setup |
| `ModuleNotFoundError: No module named 'pandas'` | pandas not installed in active environment | `pip install "pandas>=2.2,<3"` in the same env Jupyter uses |
| Memory error on `pd.read_csv` | Loading all columns on a low-RAM laptop | Confirm the cell uses `usecols=` (R3); only ~12 columns should load |
| `KeyError: 'LanguageHaveWorkedWith'` | 2025 column renamed (unlikely but possible) | Run `df.columns.tolist()` and update the constants cell; file an issue so the spec can be updated |
| Meme / diagram image missing | `assets/` subdirectory not copied | Re-clone or `git checkout -- lectures/11-pandas-analytics/assets/` |
| Notebook runs but takes > 5 min | Student loaded all columns or is on very old hardware | Ensure `usecols=` is used; close other apps; consider `low_memory=False` won't help but `dtype=` pre-assignment will |
