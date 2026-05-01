# Tasks: Lecture 12 — NumPy, Vectorization & a Logistic Regression Classifier from Scratch

**Input**: Design documents from `/specs/017-lecture12-numpy-ml/`
**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/mini-project.md, quickstart.md

**Tests**: Not explicitly requested — this is a pedagogical notebook deliverable (not runtime software). The closest equivalent is executing the notebook end-to-end via `jupyter nbconvert --execute` on **both** the Survey-CSV-present and Survey-CSV-missing (synthetic fallback) paths, captured in Polish phase tasks.

**Organization**: Sequential pipeline. Setup creates the directory skeleton and the lecture-level README. Foundational tasks lock down NumPy, verify the L11 Survey CSV is reachable (or document the synthetic-fallback path explicitly), and produce the two memes plus the LR-flow diagram. User Story 1 authors the entire teaching narrative — both the NumPy arc and the from-scratch ML arc — into a single `.ipynb` (one editor, no parallelism within). User Story 2 appends the three-part mini-project. Polish runs the dual-path nbconvert smoke tests plus the standard scope/source/time-estimate greps.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1, US2)
- Include exact repo-relative file paths in descriptions

## Path Conventions

All notebook and asset paths are relative to the repository root `d:/applied_software_development_python_2026/`. No `src/` / `tests/` — this is a content deliverable.

---

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Create the lecture directory layout and the tiny placeholder / config files needed before any content authoring can begin.

- [X] T001 Create lecture directory skeleton: `lectures/12-numpy-ml/`, `lectures/12-numpy-ml/artifacts/`, `lectures/12-numpy-ml/assets/memes/`, `lectures/12-numpy-ml/assets/diagrams/`
- [X] T002 [P] Create empty placeholder `lectures/12-numpy-ml/artifacts/.gitkeep` so the otherwise-empty `artifacts/` directory is tracked
- [X] T003 [P] Append `lectures/12-numpy-ml/artifacts/*.npz` to the repository root `.gitignore` so the student-generated trained-model file is never committed (ref: plan.md Project Structure; data-model.md Stage 5)
- [X] T004 [P] Author student-facing setup guide at `lectures/12-numpy-ml/README.md` covering: (1) `pip install "numpy>=1.26,<3"` (or `uv add ...`), (2) optional `pip install scikit-learn` for the gated comparison cell, (3) a one-line pointer to `lectures/11-pandas-analytics/README.md` for downloading the Survey CSV, (4) explicit "the synthetic-data fallback runs end-to-end without the CSV — the lesson works either way" paragraph (ref: research.md R1, R8, R12; quickstart.md One-Time Setup)
- [X] T005 [P] Append a Lecture 12 entry to the repository-root `README.md` lectures index, mirroring the style of the existing L11 entry (one heading link to `lectures/12-numpy-ml/lecture-12.ipynb` plus a 10–14 line bulleted topic summary derived from spec.md FR-001 + spec.md User Story 1) (ref: data-model.md File Change Map)
- [X] T006 Verify `numpy>=1.26,<3` installs cleanly in the notebook authoring environment: run `python -c "import numpy; print(numpy.__version__)"` and confirm the printed version satisfies the pin (ref: research.md R8)

**Checkpoint**: Directory layout exists, `.gitignore` is updated, student-setup README is in place, repo README links to L12, NumPy is installable. No notebook yet.

---

## Phase 2: Foundational (Dataset + Assets Lockdown)

**Purpose**: Confirm the L11 Survey CSV is reachable from the L12 notebook (or explicitly document running on the synthetic-fallback path), pre-flight the Stage-1 feature engineering against the actual 2025 schema (so authoring doesn't hit `KeyError` mid-section), and produce the two meme images and the LR-flow diagram that the notebook will embed. These MUST complete before User Story 1 content authoring because multiple sections reference these exact columns and assets.

**⚠️ CRITICAL**: No User Story work can begin until this phase is complete.

- [X] T007 Verify the L11 Survey CSV is present at `lectures/11-pandas-analytics/data/survey_results_public.csv`. If MISSING: do NOT re-download — instead, set the L12 authoring environment to exercise the synthetic-fallback path (the notebook MUST work on both paths anyway). If PRESENT: proceed and use the real-data path for authoring. Record which path is active in a one-line note in `lectures/12-numpy-ml/README.md` under a "Authoring environment" section. (ref: research.md R1; spec.md FR-028, FR-029; quickstart.md Step 4)
- [X] T008 Pre-flight feature engineering: in a temporary Python REPL, run the data-model.md Stage 1 pipeline (load with `usecols=["ResponseId", "Country", "YearsCode", "WorkExp", "EdLevel", "RemoteWork", "ConvertedCompYearly"]`, drop NaN target/country, compute per-country median, build `y`, build the four features, drop NaN rows). Confirm: (a) every column in the `usecols` list exists in the 2025 CSV, (b) `EdLevel` unique values match the R3 ordinal lookup keys (account for U+2019 curly apostrophe per L11's T007 finding), (c) final `X.shape[0]` is in `[20000, 35000]`, (d) `y` is roughly balanced (`y.mean() ∈ [0.4, 0.6]`). If ANY check fails, update `specs/017-lecture12-numpy-ml/data-model.md` Stage 1 table AND `specs/017-lecture12-numpy-ml/research.md` R3 to match the actual 2025 schema before authoring (ref: research.md R3; data-model.md Stage 1; spec.md FR-014, FR-015). **Skip this task** if T007 selected the synthetic-fallback authoring path — note "skipped: synthetic authoring path" in the README.
- [X] T009 [P] Create the LR-flow diagram at `lectures/12-numpy-ml/assets/diagrams/lr-flow.png` per research.md R9. Boxes/arrows: `X (n,p) → z = X@w + b → ŷ = σ(z) → L = BCE(y, ŷ)` with a feedback arrow showing `gradient ∂L/∂{w,b}` flowing back to update `(w, b)`. Render via a small matplotlib script committed as `lectures/12-numpy-ml/assets/diagrams/_build_lr_flow.py` so the diagram is reproducible (mirror the L11 `_build_explode_diagram.py` pattern). Include Ukrainian alt-text in the markdown cell that will embed it (ref: research.md R9; spec.md FR-026)
- [X] T010 [P] Place two memes at `lectures/12-numpy-ml/assets/memes/numpy-vs-python-speed.png` and `lectures/12-numpy-ml/assets/memes/lr-is-just-sigmoid.png`. Sources MUST be generic meme templates (no russian text, no copyrighted characters beyond standard meme-culture imagery). Document source template + authorship/license in a new `lectures/12-numpy-ml/assets/memes/CREDITS.md` (mirror the L11 CREDITS.md format) (ref: research.md R10; spec.md FR-025)

**Checkpoint**: Authoring path is decided (Survey CSV or synthetic), the data-model.md Stage 1 column list is verified or updated, diagram and memes are committed. Content authoring can now begin.

---

## Phase 3: User Story 1 — Lecture Notebook: NumPy + Vectorization + Logistic Regression from Scratch (Priority: P1) 🎯 MVP

**Goal**: Author the complete 1.5-hour teaching narrative as a single Jupyter notebook with all 17 teaching sections (Why-NumPy → ndarray → dtypes → indexing → broadcasting → ops → %timeit → ML dataset load → standardize → split → math → train loop → eval → save/load → sklearn coda → summary → references → what's next), all memes and the diagram embedded, every FR-required example, every acceptance scenario covered, and an end-to-end execution pass on the active authoring path.

**Independent Test**: `jupyter nbconvert --to notebook --execute lectures/12-numpy-ml/lecture-12.ipynb --output /tmp/us1-check.ipynb` completes in under 90 seconds with zero cell errors on an 8–16 GB laptop with `numpy>=1.26` and `pandas>=2.2` installed (sklearn NOT required). Notebook works on BOTH paths: with the L11 Survey CSV present (real-data) AND with it absent (synthetic fallback). Every structural element (learning objectives, memes, diagram, sklearn-coda gate, summary, references, what's next) renders correctly. (ref: spec.md User Story 1 Independent Test; SC-004, SC-005)

**Note on parallelism**: All T011–T029 tasks edit the same `lecture-12.ipynb` file and MUST run sequentially. No `[P]` markers inside this phase.

### Implementation for User Story 1

- [X] T011 [US1] Create the notebook skeleton at `lectures/12-numpy-ml/lecture-12.ipynb` — a new empty Jupyter notebook containing just: the Ukrainian-language header cell (Lecture 12 title, date, prerequisites referencing L1–L5 plus L11 only per FR-002, and 3–5 learning objectives per FR-001), a constants cell pinning `SURVEY_CSV_PATH = Path("lectures/11-pandas-analytics/data/survey_results_public.csv")`, `SEED = 42`, `LEARNING_RATE = 0.1`, `EPOCHS = 1000`, `PRINT_EVERY = 100`, `ARTIFACT_PATH = Path("lectures/12-numpy-ml/artifacts/model.npz")`, an environment-check cell that imports numpy/pandas and prints versions, and stub markdown cells for every section in data-model.md's Notebook Section Map (sections 0 through 20) — each stub is a single markdown cell with only the section title, empty body. This locks the section ordering before any content is written. Consider mirroring L11's `_build_notebook.py` generator pattern for reproducibility (ref: data-model.md Notebook Section Map; spec.md FR-001, FR-002, FR-005)
- [X] T012 [US1] Author Section 2 "Чому NumPy швидкий?" in `lecture-12.ipynb` — plain-Ukrainian explanation (no code) of contiguous-memory layout, fixed dtypes, and dispatch to compiled C/SIMD loops as the three reasons NumPy outpaces a Python list. One short markdown paragraph per reason. End with a one-sentence teaser of the `%timeit` benchmark coming in Section 8 (ref: spec.md FR-007; Acceptance Scenario 2)
- [X] T013 [US1] Author Section 3 "Основи ndarray: створення та властивості" in `lecture-12.ipynb` — one code cell per construction function: `np.array(list)`, `np.zeros((m, n))`, `np.ones(p)`, `np.arange(start, stop, step)`, `np.linspace(start, stop, num)`, `np.random.default_rng(seed=42).standard_normal((m, n))`. Follow with one inspection cell printing `.shape`, `.dtype`, `.ndim`, `.size`, `.nbytes` for at least one 2-D array. Total ≤ 7 code cells (ref: spec.md FR-008; Acceptance Scenario 3)
- [X] T014 [US1] Author Section 4 "dtype: int32 vs int64 vs float32 vs float64" in `lecture-12.ipynb` — one cell creating an `int64` array and `.astype(np.int32)`-ing it, printing the `nbytes` before/after; one cell doing the same for `float64 → float32`; one short markdown paragraph on memory vs precision tradeoffs (when to downcast: large arrays, GPU prep; when not: financial calculations) (ref: spec.md FR-009; Acceptance Scenario 4)
- [X] T015 [US1] Author Section 5 "Індексація та зрізи: view vs copy" in `lecture-12.ipynb` — basic 1-D and 2-D slicing (`arr[1:4]`, `arr[1:4, ::2]`), fancy indexing with an integer array (`arr[[0, 2, 5]]`), boolean masking (`arr[arr > 0]`), and a short "modify a view, see the original change" cell (e.g., `view = arr[1:4]; view[0] = -999; print(arr)`). Close with a one-line summary stating: "basic slicing returns a view, fancy/boolean indexing returns a copy" (ref: spec.md FR-010; Acceptance Scenario 5; Edge Case "view vs copy")
- [X] T016 [US1] Author Section 6 "Broadcasting: правила + приклади" in `lecture-12.ipynb` — markdown cell stating the broadcasting rules in plain Ukrainian, then three code cells showing successful broadcasts: `(3, 4) + (4,) → (3, 4)`, `(3, 1) + (1, 4) → (3, 4)`, `(5,) + scalar → (5,)`. Then ONE cell intentionally triggering a failure: `(3, 4) + np.zeros(3) → ValueError`, captured via `try / except` so the notebook still runs end-to-end. Include the LR-flow diagram embed AT THE START of this section is INCORRECT — the diagram belongs in Section 12/13 (ref: spec.md FR-011; Acceptance Scenario 6; research.md R9)
- [X] T017 [US1] Author Section 7 "Поелементні, редукційні та лінійно-алгебраїчні операції" in `lecture-12.ipynb` — one cell each for: `np.exp / np.log / np.sqrt / np.maximum` on a sample 1-D array; reductions `arr.sum(axis=0)` vs `arr.sum(axis=1)` on a `(3, 4)` array (with a markdown explaining "axis=0 is along rows-axis, collapsing rows; axis=1 is along columns-axis, collapsing columns"); `arr.mean(axis=...)`, `arr.std`, `arr.argmax`; the equivalence `np.dot(a, b) == a @ b` for 1-D and 2-D operands (with the explicit "prefer `@` for matrix-multiply readability" note). Address Edge Case "np.dot vs @ shape divergence" with one short markdown line (ref: spec.md FR-012; Acceptance Scenario 7; Edge Case "np.dot vs @")
- [X] T018 [US1] Author Section 8 "Швидкість: %timeit Python vs NumPy" in `lecture-12.ipynb` — embed `lectures/12-numpy-ml/assets/memes/numpy-vs-python-speed.png` at section start with Ukrainian alt-text. Then one cell: `data = list(range(1_000_000)); %timeit [x * x for x in data]`. Then one cell: `arr = np.arange(1_000_000); %timeit arr ** 2`. Then a markdown paragraph explaining the ~100×–500× ratio in plain Ukrainian (loop overhead, dispatch to C, cache friendliness). Finally one "vectorization loses on tiny input" counter-example: `tiny = np.arange(3); %timeit tiny ** 2` vs `%timeit [x * x for x in [0, 1, 2]]` — Python wins or ties because of NumPy's per-call overhead. End with the takeaway "vectorize when it's natural, not religiously" (ref: spec.md FR-013, FR-025; research.md R10; Acceptance Scenario 8)
- [X] T019 [US1] Author Section 9 "Перехід до ML: завантаження даних з Survey (або синтетика)" in `lecture-12.ipynb` — embed `lectures/12-numpy-ml/assets/memes/lr-is-just-sigmoid.png` at section start (it bookends the ML arc), with Ukrainian alt-text framing it as "ML feels mysterious until you see it's just sigmoid + cross-entropy." Then one cell containing the dual-path data loader: check `SURVEY_CSV_PATH.exists()`, on the True branch run the data-model.md Stage 1 pipeline as a SINGLE black-box cell (`pd.read_csv` with `usecols=...`, drop NaN target/country, per-country median via `transform("median")`, build `y`, build the four features per R3, drop NaN feature rows, `np.column_stack` to `X`, print `f"Loaded {n} rows from {SURVEY_CSV_PATH}"`); on the False branch run the R4 synthetic generator (`X_synth = rng.standard_normal((5000, 4))`, plant `true_w` and `true_b`, sigmoid + Bernoulli sample to get `y_synth`, print "Survey CSV not found at <path>; using synthetic data instead — see lectures/11-pandas-analytics/README.md to enable the real dataset"). Both branches MUST produce the same `(X, y)` shape contract `(n, 4)` and `(n,)`. Address Edge Cases "CSV not present" and "NaN in features" via the dropna step (ref: spec.md FR-014, FR-015, FR-029; research.md R1, R3, R4; Acceptance Scenario 9; data-model.md Stage 0/Stage 1; Edge Case "Survey CSV not present", Edge Case "NaN in features")
- [X] T020 [US1] Author Section 10 "Стандартизація: чому, як, без витоку даних" in `lecture-12.ipynb` — markdown cell explaining z-score standardization in Ukrainian, why scale matters for gradient descent (gradients along different feature axes step at the same rate only when features are on comparable scales), and what data leakage means in this context. Then one code cell that DEFERS computing `feature_mean` / `feature_std` until after the train/test split (Section 11) — i.e., this section just defines the standardize function `def standardize(X, mean, std): return (X - mean) / std` and explains it. The actual fit happens in Section 11. Include the explicit warning "do NOT use `X.mean(axis=0)` over the full dataset — that leaks test-set information into the training pipeline" (ref: spec.md FR-016; data-model.md Stage 2; Acceptance Scenario 10)
- [X] T021 [US1] Author Section 11 "Поділ train/test без sklearn" in `lecture-12.ipynb` — one cell: `rng_split = np.random.default_rng(seed=SEED); perm = rng_split.permutation(n); n_train = int(0.8 * n); train_idx, test_idx = perm[:n_train], perm[n_train:]; X_train, X_test = X[train_idx], X[test_idx]; y_train, y_test = y[train_idx], y[test_idx]`. Then a second cell that NOW fits `feature_mean = X_train.mean(axis=0); feature_std = X_train.std(axis=0, ddof=0)` and applies the standardize function from Section 10 to both `X_train` and `X_test` to get `X_train_std`, `X_test_std`. Print all four shapes and `feature_mean` / `feature_std` for inspection (ref: spec.md FR-016, FR-017; data-model.md Stages 2–3; Acceptance Scenario 11)
- [X] T022 [US1] Author Section 12 "Логістична регресія: математика" in `lecture-12.ipynb` — markdown cell with the three formulas in plain Ukrainian + LaTeX: sigmoid `σ(z) = 1 / (1 + e^{-z})`, model `ŷ = σ(X w + b)`, BCE loss `L = -(1/n) Σ [y log(ŷ) + (1-y) log(1-ŷ)]`. Then one code cell: the **naive** sigmoid `def sigmoid_naive(z): return 1.0 / (1.0 + np.exp(-z))` with a demo showing `sigmoid_naive(np.array([-1000.0]))` emits an overflow warning OR returns `0.0` after warning. Then one code cell: the **stable** sigmoid via the branch-on-sign trick from research.md R5, with a demo showing `sigmoid(np.array([-1000.0])) == 0.0` cleanly, no warning. Then one code cell defining the BCE loss with `np.clip(yhat, 1e-15, 1 - 1e-15)` to avoid `log(0)`. (ref: spec.md FR-018; research.md R5, R6; Acceptance Scenario 12; Edge Case "sigmoid overflow")
- [X] T023 [US1] Author Section 13 "Цикл градієнтного спуску" in `lecture-12.ipynb` — embed `lectures/12-numpy-ml/assets/diagrams/lr-flow.png` at section start with Ukrainian alt-text. Then one markdown cell deriving the analytic gradient `∂L/∂w = (1/n) X.T (ŷ - y)` and `∂L/∂b = (1/n) Σ (ŷ - y)` in three lines. Then ONE code cell containing the full training loop: initialize `w = np.zeros(p); b = 0.0; loss_history = []; for epoch in range(EPOCHS): z = X_train_std @ w + b; yhat = sigmoid(z); loss = bce(y_train, yhat); loss_history.append(loss); grad_w = (1/n_train) * X_train_std.T @ (yhat - y_train); grad_b = (1/n_train) * (yhat - y_train).sum(); w -= LEARNING_RATE * grad_w; b -= LEARNING_RATE * grad_b; if epoch % PRINT_EVERY == 0: print(f"epoch {epoch:4d}  loss = {loss:.4f}")`. Confirm via the printed sequence that loss is monotonically (or near-monotonically) decreasing. Include a small "common gotchas" callout listing the three culprits from Edge Case "diverges": LR too high, features not standardized, naive sigmoid overflow (ref: spec.md FR-019; research.md R5, R6, R7, R9; data-model.md Stage 4; Acceptance Scenario 13; Edge Case "gradient descent diverges")
- [X] T024 [US1] Author Section 14 "Метрики: accuracy, precision, recall, confusion matrix" in `lecture-12.ipynb` — one code cell defining the prediction step: `y_pred = (sigmoid(X_test_std @ w + b) >= 0.5).astype(int)`. Then one cell computing `accuracy = (y_pred == y_test).mean()`. Then one cell computing the four confusion-matrix entries (`tn`, `fp`, `fn`, `tp`) as boolean-array sums (`((y_pred == 1) & (y_test == 1)).sum()` etc.) and assembling `cm = np.array([[tn, fp], [fn, tp]])`. Then one cell computing `precision = tp / (tp + fp); recall = tp / (tp + fn)`. Print all four metrics. Then a "why accuracy lies" cell: `np.bincount(y_test) / len(y_test)` to show class balance, and a comment on what a constant-prediction baseline would score. On the synthetic-fallback path expect `accuracy ≥ 0.75`; on the Survey path expect `accuracy ∈ [0.65, 0.80]`. (ref: spec.md FR-020, SC-003; research.md R7; data-model.md Stage 6; Acceptance Scenario 14; Edge Case "imbalanced target")
- [X] T025 [US1] Author Section 15 "Збереження та завантаження моделі (.npz)" in `lecture-12.ipynb` — one cell: `ARTIFACT_PATH.parent.mkdir(parents=True, exist_ok=True); np.savez(ARTIFACT_PATH, w=w, b=np.float64(b), feature_mean=feature_mean, feature_std=feature_std); print(f"Saved {ARTIFACT_PATH.stat().st_size} bytes to {ARTIFACT_PATH}")`. Then one cell defining a reusable `def predict(X_raw, w, b, mean, std): return (sigmoid(((X_raw - mean) / std) @ w + b) >= 0.5).astype(int)` and computing `pred_before = predict(X_test, w, b, feature_mean, feature_std)`. Then one cell loading: `loaded = np.load(ARTIFACT_PATH, allow_pickle=False); w_r = loaded["w"]; b_r = float(loaded["b"]); m_r = loaded["feature_mean"]; s_r = loaded["feature_std"]`. Then one cell asserting `pred_after = predict(X_test, w_r, b_r, m_r, s_r); assert np.array_equal(pred_before, pred_after); print("Round-trip OK — predictions identical.")`. Add a short markdown note on `allow_pickle=False` as the safe default for untrusted files (ref: spec.md FR-021; research.md R12; data-model.md Stage 5; Acceptance Scenario 15; Edge Case ".npz on different NumPy version")
- [X] T026 [US1] Author Section 16 "scikit-learn для контексту: 5 рядків" in `lecture-12.ipynb` — one markdown cell framing this as "what we just did in 80 lines, sklearn does in 5 — for context, not as a replacement for what we just learned." Then exactly ONE code cell wrapped in `try / except ImportError` per research.md R12: import `LogisticRegression` and `accuracy_score`, fit on `X_train_std` / `y_train` with `max_iter=1000`, print sklearn accuracy alongside `our_accuracy` for comparison. On `ImportError`, print "scikit-learn not installed — skipping comparison cell. Install with: pip install scikit-learn (optional, only for this comparison)". MUST NOT add sklearn to the notebook's setup instructions or import it at the top of the notebook — it appears ONLY inside this gated block (ref: spec.md FR-022, FR-031, FR-035; research.md R12; Acceptance Scenario 16)
- [X] T027 [US1] Author Section 18 "Підсумок" + Section 19 "Джерела" + Section 20 "Що далі?" in `lecture-12.ipynb`. Summary: bulleted key takeaways (NumPy is fast because of contiguous memory + C dispatch; broadcasting is the rules + practice; gradient descent on logistic regression is just `X.T @ (ŷ - y)` divided by `n`; metrics beyond accuracy matter; `.npz` round-trips). MUST include exactly one sentence calling out that "logistic regression is the simplest single-layer neural network — the sigmoid + linear-combination pattern you just implemented underlies every deep-learning library you'll meet later" per FR-038. References: NumPy official docs (`numpy.org`) — broadcasting tutorial + `np.random.Generator` page; Stack Overflow Developer Survey 2025 (`survey.stackoverflow.co/2025/`) under ODbL; Andrew Ng — Coursera ML Specialization Course 1 Week 3 (Logistic Regression); Wes McKinney *Python for Data Analysis* (3rd ed.) Chapters 4 & 12; scikit-learn `LogisticRegression` doc (optional reference for the gated coda); 3Blue1Brown "But what is a neural network?" series (optional). What's Next: preview L13 (matplotlib over the loss curve + decision boundary the student just trained) and L14 (packaging + serving the saved `.npz` model behind a FastAPI endpoint) per FR-003. Zero russian sources per Constitution Principle I. (ref: spec.md FR-003, FR-038; research.md R14; Acceptance Scenario 17)
- [X] T028 [US1] Add the optional R13 ground-truth-sanity-check cell at the end of Section 13 (gradient descent loop), gated on the synthetic-fallback path: `if data_path == "synthetic": print(f"true   w = {true_w}\nlearnt w = {w}\nL2 dist  = {np.linalg.norm(true_w - w):.3f}")`. On the Survey path this cell is a no-op. This cell MUST be hidden / collapsed by default to avoid distracting students on the Survey path (ref: research.md R13)
- [X] T029 [US1] Run `jupyter nbconvert --to notebook --execute lectures/12-numpy-ml/lecture-12.ipynb --output /tmp/us1-check.ipynb` on the active authoring path (Survey or synthetic) and fix any cell-execution errors surfaced. Re-run until the notebook executes top-to-bottom in under 90 seconds with zero errors (SC-004). Do NOT commit the `/tmp` output notebook — this is a verification step only (ref: spec.md SC-004; User Story 1 Independent Test; quickstart.md Step 3 / Step 4)

**Checkpoint**: All 17 teaching sections authored, memes and diagram embedded, learning objectives stated, references + summary + what's-next present, save/load round-trip verified, sklearn coda gated, notebook executes end-to-end cleanly on at least one path. User Story 1 is complete and independently testable. This is the MVP — the lecture could be delivered as-is (mini-project deferred to US2).

---

## Phase 4: User Story 2 — Mini-Project "Survey Salary Classifier" (Priority: P2)

**Goal**: Append the three-part progressive mini-project (Section 17) to `lecture-12.ipynb`, satisfying constitution Principle II ("mini-project per L5+ lecture, 20–30 min in-class + 30–60 min homework") and closing the FR-023 requirement.

**Independent Test**: Open the notebook, scroll to Section 17. Verify: clear 3-part structure header with in-class vs homework split, Parts 1–2 each have a task statement + hidden solution cell that matches the output contracts in `contracts/mini-project.md`, Part 3 has a task statement + requirements list + a collapsed reference-solution cell at the notebook end + a grading rubric. Run all mini-project cells end-to-end and confirm output shapes match the contracts (ref: spec.md User Story 2 Independent Test; contracts/mini-project.md).

### Implementation for User Story 2

- [X] T030 [US2] Author Section 17 mini-project header in `lecture-12.ipynb` — one markdown cell introducing "Міні-проєкт: Survey Salary Classifier", stating the 3-part structure (Part 1 & 2 in-class ~25 min total, Part 3 homework ~30–60 min), total time budget, and that Part 3's reference solution is collapsed at the end of the notebook (ref: spec.md FR-023; contracts/mini-project.md; User Story 2 Acceptance Scenario 1)
- [X] T031 [US2] Author Mini-Project Part 1 in `lecture-12.ipynb` — task statement in Ukrainian per `contracts/mini-project.md` Part 1 (per-country mean salary, for-loop vs vectorized, `%timeit` benchmark). One "hint" bullet referencing Section 8 (`%timeit`) and Section 5 (boolean masking). Hidden solution cell using a `<details>` HTML block or Jupyter cell-metadata toggle: produce both `loop_means` and `vec_means` arrays, assert `np.allclose`, print the `%timeit` ratio. Inputs MUST be derivable from the existing `df` (Survey path) or synthetic equivalents — do NOT require new dataset loading (ref: contracts/mini-project.md Part 1; spec.md FR-023; User Story 2 Acceptance Scenario 2)
- [X] T032 [US2] Author Mini-Project Part 2 in `lecture-12.ipynb` — task statement in Ukrainian per `contracts/mini-project.md` Part 2 (fit from-scratch LR on the 4-feature subset, report accuracy + 2×2 confusion matrix, `lr=0.1, epochs=1000, seed=42`). One "hint" bullet referencing Sections 10–14 (the lecture body's pipeline). Hidden solution cell that essentially re-runs the lecture pipeline as a single coherent block and prints the documented `(accuracy, confusion_matrix)` per the output contract. Note explicitly: "you've already done this in the lecture body — Part 2 is about being able to do it again in one shot." (ref: contracts/mini-project.md Part 2; spec.md FR-023; User Story 2 Acceptance Scenario 2)
- [X] T033 [US2] Author Mini-Project Part 3 in `lecture-12.ipynb` — task statement in Ukrainian per `contracts/mini-project.md` Part 3 (engineer one new feature, retrain, compare accuracy AND precision/recall, write 3–5 sentence Ukrainian reflection). Explicit requirements list per the contract. NO hidden solution inline. Add a collapsed "Еталонне рішення міні-проєкту (Частина 3)" cell at the very end of the notebook (after References / What's Next) with the reference solution (using `is_hybrid` as the example fifth feature) + the 6-point grading rubric table per `contracts/mini-project.md` (ref: contracts/mini-project.md Part 3; spec.md FR-023; User Story 2 Acceptance Scenario 3)
- [X] T034 [US2] Re-run `jupyter nbconvert --to notebook --execute lectures/12-numpy-ml/lecture-12.ipynb --output /tmp/us2-check.ipynb` on the active authoring path and verify the mini-project cells execute without error: Part 1 outputs match `np.allclose` and the vectorized timing is strictly faster; Part 2 produces accuracy in the documented range and a 2×2 confusion matrix whose entries sum to `len(y_test)`; Part 3 reference solution produces the required 2-row tidy DataFrame with the right columns. Do NOT commit the `/tmp` output (ref: User Story 2 Independent Test; contracts/mini-project.md)

**Checkpoint**: All three mini-project parts authored with solutions + rubric, notebook still executes end-to-end. Constitution Principle II requirement satisfied. User Story 2 complete.

---

## Phase 5: Polish & Cross-Cutting Concerns

**Purpose**: Run the dual-path execution check (the unique L12 quirk: notebook MUST work both with the Survey CSV present AND with it absent — synthetic fallback), plus the standard scope-leakage / russian-source / time-estimate / sklearn-gating greps. These tasks are mostly read-only checks against the authored notebook and can run in parallel, except T035 / T036 which require renaming the L11 CSV and back.

- [X] T035 Run quickstart.md Step 3 (Survey-path smoke test): if and only if `lectures/11-pandas-analytics/data/survey_results_public.csv` exists, run `jupyter nbconvert --to notebook --execute lectures/12-numpy-ml/lecture-12.ipynb --output /tmp/final-survey.ipynb`. Confirm clean execution in < 90 sec wall-clock (SC-004), the loaded-rows print line shows the CSV path, and the test accuracy falls in the documented `[0.65, 0.80]` range. If the CSV is not present, mark this task SKIPPED with a one-line note in the commit message (ref: spec.md SC-004; quickstart.md Step 3)
- [X] T036 Run quickstart.md Step 4 (missing-CSV failure mode): temporarily rename the L11 CSV, run `jupyter nbconvert --execute`, confirm the notebook fails with a clear `FileNotFoundError` pointing at the L11 README (no silent degradation), then restore the CSV. **OBSOLETE/REPURPOSED 2026-05-01:** the synthetic-data fallback was removed (per instructor decision); this task now verifies the fail-fast message instead of an alternate execution path.
- [X] T037 [P] Run quickstart.md Step 5 (saved-model round-trip check): after T035 or T036, confirm `lectures/12-numpy-ml/artifacts/model.npz` exists and is non-empty, and the executed notebook contains a printed line confirming `np.array_equal(pred_before, pred_after)` is `True` (or equivalent assertion success message) (ref: spec.md FR-021, SC-006)
- [X] T038 [P] Run quickstart.md Step 8 (project-leakage grep, tightened for precision per L11 T035): `grep -Ei "notes-api|NoteModel|TagModel|pd\\.read_sql|(from|import) sqlalchemy|FastAPI\\(|@app\\.(get|post|put|delete|patch)|alembic (upgrade|revision|init)" lectures/12-numpy-ml/lecture-12.ipynb` MUST return zero matches per FR-031, FR-032 (the "What's Next" mention of L14 serving the model via FastAPI is allowed because it's a forward reference in markdown prose, not a code dependency — the grep pattern targets imports / decorators / actual function calls, not the literal string "FastAPI" in markdown). Verify the grep pattern does not fire on the prose mention before declaring PASS — adjust the pattern if it does
- [X] T039 [P] Run quickstart.md Step 9 (sklearn-coda gating check): `grep -nE "import sklearn|from sklearn" lectures/12-numpy-ml/lecture-12.ipynb` — every match MUST appear inside a `try:` block (verify by inspecting the surrounding cell). The notebook MUST execute end-to-end with sklearn uninstalled — verify by ensuring T036 ran in an environment without sklearn (or by `pip uninstall scikit-learn` before T036 and reinstalling after if it was present) (ref: spec.md FR-022, FR-031, FR-035)
- [X] T040 [P] Run quickstart.md Step 10 (non-russian sources grep): `grep -Ei "habr\\.(com|ru)|\\.ru/|pythonworld\\.ru|ruby2ru" lectures/12-numpy-ml/lecture-12.ipynb` MUST return zero matches per Constitution Principle I and research.md R14
- [X] T041 [P] Run quickstart.md Step 11 (no per-section time estimates grep): `grep -E '\\(~?[0-9]+\\s*(хв|мин|min)\\)' lectures/12-numpy-ml/lecture-12.ipynb` MUST return zero matches EXCEPT inside the Section 17 mini-project header (which legitimately cites "~25 min" for in-class Parts 1–2 and "~30–60 min" for Part 3 homework — those are project-level, not section-level estimates, per Constitution v1.5.1)
- [X] T042 Final proofread of Ukrainian explanatory text across all 17 sections in `lecture-12.ipynb` — check grammar, punctuation, English-in-parentheses rule (FR-006: parentheticals ONLY for specific technical terms like "broadcasting", "sigmoid", "vectorization", "logistic regression", "confusion matrix"; NOT for obvious phrases like "Підсумок (Summary)" or "Що далі? (What's Next)"). Fix any violations
- [X] T043 Visual asset-rendering check: open `lectures/12-numpy-ml/lecture-12.ipynb` in Jupyter or VS Code and confirm: meme 1 (`numpy-vs-python-speed.png`) renders at the start of Section 8, meme 2 (`lr-is-just-sigmoid.png`) renders at the start of Section 9, the LR-flow diagram (`lr-flow.png`) renders at the start of Section 13. Fix any broken paths

**Checkpoint**: All verification checks pass on at least one execution path (ideally both), notebook is shippable. Constitution gates remain PASS (see plan.md Constitution Check). The feature is ready for review and merge into master.

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — can start immediately. T001 must complete before T002/T003/T004 (directory must exist); T005 and T006 independent.
- **Foundational (Phase 2)**: Depends on Phase 1 completion. T007 → T008 is sequential (T008 needs the path decision from T007, and only runs on the Survey path). T009 and T010 are fully parallel with each other and with T007/T008.
- **User Story 1 (Phase 3)**: Depends on Phase 2 completion (notebook references columns + embeds assets). T011 must be first; T012–T028 are sequential because they all edit `lecture-12.ipynb`; T029 is the final validation within US1.
- **User Story 2 (Phase 4)**: Depends on Phase 3 completion (mini-project appends to the existing notebook). T030 → T031 → T032 → T033 → T034 sequential.
- **Polish (Phase 5)**: Depends on Phase 4 completion. T035 and T036 must run sequentially (they touch the L11 CSV via rename); T037–T041 are fully parallel (read-only greps and assertions on the executed notebooks). T042 / T043 involve manual editing / visual inspection and should follow the automated checks.

### User Story Dependencies

- **US1 (P1)** is the MVP and has no dependency on US2. The notebook can ship with Section 17 blank if time pressure forces it — though the constitution then flags the missing mini-project.
- **US2 (P2)** depends on US1: the mini-project is appended to the notebook US1 authored. US2 cannot be started in parallel with US1 because they edit the same file.

### Within Each Phase

- Phase 1: T001 first, then T002/T003/T004/T005 in parallel, then T006 independent.
- Phase 2: T007 first, then T008 (only on Survey path), T009 and T010 fully parallel with each other and with T007/T008.
- Phase 3: T011 first (skeleton), then T012 through T028 strictly sequential (same file), T029 last.
- Phase 4: T030 → T031 → T032 → T033 → T034 strictly sequential.
- Phase 5: T035 → T036 sequential (CSV rename); T037–T041 in parallel; T042 / T043 after.

---

## Parallel Opportunities

| Phase | Parallel tasks |
|-------|----------------|
| Phase 1 | T002, T003, T004, T005 (after T001); T006 anytime |
| Phase 2 | T009, T010 (fully independent; can run during T007/T008 too) |
| Phase 3 | None — single-file notebook authoring |
| Phase 4 | None — single-file notebook authoring |
| Phase 5 | T037, T038, T039, T040, T041 (all read-only checks on the finished notebook, after T035/T036 produce the executed copies) |

---

## Parallel Example: Phase 2

```bash
# While T007 decides the authoring path and T008 (conditionally) pre-flights feature engineering:
#   - One agent/dev produces the LR-flow diagram (T009)
#   - Another agent/dev prepares the two meme images (T010)
#
# After T007/T008 and T009/T010 all finish, Phase 2 is complete.

Task: "T009 Create lr-flow.png diagram in lectures/12-numpy-ml/assets/diagrams/"
Task: "T010 Place two memes in lectures/12-numpy-ml/assets/memes/ with CREDITS.md"
Task: "T007 Verify L11 Survey CSV presence; record authoring path in README.md"
```

## Parallel Example: Phase 5

```bash
# After T035/T036 produce the executed notebook copies, all read-only checks run together:
Task: "T037 Verify model.npz exists and round-trip assertion message present"
Task: "T038 grep for FastAPI/SQLAlchemy/Alembic/notes-api leakage == 0"
Task: "T039 grep for sklearn imports inside try: blocks"
Task: "T040 grep for russian-source domains == 0"
Task: "T041 grep for per-section time estimates == 0 (excluding mini-project header)"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup — directory + placeholder + README + `.gitignore` entry + repo-README link
2. Complete Phase 2: Foundational — authoring path decided, columns verified (or synthetic path noted), memes + diagram committed
3. Complete Phase 3: User Story 1 — all 17 teaching sections + assets + dual-path data loader + sklearn-gated coda + validation
4. **STOP and VALIDATE**: Run T029 final smoke test; open notebook in Jupyter; confirm 1.5-hour flow reads cleanly end-to-end
5. Ship MVP: the lecture is deliverable for the 1.5-hour slot. Mini-project is explicitly marked TODO and delivered next iteration.

### Incremental Delivery (Full Feature)

1. Setup + Foundational → ready to author
2. Add User Story 1 → lecture notebook complete → deliverable as 1.5-hour lesson (MVP)
3. Add User Story 2 → mini-project appended → constitution Principle II satisfied
4. Run Polish → shippable

### Parallel Team Strategy

This is a single-author deliverable (Jupyter notebook). Parallelism is limited to asset production (Phase 2 T009/T010) and verification (Phase 5 T037–T041). The teaching-narrative authoring (T011–T029) MUST be a single writer to preserve tone consistency, which Constitution Principle III flags as critical.

---

## Notes

- All tasks reference repo-relative paths for reproducibility.
- No test suite tasks — this is a notebook deliverable; `jupyter nbconvert --execute` is the analogue of a test run, captured in T029, T034, T035, T036.
- The L12-specific dual-path execution check (T035 + T036) is the most important Polish task — it catches the lecture's biggest engineering risk: the synthetic fallback (FR-029) silently breaking and forcing every offline / no-CSV student to debug into the lecture body.
- The sklearn-gating check (T039) protects the FR-031 / FR-035 contract that students MUST be able to run the notebook without scikit-learn installed. This is verified by T036 running in a sklearn-free environment.
- Phase 5 greps are defensive: they catch scope-creep or residual notes-api references before merge, without forcing reviewers to scan the whole notebook by hand. Note that the "What's Next" section legitimately mentions FastAPI in prose (forward-reference to L14); the T038 grep pattern targets actual code-level leakage (imports, decorators, function calls), not prose mentions.
- When running nbconvert in T029 / T034 / T035 / T036, ensure the active Python environment has `numpy>=1.26` and `pandas>=2.2` — those are the only required runtime prerequisites.
- Commit cadence suggestion: one commit per phase (Phase 1, Phase 2, Phase 3, Phase 4, Phase 5), with an optional per-section commit inside Phase 3 for reviewability of the notebook's narrative progression (especially the Section 12 / 13 / 14 ML core).
