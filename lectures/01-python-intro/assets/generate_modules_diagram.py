"""
Generate Modules vs Packages diagram for Lecture 1.
Shows the difference between a module (single file) and a package (directory).
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch

# Python colors
PYTHON_BLUE = '#306998'
PYTHON_YELLOW = '#FFD43B'
LIGHT_BLUE = '#E8F4FD'
LIGHT_YELLOW = '#FFF8E1'

fig, ax = plt.subplots(figsize=(14, 8))

# === LEFT SIDE: Module ===
# File icon
file_x, file_y = 2, 5
file_width, file_height = 1.5, 2

# File shape (rectangle with folded corner)
file_body = mpatches.FancyBboxPatch(
    (file_x, file_y), file_width, file_height,
    boxstyle="round,pad=0.05",
    facecolor=LIGHT_YELLOW,
    edgecolor=PYTHON_YELLOW,
    linewidth=3
)
ax.add_patch(file_body)

# Folded corner effect
corner_x = file_x + file_width - 0.3
corner_y = file_y + file_height
ax.fill([corner_x, corner_x + 0.3, corner_x + 0.3, corner_x],
        [corner_y, corner_y, corner_y - 0.3, corner_y],
        color='#E6C200', edgecolor=PYTHON_YELLOW, linewidth=1)

# .py extension
ax.text(file_x + file_width/2, file_y + file_height/2 + 0.3, ".py",
        ha='center', va='center', fontsize=20, fontweight='bold', color=PYTHON_BLUE)

# File name
ax.text(file_x + file_width/2, file_y + file_height/2 - 0.3, "utils.py",
        ha='center', va='center', fontsize=11, color='#666666')

# Module label
ax.text(file_x + file_width/2, file_y - 0.5, "Модуль (Module)",
        ha='center', va='center', fontsize=14, fontweight='bold', color=PYTHON_BLUE)

ax.text(file_x + file_width/2, file_y - 0.9, "один .py файл",
        ha='center', va='center', fontsize=10, color='#666666')

# Import example
ax.text(file_x + file_width/2, file_y - 1.5, "import utils",
        ha='center', va='center', fontsize=11, fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

# === RIGHT SIDE: Package ===
pkg_x, pkg_y = 8, 4.5
pkg_width, pkg_height = 4, 3.5

# Package folder
folder = mpatches.FancyBboxPatch(
    (pkg_x, pkg_y), pkg_width, pkg_height,
    boxstyle="round,pad=0.1",
    facecolor=LIGHT_BLUE,
    edgecolor=PYTHON_BLUE,
    linewidth=3
)
ax.add_patch(folder)

# Folder tab
tab = mpatches.FancyBboxPatch(
    (pkg_x + 0.2, pkg_y + pkg_height - 0.1), 1.5, 0.4,
    boxstyle="round,pad=0.05",
    facecolor=LIGHT_BLUE,
    edgecolor=PYTHON_BLUE,
    linewidth=2
)
ax.add_patch(tab)

# Package name in tab
ax.text(pkg_x + 0.95, pkg_y + pkg_height + 0.1, "mypackage/",
        ha='center', va='center', fontsize=10, fontweight='bold', color=PYTHON_BLUE)

# Files inside package
inner_files = [
    ("__init__.py", pkg_x + 0.5, pkg_y + 2.5, PYTHON_YELLOW, "обов'язковий!"),
    ("module1.py", pkg_x + 0.5, pkg_y + 1.5, '#FFFFFF', None),
    ("module2.py", pkg_x + 0.5, pkg_y + 0.5, '#FFFFFF', None),
]

for fname, fx, fy, fcolor, note in inner_files:
    # Small file icon
    small_file = mpatches.FancyBboxPatch(
        (fx, fy), 1.2, 0.7,
        boxstyle="round,pad=0.02",
        facecolor=fcolor,
        edgecolor='#999999' if fcolor == '#FFFFFF' else PYTHON_YELLOW,
        linewidth=1.5
    )
    ax.add_patch(small_file)
    ax.text(fx + 0.6, fy + 0.35, fname, ha='center', va='center',
            fontsize=9, fontfamily='monospace', color='#333333')

    if note:
        ax.text(fx + 1.5, fy + 0.35, f"  {note}",
                ha='left', va='center', fontsize=8, color='#E65100',
                fontweight='bold')

# Subpackage folder
subpkg_x, subpkg_y = pkg_x + 2.2, pkg_y + 0.3
subpkg = mpatches.FancyBboxPatch(
    (subpkg_x, subpkg_y), 1.5, 2,
    boxstyle="round,pad=0.05",
    facecolor='#D4E6F1',
    edgecolor='#5DADE2',
    linewidth=1.5
)
ax.add_patch(subpkg)

ax.text(subpkg_x + 0.75, subpkg_y + 1.7, "subpkg/",
        ha='center', va='center', fontsize=8, fontweight='bold', color='#2874A6')

# Files in subpackage
sub_init = mpatches.FancyBboxPatch(
    (subpkg_x + 0.15, subpkg_y + 0.9), 1.2, 0.5,
    boxstyle="round,pad=0.02",
    facecolor=PYTHON_YELLOW,
    edgecolor='#999999',
    linewidth=1
)
ax.add_patch(sub_init)
ax.text(subpkg_x + 0.75, subpkg_y + 1.15, "__init__.py",
        ha='center', va='center', fontsize=7, fontfamily='monospace')

sub_mod = mpatches.FancyBboxPatch(
    (subpkg_x + 0.15, subpkg_y + 0.2), 1.2, 0.5,
    boxstyle="round,pad=0.02",
    facecolor='#FFFFFF',
    edgecolor='#999999',
    linewidth=1
)
ax.add_patch(sub_mod)
ax.text(subpkg_x + 0.75, subpkg_y + 0.45, "helper.py",
        ha='center', va='center', fontsize=7, fontfamily='monospace')

# Package label
ax.text(pkg_x + pkg_width/2, pkg_y - 0.5, "Пакет (Package)",
        ha='center', va='center', fontsize=14, fontweight='bold', color=PYTHON_BLUE)

ax.text(pkg_x + pkg_width/2, pkg_y - 0.9, "директорія з __init__.py",
        ha='center', va='center', fontsize=10, color='#666666')

# Import examples
ax.text(pkg_x + pkg_width/2, pkg_y - 1.5, "import mypackage\nfrom mypackage import module1\nfrom mypackage.subpkg import helper",
        ha='center', va='center', fontsize=9, fontfamily='monospace',
        bbox=dict(boxstyle='round,pad=0.3', facecolor='#F5F5F5', edgecolor='#CCCCCC'))

# === VS in the middle ===
ax.text(5.5, 5.5, "vs",
        ha='center', va='center', fontsize=24, fontweight='bold', color='#999999')

# === Title ===
ax.text(7, 9, "Модулі та Пакети в Python",
        ha='center', va='center', fontsize=18, fontweight='bold', color=PYTHON_BLUE)
ax.text(7, 8.5, "(Modules and Packages)",
        ha='center', va='center', fontsize=12, color='#666666')

# === sys.path explanation at bottom ===
syspath_y = 1.5
ax.text(7, syspath_y + 0.8, "Python шукає модулі в такому порядку (sys.path):",
        ha='center', va='center', fontsize=11, fontweight='bold', color='#333333')

search_order = [
    "1. Директорія скрипта",
    "2. PYTHONPATH (змінна середовища)",
    "3. Стандартна бібліотека",
    "4. site-packages (встановлені пакети)"
]

for i, item in enumerate(search_order):
    ax.text(7, syspath_y + 0.3 - i * 0.35, item,
            ha='center', va='center', fontsize=9, color='#666666')

# Styling
ax.set_xlim(0, 14)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('diagrams/modules-packages.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print("Modules diagram saved to diagrams/modules-packages.png")
