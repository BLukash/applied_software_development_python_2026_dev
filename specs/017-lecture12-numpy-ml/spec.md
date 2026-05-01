# Feature Specification: Lecture 12 — NumPy, Vectorization & a Logistic Regression Classifier from Scratch

**Feature Branch**: `017-lecture12-numpy-ml`
**Created**: 2026-04-30
**Status**: Draft
**Input**: User description: "Implement Lecture 12"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Lecture Notebook: NumPy + Vectorization + Logistic Regression from Scratch (Priority: P1)

A student opens the Lecture 12 Jupyter notebook and follows a 1.5-hour, **standalone** session that takes them from "I've heard NumPy is fast" to "I can build, train, evaluate, and persist a binary classifier using only NumPy and basic math." The lecture has two intertwined arcs: (a) NumPy as the array-and-vectorization workhorse beneath every Python data tool, and (b) a from-scratch logistic regression classifier that justifies *why* the class learned NumPy in the first place. Concretely, students walk through: NumPy arrays vs. Python lists with a measured speedup, dtypes and shapes, indexing/slicing/fancy indexing/boolean masking, broadcasting (the rules + concrete shape examples), elementwise + reduction + linear-algebra ops (`np.dot`, `@`), a small `%timeit`-driven performance section to internalise *why* vectorization wins, and finally the full lifecycle of a binary logistic regression: feature matrix, sigmoid, log-loss, gradient descent loop, train/test split, metric evaluation (accuracy, precision, recall, confusion matrix), and saving/loading parameters with `np.save` / `np.load`. The notebook is self-contained — it does NOT add code to the L6–L10 `notes-api` project — and it explicitly contrasts the from-scratch approach with what scikit-learn would do in three lines (one short coda, no scikit-learn dependency required to run the notebook).

**Why this priority**: The notebook is the primary deliverable for this lecture. It is also the first lecture in the course where students touch a real machine-learning concept end-to-end (training loop, loss, gradients, evaluation), and it cements vectorization as a habit before L13 visualization and L14 deployment.

**Independent Test**: Open the notebook in Jupyter, run every cell top-to-bottom against a clean Python 3.13 environment with NumPy (and pandas, only for the dataset-loading bridge from L11) installed; verify all cells execute without error, the trained classifier reports a sensible accuracy on a held-out test set, and the saved `.npz` file round-trips through `np.load` to produce identical predictions. No database, no FastAPI, no Docker, no scikit-learn required.

**Acceptance Scenarios**:

1. **Given** a student opening the L12 notebook, **When** they read the header, **Then** they see prerequisites referencing only basic Python (L1–L5: types, functions, loops, comprehensions) plus pandas DataFrame familiarity from L11 (the dataset loading is a `pd.read_csv` one-liner — no pandas teaching is repeated here). It MUST NOT require L6–L10 (FastAPI, Postgres, Alembic, SQLAlchemy, Docker).
2. **Given** a student reading the "Why NumPy?" opener, **When** they finish, **Then** they can state in their own words that NumPy stores homogeneous numeric data in contiguous memory, that operations dispatch to compiled C/SIMD loops, and that this is the single biggest reason it's faster than a Python list.
3. **Given** a student reading the "ndarray basics" section, **When** they finish, **Then** they can construct an `ndarray` from a Python list, use `np.zeros`, `np.ones`, `np.arange`, `np.linspace`, `np.random.default_rng()`, and inspect `.shape`, `.dtype`, `.ndim`, `.size`, `.nbytes`.
4. **Given** a student reading the dtype section, **When** they finish, **Then** they can explain why `int64` vs `int32` vs `float32` matters (memory + range + precision) and convert between dtypes via `.astype()`.
5. **Given** a student reading the indexing section, **When** they finish, **Then** they can use basic slicing on 1-D and 2-D arrays, fancy indexing with an integer array, boolean masking (`arr[arr > 0]`), and explain that basic slicing returns a view while fancy/boolean indexing returns a copy.
6. **Given** a student reading the broadcasting section, **When** they finish, **Then** they can apply the broadcasting rules to predict the output shape of `a + b` for at least three concrete shape pairs (e.g., `(3, 4) + (4,)`, `(3, 1) + (1, 4)`, `(5,) + (5,)`), and they can name one shape pair that does NOT broadcast and why.
7. **Given** a student reading the elementwise / reduction / linear-algebra section, **When** they finish, **Then** they have seen and run `np.exp`, `np.log`, `np.sqrt`, `np.maximum`, `arr.sum(axis=...)`, `arr.mean(axis=...)`, `arr.std`, `arr.argmax`, `np.dot(a, b)` and the equivalent `a @ b`, with an explicit note on what `axis=0` vs `axis=1` mean for a 2-D array.
8. **Given** a student reading the performance section, **When** they finish, **Then** they have seen a `%timeit` benchmark comparing a pure-Python list comprehension squaring 1 million numbers vs the equivalent `arr ** 2` on an ndarray, with a one-paragraph plain-Ukrainian explanation of why the gap is roughly two orders of magnitude. They have also seen one example where vectorization loses (e.g., trivially small input) so the lesson is "vectorize when it's natural, not religiously."
9. **Given** a student reading the "from scratch ML" arc, **When** they finish the dataset-loading subsection, **Then** they have a `pd.read_csv` snippet that pulls a small, prepared subset of the 2025 Stack Overflow Developer Survey (the same CSV from L11), selects 4–6 numeric/encodable feature columns and a binary target column, drops rows with missing target, fills missing features, and converts the result into a NumPy feature matrix `X` (shape `(n_samples, n_features)`) and target vector `y` (shape `(n_samples,)`). The notebook MUST clearly state which columns become features and what the binary target is.
10. **Given** a student reading the "feature standardization" subsection, **When** they finish, **Then** they understand why features should be on a comparable scale for gradient descent and have implemented z-score standardization (`(X - mean) / std`) using broadcasting, persisting the per-feature mean and std so the same transform can be applied at inference time.
11. **Given** a student reading the "train/test split" subsection, **When** they finish, **Then** they have implemented an 80/20 split using `np.random.default_rng(seed=42).permutation(n)` and integer slicing — without scikit-learn — and they understand the role of the seed for reproducibility.
12. **Given** a student reading the "logistic regression math" subsection, **When** they finish, **Then** they can write down the sigmoid `σ(z) = 1 / (1 + exp(-z))`, the model `ŷ = σ(X @ w + b)`, and the binary cross-entropy loss in plain Ukrainian, and they have seen a numerically stable sigmoid implementation that avoids overflow for large negative `z`.
13. **Given** a student reading the "gradient descent loop" subsection, **When** they finish, **Then** they can explain the analytic gradient for logistic regression (`(1/n) * X.T @ (ŷ - y)` for `w` and `(1/n) * (ŷ - y).sum()` for `b`), and they have run a training loop that prints loss every K iterations and shows the loss decreasing monotonically (or near-monotonically) to convergence.
14. **Given** a student reading the "evaluation" subsection, **When** they finish, **Then** they can implement and interpret accuracy, precision, recall, and a 2×2 confusion matrix from raw `y_true` / `y_pred` arrays using only NumPy, and they understand why accuracy alone is misleading on an imbalanced dataset.
15. **Given** a student reading the "save / load" subsection, **When** they finish, **Then** they have saved the trained weight vector, bias scalar, feature mean, and feature std into a single `.npz` file via `np.savez`, reloaded it via `np.load`, and verified the reloaded model produces bitwise-identical predictions to the original on the test set.
16. **Given** a student reading the "scikit-learn coda" subsection, **When** they finish, **Then** they have seen a 5-line side-by-side that says "what we just did in 80 lines, sklearn does in 5" — but the sklearn cell is documented as illustrative only and is gated behind a clear `try: import sklearn ... except ImportError:` guard, so the notebook still runs end-to-end on a NumPy-only environment.
17. **Given** a student finishing the notebook, **When** they read the Summary and "What's Next" section, **Then** they see a preview of L13 (visualization with matplotlib/seaborn, including plotting the loss curve and the decision boundary they just trained), and a teaser that the trained `.npz` model could be served from a FastAPI endpoint in L14.

---

### User Story 2 - Mini-Project: "Survey Salary Classifier" (Priority: P2)

A student completes a single progressive mini-project called **"Survey Salary Classifier"** that reuses the cleaned 2025 Stack Overflow Developer Survey from L11. The mini-project has three parts:

- **Part 1 — in-class**: Vectorize a small numeric task — given a 1-D NumPy array of yearly salaries and a 1-D array of country codes, compute (a) the per-country mean salary using a `for` loop AND using vectorized boolean masking, then (b) confirm both produce the same result and benchmark them with `%timeit`.
- **Part 2 — in-class**: Fit the from-scratch logistic regression on a 4-feature, 2-class subset of the Survey (target: "above-median compensation in respondent's country", features chosen from `WorkExp`, `YearsCode`, `Age`-bucket-encoded, `EdLevel`-ordinal-encoded), using the standardize → split → train → evaluate pipeline shown earlier in the lecture, and report accuracy and confusion matrix.
- **Part 3 — homework extension**: Add a fifth engineered feature of the student's choice (e.g., a 0/1 "remote-only" flag derived from `RemoteWork`, or a one-hot expansion of the top-5 `DevType`s), retrain, and write a 3–5 sentence Ukrainian-language reflection comparing the two models on accuracy AND on precision/recall — explicitly addressing whether the new feature actually helped or just added noise.

Each part ships with a hidden solution cell for the in-class portions (Parts 1–2) and a reference solution + grading rubric for Part 3. Total student time target: ~25 min in-class (Parts 1–2) + 30–60 min homework (Part 3).

**Why this priority**: Satisfies constitution Principle II (every L5+ lecture must include a runnable mini-project, ~25 min in class + 30–60 min homework). Independent of the main notebook walkthrough so it can be removed or skipped without breaking the rest of the notebook. P2 because the homework portion exceeds the 1.5-hour lecture slot.

**Independent Test**: A student can complete Parts 1 and 2 within ~25 minutes using only knowledge from the notebook's earlier sections; their in-class outputs match the hidden solution cells in shape and within a small tolerance on accuracy (the random seed pins everything for reproducibility). Part 3 is graded against the reference solution + rubric.

**Acceptance Scenarios**:

1. **Given** the notebook, **When** a student reads the mini-project header, **Then** they see a clear statement that this is the lecture's mini-project (not a loose set of exercises), its three-part structure, the in-class vs homework split, and the expected total time (~1 hour total).
2. **Given** Parts 1 and 2, **When** a student reads each part, **Then** each has a clear problem statement, expected output shape (e.g., "a `(num_countries,)` 1-D array sorted by country code", or "an accuracy in the 0.65–0.80 range"), at least one "hint" bullet that references the earlier notebook section where the relevant technique was introduced, and a hidden solution cell below.
3. **Given** Part 3, **When** a student reads it, **Then** they see (a) the open-ended task description, (b) explicit requirements (must engineer one new feature, must retrain, must compare accuracy AND precision/recall, must include a 3–5 sentence Ukrainian reflection on whether the feature helped), (c) a reference solution revealed only in a collapsed section at the end of the notebook, and (d) a short grading rubric (e.g., "3 points: correctness; 2 points: clean vectorized code; 1 point: reflection quality").
4. **Given** Parts 1–2 completed in class, **When** a student starts Part 3 at home, **Then** they can proceed without re-reading the lecture body because Parts 1–2 have already exercised every NumPy + ML technique Part 3 requires.

---

### Edge Cases

- **What happens when NumPy is not installed in the student's environment?** The notebook's first code cell MUST check for NumPy and, if missing, print the exact `pip install` or `uv add` command (no auto-install).
- **What happens when the 2025 Stack Overflow Survey CSV is not present locally?** The notebook MUST raise a `FileNotFoundError` with the exact expected path and a one-line pointer to the L11 download instructions (`lectures/11-pandas-analytics/README.md`). The notebook is **Survey-only** — there is no synthetic-data fallback (a 2026-05-01 instructor decision; the previous fallback was removed because it diluted the lesson with a parallel data path no student would ever run in production).
- **What happens when gradient descent diverges (loss goes up or NaN)?** The notebook MUST include a short "common gotchas" callout naming the three usual culprits (learning rate too high, features not standardised, numerical overflow in sigmoid) and link each gotcha back to the section that prevents it.
- **What happens when the binary target is severely imbalanced (e.g., 95% one class)?** The notebook MUST include a "why accuracy lies" example showing that a constant-prediction baseline gets 95% accuracy on such a dataset, motivating precision/recall as the more honest metrics.
- **What happens when a student tries to run the gradient-descent loop on a feature matrix that contains NaN values?** The notebook MUST demonstrate `np.isnan(X).any()` as a pre-flight check and explicitly drop or impute NaN rows BEFORE training, with a short note on why NaN in features silently breaks gradient descent.
- **What happens when `np.dot` and `@` produce different shapes for the same operands?** They don't (for 1-D and 2-D, they are equivalent), but the notebook MUST briefly state this so students don't waste time hunting a phantom difference; it MUST also note the one place they diverge in spirit (`np.dot` for higher-dimensional tensors falls back to a sum-product semantics that `@` does not).
- **What happens when a student's `.npz` save file is opened on a machine with a different NumPy version?** The notebook MUST briefly note that `.npy` / `.npz` is a stable format across NumPy versions but is *not* a security boundary — it MUST NOT be loaded from untrusted sources, and `allow_pickle=False` MUST be the explicit default in the load call shown.

## Requirements *(mandatory)*

### Functional Requirements

**Notebook Content — Structure:**

- **FR-001**: The notebook MUST state 3–5 learning objectives at the start covering: why NumPy is fast, ndarray fundamentals (creation, dtypes, indexing, broadcasting), vectorization habits (`%timeit`-grounded), and the full lifecycle of a from-scratch binary logistic regression (math → training → evaluation → persistence).
- **FR-002**: The notebook MUST include prerequisites referencing only basic Python (L1–L5: types, functions, loops, comprehensions, file I/O) plus minimal pandas familiarity from L11 (`pd.read_csv`, column selection, `.dropna`). It MUST NOT reference L6–L10 content (FastAPI, Postgres, SQLAlchemy, Alembic, Docker) as required prior knowledge.
- **FR-003**: The notebook MUST end with a Summary and "What's Next" section previewing L13 (matplotlib/seaborn — including a callout that the loss curve and decision boundary the student just trained will be plotted there) and L14 (packaging + serving the saved `.npz` model behind a FastAPI endpoint).
- **FR-004**: The notebook MUST NOT include per-section time estimates in parentheses (e.g., "(~10 хв)"), per the constitution's Prohibited Practices clause.
- **FR-005**: The notebook target duration MUST be 1.5 hours of lecture content.
- **FR-006**: All explanatory text MUST be in Ukrainian; English technical terms in parentheses ONLY for specific terms students need to recognize (e.g., "broadcasting", "vectorization", "gradient descent", "logistic regression", "confusion matrix", "sigmoid"). Obvious phrases (e.g., "Підсумок", "Що далі?") MUST NOT be translated in parentheses.

**Notebook Content — NumPy Arc:**

- **FR-007**: The notebook MUST include a "Why NumPy?" opening section that names contiguous-memory layout, fixed dtypes, and dispatch to compiled C/SIMD loops as the three reasons NumPy is fast — explained in plain Ukrainian, no jargon dump.
- **FR-008**: The notebook MUST include an "ndarray basics" section showing array construction via `np.array(list)`, `np.zeros`, `np.ones`, `np.arange`, `np.linspace`, `np.random.default_rng().standard_normal((m, n))`, and inspection of `.shape`, `.dtype`, `.ndim`, `.size`, `.nbytes`. MUST include at least one 2-D example (not just 1-D).
- **FR-009**: The notebook MUST include a dtype section showing `.astype()` conversion between `int32`, `int64`, `float32`, `float64`, and a one-paragraph note on memory vs precision tradeoffs.
- **FR-010**: The notebook MUST include an indexing/slicing section covering: basic slicing on 1-D and 2-D arrays (`arr[1:4]`, `arr[1:4, ::2]`), fancy indexing with an integer array, boolean masking, and the view-vs-copy distinction (basic slicing returns a view; fancy/boolean indexing returns a copy). MUST include a small "modify a view, see the original change" cell to demonstrate the view semantics concretely.
- **FR-011**: The notebook MUST include a broadcasting section that states the broadcasting rules in plain Ukrainian, walks through at least three concrete shape combinations that DO broadcast (`(3, 4) + (4,)`, `(3, 1) + (1, 4)`, `(5,) + scalar`), and at least one that does NOT (`(3, 4) + (3,)` — wrong axis), with the resulting `ValueError` shown.
- **FR-012**: The notebook MUST include an elementwise / reduction / linear-algebra section covering: `np.exp`, `np.log`, `np.sqrt`, `np.maximum`, `arr.sum(axis=...)`, `arr.mean(axis=...)`, `arr.std`, `arr.argmax`, `np.dot(a, b)`, and `a @ b` (with an explicit "they're the same for 1-D and 2-D, prefer `@` for matrix-multiply readability" note).
- **FR-013**: The notebook MUST include a `%timeit` performance section comparing a pure-Python list comprehension vs the equivalent NumPy operation on at least 1 million elements, with a one-paragraph Ukrainian explanation of the speedup. MUST also show one example where vectorization loses (very small input where Python's overhead is negligible) so students learn the nuance.

**Notebook Content — From-Scratch ML Arc:**

- **FR-014**: The notebook MUST include a dataset-loading subsection that uses `pd.read_csv` (one cell, treated as a black box — pandas was taught in L11) to load a small, prepared subset of the **2025 Stack Overflow Developer Survey** CSV from `lectures/11-pandas-analytics/data/survey_results_public.csv`, selects 4–6 feature columns plus the binary target column, drops rows with missing target, fills or drops rows with missing features, and converts the result into a NumPy feature matrix `X: shape (n, p)` and target vector `y: shape (n,)`. If the CSV is missing the cell MUST raise `FileNotFoundError` with a clear message pointing at the L11 README — no synthetic-data fallback (Survey is the single source of truth; this was a 2026-05-01 simplification).
- **FR-015**: The notebook MUST clearly document which columns become features and what the binary target is. **The binary target is "above-median `ConvertedCompYearly` within the respondent's country"** (i.e., a per-country median split, not a global median split — this avoids trivially predicting "lives in a high-income country"). The features MUST be a small, semantically meaningful subset, e.g., `WorkExp`, `YearsCode`, an ordinal encoding of `EdLevel`, and a 0/1 derived flag for remote work.
- **FR-016**: The notebook MUST include a feature-standardization subsection implementing z-score standardization (`(X - mean) / std`) using broadcasting, computing `mean` and `std` over `axis=0` from the training set only (not the test set, to avoid data leakage), and persisting the per-feature `mean` and `std` so the same transform can be applied to the test set and at inference time. MUST include a short Ukrainian-language explanation of why training-set-only statistics matter (data leakage).
- **FR-017**: The notebook MUST include a manual train/test split subsection using `np.random.default_rng(seed=42).permutation(n)` plus integer slicing — explicitly without scikit-learn — and explain the seed's role for reproducibility.
- **FR-018**: The notebook MUST include a logistic-regression-math subsection writing down the sigmoid, the model `ŷ = σ(X @ w + b)`, and the binary cross-entropy loss in plain Ukrainian. MUST include a numerically stable sigmoid implementation (using `np.where` or the standard branch-on-sign trick with `np.exp(-|z|)`) that handles large negative `z` without overflow, and a comment explaining why the naive `1 / (1 + np.exp(-z))` overflows.
- **FR-019**: The notebook MUST include a gradient-descent training-loop subsection that:
  (a) initializes `w` and `b` to zeros (or small random values),
  (b) iterates a fixed number of epochs (default 1000),
  (c) computes predictions, loss, and analytic gradients (`grad_w = (1/n) * X.T @ (ŷ - y)`, `grad_b = (1/n) * (ŷ - y).sum()`),
  (d) updates parameters with a learning rate (default 0.1 on standardised features),
  (e) prints loss every K iterations (default K=100),
  (f) shows the loss decreasing across iterations.
- **FR-020**: The notebook MUST include an evaluation subsection that implements accuracy, precision, recall, and a 2×2 confusion matrix from raw `y_true` / `y_pred` arrays using only NumPy (no scikit-learn). MUST include a short Ukrainian explanation of why accuracy alone misleads on imbalanced data, and demonstrate the imbalance check (`np.bincount(y) / len(y)`).
- **FR-021**: The notebook MUST include a save / load subsection using `np.savez` to save the weight vector, bias scalar, feature mean, and feature std into a single `.npz` file, then `np.load(..., allow_pickle=False)` to reload it, and a verification cell that confirms reloaded parameters produce bitwise-identical predictions to the originals on the test set. MUST briefly note that `allow_pickle=False` is the safe default for untrusted files.
- **FR-022**: The notebook MUST include a "scikit-learn coda" subsection (≤ 10 lines of code) showing the equivalent `sklearn.linear_model.LogisticRegression` flow as a one-screen comparison, gated behind a `try: import sklearn ... except ImportError: print("sklearn not installed — skipping comparison")` guard so the notebook still runs end-to-end without sklearn. MUST NOT add sklearn as a runtime dependency in any setup instructions; it is shown for educational comparison only.

**Notebook Content — Exercises & Visual Elements:**

- **FR-023**: The notebook MUST contain a single progressive mini-project titled "Survey Salary Classifier", anchored on the L11 Survey dataset (with the same synthetic-data fallback as the lecture body), structured as three parts: Part 1 (in-class, vectorize a small numeric task with `%timeit`), Part 2 (in-class, fit the from-scratch logistic regression and report accuracy + confusion matrix), Part 3 (homework extension, engineer one additional feature, retrain, compare metrics, write Ukrainian reflection). Parts 1–2 MUST each have a hidden solution cell; Part 3 MUST have a reference solution revealed only in a collapsed section at the end of the notebook, together with a short grading rubric.
- **FR-024**: The notebook MUST contain at least 5 runnable code examples in the instructional cells (independent of the mini-project).
- **FR-025**: The notebook MUST contain at least 2 memes or visual-humor elements relevant to the topic (e.g., the "Python `for` loop vs NumPy" speed gap, the "logistic regression is just sigmoid + cross-entropy" simplicity meme).
- **FR-026**: The notebook MUST contain at least 1 diagram. At minimum, ONE of: (a) a broadcasting-rules visual showing how `(3, 1) + (1, 4)` becomes `(3, 4)`, OR (b) a logistic-regression flow diagram showing `X → linear → sigmoid → loss → gradient → update`, OR (c) a confusion-matrix visual labelling TP / FP / FN / TN.
- **FR-027**: The notebook MUST NOT produce heavy matplotlib visualizations (line plots, scatter plots, decision-boundary plots) — that is L13's role. The only "plotting" allowed in this notebook is the final loss-curve `print` of loss values (a numeric column), or at most a single `pd.Series(...).plot(kind="line")` for the loss curve, kept under 5 lines.

**Dataset Selection & Sourcing:**

- **FR-028**: The lecture MUST reuse the **2025 Stack Overflow Annual Developer Survey** CSV that students already downloaded for L11, located at `lectures/11-pandas-analytics/data/survey_results_public.csv`. No new download instructions; just a one-line pointer to the L11 README.
- **FR-029**: When the Survey CSV is missing, the notebook MUST raise `FileNotFoundError` with the expected path and a pointer to the L11 README. **No synthetic-data fallback** (removed on 2026-05-01 — see Edge Case "What happens when the Survey CSV is not present" for rationale).
- **FR-030**: No russian-originated datasets, translations, or sources MUST be used, per constitution principle I.
- **FR-031**: The notebook MUST NOT depend on any external service beyond the (optional) locally downloaded CSV — no network calls, no database, no FastAPI app, no scikit-learn at runtime.

**Scope Boundaries (what this lecture explicitly does NOT include):**

- **FR-032**: The notebook MUST NOT add any project increment to the `notes-api` repository; L12 is a self-contained NumPy + ML lesson, consistent with the L11 precedent. The "What's Next" section MAY mention that L14 will revive the project by serving the saved `.npz` model.
- **FR-033**: The notebook MUST NOT cover deep learning, neural networks beyond logistic regression (which is a single-layer network with a sigmoid activation — this connection MAY be mentioned in one sentence, but is NOT taught), regularization (L1/L2), multi-class classification, cross-validation, or hyperparameter tuning. These are out of scope and MAY be mentioned only as one-line "next steps" in the Summary.
- **FR-034**: The notebook MUST NOT cover matplotlib / seaborn visualization beyond the at-most-one loss-curve plot allowed by FR-027 — full visualization is L13's role.
- **FR-035**: The notebook MUST NOT install scikit-learn as a runtime dependency, MUST NOT use it in any cell that runs by default, and the sklearn coda MUST be guarded by a `try: import sklearn` block.
- **FR-036**: The notebook MUST NOT cover NumPy advanced topics that would crowd out the ML arc: structured arrays, `np.einsum`, advanced linear algebra (`np.linalg.eig`, SVD), masked arrays, memory-mapped arrays, or `numba` / `cython` integration.

**Engagement & Pedagogy:**

- **FR-037**: The notebook MUST use the Survey context (Ukrainian respondents, global comparisons) as the running anchor for the ML arc — e.g., "we're predicting whether a respondent is paid above their country's median." Pure NumPy teaching sections (broadcasting, indexing, performance) MAY use abstract or geometric examples (image-as-array intuition is welcome) and do NOT need a Ukraine hook every time.
- **FR-038**: The notebook MUST explicitly call out the connection between the from-scratch logistic regression and the sigmoid + linear-combo pattern that underlies all neural networks — exactly one sentence, in the Summary or just before the sklearn coda — so students leave with the right mental model for any future ML course.

### Key Entities

- **NumPy `ndarray`** (the central object of this lecture): a homogeneous, fixed-dtype, contiguous-memory array. Key attributes the notebook works with: `.shape`, `.dtype`, `.ndim`, `.size`, `.nbytes`. Not persisted as a "thing"; instances are created, transformed, and discarded freely.
- **Trained model** (the artifact produced by the ML arc): a small `.npz` file containing four arrays — `w` (weight vector, shape `(p,)`), `b` (bias, scalar), `feature_mean` (shape `(p,)`), `feature_std` (shape `(p,)`). Persisted to a single file, not a database, and intentionally simple — it's a NumPy object, not a framework artifact.
- **Stack Overflow Developer Survey record** (reused, lightly): One respondent's answers; a single row in the CSV. Same entity as L11. The notebook works with a small subset of columns (4–6 features + 1 derived binary target) and treats the loading as a one-cell black box delegated to pandas.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: After the lecture, a student can construct an `ndarray`, slice it, apply a boolean mask, and broadcast a 1-D vector against a 2-D matrix without referring back to the notebook — verified by completing Part 1 of the mini-project independently.
- **SC-002**: A student can explain in one sentence each (a) why NumPy is faster than a Python list, (b) what broadcasting means, and (c) what a sigmoid does in logistic regression — verified by short oral or written reflection.
- **SC-003**: A student can train the from-scratch logistic regression on the Survey subset and reach an accuracy in the 0.60–0.75 range with the lecture's default hyperparameters (learning rate 0.1, 1000 epochs) — verified by Part 2 of the mini-project producing the documented expected range. (Empirically measured at ≈0.64 on the 2025 schema — just 14% above the 0.50 random-baseline. The notebook explicitly discusses why a 4-feature linear model can't go much higher and frames this as a realistic outcome rather than a failure.)
- **SC-004**: The notebook runs end-to-end in a clean Python 3.13 environment with NumPy and pandas as the only required runtime dependencies (sklearn optional via the `try: import` guard), in under 90 seconds of wall-clock time on a typical student laptop (excluding the optional Survey CSV download from L11).
- **SC-005**: The notebook contains all required structural elements: learning objectives, 5+ runnable code examples, the 3-part "Survey Salary Classifier" mini-project (Parts 1–2 with hidden solution cells, Part 3 with reference solution + grading rubric), 2+ memes/visuals, 1+ diagram, References (NumPy docs, ODbL Survey link, optional sklearn LogisticRegression doc), Summary, and What's Next — verified by the checklist in `specs/017-lecture12-numpy-ml/checklists/requirements.md`.
- **SC-006**: After the lecture, a student can save a trained model to `.npz`, reload it into a fresh Python session, and produce predictions identical to the original — verified by reproducing the save/load round-trip cell.
- **SC-007**: After the lecture, at least 80% of students in an informal show-of-hands poll can correctly answer "what is the difference between accuracy and precision?" — verified by the instructor during the session.
- **SC-008**: A student can read the gradient-descent loop and identify (a) where the prediction is computed, (b) where the loss is computed, (c) where the gradient is computed, and (d) where the parameters are updated — verified by an in-class annotation exercise on a printed copy of the loop.

### Assumptions

- Students have completed L1–L5 and are comfortable with Python basics: types, collections, comprehensions, functions, basic file I/O. They have also completed L11, so `pd.read_csv`, column selection, `.dropna`, and `.values` / `.to_numpy()` are familiar enough to be used as a one-cell black box for dataset loading.
- Students have Python 3.13+ and Jupyter (notebook or lab) working locally; `numpy>=1.26` and `pandas>=2.2` are runtime dependencies. `scikit-learn` is OPTIONAL (only used in the gated coda cell) and MUST NOT be required for the notebook to run.
- The 2025 Stack Overflow Developer Survey CSV is either already present from L11 at `lectures/11-pandas-analytics/data/survey_results_public.csv` OR the synthetic-data fallback engages automatically — both paths produce a fully runnable notebook.
- The classroom laptop has at least 4 GB of free RAM. The Survey subset used for training is small (4–6 features × ~30K post-cleaning rows), so training fits comfortably in memory and converges in under a minute.
- Numerical reproducibility is achieved with `np.random.default_rng(seed=42)` for both the train/test split and (when used) the synthetic-data fallback. Identical seed → identical numbers across runs and machines.
- The lecture is standalone by design: no `notes-api` integration, consistent with the L11 precedent. The constitution's course-capstone thread resumes in L14 (deployment), with L13 providing the visualization layer over the same ML model trained here.
- "From scratch" excludes scikit-learn, PyTorch, TensorFlow, JAX, and any other ML framework. NumPy is the only library doing math. The sklearn coda is illustrative-only and explicitly framed as such.
- The binary classification target ("above-median compensation in respondent's country") is a deliberately simple, non-sensitive proxy chosen to make gradient descent visibly learn something on a real dataset within 1000 epochs. It is NOT framed as a serious salary-prediction model and the notebook will say so plainly.
