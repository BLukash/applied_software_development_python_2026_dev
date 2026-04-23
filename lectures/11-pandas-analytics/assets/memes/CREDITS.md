# Meme assets — credits and sourcing log

Per spec FR-021 and FR-026 (no russian sources) and research.md R10.

## Required files (2 memes minimum)

### 1. `first-time-pandas.png` — embedded at start of Section 5 (cleaning)

**Template**: "First time?" (generic meme format, classic internet template).
**Caption (Ukrainian)**: "Справжні CSV-дані — перший раз?"
(Real CSV data — first time?)

**Suggested source** (check license before committing):
- <https://imgflip.com/memegenerator/First-Time> — generate with the Ukrainian caption above, export as PNG.
- Or: hand-drawn SVG with the same joke, exported to PNG.

### 2. `merge-explosion-validate.png` — embedded near end of Section 9 (merge)

**Template**: any "explosion" / "surprised Pikachu" / "everything is fine (dog in fire)" format.
**Caption (Ukrainian)**: "Коли забув `validate='one_to_many'` у `merge`" — top;
"Датафрейм виріс із 50 000 до 500 000 рядків" — bottom.

**Suggested source**:
- <https://imgflip.com/memegenerator> — pick a generic explosion/surprise template, apply the Ukrainian caption, export PNG.

## Sourcing rules (per Constitution Principle I and FR-026)

- ✅ Allowed: imgflip generator, know-your-meme generic templates, public-domain clip art, hand-drawn originals.
- ❌ Forbidden: russian-language meme platforms (pikabu.ru, dvach, vk communities), any russian-language captions.
- ❌ Forbidden: copyrighted character likenesses beyond fair-use meme territory.

## How to commit

1. Place the PNG in this directory with the exact filename shown above.
2. Record the source URL (or "hand-drawn") + author/license below in this file before committing.
3. Keep each PNG ≤ 300 KB — use 1024×768 or smaller; compress with `pngquant` if needed.

## Source log

<!-- Fill in when assets are committed. Example:
- first-time-pandas.png — generated at imgflip.com/i/ABC123 on 2026-04-23 by @instructor, public domain.
- merge-explosion-validate.png — generated at imgflip.com/i/XYZ789 on 2026-04-23 by @instructor, public domain.
-->

- `first-time-pandas.png` — **NOT YET COMMITTED** (placeholder path only)
- `merge-explosion-validate.png` — **NOT YET COMMITTED** (placeholder path only)

## Impact on notebook execution

The notebook's markdown cells reference these image paths (`![](assets/memes/first-time-pandas.png)`). If the PNGs are missing, Jupyter will render a broken-image icon but all **code** cells still execute cleanly, so `jupyter nbconvert --execute` will still pass. The memes are pedagogical garnish, not correctness-critical.
