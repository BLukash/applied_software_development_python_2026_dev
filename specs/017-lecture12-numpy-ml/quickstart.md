# Quickstart: Lecture 12 — NumPy, Vectorization & a Logistic Regression Classifier from Scratch

**Feature**: 017-lecture12-numpy-ml
**Date**: 2026-04-30

## Prerequisites

- Python 3.13+
- Jupyter (notebook or lab) installed — either via `pip install jupyter` or the VS Code Jupyter extension
- pandas already installed from L11 (`pandas>=2.2,<3`)
- ~50 MB free disk space (NumPy install only; the L11 Survey CSV is reused, not duplicated)

**No prior project setup required.** This lecture is isolated from the L6–L10 notes-api project (per spec FR-032). No Docker, no PostgreSQL, no FastAPI, no scikit-learn at runtime.

## One-Time Setup

### 1. Install NumPy

```bash
pip install "numpy>=1.26,<3"
```

Or with uv:

```bash
uv add "numpy>=1.26,<3"
```

If pandas is already installed (from L11), a compatible NumPy is usually already present — check with `python -c "import numpy; print(numpy.__version__)"`. If the version is < 1.26, upgrade with the command above.

### 2. Reuse the L11 Stack Overflow Developer Survey CSV (REQUIRED)

The lecture reads the CSV that students already downloaded for L11 at:

```text
lectures/11-pandas-analytics/data/survey_results_public.csv
```

**This step is REQUIRED.** If the CSV is missing the data-loading cell raises `FileNotFoundError` and the rest of the notebook will not run. There is no synthetic-data fallback (removed on 2026-05-01).

To download it, follow the L11 setup instructions in [`lectures/11-pandas-analytics/README.md`](../../lectures/11-pandas-analytics/README.md#2-download-the-2025-stack-overflow-annual-developer-survey).

### 3. (Optional) Install scikit-learn for the comparison cell

The notebook includes one final cell showing the same logistic-regression flow done with `sklearn.linear_model.LogisticRegression` for context. This cell is **gated behind a `try: import sklearn` block** — if sklearn is not installed, the cell prints a friendly skip message and the notebook continues. To enable the comparison:

```bash
pip install scikit-learn
```

Or with uv:

```bash
uv add scikit-learn
```

## Verification Steps

### 1. Verify lecture directory structure

```bash
ls lectures/12-numpy-ml/
# Expected: lecture-12.ipynb  README.md  artifacts/  assets/
```

### 2. Verify NumPy install

```bash
python -c "import numpy; print(numpy.__version__)"
# Expected: 1.26.x or higher (and < 3.0)
```

### 3. Run the notebook end-to-end (Survey path)

If the L11 Survey CSV is in place:

```bash
jupyter nbconvert --to notebook --execute \
    lectures/12-numpy-ml/lecture-12.ipynb \
    --output /tmp/lecture-12-survey.ipynb
```

This should complete without a cell-execution error in under 90 seconds on a typical 8–16 GB laptop (SC-004). The notebook MUST print "Loaded N rows from .../survey_results_public.csv" near the start and a final-test accuracy in the 0.65–0.80 range.

### 4. Verify the missing-CSV failure mode

Temporarily rename the L11 CSV to confirm the notebook fails fast with a clear message (instead of silently degrading):

```bash
mv lectures/11-pandas-analytics/data/survey_results_public.csv \
   lectures/11-pandas-analytics/data/survey_results_public.csv.bak

jupyter nbconvert --to notebook --execute \
    lectures/12-numpy-ml/lecture-12.ipynb \
    --output /tmp/lecture-12-missing.ipynb

# (expected: nbconvert exits non-zero; the data-loading cell raises FileNotFoundError
#  with a message pointing at lectures/11-pandas-analytics/README.md)

# Restore the CSV
mv lectures/11-pandas-analytics/data/survey_results_public.csv.bak \
   lectures/11-pandas-analytics/data/survey_results_public.csv
```

### 5. Sanity-check the saved-model round-trip

After running the notebook, confirm the model artifact exists:

```bash
ls -la lectures/12-numpy-ml/artifacts/model.npz
# Expected: file exists, ~1 KB
```

Open the executed notebook. Verify the save / load round-trip cell printed `True` (or equivalent) for the `np.array_equal(predictions_before, predictions_after)` assertion.

### 6. Sanity-check the mini-project reference solutions

Open the executed notebook. Verify:

- **Part 1**: prints two `(num_countries,)` arrays that pass `np.allclose`, plus a `%timeit` table where vectorized is at least 5× faster.
- **Part 2**: prints accuracy in the documented range (0.65–0.80 Survey, 0.75–0.90 synthetic) and a 2×2 confusion matrix whose entries sum to `len(y_test)`.
- **Part 3** (collapsed at notebook end): renders a 2-row tidy table comparing `4_features` vs `5_features` on accuracy, precision, recall, plus a 3–5 sentence Ukrainian reflection.

### 7. Verify assets render

In the opened notebook, scroll to:

- Section 8 (`%timeit` performance) — meme 1 ("NumPy vs Python speed gap") should render.
- Section 12 (logistic regression math) — meme 2 ("LR is just sigmoid + cross-entropy") should render.
- Section 13 (gradient descent loop) OR Section 14 (evaluation) — the `lr-flow.png` diagram should render.

### 8. Verify no notes-api / FastAPI leakage

```bash
grep -i "fastapi\|sqlalchemy\|alembic\|postgres\|notes-api\|read_sql" lectures/12-numpy-ml/lecture-12.ipynb
```

Expected: no matches. L12 is standalone (FR-031, FR-032).

### 9. Verify sklearn coda is gated

```bash
grep -A2 "import sklearn" lectures/12-numpy-ml/lecture-12.ipynb
```

Expected: every `import sklearn` (or `from sklearn`) appears inside a `try:` block. The notebook MUST run end-to-end with sklearn uninstalled.

### 10. Verify no russian sources

```bash
grep -i "habr\|\.ru/\|pythonworld\.ru" lectures/12-numpy-ml/lecture-12.ipynb
```

Expected: no matches (Constitution Principle I).

### 11. Verify no per-section time estimates

```bash
grep -E '\(~?[0-9]+\s*(хв|мин|min)\)' lectures/12-numpy-ml/lecture-12.ipynb
```

Expected: no matches other than the mini-project header (which cites project-level durations, not per-notebook-section). Per Constitution v1.5.1.

### 12. Cleanup

The notebook leaves one persistent artifact (the `.npz` model file in `lectures/12-numpy-ml/artifacts/`). It is gitignored, so leaving it in place is fine. To clean up:

```bash
rm lectures/12-numpy-ml/artifacts/model.npz
rm /tmp/lecture-12-survey.ipynb /tmp/lecture-12-synth.ipynb
```

## Troubleshooting

| Symptom | Likely cause | Fix |
|---------|--------------|-----|
| `ModuleNotFoundError: No module named 'numpy'` | NumPy not installed in active environment | `pip install "numpy>=1.26,<3"` in the same env Jupyter uses |
| `ModuleNotFoundError: No module named 'pandas'` | pandas not installed (should already be present from L11) | `pip install "pandas>=2.2,<3"` |
| `FileNotFoundError: Survey CSV не знайдено за шляхом ...` | Survey CSV not at the L11 path | See Step 2 of One-Time Setup — download the L11 Survey CSV and place it at the documented path |
| Loss is `nan` after epoch ~50 | Sigmoid overflow OR features not standardized | Confirm Stage 2 (standardization) ran BEFORE Stage 3 (split) and BEFORE Stage 4 (training); confirm sigmoid uses the branch-on-sign stable form (R5) |
| Loss decreases then explodes | Learning rate too high | Reduce `LEARNING_RATE` from 0.1 to 0.01; or re-confirm features were standardized |
| Accuracy is suspiciously high (≥ 0.99) on Survey path | Data leakage — target column accidentally included in features | Confirm `X` does NOT include `ConvertedCompYearly`; only `years_code`, `work_exp`, `ed_level_ord`, `is_remote` |
| `KeyError: 'WorkExp'` or similar on the Survey path | 2025 column renamed (unlikely but possible) | Run `df.columns.tolist()`; update R3 column list and the spec; file an issue |
| sklearn coda cell errors instead of skipping | sklearn is partially installed (e.g., import works but a sub-import fails) | Either install fully (`pip install -U scikit-learn`) or uninstall (`pip uninstall scikit-learn`); the gate only catches `ImportError` on the top-level import |
| Notebook runs but takes > 90 seconds | Loading all CSV columns (without `usecols=`) OR very old hardware | Confirm Stage 0 uses `usecols=[...]` from data-model.md; close other apps |
| `model.npz` save fails with permission error | `lectures/12-numpy-ml/artifacts/` not writable | Check directory exists and is writable: `mkdir -p lectures/12-numpy-ml/artifacts && chmod u+w lectures/12-numpy-ml/artifacts` |
