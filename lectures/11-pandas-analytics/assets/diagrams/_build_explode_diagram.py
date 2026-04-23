"""Generate explode-schematic.png — the FR-022 diagram for Lecture 11.

Renders two side-by-side mini-tables illustrating the row-multiplication of
`.str.split(";").explode()` on a semicolon-separated multi-value column.
Reproducible: re-run this script from the repository root (with matplotlib
installed) to regenerate the PNG.

Usage:
    python lectures/11-pandas-analytics/assets/diagrams/_build_explode_diagram.py
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

HERE = Path(__file__).parent
OUT = HERE / "explode-schematic.png"


def render() -> None:
    fig, (ax_before, ax_after) = plt.subplots(1, 2, figsize=(11, 4.2), dpi=150)
    fig.suptitle(
        "str.split(';').explode() — одне значення на рядок",
        fontsize=14,
        fontweight="bold",
    )

    before_rows = [
        ["1", "Ukraine", "Python;JavaScript;Go"],
        ["2", "USA", "Python;Rust"],
        ["3", "Poland", "JavaScript"],
    ]
    before_header = ["ResponseId", "Country", "LanguageHaveWorkedWith"]

    after_rows = [
        ["1", "Ukraine", "Python"],
        ["1", "Ukraine", "JavaScript"],
        ["1", "Ukraine", "Go"],
        ["2", "USA", "Python"],
        ["2", "USA", "Rust"],
        ["3", "Poland", "JavaScript"],
    ]
    after_header = ["ResponseId", "Country", "Language"]

    def draw(ax, header, rows, title, highlight_col: int | None = None):
        ax.set_title(title, fontsize=12, pad=10)
        ax.axis("off")
        table = ax.table(
            cellText=rows,
            colLabels=header,
            loc="center",
            cellLoc="left",
            colColours=["#DCE6F1"] * len(header),
        )
        table.auto_set_font_size(False)
        table.set_fontsize(10)
        table.scale(1.0, 1.6)
        if highlight_col is not None:
            for r in range(1, len(rows) + 1):
                cell = table[(r, highlight_col)]
                cell.set_facecolor("#FFF2CC")

    draw(ax_before, before_header, before_rows, "До: 3 рядки", highlight_col=2)
    draw(ax_after, after_header, after_rows, "Після: 6 рядків", highlight_col=2)

    # Arrow between tables
    arrow = FancyArrowPatch(
        (0.47, 0.45),
        (0.53, 0.45),
        transform=fig.transFigure,
        arrowstyle="->",
        mutation_scale=28,
        color="#2F5496",
        linewidth=2.0,
    )
    fig.patches.append(arrow)
    fig.text(
        0.50,
        0.57,
        ".str.split(';')\n.explode()",
        ha="center",
        va="center",
        fontsize=10,
        fontfamily="monospace",
        color="#2F5496",
    )

    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig(OUT, bbox_inches="tight", facecolor="white")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    render()
