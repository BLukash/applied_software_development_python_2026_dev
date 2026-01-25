<!--
================================================================================
SYNC IMPACT REPORT
================================================================================
Version change: 1.0.0 → 1.0.1 (PATCH)

Modified principles: None

Added sections: None

Modified sections:
- Prohibited Practices: Added rule about minimal icon/emoji usage in content

Removed sections: None

Templates requiring updates:
- .specify/templates/plan-template.md: ✅ Compatible (no changes needed)
- .specify/templates/spec-template.md: ✅ Compatible (no changes needed)
- .specify/templates/tasks-template.md: ✅ Compatible (no changes needed)
- .specify/templates/commands/*.md: N/A (no command templates exist)

Follow-up TODOs:
- Review existing lecture content for excessive icon usage
================================================================================
-->

# Applied Software Development (Python) 2026 Course Constitution

## Core Principles

### I. Student-Centered Design

All content MUST prioritize student learning outcomes over comprehensive coverage.

- Each lecture MUST have clearly defined learning objectives stated at the beginning
- Complex concepts MUST be introduced with relatable real-world analogies and references to the additional resources where topic is explored in depth
- Content difficulty MUST progress from foundational to advanced within each topic
- Interactive elements (exercises, questions) MUST appear throughout, not just at the end
- Students MUST be able to run all code examples independently in their own environment
- Additional resources should not contain russian ones
- Memes should be used to ease the studying process

**Rationale**: Students learn best when they understand WHY they're learning something and can immediately practice it.

### II. Practical Application Focus

The course MUST emphasize building real, functional applications over theoretical knowledge.

- Python basics MUST be condensed to essential concepts needed for practical development, however, we should not omit interesting topics like, how data structures are stored in memory, history of language, plans for the future and so on 
- Every lecture from Lecture 5 onward MUST include at least one runnable mini-project
- Technologies covered MUST reflect current industry practices (FastAPI, SQLAlchemy, LLM utilization, RAG, etc.)
- Code examples MUST demonstrate industry-inspired patterns while staying minimal and teachable (avoid overengineering)
- Each mini-project MUST fit 20–30 minutes of in-class implementation + 30–60 minutes as homework extension.
- Database, API, and visualization topics MUST be integrated, not taught in isolation
- Pandas, Numpy, Matplotlib/Seaborn must be a primary topics for the second part of the course, however in combination of other parts, that bring practical part to it

**Rationale**: The course title is "Applied" Software Development - students need skills they can use immediately in real projects.

### III. Progressive Skill Building

Each lecture MUST build upon previous lectures while remaining self-contained enough for review.
- Lecture 1 — Python intro + environment setup
    Topics
    - What Python is (interpreted, dynamic, batteries-included) + where it’s used
    - Installing Python 3.11+, checking versions, PATH
    - IDE choice (VS Code / PyCharm) + recommended extensions
    - Running code: REPL vs script vs notebook (when to use what)
    - venv basics: create/activate/deactivate
    - pip basics: install/list/freeze, requirements
    - Your first program + simple I/O: print(), input()
    - Variables, basic types (int, float, str, bool, None)
    - Basic operators, formatting (f-strings)
- Lecture 2 — Core language mechanics (how Python “works”)
    Topics
    - Names vs values, references, identity (id()), mutability
    - Memory model intuition: list vs tuple, string immutability
    - Truthiness, comparisons, is vs ==
    - Control flow: if/elif/else, match (brief, optional)
    - Loops: for, while, break/continue, range()
    - Practical patterns: counting, searching, early exit
    - Intro to time measurements (very light) to motivate performance later
- Lecture 3 — Data structures + "Pythonic" patterns
    Topics
    - Collections: list, tuple, dict, set
    - Indexing/slicing, membership checks, nested structures
    - Common methods + pitfalls (.append, .extend, .get, .pop)
    - Iteration patterns: enumerate, zip
    - Comprehensions: list/dict/set comprehensions
    - Complexity intuition: lookup in dict/set vs list scan
    - Mini parsing task (e.g., parse logs / compute frequency table)
- Lecture 4 — Functions + modules + errors
    Topics
    - Functions: parameters, return, defaults, *args/**kwargs
    - Scope: local/global, closures (light)
    - Docstrings and readable APIs (PEP 257 style)
    - Exceptions: try/except/else/finally, raising your own
    - Basic debugging (breakpoints) + minimal logging (logging)
    - Modules & imports: import, from x import y, package layout
    - Building a tiny reusable module (e.g., utils/validators.py)
    - Type hints intro: list[int], dict[str, int], Optional
- Lecture 5 — OOP in Python (focused) + files/JSON/CSV
    Topics
    - Classes vs C#/Java/C++ mindset: simplicity + conventions
    - Attributes, methods, __init__, instance vs class vars
    - Inheritance (only what’s needed), composition > inheritance
    - @dataclass: why it matters, defaults, immutability option
    - Common dunder (magic) methods: __repr__, __str__
    - File I/O: open(), context managers, encoding (utf-8)
    - JSON: json.load/dump, schema-like thinking
    - CSV: csv module + pandas teaser
    - Prep for project: define data model for your future API entities
    At the end of Lecture 5 you have the “domain model” ready (dataclasses / schemas / file formats).
- Lecture 6 — REST + FastAPI fundamentals (project bootstrap)
    Topics
    - HTTP essentials: methods, status codes, headers, body
    - REST principles + CRUD mapping
    - example of simple http server with Python builtin packages
    - FastAPI basics: app, routers, endpoints
    - Request/response models with Pydantic
    - Validation + error responses
    - Auto docs: Swagger / OpenAPI
    - Running dev server: uvicorn
    - Project structure: /app, routers, schemas, services
    - Tooling intro: ruff, black (format/lint workflow)
    - Project increment:
    Create API skeleton + CRUD in-memory storage for Note / Document
- Lecture 7 — Async + HTTP clients + quality workflow
    Topics
    - Async intuition: event loop, async def, await
    - httpx (sync/async) for calling external APIs
    - Background tasks (FastAPI basics)
    - Environment variables + .env basics
    - Testing intro (early on purpose): pytest fundamentals, FastAPI TestClient. Arrange–Act–Assert
    - Code quality workflow: ruff check, ruff format (or black), Minimal pre-commit test run
    - Project increment:
    Add: endpoint that calls an external API (example: “quote of the day” / weather)
    Add: 5–8 tests for API routes
- Lecture 8 — Docker + PostgreSQL + API-DB connection
    Topics
    - Why containers: reproducible environment (reminder from prev OS course)
    - Docker basics: images/containers, volumes, ports
    - docker compose setup: FastAPI + Postgres
    - Connection strings, config separation
    - Postgres basics refresher: tables, keys, constraints
    - DB initialization scripts (optional)
    Project increment:
    Run project with docker compose
    Prepare DB container + connect from app (no ORM yet)
- Lecture 9 — SQLAlchemy ORM + sessions + real CRUD
    Topics
    - ORM concept: mapping classes ↔ tables
    - SQLAlchemy 2.0 core concepts:
    - Engine, Session, Models, select()
    - CRUD with ORM + transaction basics
    - Error handling: unique constraint violations, not found
    - DB design: indexes, relationships (intro only)
    - Project increment:
    Replace in-memory storage with Postgres + SQLAlchemy
    CRUD endpoints persist data properly
- Lecture 10 — Alembic migrations + relationships + repository pattern
    Topics
    - Why migrations, schema evolution mindset
    - Alembic: init, autogenerate, upgrade/downgrade
    - Relationships: one-to-many (e.g., user → notes) (simple)
    - Layering: router → service → repository (minimal clean architecture)
    - “Don’t leak ORM models into API schemas” rule (important)
    - Project increment:
    Add migrations + at least one relationship
    Refactor: introduce repository.py and service.py
- Lecture 11 — pandas analytics from DB exports
    Topics
    - What pandas is good for (and not)
    - Data loading: CSV + (optional) direct DB query into DataFrame
    - Cleaning: types, missing values, datetime parsing
    - groupby, aggregations, joins/merge
    - Practical analytics examples (real):
    - top tags, activity over time, usage statistics
    - When pandas breaks: memory + alternatives overview (DuckDB / Polars) (conceptual)
    - Project increment:
    Add “/analytics/report” endpoint that returns computed stats (via pandas pipeline)
- Lecture 12 — NumPy + vectorization + simple ML from scratch
    Topics
    - NumPy arrays vs Python lists (performance reasons)
    - Vectorization: broadcasting, dot, elementwise ops
    - Measuring performance (very light): %timeit idea
    - Simple ML model from scratch:  logistic regression binary classifier
    - Metrics basics: accuracy, precision/recall (minimal)
    - Saving/loading model parameters (np.save)
    - Project increment:
    Add “/ml/predict” endpoint: example: classify note as “important vs not” (toy but real pipeline)
- Lecture 13 — Visualization (storytelling) + project reporting
    Topics
    - Matplotlib basics: line/bar/hist/scatter
    - Seaborn for quick statistical plots
    - Plotly as optional interactive bonus
    - What makes a chart “good” (labels, scale, comparisons)
    - Generating reports: export plots as images, basic HTML report generation (optional)
    - Connect to project: “analytics as visuals”
    - Project increment:
    Add “/analytics/plots” endpoint returning plot images
- Lecture 14 — Shipping: packaging + deployment + “real project checklist”
    Topics
    - Project packaging basics: pyproject.toml, dependency pinning
    - Config management: .env, settings class
    - Logging best practices (minimal)
    - Production server idea: uvicorn workers / reverse proxy concept
    - Docker production layout (one compose for prod)
    - Very basic CI idea: run tests + lint on push (GitHub Actions overview)
    - Final wrap-up: what to learn next (celery, redis, auth, OpenAPI clients)
    Project increment:
    Final deliverable: Dockerized app + DB + migrations + docs + tests
- Each lecture MUST include a "Prerequisites" section listing required prior knowledge
- Cross-references to previous lectures MUST use consistent notation
- Course Capstone Thread: students build one evolving project across the semester: API → DB → analytics → visualization → deployment. Each lecture from the later stages adds one feature to the same repo.

**Rationale**: Clear progression prevents gaps in understanding and allows students to catch up if they miss lectures.

### IV. Quality Content Standards

All lecture materials MUST follow consistent formatting and quality guidelines.

- Format: Jupyter Notebook (.ipynb) with markdown cells and executable code cells
- Language: All explanatory text MUST be in Ukrainian
- Terminology rule: keep Ukrainian explanation + show the English technical term in parentheses once, where some programming specific language is used. Example: “винятки (exceptions)”, “типізація (type hints)”
- Code comments: MAY be in English for industry-standard terminology. But there should not bee too many comments, just for the complex parts
- Every lecture MUST include:
  - Learning objectives (at the start)
  - At least 5 runnable code examples
  - At least 2 practical exercises with solutions
  - References to official documentation and additional materials
  - At least 2 relevant meme or visual humor element (maintaining educational tone)
  - At least one diagram/table/visual explanation.
  - Summary and "What's Next" section (at the end)
- Duration target: 1.5 hours of lecture content per notebook

**Rationale**: Consistent format reduces cognitive load and helps students focus on content rather than navigation.

### V. Iterative Development

Course materials MUST be developed incrementally with no rush and with human validation at each stage.

- Each lecture MUST be reviewed for technical accuracy before finalization
- Code examples MUST be tested in a clean Python environment
- Lab works MUST align with and reinforce lecture content
- Student feedback mechanisms MUST be incorporated into revision cycles
- Version control MUST track all changes to lecture materials

**Rationale**: Educational content benefits from iteration; catching errors early prevents student confusion.

## Content Standards

### Lecture Structure Template

Each Jupyter notebook MUST follow this structure:

1. **Header**: Lecture number, title, date, prerequisites
2. **Learning Objectives**: 3-5 specific, measurable outcomes
3. **Introduction**: Context and motivation (include meme if appropriate here)
4. **Main Content**: 3-5 major sections with theory and practice interleaved
5. **Practical Exercise**: Hands-on coding task with starter code
6. **Summary**: Key takeaways in bullet points
7. **References**: Links to documentation, tutorials, further reading
8. **What's Next**: Preview of next lecture's topics

### Technology Stack

The course MUST use these specific technologies and tools:

- **Python**: 3.11+ (latest stable features)
- **Environment**: Jupyter Notebook / JupyterLab / Colab for simpel code examples, VS Code / PyCharm for projects
- **Data Processing**: pandas, numpy fundamentals
- **Visualization**: matplotlib, seaborn, plotly for interactive charts
- **Web Framework**: FastAPI (modern, async-first, well-documented)
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy 2.0+ (modern async support)
- **Testing**: pytest
- **Dependency and project management**: venv + pip, uv
- **Code quality**: ruff (lint) + black (format)
- **Contaienrs**: Docker + docker-compose
- **Version Control**: Git basics


### Prohibited Practices

- DO NOT include deprecated Python 2 syntax or patterns
- DO NOT use outdated libraries (e.g., Flask instead of FastAPI for new content)
- DO NOT copy code without attribution
- DO NOT include broken or untested code examples
- DO NOT exceed 1.5 hours of content per lecture (split if necessary)
- DO NOT hallucinate facts: every non-trivial claim must link to official docs
- DO NOT include huge copy-paste blocks without explanation
- DO NOT use 3d-party packages, when standard library has the same functionality
- DO NOT overuse icons/emojis in presentation text — they distract rather than help; use sparingly (1-2 per section maximum) and only where they add genuine value (e.g., checkmarks in summaries, warning signs for important notes)

## Development Workflow

### Phase 1: Lecture Specification

Before writing any lecture content:

1. Define learning objectives aligned with course progression
2. Outline major topics and time allocation
3. Identify code examples and exercises needed
4. List required external references and materials

### Phase 2: Content Creation

1. Create Jupyter notebook with structure template
2. Write explanatory text in Ukrainian
3. Develop and test all code examples
4. Create exercises with hidden solution cells
5. Add memes and visual elements appropriately

### Phase 3: Review and Validation

1. Technical review: All code runs correctly in clean environment
2. Content review: Ukrainian text is clear and grammatically correct
3. Pedagogical review: Learning objectives are met by content
4. Timing review: Content fits 1.5-hour lecture slot

### Phase 4: Lab Work Development

After lecture content is stable:

1. Design lab work that reinforces lecture concepts
2. Include clear instructions and expected outcomes
3. Provide starter code and test cases where appropriate
4. Create grading rubric aligned with learning objectives

## Governance

This constitution establishes binding principles for the "Applied Software Development (Python)" 2026 course development project.

### Amendment Process

1. Proposed changes MUST be documented with rationale
2. Changes affecting course structure require review of all affected lectures
3. Technology stack changes require migration plan for existing content
4. Version number MUST be incremented per semantic versioning rules

### Compliance

- All lecture notebooks MUST be validated against Content Standards before publication
- Code examples MUST pass execution tests before inclusion
- Deviations from principles MUST be documented and justified

### Versioning Policy

- **MAJOR**: Fundamental changes to course structure or principles
- **MINOR**: New sections, significant content additions
- **PATCH**: Clarifications, typo fixes, minor updates

**Version**: 1.0.1 | **Ratified**: 2026-01-24 | **Last Amended**: 2026-01-25
