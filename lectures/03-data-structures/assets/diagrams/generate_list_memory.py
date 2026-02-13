"""
Generate an educational diagram showing Python list internal memory structure.
Outputs: list-memory.png in the same directory.
Run:  python generate_list_memory.py
"""

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

# ---------------------------------------------------------------------------
# Canvas setup
# ---------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(900 / 150, 600 / 150), dpi=150)
ax.set_xlim(0, 9)
ax.set_ylim(0, 6.5)
ax.axis("off")

# Font config - DejaVu Sans has good Cyrillic coverage
font_props = {"fontfamily": "DejaVu Sans"}
title_size = 11
label_size = 7.5
field_size = 6.5
small_size = 5.5

# ---------------------------------------------------------------------------
# Colours
# ---------------------------------------------------------------------------
CLR_LIST = "#D0E8FF"       # light blue  - PyListObject
CLR_INT  = "#D0F5D0"       # light green - PyObject (int)
CLR_EMPTY = "#E0E0E0"      # light gray  - empty slot
CLR_BORDER = "#333333"
CLR_ARROW = "#555555"


# ---------------------------------------------------------------------------
# Helper - draw a rounded box with centred text
# ---------------------------------------------------------------------------
def draw_box(x, y, w, h, color, texts, fontsize=field_size, bold_first=False,
             border_color=CLR_BORDER, linewidth=1.0):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.05",
        facecolor=color,
        edgecolor=border_color,
        linewidth=linewidth,
    )
    ax.add_patch(box)
    n = len(texts)
    for i, txt in enumerate(texts):
        ty = y + h - (i + 1) * h / (n + 1)
        weight = "bold" if (bold_first and i == 0) else "normal"
        ax.text(x + w / 2, ty, txt, ha="center", va="center",
                fontsize=fontsize, weight=weight, color="#222222",
                **font_props)
    return box


# ---------------------------------------------------------------------------
# 1. PyListObject box (top-centre)
# ---------------------------------------------------------------------------
list_x, list_y, list_w, list_h = 2.6, 4.4, 3.0, 1.7
draw_box(list_x, list_y, list_w, list_h, CLR_LIST,
         ["PyListObject", "ob_refcnt = 1", "ob_type = <list>",
          "ob_size = 3", "allocated = 4"],
         fontsize=field_size, bold_first=True)

# ---------------------------------------------------------------------------
# 2. Pointer array (4 slots) below PyListObject
# ---------------------------------------------------------------------------
slot_w = 1.1
slot_h = 0.55
gap = 0.15
total_w = 4 * slot_w + 3 * gap
array_x0 = (9 - total_w) / 2
array_y = 3.3

slot_labels = ["ptr -> 10", "ptr -> 20", "ptr -> 30", "NULL"]
slot_colors = [CLR_LIST, CLR_LIST, CLR_LIST, CLR_EMPTY]

slot_centres = []
for i in range(4):
    sx = array_x0 + i * (slot_w + gap)
    clr = slot_colors[i]
    draw_box(sx, array_y, slot_w, slot_h, clr,
             [slot_labels[i]], fontsize=small_size,
             linewidth=0.8)
    slot_centres.append((sx + slot_w / 2, array_y))

# Label above array
ax.annotate(
    "Масив вказівників (pointer array)",
    xy=((slot_centres[0][0] + slot_centres[2][0]) / 2, array_y + slot_h + 0.02),
    fontsize=label_size - 1, ha="center", va="bottom",
    color="#0055AA", weight="bold", **font_props,
)

# Arrow from PyListObject bottom-centre -> array
arrow_start = (list_x + list_w / 2, list_y)
arrow_end   = (list_x + list_w / 2, array_y + slot_h + 0.18)
ax.annotate(
    "", xy=arrow_end, xytext=arrow_start,
    arrowprops=dict(arrowstyle="-|>", color=CLR_ARROW, lw=1.2),
)

# Over-allocation label for the 4th slot
last_slot_x = array_x0 + 3 * (slot_w + gap)
ax.annotate(
    "Зайвий слот\n(over-allocation)",
    xy=(last_slot_x + slot_w / 2, array_y - 0.02),
    xytext=(last_slot_x + slot_w / 2, array_y - 0.50),
    fontsize=small_size, ha="center", va="top",
    color="#AA3300", weight="bold", **font_props,
    arrowprops=dict(arrowstyle="-|>", color="#AA3300", lw=0.9),
)

# ---------------------------------------------------------------------------
# 3. PyObject (int) boxes - below the first 3 slots
# ---------------------------------------------------------------------------
int_values = [10, 20, 30]
int_box_w = 1.3
int_box_h = 1.05
int_y = 1.4

for i, val in enumerate(int_values):
    cx = slot_centres[i][0]
    bx = cx - int_box_w / 2
    draw_box(bx, int_y, int_box_w, int_box_h, CLR_INT,
             ["PyObject (int)", "ob_refcnt = 1", "ob_val = {}".format(val)],
             fontsize=small_size, bold_first=True)
    arr_start = (cx, array_y)
    arr_end   = (cx, int_y + int_box_h + 0.04)
    ax.annotate(
        "", xy=arr_end, xytext=arr_start,
        arrowprops=dict(
            arrowstyle="-|>",
            color=CLR_ARROW,
            lw=1.1,
            connectionstyle="arc3,rad=0",
        ),
    )

# ---------------------------------------------------------------------------
# 4. Title and attribution
# ---------------------------------------------------------------------------
ax.text(4.5, 6.25, "Внутрішня структура list у Python",
        ha="center", va="center", fontsize=title_size,
        weight="bold", color="#003366", **font_props)

ax.text(4.5, 0.25,
        "Inspired by Laurent Luce's Python List Implementation",
        ha="center", va="center", fontsize=5, color="#888888",
        style="italic", **font_props)

# ---------------------------------------------------------------------------
# Legend boxes (top-right)
# ---------------------------------------------------------------------------
legend_items = [
    (CLR_LIST,  "PyListObject / pointer"),
    (CLR_INT,   "PyObject (int)"),
    (CLR_EMPTY, "Empty slot (NULL)"),
]
lx_start = 6.8
ly_start = 5.9
for idx, (clr, label) in enumerate(legend_items):
    ly = ly_start - idx * 0.32
    rect = FancyBboxPatch((lx_start, ly - 0.1), 0.22, 0.22,
                           boxstyle="round,pad=0.02",
                           facecolor=clr, edgecolor=CLR_BORDER, linewidth=0.6)
    ax.add_patch(rect)
    ax.text(lx_start + 0.32, ly, label, fontsize=4.5, va="center",
            color="#333333", **font_props)

# ---------------------------------------------------------------------------
# Save
# ---------------------------------------------------------------------------
out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "list-memory.png")
fig.savefig(out_path, bbox_inches="tight", pad_inches=0.15, facecolor="white")
plt.close(fig)
print("Saved diagram to:", out_path)
