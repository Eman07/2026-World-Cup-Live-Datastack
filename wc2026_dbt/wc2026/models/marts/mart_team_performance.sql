WITH all_matches AS (
    -- Home team perspective
    SELECT
        home_team        AS team,
        score_home       AS goals_scored,
        score_away       AS goals_conceded
    FROM STAGING_WC2026.STAGING.STG_MATCH_EVENTS
    WHERE status = 'FINISHED'

    UNION ALL

    -- Away team perspective
    SELECT
        away_team             AS team,
        score_away            AS goals_scored,
        score_home            AS goals_conceded
    FROM STAGING_WC2026.STAGING.STG_MATCH_EVENTS
    WHERE status = 'FINISHED'
)

SELECT
    team,
    COUNT(*)             AS matches_played,
    SUM(goals_scored)    AS total_goals_scored,
    SUM(goals_conceded)  AS total_goals_conceded
FROM all_matches
GROUP BY team
ORDER BY total_goals_scored DESC