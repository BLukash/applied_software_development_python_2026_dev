# Lecture 12 — NumPy, Vectorization & a Logistic Regression Classifier from Scratch

This lecture is a **standalone** NumPy + from-scratch ML deep dive. It does **not** depend on the L6–L10 `notes-api` project (no FastAPI, no PostgreSQL, no SQLAlchemy, no Docker). It reuses (read-only) the Stack Overflow Developer Survey CSV from L11; that CSV is **required** to run the notebook end-to-end.

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

### 3. (Optional) Install scikit-learn for the comparison cell

The notebook includes one final "context" cell showing the same logistic-regression flow done with `sklearn.linear_model.LogisticRegression`. This cell is **gated behind a `try: import sklearn` block** — if sklearn is not installed, the cell prints a friendly skip message and the notebook continues without errors.

```bash
pip install scikit-learn   # optional
```

## What's inside

```text
lectures/12-numpy-ml/
├── README.md                  ← you are here
├── lecture-12.ipynb           ← the notebook (1.5-hour lesson)
├── artifacts/
│   └── .gitkeep               ← placeholder; the notebook writes model.npz here
└── assets/
    ├── memes/                 ← 2 memes used in the notebook
    └── diagrams/              ← logistic-regression flow diagram
```

The trained `model.npz` file produced when you run the notebook is `.gitignore`d, so your local copy will not be committed.

## Authoring environment

- The L11 CSV is reachable at `lectures/11-pandas-analytics/data/survey_results_public.csv`. The notebook fails fast with a `FileNotFoundError` if the file is missing.

## License notes

- The **Stack Overflow Annual Developer Survey 2025** dataset is distributed by Stack Overflow under the **Open Database License (ODbL)**. Attribution preserved in the notebook's References section.
- The course lecture content is part of the "Applied Software Development (Python) 2026" course materials.
