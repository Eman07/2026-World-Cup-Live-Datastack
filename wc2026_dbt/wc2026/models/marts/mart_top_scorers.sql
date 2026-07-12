SELECT
    player_name,
    team,
    nationality,
    goals,
    assists,
    played_matches,
    goals + COALESCE(assists, 0)                    AS goal_contributions,
    ROUND(goals::FLOAT / NULLIF(played_matches, 0), 2) AS goals_per_game,
    RANK() OVER (ORDER BY goals DESC)               AS goal_rank
FROM STAGING_WC2026.STAGING.STG_PLAYER_SCORES
ORDER BY goal_rank