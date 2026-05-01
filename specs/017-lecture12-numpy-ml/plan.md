# Implementation Plan: Lecture 12 — NumPy, Vectorization & a Logistic Regression Classifier from Scratch

**Branch**: `017-lecture12-numpy-ml` | **Date**: 2026-04-30 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/017-lecture12-numpy-ml/spec.md`

## Summary

Create a standalone Lecture 12 Jupyter notebook teaching two intertwined arcs: (a) NumPy fundamentals (ndarray, dtypes, indexing, broadcasting, vectorization habits with `%timeit`) and (b) a from-scratch binary **logistic regression classifier** trained on a small, prepared subset of the **2025 Stack Overflow Annual Developer Survey** CSV (the same file students already downloaded for L11). The lecture is deliberately isolated from the L6–L10 `notes-api` project per the L11 precedent: no FastAPI, no PostgreSQL, no SQLAlchemy, no Docker. The notebook ships a Survey-CSV-with-synthetic-fallback so it runs end-to-end in any environment, and a one-screen scikit-learn coda gated behind a `try: import sklearn` block (no sklearn runtime dependency). Mini-project "Survey Salary Classifier" runs Parts 1–2 in class (~25 min) and Part 3 as homework (~30–60 min). Deep-learning, regularization, multi-class, cross-validation, and matplotlib visualization are explicitly out of scope.

## Technical Context

**Language/Version**: Python 3.13+ (code examples in Jupyter Notebook)
**Primary Dependencies**: numpy >= 1.26 (the new runtime dep this lecture introduces); pandas >= 2.2 (already required from L11, used only as a one-cell black box for CSV loading); Jupyter (notebook / lab). `scikit-learn` is OPTIONAL — it is referenced ONLY in the gated `try: import sklearn` coda cell and MUST NOT be required to run the notebook.
**Storage**: N/A — educational content. The notebook reads the L11 Survey CSV (`lectures/11-pandas-analytics/data/survey_results_public.csv`) when present, and writes one transient `lectures/12-numpy-ml/artifacts/model.npz` as the save/load demo (gitignored).
**Testing**: `jupyter nbconvert --to notebook --execute` verifies the notebook runs end-to-end without cell errors against both paths (Survey CSV present AND missing → synthetic fallback). No formal pytest suite — this is a notebook deliverable.
**Target Platform**: Jupyter Notebook / JupyterLab / VS Code notebook view on student laptops (Windows / macOS / Linux)
**Project Type**: Educational content (single Jupyter notebook + memes/diagrams + transient model artifact under `lectures/12-numpy-ml/`)
**Performance Goals**: Notebook runs top-to-bottom in under 90 seconds of wall-clock time on a typical 8–16 GB student laptop (SC-004), including 1000-epoch gradient descent on the Survey subset (~30K rows × 4–6 features).
**Constraints**: Lecture MUST fit 90 minutes; Survey CSV is NOT re-downloaded (one-line pointer to L11 README); synthetic-fallback path MUST be loud (printed message); no network calls during notebook execution; no `notes-api` integration; sklearn-free runtime.
**Scale/Scope**: 1 notebook, ~14 major sections (Why-NumPy → ndarray → dtypes → indexing → broadcasting → ops → %timeit → ML dataset load → standardize → split → math → train loop → eval → save/load → sklearn coda) + 3-part mini-project; Survey training subset ≤ 30K rows × 4–6 features; trained model artifact ≤ 1 KB.

## Constitution Check

| Gate | Status | Notes |
|------|--------|-------|
| Learning objectives at start | PASS | 3–5 outcomes per FR-001 covering NumPy fundamentals + ML lifecycle |
| At least 5 runnable code examples | PASS | Easily exceeded: array construction, dtypes, indexing, broadcasting, ops, %timeit, dataset load, standardize, split, sigmoid, train loop, eval, save/load — 13+ dedicated example cells |
| At least 2 exercises with solutions | PASS | Mini-project FR-023 has 3 parts (vectorize, fit, engineer-feature), all with solutions |
| At least 2 memes | PASS | FR-025 (min 2 memes), see data-model.md for placement (NumPy-vs-Python speed gap; logistic-regression simplicity) |
| At least 1 diagram | PASS | FR-026 (min 1 diagram), see data-model.md — choice between broadcasting visual / LR flow / confusion matrix |
| Ukrainian text with English terms | PASS | FR-006 terminology rule (English ONLY for specific technical terms like "broadcasting", "sigmoid"; not for obvious phrases) |
| No per-section time estimates | PASS | Constitution v1.5.1 compliance — only the mini-project header may mention project-level durations, never per-section "(~10 хв)" |
| Duration 1.5 hours | PASS | Topic budget targets ~90 min (FR-005) |
| Prerequisites section | PASS | References L1–L5 + L11 only, explicitly excludes L6–L10 (FR-002) |
| Summary + What's Next | PASS | Previews L13 (matplotlib over the loss curve + decision boundary) and L14 (serving the saved `.npz` model) per FR-003 |
| Mini-project (L5+ requirement) | PASS | "Survey Salary Classifier" 3-part project satisfies constitution Principle II (FR-023) |
| Only non-russian sources | PASS | NumPy official docs (numpy.org), Stack Overflow Developer Survey, Andrew Ng Coursera ML lecture notes (English, free), scikit-learn LogisticRegression doc (optional reference); zero russian-originated resources |

**Gate result**: ALL PASS. No constitution deviations requiring justification in Complexity Tracking.

## Project Structure

### Documentation (this feature)

```text
specs/017-lecture12-numpy-ml/
├── plan.md                 # This file
├── research.md             # Phase 0 output
├── data-model.md           # Phase 1 output (notebook section map + array shape contracts + model artifact schema)
├── contracts/
│   └── mini-project.md     # Grading rubric + expected output shapes for mini-project Parts 1–3
├── quickstart.md           # Phase 1 output (verification steps)
├── spec.md                 # Feature specification (already present)
└── checklists/
    └── requirements.md     # Quality checklist (already present)
```

### Source Code (repository root)

```text
lectures/
└── 12-numpy-ml/                       # NEW directory
    ├── lecture-12.ipynb               # NEW — the deliverable notebook
    ├── README.md                      # NEW — one-page student setup guide (pip install numpy; pointer to L11 README for Survey CSV)
    ├── artifacts/                     # NEW — .gitignore'd; transient model.npz lives here after notebook runs
    │   └── .gitkeep                   # NEW — placeholder so the empty dir is tracked
    └── assets/
        ├── memes/                     # NEW — at least 2 meme images
        └── diagrams/                  # NEW — at least 1 diagram (broadcasting OR LR flow OR confusion matrix)
```

No changes to `project/notes-api/` or to `lectures/11-pandas-analytics/` or any other repository area. The spec's FR-032 explicitly forbids project-repository changes; the spec's FR-028 reuses (does not modify) the L11 dataset download.

**Structure Decision**: Follow the established per-lecture directory convention (`lectures/NN-topic-slug/lecture-NN.ipynb`) observed in L5–L11. Add an `artifacts/` subfolder to host the student-generated `.npz` model file locally without committing it (`.npz` files added to `.gitignore`; only `.gitkeep` tracked). Add a lightweight `README.md` inside the lecture directory documenting the two-step setup (install numpy; reuse L11 Survey CSV OR rely on synthetic fallback) — symmetric with the L11 README pattern.

## Complexity Tracking

> No violations detected. Single-notebook deliverable with no new services, no new infrastructure, one new dependency (numpy) and one optional dev-only reference (sklearn). Complexity is entirely pedagogical (sequencing the NumPy → ML arc so gradient descent feels inevitable rather than mysterious), not architectural.
