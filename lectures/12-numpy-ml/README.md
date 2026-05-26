# Lecture 12 — NumPy & Vectorization on Real Data

This lecture is a **standalone** NumPy deep dive applied to real-world data. It does **not** depend on the L6–L10 `notes-api` project (no FastAPI, no PostgreSQL, no SQLAlchemy, no Docker). It reuses (read-only) the Stack Overflow Developer Survey CSV from L11; that CSV is **required** to run the notebook end-to-end.

> **No machine learning here.** Gradient descent, loss-minimization, classification metrics and `scikit-learn` are intentionally absent — those belong to next year's ML course. Today's focus is **NumPy as a tool**: indexing, broadcasting, vectorized statistics, group aggregations, top-K, loss-function formulas, and pairwise distances.

## One-time setup

### 1. Install NumPy

```bash
pip install "numpy>=1.26,<3"
```

Or, if you are using `uv`:

```bash
uv add "numpy>=1.26,<3"
```

That is the **only** new runtime dependency introduced by this lecture. (`pandas>=2.2` is already required from L11.)

### 2. Reuse the L11 Stack Overflow Developer Survey CSV (REQUIRED)

The lecture reads the CSV that students already downloaded for L11 at:

```text
lectures/11-pandas-analytics/data/survey_results_public.csv
```

**This step is REQUIRED.** If the CSV is missing, the data-loading cell raises a `FileNotFoundError` with the exact path it expected and a pointer back here.

To download it, follow the L11 setup instructions in [`../11-pandas-analytics/README.md`](../11-pandas-analytics/README.md).

## What's inside

```text
lectures/12-numpy-ml/
├── README.md                  ← you are here
└── lecture-12.ipynb           ← the notebook
```

## Authoring environment

- The L11 CSV is reachable at `lectures/11-pandas-analytics/data/survey_results_public.csv`. The notebook fails fast with a `FileNotFoundError` if the file is missing.

## License notes

- The **Stack Overflow Annual Developer Survey 2025** dataset is distributed by Stack Overflow under the **Open Database License (ODbL)**. Attribution preserved in the notebook's References section.
- The course lecture content is part of the "Applied Software Development (Python) 2026" course materials.
