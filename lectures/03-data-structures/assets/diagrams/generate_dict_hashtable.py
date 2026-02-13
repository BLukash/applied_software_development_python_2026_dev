#!/usr/bin/env python3
# Auto-generated builder for dict-hashtable diagram
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

fig_w, fig_h = 900/150, 700/150
fig, ax = plt.subplots(figsize=(fig_w, fig_h), dpi=150)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

FONT = {"fontfamily": "DejaVu Sans"}
FONT_BOLD = {**FONT, "fontweight": "bold"}

CLR_KEY = "#FFF59D"
CLR_VAL = "#A5D6A7"
CLR_SLOT = "#E1BEE7"
CLR_EMPTY = "#F5F5F5"
CLR_ARROW = "#5C6BC0"
CLR_HASH_BOX = "#BBDEFB"
fig.patch.set_facecolor("#FFFFFF")

# Title
ax.text(5, 9.65,
        "Хеш-таблиця (hash table) — основа dict та set",
        ha="center", va="center", fontsize=9.5, color="#212121", **FONT_BOLD)

# Dict literal
dict_y = 8.85
dict_box = FancyBboxPatch((1.3, dict_y - 0.25), 7.4, 0.5,
    boxstyle="round,pad=0.12", linewidth=1.2,
    edgecolor="#616161", facecolor="#FFF9C4")
ax.add_patch(dict_box)
ax.text(5, dict_y,
    '{"name": "Іван",  "age": 25,  "city": "Київ"}',
    ha="center", va="center", fontsize=7.2, family="monospace", color="#333333")

# Hash mapping rows
q = chr(34)
mappings = [
    (q+"name"+q, "slot 3", 3),
    (q+"age"+q,  "slot 7", 7),
    (q+"city"+q, "slot 1", 1),
]

start_y = 7.8
row_gap = 0.65

for i, (key, slot_label, _slot_idx) in enumerate(mappings):
    y = start_y - i * row_gap
    kx = 1.8
    kw, kh = 1.3, 0.40
    key_box = FancyBboxPatch((kx - kw/2, y - kh/2), kw, kh,
        boxstyle="round,pad=0.08", linewidth=1,
        edgecolor="#F9A825", facecolor=CLR_KEY)
    ax.add_patch(key_box)
    ax.text(kx, y, key, ha="center", va="center", fontsize=7,
        family="monospace", color="#333")
    ax.annotate("", xy=(3.55, y), xytext=(2.5, y),
        arrowprops=dict(arrowstyle="->,head_width=0.18,head_length=0.12",
        color=CLR_ARROW, lw=1.3))
    hx = 4.55
    hw, hh = 1.5, 0.40
    hash_box = FancyBboxPatch((hx - hw/2, y - hh/2), hw, hh,
        boxstyle="round,pad=0.08", linewidth=1,
        edgecolor="#1565C0", facecolor=CLR_HASH_BOX)
    ax.add_patch(hash_box)
    ax.text(hx, y, "hash()", ha="center", va="center", fontsize=7,
        family="monospace", fontweight="bold", color="#0D47A1")
    ax.annotate("", xy=(6.4, y), xytext=(5.35, y),
        arrowprops=dict(arrowstyle="->,head_width=0.18,head_length=0.12",
        color=CLR_ARROW, lw=1.3))
    sx = 7.4
    sw, sh = 1.3, 0.40
    slot_box = FancyBboxPatch((sx - sw/2, y - sh/2), sw, sh,
        boxstyle="round,pad=0.08", linewidth=1,
        edgecolor="#7B1FA2", facecolor=CLR_SLOT)
    ax.add_patch(slot_box)
    ax.text(sx, y, slot_label, ha="center", va="center", fontsize=7,
        family="monospace", color="#4A148C")

# Label between dict and hash rows
ax.text(5, 8.35,
    "hash() обчислює номер слота",
    ha="center", va="center", fontsize=7, style="italic",
    color="#5C6BC0", **FONT)

# Hash table array
table_top = 5.5
slot_h = 0.48
slot_w = 5.4
table_x = 2.3

slot_data = {
    1: (q+"city"+q, q+"Київ"+q),
    3: (q+"name"+q, q+"Іван"+q),
    7: (q+"age"+q, "25"),
}

ax.text(5, table_top + 0.35,
    "Hash table (масив із 8 слотів)",
    ha="center", va="center", fontsize=7.5, color="#424242", **FONT_BOLD)

for idx in range(8):
    y = table_top - idx * slot_h
    is_filled = idx in slot_data
    ax.text(table_x - 0.35, y, f"[{idx}]", ha="center", va="center",
        fontsize=6.5, family="monospace", color="#757575")
    if is_filled:
        key_str, val_str = slot_data[idx]
        key_w = 2.2
        key_rect = FancyBboxPatch((table_x, y - slot_h/2 + 0.04), key_w, slot_h - 0.08,
            boxstyle="round,pad=0.05", linewidth=0.8,
            edgecolor="#F9A825", facecolor=CLR_KEY)
        ax.add_patch(key_rect)
        ax.text(table_x + key_w/2, y, key_str, ha="center", va="center",
            fontsize=6.5, family="monospace", color="#333")
        val_rect = FancyBboxPatch((table_x + key_w + 0.1, y - slot_h/2 + 0.04),
            slot_w - key_w - 0.1, slot_h - 0.08,
            boxstyle="round,pad=0.05", linewidth=0.8,
            edgecolor="#2E7D32", facecolor=CLR_VAL)
        ax.add_patch(val_rect)
        ax.text(table_x + key_w + 0.1 + (slot_w - key_w - 0.1)/2, y, val_str,
            ha="center", va="center", fontsize=6.5, family="monospace",
            color="#1B5E20")
    else:
        empty_rect = FancyBboxPatch((table_x, y - slot_h/2 + 0.04), slot_w, slot_h - 0.08,
            boxstyle="round,pad=0.05", linewidth=0.6,
            edgecolor="#BDBDBD", facecolor=CLR_EMPTY, linestyle="--")
        ax.add_patch(empty_rect)
        ax.text(table_x + slot_w/2, y,
            "— пусто —",
            ha="center", va="center",
            fontsize=6, color="#BDBDBD", style="italic", **FONT)

# Arrows from slot labels to hash-table rows
for _i, (_key, _slot_label, slot_idx) in enumerate(mappings):
    target_y = table_top - slot_idx * slot_h
    src_y = start_y - _i * row_gap - 0.25
    ax.annotate("",
        xy=(table_x + slot_w + 0.2, target_y),
        xytext=(8.05, src_y),
        arrowprops=dict(arrowstyle="->,head_width=0.15,head_length=0.1",
            color="#AB47BC", lw=1.0,
            connectionstyle="arc3,rad=0.25"))

# Notes
note_y = table_top - 8 * slot_h - 0.2
ax.text(5, note_y,
    "O(1) — прямий доступ за хешем",
    ha="center", va="center", fontsize=8, color="#C62828",
    **FONT_BOLD,
    bbox=dict(boxstyle="round,pad=0.3", facecolor="#FFEBEE",
              edgecolor="#EF9A9A", linewidth=1))

analogy_y = note_y - 0.55
ax.text(5, analogy_y,
    "Як роздягальня: знаєш номер шафки → йдеш прямо туди",
    ha="center", va="center", fontsize=6.5, color="#6D4C41",
    style="italic", **FONT,
    bbox=dict(boxstyle="round,pad=0.25", facecolor="#EFEBE9",
              edgecolor="#BCAAA4", linewidth=0.8))

# Save
out_dir = os.path.dirname(os.path.abspath(__file__))
out_path = os.path.join(out_dir, "dict-hashtable.png")
plt.tight_layout(pad=0.3)
fig.savefig(out_path, dpi=150, bbox_inches="tight",
    facecolor=fig.get_facecolor(), edgecolor="none")
plt.close(fig)
print(f"Saved: {out_path}")
