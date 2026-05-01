"""Build the logistic-regression flow diagram for Lecture 12.

Re-run this script to regenerate ``lr-flow.png``::

    python lectures/12-numpy-ml/assets/diagrams/_build_lr_flow.py

The diagram shows the forward pass (data → linear → sigmoid → loss) with the
backward update arrow that closes the gradient-descent loop.
"""
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

OUT = Path(__file__).with_name("lr-flow.png")

# Colors — print-safe, color-blind-safe
DATA_COLOR = "#dbe7f5"
LINEAR_COLOR = "#fff2cf"
SIGMOID_COLOR = "#dcecd4"
LOSS_COLOR = "#f8d4d4"
PARAM_COLOR = "#ece6f5"
EDGE_COLOR = "#3a3a3a"
ARROW_COLOR = "#3a3a3a"
UPDATE_COLOR = "#b3261e"

fig, ax = plt.subplots(figsize=(11, 4.6), dpi=160)
ax.set_xlim(0, 11)
ax.set_ylim(0, 4.6)
ax.set_aspect("equal")
ax.axis("off")


def box(x, y, w, h, label, color):
    """Draw a labeled rounded box."""
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.04,rounding_size=0.18",
        linewidth=1.4, edgecolor=EDGE_COLOR, facecolor=color,
    )
    ax.add_patch(patch)
    ax.text(x + w / 2, y + h / 2, label, ha="center", va="center",
            fontsize=12, family="DejaVu Sans")


def arrow(x1, y1, x2, y2, color=ARROW_COLOR, lw=1.4, style="->",
          rad=0.0, label=None, label_xy=None):
    a = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle=style, color=color, linewidth=lw,
        mutation_scale=14,
        connectionstyle=f"arc3,rad={rad}",
    )
    ax.add_patch(a)
    if label is not None and label_xy is not None:
        ax.text(*label_xy, label, ha="center", va="center",
                fontsize=10, color=color, family="DejaVu Sans",
                bbox=dict(facecolor="white", edgecolor="none", pad=1.5))


# Forward pass — top row
y_top = 2.9
box(0.2, y_top, 1.6, 0.9, "X\n(n, p)", DATA_COLOR)
box(2.4, y_top, 2.0, 0.9, "z = X @ w + b\n(linear)", LINEAR_COLOR)
box(5.0, y_top, 1.8, 0.9, "ŷ = σ(z)\n(sigmoid)", SIGMOID_COLOR)
box(7.4, y_top, 2.0, 0.9, "L = BCE(y, ŷ)\n(loss)", LOSS_COLOR)

# Forward arrows
arrow(1.8, y_top + 0.45, 2.4, y_top + 0.45)
arrow(4.4, y_top + 0.45, 5.0, y_top + 0.45)
arrow(6.8, y_top + 0.45, 7.4, y_top + 0.45)

# Parameters node — bottom row
y_bot = 0.6
box(2.4, y_bot, 2.0, 0.9, "params (w, b)", PARAM_COLOR)

# Up-arrow: params feed the linear box
arrow(3.4, y_bot + 0.9, 3.4, y_top, color="#5b6770", lw=1.2)

# Backward update arrow: from loss back to params
arrow(8.4, y_top, 4.4, y_bot + 0.45,
      color=UPDATE_COLOR, lw=1.6, rad=-0.25,
      label="оновлення:  w ← w − η·∂L/∂w,   b ← b − η·∂L/∂b",
      label_xy=(6.4, 1.45))

# Title
ax.text(5.5, 4.3, "Цикл навчання логістичної регресії",
        ha="center", va="center", fontsize=14, fontweight="bold",
        family="DejaVu Sans")

plt.tight_layout()
fig.savefig(OUT, dpi=160, bbox_inches="tight", facecolor="white")
print(f"Wrote {OUT}")
