SELECT DISTINCT
    match_id,
    home_team,
    away_team,
    score_away,
    score_home,
    stage,
    status,
    CASE 
        WHEN score_home > score_away THEN 'Home Win'
        WHEN score_home < score_away THEN 'Away Win'
        ELSE 'Draw'
    END AS result
FROM STAGING_WC2026.STAGING.STG_MATCH_EVENTS
WHERE status = 'FINISHED'