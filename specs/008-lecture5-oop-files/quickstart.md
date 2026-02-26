# Quickstart: Lecture 5 — OOP in Python and Working with Files

**Branch**: `008-lecture5-oop-files`
**Deliverable**: `lectures/05-oop-files/lecture-05.ipynb`

## Prerequisites

- Completed Lectures 1–4 content (or at least Lecture 4 for the direct predecessor context)
- Python 3.11+ installed and accessible
- JupyterLab or Jupyter Notebook installed (`pip install jupyterlab`)
- Optional (for pandas teaser cell): `pip install pandas`

## Step 1: Create the Lecture Directory

```bash
mkdir -p lectures/05-oop-files/assets/diagrams
mkdir -p lectures/05-oop-files/assets/memes
```

## Step 2: Create the Notebook

Create `lectures/05-oop-files/lecture-05.ipynb` by following the notebook structure contract at `specs/008-lecture5-oop-files/contracts/notebook-structure.md`.

The notebook follows the exact same cell structure as Lectures 1–4:
- Markdown cells for explanatory text (in Ukrainian)
- Code cells with inline Ukrainian comments
- Output cells immediately follow their code cell
- Exercise solutions in `<details>` HTML blocks

## Step 3: Gather Assets

### Diagrams

The following visuals are needed in `assets/diagrams/`:

| Visual | Recommended approach |
|--------|---------------------|
| OOP Pillars | Use inline markdown table (no download needed) |
| MRO Diagram | Download from Real Python or Python docs |
| JSON Types | Use inline markdown table (no download needed) |

Search terms for MRO diagram: `"Python MRO C3 linearization diagram"`

### Memes

The following memes are needed in `assets/memes/`:

| Meme | Placement | Search term |
|------|-----------|-------------|
| OOP humor | Section 0.1 intro | `"OOP meme python classes"` |
| Encoding humor | Section 4.2 encoding | `"encoding utf-8 meme"` or `"unicode error meme"` |

Download and save locally. Do NOT use remote image URLs — all images must be local assets (learned from Lecture 4 refinement).

## Step 4: Build the Mini-Project Entities

The Contact Book mini-project uses two Python entities (see `data-model.md`):

```python
# Contact — @dataclass (name, phone, email)
# ContactBook — full class with add/search/remove/save/load
```

Both entities must be implemented as notebook cells split into 4 progressive steps. See `contracts/notebook-structure.md` Section 8 for the exact step breakdown.

## Step 5: Validate Before Finalizing

Run all validation checks:

1. **Execution test**: Restart kernel → Run All Cells → verify zero errors
2. **Language check**: Confirm all markdown text is Ukrainian with English terms in parentheses
3. **Constitution checklist**:
   - [ ] ≥ 5 runnable code examples
   - [ ] ≥ 2 exercises with hidden solutions
   - [ ] ≥ 2 memes (local files only)
   - [ ] ≥ 1 diagram or table
   - [ ] Summary + "What's Next" sections present
   - [ ] Mini-project completable in 20–30 min
4. **Topic coverage**:
   - [ ] All 12 constitution topics covered (see spec.md FR-001 through FR-029)
   - [ ] All 5 educator enhancements covered (@property, @classmethod/@staticmethod, ABC, pathlib, context manager protocol)
5. **Timing estimate**: Read through notebook and estimate delivery time — must be ≤ 90 minutes

## Key Design Decisions

| Decision | Choice | Rationale |
|----------|--------|-----------|
| Mini-project domain | Contact Book | Universal, no domain complexity; natural fit for @dataclass + JSON |
| Persistence layer | JSON file | Connects File I/O section with OOP; simple, no dependencies |
| Contact model | `@dataclass` (not frozen) | Demonstrates @dataclass value; frozen=True shown as homework extension |
| ContactBook persistence | `@classmethod load_from_json()` | Classic "alternative constructor" pattern — teaches classmethod naturally |
| Abstraction example | `Shape(ABC)` → `Circle`, `Rectangle` | Timeless, universally understood domain for teaching polymorphism |
| Encapsulation example | `BankAccount` with `@property balance` | Relatable domain; balance validation is intuitive |
| pathlib | Primary API; os.path mentioned once | Modern Python standard; cross-platform |
| Encoding | Always utf-8; explicit in all examples | Ukrainian characters require explicit encoding |

## Files to Create

```text
lectures/05-oop-files/
├── lecture-05.ipynb          ← Main deliverable
└── assets/
    ├── diagrams/
    │   ├── mro-diagram.png   ← Downloaded from web (or inline markdown table)
    │   └── (others optional if using inline tables)
    └── memes/
        ├── oop-meme.png      ← OOP humor (for Section 0.1)
        └── encoding-meme.png ← Encoding humor (for Section 4.2)
```

## Cross-Reference Opportunities

When writing the notebook, include these cross-references to prior lectures:

| Topic | Cross-reference |
|-------|----------------|
| `__iter__`/`__next__` in dunder methods | "як ми бачили в Лекції 4 з ітераторами (iterators)..." |
| `with` context manager | "синтаксис `with`, який ми використаємо у Файловому I/O нижче..." |
| type hints in class methods | "продовжуємо використовувати анотації типів (type hints) з Лекції 4..." |
| `@dataclass` as decorator | "декоратори (decorators) ми розглядали в Лекції 4..." |
| Custom exceptions in mini-project | "для обробки помилок (error handling) використаємо try/except з Лекції 4..." |

## What's Next (for Summary cell)

Lecture 6: REST + FastAPI fundamentals
- "Ваш клас `Contact` з сьогоднішнього проєкту — це точна концептуальна основа для Pydantic-моделей у FastAPI"
- Preview topics: HTTP methods, endpoints, Pydantic schemas, auto-docs
