import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('data/touchpoint_one_mock_data.csv')
df['Status_Label'] = df['Retention_Status'].map({1: 'Retained', 0: 'At Risk'})

NAVY, TEAL, GOLD, RED = '#1B2A4A', '#00A9A5', '#F4A100', '#D94F3D'
plt.rcParams.update({'font.family': 'DejaVu Sans'})

fig, axes = plt.subplots(2, 2, figsize=(16, 12))
fig.suptitle('Gamification as a Retention Strategy\nContact Center Analytics | 100 Agents',
             fontsize=18, fontweight='bold', color=NAVY, y=0.98)

ax1 = axes[0, 0]
for label, color in [('Retained', TEAL), ('At Risk', RED)]:
    subset = df[df['Status_Label'] == label]['AGAME_Points']
    ax1.hist(subset, bins=15, alpha=0.7, color=color, label=label, edgecolor='white')
ax1.set_title('AGAME Points Distribution', fontweight='bold', color=NAVY)
ax1.set_xlabel('AGAME Points')
ax1.set_ylabel('Agent Count')
ax1.legend()

ax2 = axes[0, 1]
colors = df['Retention_Status'].map({1: TEAL, 0: RED})
ax2.scatter(df['Tone_Sentiment'], df['FCR_Percent'],
            c=colors, alpha=0.6, s=60, edgecolors='white', linewidth=0.5)
z = np.polyfit(df['Tone_Sentiment'], df['FCR_Percent'], 1)
p = np.poly1d(z)
x_line = np.linspace(df['Tone_Sentiment'].min(), df['Tone_Sentiment'].max(), 100)
ax2.plot(x_line, p(x_line), '--', color=GOLD, linewidth=2, label='Trend')
ax2.set_title('Tone Predicts FCR', fontweight='bold', color=NAVY)
ax2.set_xlabel('Tone Sentiment Score')
ax2.set_ylabel('FCR %')
retained_patch = mpatches.Patch(color=TEAL, label='Retained')
risk_patch = mpatches.Patch(color=RED, label='At Risk')
ax2.legend(handles=[retained_patch, risk_patch])

ax3 = axes[1, 0]
df['Training_Tier'] = df['Training_Hours'].apply(
    lambda h: 'High (12h+)' if h >= 12 else ('Mid (8-12h)' if h >= 8 else 'Low (<8h)'))
tier_order = ['High (12h+)', 'Mid (8-12h)', 'Low (<8h)']
tier_stats = df.groupby('Training_Tier')['Retention_Status'].mean() * 100
tier_stats = tier_stats.reindex(tier_order)
bars = ax3.bar(tier_stats.index, tier_stats.values,
               color=[TEAL, GOLD, RED], edgecolor='white', width=0.5)
for bar, val in zip(bars, tier_stats.values):
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
             f'{val:.1f}%', ha='center', fontweight='bold', color=NAVY)
ax3.set_title('Retention Rate by Training Tier', fontweight='bold', color=NAVY)
ax3.set_ylabel('Retention Rate %')
ax3.set_ylim(0, 105)

ax4 = axes[1, 1]
df['Engagement_Score'] = (df['AGAME_Points']/10 +
                           df['Training_Hours']*2 +
                           df['FCR_Percent'] +
                           df['Tone_Sentiment']*10)
for label, color in [('Retained', TEAL), ('At Risk', RED)]:
    subset = df[df['Status_Label'] == label]['Engagement_Score']
    ax4.hist(subset, bins=15, alpha=0.7, color=color, label=label, edgecolor='white')
ax4.set_title('Composite Engagement Score', fontweight='bold', color=NAVY)
ax4.set_xlabel('Engagement Score')
ax4.set_ylabel('Agent Count')
ax4.legend()

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('outputs/retention_analysis_charts.png', dpi=150, bbox_inches='tight')
print('Charts saved to outputs/retention_analysis_charts.png')
plt.show()
