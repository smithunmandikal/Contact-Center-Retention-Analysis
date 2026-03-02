-- ============================================================
-- PROJECT: Gamification as a Retention Strategy
-- Dataset: touchpoint_one_mock_data.csv (100 Contact Center Agents)
-- Author:  [Your Name] | github.com/[yourusername]
-- ============================================================
 
-- Preview the full dataset
SELECT *
FROM agents
LIMIT 10;
-- The Core Finding: What separates retained vs. churned agents?
SELECT
    CASE WHEN Retention_Status = 1 THEN 'Retained' ELSE 'At Risk' END AS Agent_Status,
    COUNT(*)                              AS Agent_Count,
    ROUND(AVG(AGAME_Points), 0)           AS Avg_Gamification_Score,
    ROUND(AVG(Training_Hours), 1)         AS Avg_Training_Hours,
    ROUND(AVG(FCR_Percent), 1)            AS Avg_FCR_Percent,
    ROUND(AVG(Tone_Sentiment), 2)         AS Avg_Sentiment_Score
FROM agents
GROUP BY Retention_Status
ORDER BY Retention_Status DESC;
-- Segment agents into Training Tiers, then show FCR per tier
-- This demonstrates SQL JOIN logic on a single-table dataset
SELECT
    training_tier.Training_Tier,
    COUNT(a.Agent_ID)               AS Agent_Count,
    ROUND(AVG(a.FCR_Percent), 1)    AS Avg_FCR,
    ROUND(AVG(a.Tone_Sentiment), 2) AS Avg_Tone,
    ROUND(AVG(a.AGAME_Points), 0)   AS Avg_AGAME_Points,
    SUM(a.Retention_Status)         AS Retained_Count,
    ROUND(100.0 * SUM(a.Retention_Status) / COUNT(*), 1) AS Retention_Rate_Pct
FROM agents a
JOIN (
    SELECT Agent_ID,
        CASE
            WHEN Training_Hours >= 12 THEN 'High (12h+)'
            WHEN Training_Hours >= 8  THEN 'Mid (8-12h)'
            ELSE 'Low (<8h)'
        END AS Training_Tier
    FROM agents
) AS training_tier ON a.Agent_ID = training_tier.Agent_ID
GROUP BY training_tier.Training_Tier
ORDER BY Avg_FCR DESC;
-- The Headline Insight: Higher Tone Sentiment = Higher Retention
SELECT
    CASE
        WHEN Tone_Sentiment >= 4.0 THEN 'High Tone (4.0-5.0)'
        WHEN Tone_Sentiment >= 3.0 THEN 'Mid Tone (3.0-3.9)'
        ELSE 'Low Tone (<3.0)'
    END AS Tone_Bucket,
    COUNT(*)                                                      AS Agents,
    ROUND(100.0 * SUM(Retention_Status) / COUNT(*), 1)           AS Retention_Rate_Pct,
    ROUND(AVG(AGAME_Points), 0)                                   AS Avg_AGAME_Points,
    ROUND(AVG(FCR_Percent), 1)                                    AS Avg_FCR_Pct
FROM agents
GROUP BY Tone_Bucket
ORDER BY Retention_Rate_Pct DESC;
-- Identify the TOP 10 at-risk agents for proactive intervention
SELECT
    Agent_ID,
    AGAME_Points,
    ROUND(Training_Hours, 1)  AS Training_Hours,
    ROUND(FCR_Percent, 1)     AS FCR_Percent,
    ROUND(Tone_Sentiment, 2)  AS Tone_Sentiment,
    -- Composite risk score (lower = more at risk)

    ROUND(
        (AGAME_Points / 10.0) +
        (Training_Hours * 2) +
        FCR_Percent +
        (Tone_Sentiment * 10)
    , 1) AS Engagement_Score
FROM agents
WHERE Retention_Status = 0
ORDER BY Engagement_Score ASC
LIMIT 10;
