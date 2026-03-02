# ============================================================
# analysis.py
# Gamification as a Retention Strategy
# Contact Center Analytics | TouchPoint One Mock Data
# ============================================================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')
 
# ── Load Data ───────────────────────────────────────────────
df = pd.read_csv('../data/touchpoint_one_mock_data.csv')
print(f'Dataset loaded: {len(df)} agents')
print(df.describe().round(2))
 
# ── Executive Headline Calculation ──────────────────────────
retained = df[df['Retention_Status'] == 1]
at_risk  = df[df['Retention_Status'] == 0]
 
print('\n=== EXECUTIVE HEADLINE METRICS ===')
print(f'Total Agents:          {len(df)}')
print(f'Retained:              {len(retained)} ({len(retained)/len(df)*100:.1f}%)')
print(f'At Risk:               {len(at_risk)} ({len(at_risk)/len(df)*100:.1f}%)')
print(f'Avg AGAME - Retained:  {retained["AGAME_Points"].mean():.0f}')
print(f'Avg AGAME - At Risk:   {at_risk["AGAME_Points"].mean():.0f}')
print(f'Avg Tone  - Retained:  {retained["Tone_Sentiment"].mean():.2f}')
print(f'Avg Tone  - At Risk:   {at_risk["Tone_Sentiment"].mean():.2f}')
 
# ── Training Tiers (mirrors SQL Query 3) ────────────────────
def training_tier(h):
    if h >= 12:  return 'High (12h+)'
    elif h >= 8: return 'Mid (8-12h)'
    else:        return 'Low (<8h)'
 
df['Training_Tier'] = df['Training_Hours'].apply(training_tier)
 
# ── Tone Buckets (mirrors SQL Query 4) ──────────────────────
def tone_bucket(t):
    if t >= 4.0:  return 'High Tone'
    elif t >= 3.0: return 'Mid Tone'
    else:          return 'Low Tone'
 
df['Tone_Bucket'] = df['Tone_Sentiment'].apply(tone_bucket)
print('\nScript complete. Run charts.py to generate visuals.')
