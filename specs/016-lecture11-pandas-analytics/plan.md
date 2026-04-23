# Implementation Plan: Lecture 11 — pandas Deep Dive on the Stack Overflow Developer Survey

**Branch**: `016-lecture11-pandas-analytics` | **Date**: 2026-04-23 | **Spec**: [spec.md](spec.md)
**Input**: Feature specification from `/specs/016-lecture11-pandas-analytics/spec.md`

## Summary

Create a standalone Lecture 11 Jupyter notebook teaching a pandas deep dive anchored on the **2025 Stack Overflow Annual Developer Survey** (ODbL). The lecture is deliberately isolated from the L6–L10 notes-api project per the 2026-04-23 clarifications: no FastAPI, no PostgreSQL, no SQLAlchemy, no Docker. A single CSV is loaded, cleaned, sliced, grouped, merged, pivoted, and summarized across thirteen notebook sections, culminating in a three-part mini-project ("Developer Survey Insights") that runs Parts 1–2 in class (~25 min) and Part 3 as homework (~30–60 min). Intermediate pandas patterns — method chaining (`.pipe`/`.assign`), `.apply`/`.map`, and `Categorical` dtype — are covered per the "deep dive" clarification; MultiIndex, rolling/resample, and performance internals are explicitly out of scope. Ukraine is used as a selective running anchor in the `groupby` and `Categorical` sections and in mini-project Part 1; other sections stay global / multi-country.

## Technical Context

**Language/Version**: Python 3.13+ (code examples in Jupyter Notebook)
**Primary Dependencies**: pandas 2.2+ (the only new runtime dep); Jupyter (notebook / lab). `pyarrow` is implicitly pulled in by modern pandas for Arrow-backed strings, but students are not asked to think about it.
**Storage**: N/A — educational content; one local CSV file (`survey_results_public.csv` from the 2025 Survey ZIP) read at notebook runtime
**Testing**: `jupyter nbconvert --to notebook --execute` verifies the notebook runs end-to-end without cell errors (no pytest / unit tests — this is a notebook deliverable)
**Target Platform**: Jupyter Notebook / JupyterLab / VS Code notebook view on student laptops (Windows / macOS / Linux)
**Project Type**: Educational content (single Jupyter notebook + memes/diagrams under `lectures/11-pandas-analytics/`)
**Performance Goals**: Notebook runs top-to-bottom in under 5 minutes of wall-clock time on a typical 8-16 GB student laptop (SC-004)
**Constraints**: Lecture MUST fit 90 minutes; dataset not embedded in repo (students download Survey ZIP manually from survey.stackoverflow.co); no network calls during notebook execution; no secondary datasets beyond the pinned 2025 Survey CSV
**Scale/Scope**: 1 notebook, ~13 major sections + 3-part mini-project; target dataset size ~49K rows × ~90 columns (loaded subset via `usecols=` ≤ ~20 columns for demo cells)

## Constitution Check

| Gate | Status | Notes |
|------|--------|-------|
| Learning objectives at start | PASS | 3–5 outcomes per FR-001 covering fundamentals + intermediate topics |
| At least 5 runnable code examples | PASS | Easily exceeded: loading, cleaning, indexing, explode, groupby, merge, pivot, sort, chaining, apply, Categorical — 11+ dedicated example cells |
| At least 2 exercises with solutions | PASS | Mini-project FR-019 has 3 parts, all with solutions |
| At least 2 memes | PASS | FR-021 (min 2 memes), see data-model.md for placement |
| At least 1 diagram | PASS | FR-022 (min 1 diagram), see data-model.md for `.explode()` transformation schematic |
| Ukrainian text with English terms | PASS | FR-013 terminology rule |
| No per-section time estimates | PASS | Constitution v1.5.1 compliance — only the mini-project header mentions timing at the project-level, not per notebook section |
| Duration 1.5 hours | PASS | Topic budget targets ~90 min (FR-005) |
| Prerequisites section | PASS | References L1–L5 only, explicitly excludes L6–L10 (FR-002) |
| Summary + What's Next | PASS | Previews L12 (NumPy + ML) and L13 (visualization) per FR-003 |
| Mini-project (L5+ requirement) | PASS | "Developer Survey Insights" 3-part project restores constitution Principle II compliance (FR-019) |
| Only non-russian sources | PASS | Stack Overflow Developer Survey, official pandas docs (pandas.pydata.org), and Real Python / OWID links; zero russian-originated resources |

**Gate result**: ALL PASS. No constitution deviations requiring justification in Complexity Tracking.

## Project Structure

### Documentation (this feature)

```text
specs/016-lecture11-pandas-analytics/
├── plan.md                 # This file
├── research.md             # Phase 0 output
├── data-model.md           # Phase 1 output (notebook section map + DataFrame schema contracts)
├── contracts/
│   └── mini-project.md     # Grading rubric + expected output schemas for mini-project Parts 1–3
├── quickstart.md           # Phase 1 output (verification steps)
├── spec.md                 # Feature specification (already present)
└── checklists/
    └── requirements.md     # Quality checklist (already present)
```

### Source Code (repository root)

```text
lectures/
└── 11-pandas-analytics/                 # NEW directory
    ├── lecture-11.ipynb                 # NEW — the deliverable notebook
    ├── README.md                        # NEW — one-page student setup guide (dataset download + pip install pandas + where to put the CSV)
    ├── data/                            # NEW — .gitignore'd; students drop the Survey CSV here
    │   └── .gitkeep                     # NEW — placeholder so the empty dir is tracked
    └── assets/
        ├── memes/                       # NEW — at least 2 meme images
        └── diagrams/                    # NEW — at least 1 diagram (explode transformation schematic)
```

No changes to `project/notes-api/` or any other repository area. The spec's FR-028 / FR-029 explicitly forbid project-repository changes.

**Structure Decision**: Follow the established per-lecture directory convention (`lectures/NN-topic-slug/lecture-NN.ipynb`) observed in L5–L10. Add a `data/` subfolder to host the student-downloaded Survey CSV locally without committing it (CSV file added to `.gitignore`; only `.gitkeep` tracked). Add a lightweight `README.md` inside the lecture directory to document the two-step setup (install pandas; download + extract Survey ZIP) because FR-025 requires setup friction to be minimal but not automated.

## Complexity Tracking

> No violations detected. Single-notebook deliverable with no new services, no new dependencies beyond pandas, no cross-component wiring. Complexity is entirely pedagogical (getting the 1.5-hour flow right), not architectural.
