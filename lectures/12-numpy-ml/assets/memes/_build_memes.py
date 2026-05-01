"""Generate placeholder meme images for Lecture 12.

These placeholders let the notebook render cleanly during smoke tests.
Instructors are encouraged to swap them for higher-quality generic meme
templates (see CREDITS.md). Re-run this script to regenerate::

    python lectures/12-numpy-ml/assets/memes/_build_memes.py
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

HERE = Path(__file__).parent


def _placeholder(out_path: Path, top_text: str, bottom_text: str,
                 punchline: str, accent: str) -> None:
    fig, ax = plt.subplots(figsize=(8, 4.5), dpi=140)
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4.5)
    ax.set_aspect("equal")
    ax.axis("off")

    # Border + background
    ax.add_patch(FancyBboxPatch(
        (0.1, 0.1), 7.8, 4.3,
        boxstyle="round,pad=0.05,rounding_size=0.18",
        linewidth=2.0, edgecolor="#1f1f1f", facecolor="#fafafa",
    ))
    # Accent bar
    ax.add_patch(FancyBboxPatch(
        (0.1, 3.55), 7.8, 0.85,
        boxstyle="round,pad=0.0,rounding_size=0.18",
        linewidth=0.0, facecolor=accent,
    ))
    ax.text(4, 3.97, top_text, ha="center", va="center",
            fontsize=18, fontweight="bold", color="#1f1f1f",
            family="DejaVu Sans")

    # Body
    ax.text(4, 2.55, bottom_text, ha="center", va="center",
            fontsize=15, color="#1f1f1f", family="DejaVu Sans")
    ax.text(4, 1.25, punchline, ha="center", va="center",
            fontsize=13, fontstyle="italic", color="#444",
            family="DejaVu Sans")
    ax.text(4, 0.4, "[placeholder — see CREDITS.md]", ha="center", va="center",
            fontsize=8, color="#888", family="DejaVu Sans")

    plt.tight_layout()
    fig.savefig(out_path, dpi=140, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Wrote {out_path}")


_placeholder(
    HERE / "numpy-vs-python-speed.png",
    top_text="Python loop vs NumPy",
    bottom_text="«Я просто посуну цикл for на 1 млн елементів»",
    punchline="NumPy: 0.41 ms      Python: 24.3 ms",
    accent="#ffe082",
)

_placeholder(
    HERE / "lr-is-just-sigmoid.png",
    top_text="Логістична регресія",
    bottom_text="Звучить страшно. Виглядає як магія.",
    punchline="Насправді — це σ(Xw + b) і одна формула градієнта.",
    accent="#c5e1a5",
)
