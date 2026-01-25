"""
Generate Python History Timeline diagram for Lecture 1.
"""
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

# Timeline data
events = [
    (1989, "Guido van Rossum\nрозпочинає роботу\nнад Python"),
    (1991, "Python 0.9.0\nперший публічний\nреліз"),
    (1994, "Python 1.0\nофіційний реліз"),
    (2000, "Python 2.0\nlist comprehensions,\ngarbage collection"),
    (2008, "Python 3.0\nнесумісний з 2.x,\nмодернізація"),
    (2020, "Python 2\nEnd of Life"),
    (2024, "Python 3.13"),
    (2025, "Python 3.14\nсучасна версія"),
]

fig, ax = plt.subplots(figsize=(14, 6))

# Set up the timeline
years = [e[0] for e in events]
min_year, max_year = min(years) - 2, max(years) + 2

# Draw main timeline
ax.axhline(y=0.5, color='#306998', linewidth=4, zorder=1)

# Colors for events (alternating)
colors = ['#FFD43B', '#306998', '#FFD43B', '#306998', '#FFD43B', '#306998', '#FFD43B', '#306998']

# Draw events
for i, (year, label) in enumerate(events):
    # Alternate above and below the timeline
    y_offset = 0.7 if i % 2 == 0 else 0.3
    text_y = 0.85 if i % 2 == 0 else 0.15

    # Draw vertical line
    ax.plot([year, year], [0.5, y_offset], color=colors[i], linewidth=2, zorder=2)

    # Draw circle marker
    ax.scatter(year, y_offset, s=200, color=colors[i], edgecolor='black', linewidth=1.5, zorder=3)

    # Add year label
    ax.text(year, y_offset + (0.05 if i % 2 == 0 else -0.05),
            str(year), ha='center', va='bottom' if i % 2 == 0 else 'top',
            fontsize=12, fontweight='bold', color='#333333')

    # Add event description
    ax.text(year, text_y, label, ha='center', va='center',
            fontsize=9, color='#333333',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', edgecolor=colors[i], alpha=0.9))

# Title
ax.text((min_year + max_year) / 2, 1.05,
        'Історія Python (History of Python)',
        ha='center', va='bottom', fontsize=16, fontweight='bold', color='#306998')

# Styling
ax.set_xlim(min_year, max_year)
ax.set_ylim(0, 1.15)
ax.axis('off')

# Add Python logo colors legend
python_blue = mpatches.Patch(color='#306998', label='Python Blue')
python_yellow = mpatches.Patch(color='#FFD43B', label='Python Yellow')

plt.tight_layout()
plt.savefig('diagrams/python-timeline.png', dpi=150, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.close()

print("Timeline saved to diagrams/python-timeline.png")
