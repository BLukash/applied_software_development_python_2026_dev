import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm
import numpy as np

WIDTH_PX, HEIGHT_PX, DPI = 800, 600, 150
fig_w = WIDTH_PX / DPI
fig_h = HEIGHT_PX / DPI

FONT_FAMILY = 'DejaVu Sans'
available_fonts = [f.name for f in fm.fontManager.ttflist]
if FONT_FAMILY not in available_fonts:
    FONT_FAMILY = 'sans-serif'
    print(f'[warn] DejaVu Sans not found, falling back to {FONT_FAMILY}')
else:
    print(f'[info] Using font: {FONT_FAMILY}')

RED_BG = '#FFCCCC'
GREEN_BG = '#CCFFCC'
RED_DARK = '#CC3333'
GREEN_DARK = '#228B22'
FACE_SKIN = '#FFD93D'
FACE_SKIN_SAD = '#FFB347'

fig = plt.figure(figsize=(fig_w, fig_h), dpi=DPI, facecolor='white')

ax_title = fig.add_axes([0, 0.92, 1, 0.08])
ax_title.set_xlim(0, 1)
ax_title.set_ylim(0, 1)
ax_title.axis('off')
ax_title.set_facecolor('#333333')

title_bg = patches.FancyBboxPatch(
    (0.01, 0.1), 0.98, 0.8,
    boxstyle='round,pad=0.02', fc='#333333', ec='#333333',
    transform=ax_title.transAxes, zorder=1)
ax_title.add_patch(title_bg)
ax_title.text(0.5, 0.5, 'Python Data Structures: list vs set',
              fontsize=10, fontfamily=FONT_FAMILY, fontweight='bold',
              color='white', ha='center', va='center',
              transform=ax_title.transAxes, zorder=2)

ax_top = fig.add_axes([0, 0.46, 1, 0.46])
ax_top.set_xlim(0, 10)
ax_top.set_ylim(0, 5)
ax_top.set_aspect('auto')
ax_top.axis('off')
ax_top.set_facecolor(RED_BG)

ax_bot = fig.add_axes([0, 0, 1, 0.46])
ax_bot.set_xlim(0, 10)
ax_bot.set_ylim(0, 5)
ax_bot.set_aspect('auto')
ax_bot.axis('off')
ax_bot.set_facecolor(GREEN_BG)

def draw_face(ax, cx, cy, radius, happy=True):
    skin = FACE_SKIN if happy else FACE_SKIN_SAD
    outline = GREEN_DARK if happy else RED_DARK
    head = plt.Circle((cx, cy), radius, fc=skin, ec=outline, lw=2.5, zorder=5)
    ax.add_patch(head)
    eye_y = cy + radius * 0.25
    eye_dx = radius * 0.32
    eye_r = radius * 0.09
    for sign in (-1, 1):
        eye = plt.Circle((cx + sign * eye_dx, eye_y), eye_r,
                          fc='#333333', ec='#333333', zorder=6)
        ax.add_patch(eye)
    brow_y = cy + radius * 0.5
    brow_dx = radius * 0.32
    brow_len = radius * 0.18
    if happy:
        for sign in (-1, 1):
            bx = cx + sign * brow_dx
            ax.plot([bx - brow_len, bx + brow_len],
                    [brow_y - 0.03, brow_y + 0.06],
                    color='#333333', lw=2, zorder=6)
    else:
        for sign in (-1, 1):
            bx = cx + sign * brow_dx
            ax.plot([bx - sign * brow_len, bx + sign * brow_len],
                    [brow_y + 0.08, brow_y - 0.06],
                    color='#333333', lw=2, zorder=6)
    if happy:
        theta = np.linspace(np.pi + 0.3, 2 * np.pi - 0.3, 40)
        mx = cx + radius * 0.4 * np.cos(theta)
        my = cy - radius * 0.2 + radius * 0.28 * np.sin(theta)
        ax.plot(mx, my, color='#333333', lw=2.2, zorder=6)
    else:
        theta = np.linspace(0.3, np.pi - 0.3, 40)
        mx = cx + radius * 0.4 * np.cos(theta)
        my = cy - radius * 0.45 + radius * 0.2 * np.sin(theta)
        ax.plot(mx, my, color='#333333', lw=2.2, zorder=6)
    sym_x = cx + radius + 0.6
    sym_y = cy
    if happy:
        ax.text(sym_x, sym_y, chr(0x2714), fontsize=20, fontweight='bold',
                color=GREEN_DARK, ha='center', va='center',
                fontfamily=FONT_FAMILY, zorder=6)
    else:
        ax.text(sym_x, sym_y, chr(0x2718), fontsize=20, fontweight='bold',
                color=RED_DARK, ha='center', va='center',
                fontfamily=FONT_FAMILY, zorder=6)

ax_top.plot([0, 10], [0.02, 0.02], color='#AAAAAA', lw=1.5, zorder=10)
draw_face(ax_top, cx=1.8, cy=2.5, radius=1.3, happy=False)

top_line1 = chr(0x428) + chr(0x443) + chr(0x43a) + chr(0x430) + chr(0x442) + chr(0x438) + ' ' + chr(0x435) + chr(0x43b) + chr(0x435) + chr(0x43c) + chr(0x435) + chr(0x43d) + chr(0x442) + ' ' + chr(0x443) + ' list'
top_line2 = chr(0x437) + ' 100 000 ' + chr(0x435) + chr(0x43b) + chr(0x435) + chr(0x43c) + chr(0x435) + chr(0x43d) + chr(0x442) + chr(0x456) + chr(0x432)
top_text = top_line1 + chr(10) + top_line2

ax_top.text(6.2, 2.8, top_text,
            fontsize=12, fontweight='bold', fontfamily=FONT_FAMILY,
            color='#4A0000', ha='center', va='center',
            linespacing=1.6, zorder=6)

badge_top = patches.FancyBboxPatch(
    (5.1, 0.55), 2.2, 0.85,
    boxstyle='round,pad=0.18', fc='#FF8888', ec=RED_DARK, lw=1.8, zorder=6)
ax_top.add_patch(badge_top)
ax_top.text(6.2, 0.97, 'O(n)  slow...', fontsize=9, fontfamily=FONT_FAMILY,
            fontweight='bold', color='#4A0000', ha='center', va='center', zorder=7)

draw_face(ax_bot, cx=1.8, cy=2.5, radius=1.3, happy=True)

bot_line1 = chr(0x428) + chr(0x443) + chr(0x43a) + chr(0x430) + chr(0x442) + chr(0x438) + ' ' + chr(0x435) + chr(0x43b) + chr(0x435) + chr(0x43c) + chr(0x435) + chr(0x43d) + chr(0x442) + ' ' + chr(0x443) + ' set'
bot_line2 = chr(0x437) + chr(0x430) + ' O(1)'
bot_text = bot_line1 + chr(10) + bot_line2

ax_bot.text(6.2, 2.8, bot_text,
            fontsize=12, fontweight='bold', fontfamily=FONT_FAMILY,
            color='#003300', ha='center', va='center',
            linespacing=1.6, zorder=6)

badge_bot = patches.FancyBboxPatch(
    (5.1, 0.55), 2.2, 0.85,
    boxstyle='round,pad=0.18', fc='#88DD88', ec=GREEN_DARK, lw=1.8, zorder=6)
ax_bot.add_patch(badge_bot)
ax_bot.text(6.2, 0.97, 'O(1)  fast!', fontsize=9, fontfamily=FONT_FAMILY,
            fontweight='bold', color='#003300', ha='center', va='center', zorder=7)

output_path = r'd:' + chr(92) + 'applied_software_development_python_2026' + chr(92) + 'lectures' + chr(92) + '03-data-structures' + chr(92) + 'assets' + chr(92) + 'memes' + chr(92) + 'collections-meme.png'
fig.savefig(output_path, dpi=DPI, pad_inches=0, facecolor=fig.get_facecolor())
plt.close(fig)
print(f'[done] Meme saved to: {output_path}')