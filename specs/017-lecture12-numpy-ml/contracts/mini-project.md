# Mini-Project Contract: "Survey Salary Classifier"

**Feature**: 017-lecture12-numpy-ml
**Date**: 2026-04-30

This document defines the expected output shapes and grading rubric for the three-part mini-project (FR-023). The notebook's hidden solution cells (Parts 1–2) and the collapsed reference solution (Part 3) MUST conform to these contracts. All three parts use the same data path (Survey if available, synthetic fallback otherwise) and the same `np.random.default_rng(seed=42)` for reproducibility.

## Part 1 — In-class: Per-Country Mean Salary, For-Loop vs Vectorized

**Task statement (Ukrainian)**: "Дано два 1-D NumPy-масиви: `salaries` (річна компенсація, `float64`) та `country_codes` (цілі коди країн, `int64`), обидва довжиною `N`. Обчисліть середню зарплату для кожної країни **двома способами** — (a) звичайним `for`-циклом по унікальних кодах країн, (b) векторизовано через boolean masking. Переконайтеся, що результати співпадають (з точністю `np.allclose`), та порівняйте їхню швидкість через `%timeit`."

**Required techniques from earlier sections**: `np.unique`, boolean masking on a 1-D array, `arr.mean()`, `%timeit` magic, `np.allclose`.

**Expected output contract**:

```text
Two 1-D arrays of equal shape (num_countries,):
  loop_means:  np.ndarray, shape (num_countries,), dtype float64
  vec_means:   np.ndarray, shape (num_countries,), dtype float64

Both sorted by ascending country code (i.e., the i-th element corresponds to the i-th
unique country code in np.unique(country_codes)).

assert np.allclose(loop_means, vec_means)
```

Plus a printed `%timeit` result showing the vectorized version is at least 5× faster (typically 20–100× on the Survey-derived inputs).

Printed form (exemplar):

```text
For-loop:    24.3 ms ± 1.2 ms per loop
Vectorized:   0.41 ms ± 0.02 ms per loop
Speedup:     ~59×
```

**Acceptance**: Both arrays match to within `rtol=1e-9`, AND the vectorized timing is strictly less than the for-loop timing.

## Part 2 — In-class: Fit From-Scratch Logistic Regression on the Survey

**Task statement (Ukrainian)**: "Використовуючи код з основної частини лекції (стандартизація → train/test split → цикл градієнтного спуску → метрики), навчіть логістичну регресію на 4-ознаковому підмножині Survey з ціллю 'вище медіани компенсації по своїй країні'. Виведіть accuracy на тестовій вибірці та матрицю помилок розміром 2×2. Гіперпараметри: `lr=0.1`, `epochs=1000`, `seed=42`."

**Required techniques from earlier sections**: every prior cell from Stages 1–6 (load → engineer → standardize → split → train → evaluate).

**Expected output contract**:

```text
Two values printed:
  accuracy:           float in [0.60, 0.75]    (Survey path; empirically ≈0.64 on 2025 schema)
                      float in [0.75, 0.90]    (synthetic fallback path)
  confusion_matrix:   np.ndarray, shape (2, 2), dtype int64

Layout of confusion_matrix:
  [[TN, FP],
   [FN, TP]]
```

Printed form (exemplar):

```text
Accuracy on test:  0.71
Confusion matrix:
              pred=0   pred=1
  actual=0     2103     897
  actual=1      853    2147
```

**Acceptance**: With `seed=42`, the accuracy on the Survey path is reproducible and falls within the documented range. On the synthetic fallback, the accuracy MUST exceed 0.75 (the synthetic generator R4 plants a clean linear signal). Confusion matrix entries MUST sum to `len(y_test)`.

## Part 3 — Homework: Engineer One New Feature, Retrain, Compare

**Task statement (Ukrainian)**: "Додайте п'яту ознаку власного вибору: наприклад, бінарний прапорець `is_hybrid` (з `RemoteWork == 'Hybrid (some remote, some in-person)'`), або одну з топ-5 категорій `DevType` як 0/1 індикатор, або довжину `LanguageHaveWorkedWith` (кількість мов, які знає респондент). Перенавчіть логістичну регресію з тими самими гіперпараметрами та порівняйте обидві моделі за: (a) accuracy, (b) precision, (c) recall. Напишіть коментар українською (3–5 речень) про те, чи допомогла нова ознака — і чому ви так вважаєте."

**Required techniques**: column derivation in pandas/NumPy, re-running Stages 1.9–6 with `X.shape == (n, 5)`, computing precision and recall on both models, written reflection.

**Expected output contract**:

```text
A 2-row tidy DataFrame (or a small dict-of-arrays) with exactly these columns:
  model       str       (one of: "4_features", "5_features")
  accuracy    float64
  precision   float64
  recall      float64

Plus a markdown / text cell containing a 3–5 sentence Ukrainian-language reflection.
```

Exemplar (illustrative):

```text
        model     accuracy  precision   recall
  4_features        0.711      0.715    0.704
  5_features        0.718      0.722    0.711
```

Reflection MUST cite at least one specific number from the table.

**Reference solution placement**: End of notebook, inside a collapsed cell with a clear header "Еталонне рішення міні-проєкту (Частина 3)". Students are encouraged to attempt the task before expanding.

**Grading rubric (6 points total)**:

| Criterion | Points | What passes |
|-----------|--------|-------------|
| Correctness — feature is engineered without leakage, model retrained with same hyperparameters | 3 | New feature is derived only from input columns (not from the target); training uses `seed=42`, `lr=0.1`, `epochs=1000`; accuracy/precision/recall are within ±0.02 of reference |
| Clean vectorized code (no row-wise `for` loops; uses NumPy / pandas operations) | 2 | Feature derivation is one or two vectorized expressions; no explicit `for r in df.iterrows()` or equivalent |
| Reflection quality (Ukrainian, 3–5 sentences, references at least one number) | 1 | Reflection is in Ukrainian, falls within 3–5 sentences, names at least one number from the comparison table, and offers a non-trivial interpretation (not just "більше ознак — краще") |

Passing threshold: ≥ 4 / 6 points.

## Summary

| Part | Duration | Output type | Solution visibility |
|------|----------|-------------|---------------------|
| 1 | In-class 10–15 min | Two `(num_countries,)` arrays + %timeit ratio | Hidden cell below the task |
| 2 | In-class 10–15 min | Accuracy scalar + 2×2 confusion matrix | Hidden cell below the task |
| 3 | Homework 30–60 min | 2-row tidy DataFrame + UA reflection | Collapsed reference solution + rubric at notebook end |

## Reproducibility

All three parts MUST produce deterministic output across runs and across student machines, given the same data path. The `seed=42` constant is the single source of randomness for the train/test split (Stage 3) and the synthetic fallback (R4). On the Survey path, the median-split target derivation (R2) is also deterministic. On the synthetic path, the entire pipeline is deterministic from the seed.

## Out of Scope for the Mini-Project

The mini-project MUST NOT introduce: regularization (L1/L2), multi-class classification, k-fold cross-validation, hyperparameter search, or any external ML library beyond the optional sklearn coda from the lecture body. These belong to a future ML course; the homework reflection MAY mention them as "next steps" but MUST NOT implement them.
