# Data Model: Lecture 12 — NumPy, Vectorization & a Logistic Regression Classifier from Scratch

**Feature**: 017-lecture12-numpy-ml
**Date**: 2026-04-30

This lecture has no persisted entities in the traditional sense. The "data model" here is (a) the array-shape contract at each stage of the ML pipeline, (b) the saved-model file schema, and (c) the notebook section map.

## Array Shape Contracts (Pipeline Stages)

### Stage 0 — Raw Survey Load (or synthetic fallback)

The notebook loads either the L11 Survey CSV OR the synthetic fallback into a single pandas DataFrame `df_raw`.

**Survey path** (when `lectures/11-pandas-analytics/data/survey_results_public.csv` exists):

```python
df_raw = pd.read_csv(
    SURVEY_CSV_PATH,
    usecols=["ResponseId", "Country", "YearsCode", "WorkExp",
             "EdLevel", "RemoteWork", "ConvertedCompYearly"],
)
# df_raw.shape ≈ (49191, 7) on the 2025 Survey
```

**Synthetic path** (when CSV is missing):

```python
N_SYNTH, P_SYNTH = 5000, 4
rng = np.random.default_rng(seed=42)
X_synth = rng.standard_normal((N_SYNTH, P_SYNTH))
true_w = np.array([1.5, -1.0, 0.8, 0.3])
true_b = -0.5
logits = X_synth @ true_w + true_b
probs = 1.0 / (1.0 + np.exp(-logits))
y_synth = (rng.uniform(size=N_SYNTH) < probs).astype(int)
# X_synth.shape == (5000, 4); y_synth.shape == (5000,)
```

The path taken MUST be printed clearly: `print(f"Loaded {len(df_raw)} rows from {data_path}")` for the Survey path, `print("Survey CSV not found at <path>; using synthetic data instead.")` for the fallback.

### Stage 1 — Feature engineering & target derivation (Survey path only)

| Step | Operation | Result shape |
|------|-----------|--------------|
| 1.1 | Drop rows with `Country.isna()` or `ConvertedCompYearly.isna()` | `df.shape ≈ (23947, 7)` (verified on 2025 CSV) |
| 1.2 | Compute `country_median = df.groupby("Country")["ConvertedCompYearly"].transform("median")` | `(23947,)` series |
| 1.3 | Set `y = (df["ConvertedCompYearly"] > country_median).astype(int).to_numpy()` | `y.shape == (23947,)`; `y.mean() ≈ 0.486` (per-country median makes it near-balanced) |
| 1.4 | Build `years_code = df["YearsCode"].to_numpy()` (already float64 in 2025) | `(23947,)` |
| 1.5 | Build `work_exp = df["WorkExp"].to_numpy()` (already float64 in 2025) | `(23947,)` |
| 1.6 | Map `EdLevel` via lookup dict → `ed_level_ord` (float). Real 2025 values use **curly apostrophe** (U+2019) in `"Bachelor’s degree …"` and `"Master’s degree …"` — the lookup dict must use the curly form. The 2025 schema also includes `"Other (please specify):"` (mapped to `2.5`); the pre-2025 `"Something else"` value is absent. | `(23947,)` |
| 1.7 | Build `is_remote = (df["RemoteWork"] == "Remote").astype(int).to_numpy()`. Note 2025 also has two `"Hybrid (...)"` variants and `"Your choice (very flexible…)"` — the binary flag treats all of these as `0`. | `(23947,)` |
| 1.8 | Drop rows where any of `years_code`, `work_exp`, `ed_level_ord` is `NaN` | `(23177,)` (verified on 2025 CSV) |
| 1.9 | Stack into `X = np.column_stack([years_code, work_exp, ed_level_ord, is_remote])` | `X.shape == (23177, 4)` |
| 1.10 | Filter `y` to the same surviving rows | `y.shape == (23177,)`; `y.mean() ≈ 0.497` |

Both paths converge on a uniform `X.shape = (n, 4)`, `y.shape = (n,)`, `dtype=float64` for `X` and `int64` for `y`.

### Stage 2 — Standardization (FR-016)

Z-score standardization computed from the **training set only** (no data leakage):

```python
feature_mean = X_train.mean(axis=0)              # shape (4,)
feature_std  = X_train.std(axis=0, ddof=0)       # shape (4,)
X_train_std  = (X_train - feature_mean) / feature_std   # shape (n_train, 4)
X_test_std   = (X_test  - feature_mean) / feature_std   # shape (n_test, 4)
```

Both `feature_mean` and `feature_std` are saved to the model artifact (Stage 5).

### Stage 3 — Train/test split (FR-017)

```python
rng_split = np.random.default_rng(seed=42)
perm = rng_split.permutation(n)                  # shape (n,)
n_train = int(0.8 * n)
train_idx, test_idx = perm[:n_train], perm[n_train:]
X_train, X_test = X[train_idx], X[test_idx]
y_train, y_test = y[train_idx], y[test_idx]
```

Survey path actual (2025): `n_train = 18541`, `n_test = 4636`.
Synthetic path: `n_train = 4000`, `n_test = 1000`.

### Stage 4 — Trained parameters (FR-019)

After 1000 epochs of gradient descent at learning rate 0.1:

| Parameter | Shape | dtype | Notes |
|-----------|-------|-------|-------|
| `w` | `(4,)` | float64 | Weight vector — converged via gradient descent |
| `b` | scalar | float64 | Bias — `np.float64` scalar, NOT a `(1,)` array |
| `loss_history` | `(1000,)` or `(11,)` if subsampled | float64 | Loss values per epoch (or every 100 epochs) |

### Stage 5 — Saved model artifact (FR-021)

Single file: `lectures/12-numpy-ml/artifacts/model.npz` (gitignored). Contents:

| Array name | Shape | dtype | Source |
|------------|-------|-------|--------|
| `w` | `(4,)` | float64 | Trained weights from Stage 4 |
| `b` | scalar | float64 | Trained bias from Stage 4 |
| `feature_mean` | `(4,)` | float64 | Per-feature mean from Stage 2 |
| `feature_std` | `(4,)` | float64 | Per-feature std from Stage 2 |

Save / load round-trip:

```python
np.savez(ARTIFACT_PATH, w=w, b=b, feature_mean=feature_mean, feature_std=feature_std)
loaded = np.load(ARTIFACT_PATH, allow_pickle=False)
w_r, b_r, m_r, s_r = loaded["w"], loaded["b"], loaded["feature_mean"], loaded["feature_std"]
assert np.array_equal(predict(X_test, w, b, feature_mean, feature_std),
                      predict(X_test, w_r, b_r, m_r, s_r))
```

`allow_pickle=False` is the explicit default per FR-021.

### Stage 6 — Evaluation outputs (FR-020)

The evaluation section produces four scalar metrics from `y_true` and `y_pred`:

| Metric | Formula (NumPy) | Expected range (Survey path) |
|--------|-----------------|------------------------------|
| accuracy | `(y_pred == y_true).mean()` | 0.60–0.75 (empirically ≈0.64 on 2025 schema) |
| precision | `(tp / (tp + fp))` where `tp = ((y_pred == 1) & (y_true == 1)).sum()` | 0.60–0.75 |
| recall | `(tp / (tp + fn))` where `fn = ((y_pred == 0) & (y_true == 1)).sum()` | 0.55–0.75 |
| confusion matrix | `np.array([[tn, fp], [fn, tp]])`, shape `(2, 2)` | depends on data |

All four implemented from raw boolean array operations — no scikit-learn.

## Notebook Section Map

| # | Section (Ukrainian title) | FR coverage | Notes |
|---|---------------------------|-------------|-------|
| 0 | Header + Prerequisites | FR-002 | Lists L1–L5 + L11 only; explicitly excludes L6–L10 |
| 1 | Цілі заняття (Learning Objectives) | FR-001 | 3–5 outcomes |
| 2 | Чому NumPy швидкий? | FR-007 | Contiguous memory + dtypes + C/SIMD dispatch |
| 3 | Основи ndarray: створення та властивості | FR-008 | `np.array`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`, `default_rng().standard_normal`; `.shape`, `.dtype`, `.ndim`, `.size`, `.nbytes` |
| 4 | dtype: int32 vs int64 vs float32 vs float64 | FR-009 | `.astype()`; memory vs precision tradeoff |
| 5 | Індексація та зрізи: view vs copy | FR-010 | basic slicing, fancy indexing, boolean masking; "modify a view, see the original change" demo |
| 6 | Broadcasting: правила + приклади | FR-011 | 3 broadcasting examples + 1 ValueError example |
| 7 | Поелементні, редукційні та лінійно-алгебраїчні операції | FR-012 | `np.exp`, `np.log`, `np.sqrt`, `np.maximum`, `.sum(axis=)`, `.mean(axis=)`, `.std`, `.argmax`, `np.dot`, `@` |
| 8 | Швидкість: %timeit Python vs NumPy | FR-013 | 1M-element list comprehension vs `arr ** 2`; one "vectorization loses on tiny input" counter-example |
| 9 | Перехід до ML: завантаження даних з Survey (або синтетика) | FR-014 | `pd.read_csv` 1-cell black box; loud printed branch; matching synthetic path |
| 10 | Стандартизація: чому, як, без витоку даних | FR-016 | z-score from train-set only; broadcast to test set |
| 11 | Поділ train/test без sklearn | FR-017 | `default_rng(seed=42).permutation(n)` |
| 12 | Логістична регресія: математика | FR-018 | sigmoid (numerically stable), model `ŷ = σ(X @ w + b)`, BCE loss |
| 13 | Цикл градієнтного спуску | FR-019 | analytic gradient, 1000 epochs, lr=0.1, print every 100 |
| 14 | Метрики: accuracy, precision, recall, confusion matrix | FR-020 | from-scratch NumPy; "why accuracy lies" demo |
| 15 | Збереження та завантаження моделі (.npz) | FR-021 | `np.savez` + `np.load(allow_pickle=False)`; round-trip verification |
| 16 | scikit-learn для контексту: 5 рядків | FR-022 | `try: import sklearn` gated; print acknowledges absence gracefully |
| 17 | Міні-проєкт "Survey Salary Classifier" (3 частини) | FR-023, FR-037 | Part 1 in-class, Part 2 in-class, Part 3 homework |
| 18 | Підсумок (Summary) | FR-003, FR-038 | One-line callout: "logistic regression is the simplest neural network" |
| 19 | Джерела (References) | R14 | numpy.org, survey.stackoverflow.co, Andrew Ng, McKinney, sklearn docs, 3Blue1Brown |
| 20 | Що далі? (Preview of L13, L14) | FR-003 | L13 plots loss curve + decision boundary; L14 serves the .npz model |

## Mini-Project Structure (FR-023)

| Part | When | Time | Task | Hidden solution? |
|------|------|------|------|------------------|
| 1 | In-class | ~10–15 min | Per-country mean salary: for-loop vs vectorized boolean masking + `%timeit` benchmark | Hidden solution cell |
| 2 | In-class | ~10–15 min | Fit from-scratch LR on the 4-feature Survey subset (or synthetic); report accuracy + confusion matrix | Hidden solution cell |
| 3 | Homework | ~30–60 min | Engineer one new feature; retrain; compare accuracy AND precision/recall; 3–5 sentence Ukrainian reflection | Reference solution collapsed at notebook end + grading rubric |

## Asset Inventory

| Asset | Path | Source | Licensing |
|-------|------|--------|-----------|
| Survey CSV (reused, not duplicated) | `lectures/11-pandas-analytics/data/survey_results_public.csv` | Student download from L11 (survey.stackoverflow.co) | ODbL (not committed to repo) |
| Trained model (transient, gitignored) | `lectures/12-numpy-ml/artifacts/model.npz` | Generated by notebook | n/a — not committed |
| Meme 1 | `lectures/12-numpy-ml/assets/memes/numpy-vs-python-speed.png` | Generic meme template (e.g. Drake / expanding-brain) | Public-domain meme template |
| Meme 2 | `lectures/12-numpy-ml/assets/memes/lr-is-just-sigmoid.png` | Generic meme template | Public-domain meme template |
| Diagram | `lectures/12-numpy-ml/assets/diagrams/lr-flow.png` | Hand-rendered with matplotlib / draw.io | Original work for this lecture |

## File Change Map

| File | Action |
|------|--------|
| `lectures/12-numpy-ml/lecture-12.ipynb` | CREATE |
| `lectures/12-numpy-ml/README.md` | CREATE (one-page setup: install numpy, pointer to L11 README for Survey CSV, note that synthetic fallback exists) |
| `lectures/12-numpy-ml/artifacts/.gitkeep` | CREATE (placeholder; `.npz` files inside are gitignored) |
| `lectures/12-numpy-ml/assets/memes/numpy-vs-python-speed.png` | CREATE |
| `lectures/12-numpy-ml/assets/memes/lr-is-just-sigmoid.png` | CREATE |
| `lectures/12-numpy-ml/assets/diagrams/lr-flow.png` | CREATE |
| `.gitignore` | MODIFY (append `lectures/12-numpy-ml/artifacts/*.npz`) |
| `README.md` (repo root) | MODIFY (append L12 entry to the lectures index, mirroring L11's entry style) |

No changes to `project/notes-api/` per FR-032; no changes to `lectures/11-pandas-analytics/` (the Survey CSV is read but not modified).
