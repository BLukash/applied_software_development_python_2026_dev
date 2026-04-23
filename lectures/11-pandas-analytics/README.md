# Lecture 11 — pandas Deep Dive on the Stack Overflow Developer Survey

This lecture is a **standalone** pandas deep dive. It does **not** depend on the L6–L10 `notes-api` project (no FastAPI, no PostgreSQL, no SQLAlchemy, no Docker).

## One-time setup

### 1. Install pandas

```bash
pip install "pandas>=2.2,<3"
```

Or, if you are using `uv`:

```bash
uv add "pandas>=2.2,<3"
```

That is the **only** new runtime dependency introduced by this lecture.

### 2. Download the 2025 Stack Overflow Annual Developer Survey

1. Open <https://survey.stackoverflow.co/>.
2. On the 2025 survey page (or the methodology page), click **"Download the full data set (CSV)"**.
3. You will get a ZIP archive (typically named `stack-overflow-developer-survey-2025.zip`, ~100 MB).
4. Extract it. The file you need is `survey_results_public.csv`.
5. Place `survey_results_public.csv` at:

   ```text
   lectures/11-pandas-analytics/data/survey_results_public.csv
   ```

The `data/` directory is already present in the repo (tracked via `.gitkeep`). `.csv` and `.zip` files inside `data/` are listed in the repository root `.gitignore`, so your local download will **not** be committed accidentally.

### Why is the download manual and not auto-fetched from the notebook?

Per feature spec FR-027, the notebook **must not** perform network calls during execution. Automating the download would:

- Break in offline-classroom scenarios.
- Hide the real "I need to find, download, and unzip a dataset" skill that every analyst exercises weekly.
- Introduce failure modes (firewall, proxy, rate limits, auth changes) that steal classroom time.

Manual download is a two-minute task and matches Stack Overflow's own public-access flow.

## What's inside

```text
lectures/11-pandas-analytics/
├── README.md                  ← you are here
├── lecture-11.ipynb           ← the notebook (1.5-hour lesson)
├── data/
│   └── .gitkeep               ← placeholder (you drop the Survey CSV here)
└── assets/
    ├── memes/                 ← 2 memes used in the notebook
    └── diagrams/              ← .explode() transformation schematic
```

## License notes

- The **Stack Overflow Annual Developer Survey 2025** dataset is distributed by Stack Overflow under the **Open Database License (ODbL)**. Attribution preserved in the notebook's References section.
- The course lecture content is part of the "Applied Software Development (Python) 2026" course materials.

## License / Download log

<!-- Populated during T006 notebook-authoring session. Update on re-download if a schema shift breaks the notebook. -->
- Downloaded on: 2026-04-23
- File size: ~134 MB (`survey_results_public.csv`, 49,191 rows × 172 columns)
- Source: <https://survey.stackoverflow.co/2025>
- Schema notes (caught during T007 verification on 2026-04-23): the 2025 schema **drops** `YearsCodePro` (use `WorkExp` as the professional-experience proxy), **pre-cleans** `YearsCode` to numeric, and uses **curly apostrophe** (`'`, U+2019) in `EdLevel` values. All three are handled in the notebook.
