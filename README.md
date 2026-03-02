# Contact-Center-Retention-Analysis
A data-driven strategy using SQL and Python to link agent gamification to 15% lower attrition risk

# Gamification as a Retention Strategy
## 15% Reduction in Attrition Risk | Contact Center Analytics
 
![Python](https://img.shields.io/badge/Python-3.11-blue)
![SQL](https://img.shields.io/badge/SQL-SQLite-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
 
---
 
## Executive Headline
> **Agents who participate in gamification training show a measurable
> reduction in attrition risk — and their tone (sentiment) predicts
> their performance 3 months in advance.**
 
## The Data Story
| Metric               | Retained Agents | At-Risk Agents |
|----------------------|-----------------|----------------|
| Avg AGAME Points     | ~720            | ~380           |
| Avg Training Hours   | 12.8h           | 7.9h           |
| Avg FCR Rate         | 84%             | 76%            |
| Avg Tone Sentiment   | 4.4 / 5.0       | 2.8 / 5.0      |
 
## Project Structure
```
data/           ← Mock dataset (100 contact center agents)
sql/            ← 5 SQL queries: segmentation, JOINs, risk scoring
python/         ← Analysis + visualization scripts
outputs/        ← Generated charts (PNG)
```
 
## Key Findings
1. **Tone predicts Talent** — Sentiment score is the #1 leading indicator of retention
2. **Training Tier matters** — High-training agents retain at 2x the rate of low-training agents
3. **Gamification works** — AGAME engagement score separates retained vs. at-risk with 78% accuracy
 
## How to Run
```bash
git clone https://github.com/[yourusername]/gamification-retention-analysis
cd gamification-retention-analysis
pip install -r python/requirements.txt
python python/analysis.py
python python/charts.py
```
 
## Author
**[Shwetha Mithun Mandikal]** | Contact Center Analyst | [linkedin.com/in/shwethamm]

