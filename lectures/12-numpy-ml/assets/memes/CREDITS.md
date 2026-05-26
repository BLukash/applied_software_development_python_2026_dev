# Memes — Credits & Sourcing

The Lecture 12 notebook embeds memes **by URL**, not by local file. There are
currently no images committed to this directory.

## Embedded comics (all xkcd)

| Section | Comic | URL |
|---------|-------|-----|
| 8 — `%timeit` Python vs NumPy | xkcd 1205 — *Is It Worth the Time?* | <https://xkcd.com/1205/> |
| 11 — NumPy на даних Survey 2025 | xkcd 2400 — *Statistics* | <https://xkcd.com/2400/> |
| 13 — Виявлення викидів через IQR | xkcd 1798 — *Box Plot* | <https://xkcd.com/1798/> |
| 16 — Функції втрат (MSE, MAE, RMSE) | xkcd 2048 — *Curve-Fitting* | <https://xkcd.com/2048/> |

## License

xkcd comics by Randall Munroe are licensed under
[**Creative Commons Attribution-NonCommercial 2.5**](https://xkcd.com/license.html).
Inline attribution is provided in each markdown cell that embeds a comic.

## If a hot-linked image breaks

xkcd image URLs follow the stable pattern `https://imgs.xkcd.com/comics/<slug>.png`
and are cached aggressively by their CDN. If a URL stops resolving, check the
landing page (`https://xkcd.com/<num>/`) for the current image path and update
the notebook accordingly.

## Adding new memes

When choosing a new meme:

- Prefer **stable hosts** (xkcd, Wikimedia Commons, GitHub raw URLs in
  long-established repos). Avoid imgur / 9gag / random forum hosts — they break.
- Verify the **license** allows embedding (xkcd CC BY-NC 2.5 is fine for
  non-commercial classroom use; always credit the author inline).
- Constitution Principle I: **no russian-language text or russian-cultural
  references** in any embedded image.
- Add a row to the table above so the inventory stays current.
