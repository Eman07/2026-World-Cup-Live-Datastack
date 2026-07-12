WITH all_matches AS (
    -- Home team perspective
    SELECT
        group_name,
        home_team                                               AS team,
        score_home                                              AS goals_for,
        score_away                                              AS goals_against,
        CASE WHEN score_home > score_away THEN 1 ELSE 0 END    AS wins,
        CASE WHEN score_home = score_away THEN 1 ELSE 0 END    AS draws,
        CASE WHEN score_home < score_away THEN 1 ELSE 0 END    AS losses,
        CASE 
            WHEN score_home > score_away THEN 3
            WHEN score_home = score_away THEN 1
            ELSE 0 
        END                                                     AS points
    FROM STAGING_WC2026.STAGING.STG_MATCH_EVENTS
    WHERE status = 'FINISHED'
    AND group_name IS NOT NULL

    UNION ALL

    -- Away team perspective — fill this in yourself
    SELECT
        group_name,
        away_team                                         AS team,
        score_away                                              AS goals_for,
        score_home                                            AS goals_against,
        CASE WHEN score_away > score_home THEN 1 ELSE 0 END    AS wins,
        CASE WHEN score_away = score_home THEN 1 ELSE 0 END    AS draws,
        CASE WHEN score_away < score_home THEN 1 ELSE 0 END    AS losses,
        CASE 
            WHEN score_away > score_home THEN 3
            WHEN score_away = score_home THEN 1
            ELSE 0 
        END                                                     AS points
    FROM STAGING_WC2026.STAGING.STG_MATCH_EVENTS
    WHERE status = 'FINISHED'
    AND group_name IS NOT NULL
)

SELECT
    group_name,
    team,
    SUM(wins)                                    AS wins,
    SUM(draws)                                   AS draws,
    SUM(losses)                                  AS losses,
    COUNT(*)                                     AS matches_played,
    SUM(goals_for)                               AS goals_for,
    SUM(goals_against)                           AS goals_against,
    SUM(goals_for) - SUM(goals_against)          AS goal_difference,
    SUM(points)                                  AS points
FROM all_matches
GROUP BY group_name, team
ORDER BY group_name, points DESC, goal_difference DESC