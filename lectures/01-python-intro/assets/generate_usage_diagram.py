"""
Generate Python Usage Areas diagram for Lecture 1.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle
import numpy as np

fig, ax = plt.subplots(figsize=(14, 10))

# Python logo colors
PYTHON_BLUE = '#306998'
PYTHON_YELLOW = '#FFD43B'

# Usage areas data with icons (emoji-style markers) and examples
areas = [
    {"name": "Веб-розробка\n(Web Development)", "examples": "Django, FastAPI, Flask", "color": "#E74C3C", "icon": "🌐", "pos": (0.5, 0.85)},
    {"name": "Data Science & ML", "examples": "pandas, NumPy,\nTensorFlow, PyTorch", "color": "#9B59B6", "icon": "📊", "pos": (0.15, 0.6)},
    {"name": "Автоматизація\n(Automation)", "examples": "Скрипти, DevOps,\nтестування", "color": "#3498DB", "icon": "⚙️", "pos": (0.85, 0.6)},
    {"name": "Наукові обчислення\n(Scientific)", "examples": "SciPy, Jupyter", "color": "#1ABC9C", "icon": "🔬", "pos": (0.25, 0.25)},
    {"name": "Ігри\n(Games)", "examples": "Pygame, Godot", "color": "#F39C12", "icon": "🎮", "pos": (0.75, 0.25)},
    {"name": "Десктоп-додатки\n(Desktop Apps)", "examples": "PyQt, Tkinter", "color": "#2ECC71", "icon": "🖥️", "pos": (0.5, 0.1)},
]

# Draw central Python circle
center = (0.5, 0.5)
python_circle = Circle(center, 0.12, color=PYTHON_BLUE, ec='black', linewidth=2, zorder=10)
ax.add_patch(python_circle)
ax.text(center[0], center[1], "Python", ha='center', va='center',
        fontsize=18, fontweight='bold', color='white', zorder=11)

# Draw each usage area
for area in areas:
    x, y = area['pos']

    # Draw connecting line to center
    ax.plot([center[0], x], [center[1], y], color=area['color'], linewidth=3, alpha=0.6, zorder=1)

    # Draw area box
    box_width = 0.22
    box_height = 0.18
    box = FancyBboxPatch((x - box_width/2, y - box_height/2), box_width, box_height,
                         boxstyle="round,pad=0.02,rounding_size=0.02",
                         facecolor='white', edgecolor=area['color'], linewidth=3, zorder=5)
    ax.add_patch(box)

    # Add area name
    ax.text(x, y + 0.03, area['name'], ha='center', va='center',
            fontsize=11, fontweight='bold', color=area['color'], zorder=6)

    # Add examples
    ax.text(x, y - 0.045, area['examples'], ha='center', va='center',
            fontsize=9, color='#555555', zorder=6)

# Title
ax.text(0.5, 0.98, 'Де використовується Python?', ha='center', va='top',
        fontsize=20, fontweight='bold', color=PYTHON_BLUE)
ax.text(0.5, 0.94, '(Where is Python used?)', ha='center', va='top',
        fontsize=14, color='#666666')

# Styling
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.set_aspect('equal')
ax.axis('off')

plt.tight_layout()
plt.savefig('diagrams/python-usage.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print("Usage diagram saved to diagrams/python-usage.png")
