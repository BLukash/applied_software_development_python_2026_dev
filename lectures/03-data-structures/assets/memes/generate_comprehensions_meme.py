"""
Generate an "Expanding Brain" meme about Python comprehension readability.
Run:  python generate_comprehensions_meme.py
Saves: comprehensions-meme.png in the same directory.
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.patheffects as pe
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from pathlib import Path

OUTPUT = Path(__file__).parent / "comprehensions-meme.png"

levels = [
    {
        "label": "for \u0446\u0438\u043a\u043b",
        "code": "result = []\nfor x in items:\n    result.append(x**2)",
        "bg_colors": ["#e8eaf6", "#c5cae9"],
        "brain_color": "#90a4ae",
        "brain_glow": None,
        "brain_scale": 0.55,
        "brain_rings": 0,
        "code_size": 11,
    },
    {
        "label": "List comprehension",
        "code": "[x**2 for x in items]",
        "bg_colors": ["#e0f7fa", "#80deea"],
        "brain_color": "#4fc3f7",
        "brain_glow": None,
        "brain_scale": 0.72,
        "brain_rings": 1,
        "code_size": 13,
    },
    {
        "label": "Filtered comprehension",
        "code": "[x**2 for x in items if x > 0]",
        "bg_colors": ["#fff9c4", "#fff176"],
        "brain_color": "#ffb300",
        "brain_glow": "#ffe082",
        "brain_scale": 0.88,
        "brain_rings": 2,
        "code_size": 13,
    },
    {
        "label": "Nested comprehension",
        "code": "[f(x) for sublist in matrix\n for x in sublist\n if pred(x) and g(x)]",
        "bg_colors": ["#ffccbc", "#ff7043"],
        "brain_color": "#ff1744",
        "brain_glow": "#ffeb3b",
        "brain_scale": 1.0,
        "brain_rings": 3,
        "code_size": 11.5,
    },
]

fig_w, fig_h = 800 / 150, 900 / 150
fig, axes = plt.subplots(
    len(levels), 1,
    figsize=(fig_w, fig_h),
    dpi=150,
    gridspec_kw={"hspace": 0.0},
)
fig.patch.set_facecolor("#1a1a2e")


def draw_gradient_bg(ax, color_left, color_right):
    gradient = np.linspace(0, 1, 256).reshape(1, -1)
    cmap = LinearSegmentedColormap.from_list("bg", [color_left, color_right])
    ax.imshow(gradient, aspect="auto", cmap=cmap, extent=[0, 1, 0, 1], zorder=0)


def draw_brain(ax, cx, cy, scale, base_color, glow_color, rings):
    if glow_color:
        for i in range(rings, 0, -1):
            glow_r = scale * 0.18 + i * 0.035
            glow_circle = plt.Circle(
                (cx, cy), glow_r,
                color=glow_color, alpha=0.12 + 0.04 * i,
                transform=ax.transAxes, zorder=1,
            )
            ax.add_patch(glow_circle)

    r = scale * 0.18
    brain = plt.Circle(
        (cx, cy), r,
        color=base_color, ec="white", linewidth=1.5,
        transform=ax.transAxes, zorder=2,
    )
    ax.add_patch(brain)

    n_bumps = int(6 + rings * 3)
    bump_r = r * 0.32
    for k in range(n_bumps):
        angle = 2 * np.pi * k / n_bumps
        bx = cx + r * 0.78 * np.cos(angle)
        by = cy + r * 0.78 * np.sin(angle)
        bump = plt.Circle(
            (bx, by), bump_r,
            color=base_color, ec="white", linewidth=0.7,
            transform=ax.transAxes, zorder=2,
        )
        ax.add_patch(bump)

    for k in range(2 + rings):
        angle = np.pi * 0.3 + k * np.pi / (3 + rings)
        x0 = cx + r * 0.1 * np.cos(angle)
        y0 = cy + r * 0.1 * np.sin(angle)
        x1 = cx + r * 0.55 * np.cos(angle)
        y1 = cy + r * 0.55 * np.sin(angle)
        ax.plot(
            [x0, x1], [y0, y1],
            color="white", alpha=0.5, linewidth=0.8,
            transform=ax.transAxes, zorder=3,
        )

    if rings >= 3:
        for angle_deg in [30, 110, 200, 290]:
            angle = np.radians(angle_deg)
            sx = cx + r * 1.35 * np.cos(angle)
            sy = cy + r * 1.35 * np.sin(angle)
            ex = cx + r * 1.9 * np.cos(angle)
            ey = cy + r * 1.9 * np.sin(angle)
            mx = (sx + ex) / 2 + 0.015 * np.sin(angle)
            my = (sy + ey) / 2 - 0.015 * np.cos(angle)
            ax.plot(
                [sx, mx, ex], [sy, my, ey],
                color="#ffeb3b", linewidth=2, alpha=0.9,
                transform=ax.transAxes, zorder=4,
            )


for idx, (ax, lv) in enumerate(zip(axes, levels)):
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)

    draw_gradient_bg(ax, lv["bg_colors"][0], lv["bg_colors"][1])

    if idx > 0:
        ax.axhline(y=1.0, color="#1a1a2e", linewidth=2, zorder=10)

    draw_brain(
        ax, cx=0.18, cy=0.50,
        scale=lv["brain_scale"],
        base_color=lv["brain_color"],
        glow_color=lv["brain_glow"],
        rings=lv["brain_rings"],
    )

    ax.text(
        0.62, 0.88, lv["label"],
        transform=ax.transAxes, ha="center", va="top",
        fontsize=10, fontfamily="DejaVu Sans",
        fontweight="bold", color="#263238",
        zorder=5,
    )

    code_lines = lv["code"].split("\n")
    code_y_start = 0.72 if len(code_lines) > 1 else 0.55

    box_h = 0.12 + 0.14 * (len(code_lines) - 1)
    box_y = code_y_start - box_h + 0.06
    code_bg = patches.FancyBboxPatch(
        (0.36, max(box_y, 0.05)), 0.58, min(box_h, 0.88),
        boxstyle="round,pad=0.025",
        facecolor="#263238", alpha=0.82,
        transform=ax.transAxes, zorder=4,
    )
    ax.add_patch(code_bg)

    ax.text(
        0.39, code_y_start, lv["code"],
        transform=ax.transAxes, ha="left", va="top",
        fontsize=lv["code_size"], fontfamily="DejaVu Sans Mono",
        color="#e0f7fa", linespacing=1.35,
        zorder=5,
        path_effects=[pe.withStroke(linewidth=0.6, foreground="#000000")],
    )

fig.text(
    0.50, 0.99,
    "Expanding Brain: Python Comprehensions",
    ha="center", va="top",
    fontsize=13, fontfamily="DejaVu Sans", fontweight="bold",
    color="#ffffff",
    path_effects=[pe.withStroke(linewidth=2, foreground="#1a1a2e")],
)

plt.subplots_adjust(left=0.01, right=0.99, top=0.96, bottom=0.01)
plt.savefig(
    OUTPUT,
    dpi=150,
    facecolor=fig.get_facecolor(),
    edgecolor="none",
    bbox_inches="tight",
    pad_inches=0.08,
)
plt.close(fig)
print(f"Meme saved to: {OUTPUT}")
