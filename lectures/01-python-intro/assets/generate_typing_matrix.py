"""
Generate Typing Matrix diagram for Lecture 1.
Shows static/dynamic vs strong/weak typing with language examples.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Python colors
PYTHON_BLUE = '#306998'
PYTHON_YELLOW = '#FFD43B'
LIGHT_BLUE = '#4B8BBE'
LIGHT_YELLOW = '#FFE873'

fig, ax = plt.subplots(figsize=(10, 8))

# Draw the 2x2 grid
# Quadrant colors
quadrant_colors = [
    ['#E8F4FD', '#FFF8E1'],  # Top row: Static+Strong, Static+Weak
    ['#E3F2E8', '#FFEBEE'],  # Bottom row: Dynamic+Strong, Dynamic+Weak
]

# Draw quadrants
for i in range(2):
    for j in range(2):
        rect = mpatches.FancyBboxPatch(
            (j, 1-i), 1, 1,
            boxstyle="round,pad=0.02",
            facecolor=quadrant_colors[i][j],
            edgecolor='#666666',
            linewidth=2
        )
        ax.add_patch(rect)

# Quadrant content
quadrants = [
    # (x, y, title, languages, is_python)
    (0.5, 1.5, "Статична + Сильна", "Java, C#, Rust,\nTypeScript, Kotlin", False),
    (1.5, 1.5, "Статична + Слабка", "C, C++", False),
    (0.5, 0.5, "Динамічна + Сильна", "Python, Ruby,\nErlang", True),
    (1.5, 0.5, "Динамічна + Слабка", "JavaScript, PHP,\nPerl", False),
]

for x, y, title, langs, is_python in quadrants:
    # Draw title
    ax.text(x, y + 0.25, title, ha='center', va='center',
            fontsize=12, fontweight='bold', color='#333333')

    # Draw languages with Python highlighted if applicable
    if is_python:
        # Split to highlight Python
        ax.text(x, y - 0.05, "Python", ha='center', va='center',
                fontsize=14, fontweight='bold', color=PYTHON_BLUE,
                bbox=dict(boxstyle='round,pad=0.3', facecolor=PYTHON_YELLOW,
                         edgecolor=PYTHON_BLUE, linewidth=2))
        ax.text(x, y - 0.3, "Ruby, Erlang", ha='center', va='center',
                fontsize=10, color='#666666')
    else:
        ax.text(x, y - 0.1, langs, ha='center', va='center',
                fontsize=10, color='#666666')

# Axis labels
ax.text(1, 2.15, "Сильна (Strong)", ha='center', va='center',
        fontsize=14, fontweight='bold', color='#333333')
ax.text(1, -0.15, "Слабка (Weak)", ha='center', va='center',
        fontsize=14, fontweight='bold', color='#333333')
ax.text(-0.15, 1.5, "Статична\n(Static)", ha='center', va='center',
        fontsize=12, fontweight='bold', color='#333333', rotation=90)
ax.text(-0.15, 0.5, "Динамічна\n(Dynamic)", ha='center', va='center',
        fontsize=12, fontweight='bold', color='#333333', rotation=90)

# Arrows for axes
ax.annotate('', xy=(2, 2.05), xytext=(0, 2.05),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=2))
ax.annotate('', xy=(-0.05, 0), xytext=(-0.05, 2),
            arrowprops=dict(arrowstyle='->', color='#333333', lw=2))

# Title
ax.text(1, 2.4, "Матриця типізації мов програмування",
        ha='center', va='center', fontsize=16, fontweight='bold', color=PYTHON_BLUE)

# Subtitle
ax.text(1, 2.25, "(Type System Matrix)",
        ha='center', va='center', fontsize=11, color='#666666')

# Note at bottom
ax.text(1, -0.35, "Python = динамічна типізація (тип перевіряється при виконанні)\n+ сильна типізація (немає неявних перетворень типів)",
        ha='center', va='center', fontsize=9, color='#666666', style='italic')

# Styling
ax.set_xlim(-0.4, 2.2)
ax.set_ylim(-0.5, 2.5)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('diagrams/typing-matrix.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print("Typing matrix saved to diagrams/typing-matrix.png")
