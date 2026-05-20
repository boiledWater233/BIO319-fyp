import matplotlib.pyplot as plt
import numpy as np

# ============================================================
# DATA — Per-paper metrics for Method / Protocol / Instrument (%)
# ============================================================
papers_short = [
    '60378-0\n(AD)',
    '65355-1\n(CMV)',
    '63021-0\n(METTL16)',
    '60199-1\n(WYMV)',
    '59117-2\n(ALS)',
    '58995-w\n(Cataract)',
    '55694-w\n(Adipocyte)',
]

# ---- Method ----
method_recall    = [100.0, 84.6, 100.0, 100.0, 87.0, 100.0, 100.0]
method_precision = [100.0, 100.0, 100.0, 100.0, 95.2, 100.0, 100.0]
method_f1        = [100.0, 91.7, 100.0, 100.0, 90.9, 100.0, 100.0]

# ---- Protocol ----
proto_recall    = [88.9, 81.8, 100.0, 86.7, 72.7, 83.3, 88.9]
proto_precision = [100.0, 100.0, 100.0, 100.0, 100.0, 100.0, 100.0]
proto_f1        = [94.1, 90.0, 100.0, 92.9, 84.2, 90.9, 94.1]

# ---- Instrument ----
inst_recall    = [80.0, 80.0, 83.3, 81.3, 77.8, 70.0, 68.8]
inst_precision = [100.0, 100.0, 100.0, 100.0, 94.4, 100.0, 100.0]
inst_f1        = [88.9, 88.9, 90.9, 89.7, 85.4, 82.4, 81.5]

# ---- Averages ----
avg_method = [np.mean(method_recall), np.mean(method_precision), np.mean(method_f1)]
avg_proto  = [np.mean(proto_recall),  np.mean(proto_precision),  np.mean(proto_f1)]
avg_inst   = [np.mean(inst_recall),   np.mean(inst_precision),   np.mean(inst_f1)]

# ============================================================
# PLOT — 3 grouped bars per panel, thicker & tighter
# ============================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 7), sharey=True)

categories = ['Recall', 'Precision', 'F1']
colors = ['#2E86AB', '#A23B72', '#F18F01']
x = np.arange(3)
width = 0.5          # much thicker bars
gap = 0           # tiny gap between bars within group

# --- PANEL 1: Method ---
ax = axes[0]
for i, (vals, label) in enumerate(zip(
    [avg_method],
    ['Method']
)):
    bars = ax.bar(x + i * gap, vals, width, color=colors,
                  edgecolor='white', linewidth=0.7)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f'{val:.1f}', ha='center', va='bottom', fontsize=16, fontweight='bold')
ax.set_title('Method', fontsize=18, fontweight='bold', pad=18)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(60, 106)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# --- PANEL 2: Protocol ---
ax = axes[1]
for i, (vals, label) in enumerate(zip(
    [avg_proto],
    ['Protocol']
)):
    bars = ax.bar(x + i * gap, vals, width, color=colors,
                  edgecolor='white', linewidth=0.7)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f'{val:.1f}', ha='center', va='bottom', fontsize=16, fontweight='bold')
ax.set_title('Protocol', fontsize=18, fontweight='bold', pad=18)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(60, 106)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# --- PANEL 3: Instrument ---
ax = axes[2]
for i, (vals, label) in enumerate(zip(
    [avg_inst],
    ['Instrument']
)):
    bars = ax.bar(x + i * gap, vals, width, color=colors,
                  edgecolor='white', linewidth=0.7)
    for bar, val in zip(bars, vals):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.8,
                f'{val:.1f}', ha='center', va='bottom', fontsize=16, fontweight='bold')
ax.set_title('Instrument', fontsize=18, fontweight='bold', pad=18)
ax.set_xticks(x)
ax.set_xticklabels(categories, fontsize=12)
ax.set_ylim(60, 106)
ax.grid(axis='y', alpha=0.3, linestyle='--')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# ============================================================
# Labels & legend
# ============================================================
axes[0].set_ylabel('Percentage (%)', fontsize=15, fontweight='bold')
fig.suptitle('Section entities extraction precision',
             fontsize=20, fontweight='bold', y=1)

from matplotlib.patches import Patch
legend_elements = [
    Patch(facecolor='#2E86AB', label='Recall'),
    Patch(facecolor='#A23B72', label='Precision'),
    Patch(facecolor='#F18F01', label='F1'),
]
fig.legend(handles=legend_elements, loc='lower center', ncol=3,
           fontsize=11, framealpha=0.9, edgecolor='gray', bbox_to_anchor=(0.5, -0.06))

plt.tight_layout()
plt.savefig('method_protocol_instrument_performance.png', dpi=200, bbox_inches='tight')
plt.show()

# ============================================================
# Print summary
# ============================================================
print(f"\n{'Category':<14} {'Recall':>8} {'Precision':>10} {'F1':>8}")
print("-" * 42)
print(f"{'Method':<14} {avg_method[0]:>7.1f}% {avg_method[1]:>9.1f}% {avg_method[2]:>7.1f}%")
print(f"{'Protocol':<14} {avg_proto[0]:>7.1f}% {avg_proto[1]:>9.1f}% {avg_proto[2]:>7.1f}%")
print(f"{'Instrument':<14} {avg_inst[0]:>7.1f}% {avg_inst[1]:>9.1f}% {avg_inst[2]:>7.1f}%")
