# Memes — Credits & Sourcing

This directory holds the two memes embedded in the Lecture 12 notebook.

## Files

| File | Used in section | Caption / template intent |
|------|-----------------|---------------------------|
| `numpy-vs-python-speed.png` | Section 8 — `%timeit` Python vs NumPy | Riff on the ~100×–500× speed gap. Suggested template: "Drake approving / disapproving" or "expanding-brain". |
| `lr-is-just-sigmoid.png` | Section 9 — Перехід до ML | Riff on the "logistic regression sounds scary; actually it's just σ + cross-entropy" insight. Suggested template: "How it started / How it's going" or "It's not magic, it's just X". |

## License

The currently-committed PNGs are **placeholder images** rendered programmatically by `_build_memes.py` so the notebook displays cleanly out-of-the-box. Re-run that script after editing it to regenerate them.

Instructors are encouraged to replace these placeholders with higher-quality generic meme templates that:

- Use **public-domain meme templates** (no copyrighted characters beyond standard meme-culture imagery).
- Contain **no russian-language text or russian-cultural references** (Constitution Principle I).
- Render legibly at slide-projection size (≥ 600 px wide, sans-serif body text ≥ 24 pt).

If you swap in a hand-sourced PNG, please:

1. Update this file with the source URL / template name and the meme's author/license.
2. Keep the filename stable (`numpy-vs-python-speed.png`, `lr-is-just-sigmoid.png`) so the notebook's image references continue to resolve.
3. If the notebook caption needs to change, edit it in `lecture-12.ipynb` rather than relying on the filename.
