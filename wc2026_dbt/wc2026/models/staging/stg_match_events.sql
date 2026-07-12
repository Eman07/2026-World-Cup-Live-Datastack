SELECT
    RAW_DATA:match_id::INTEGER    AS match_id,
    RAW_DATA:status::VARCHAR      AS status,
    RAW_DATA:stage::VARCHAR       AS stage,
    RAW_DATA:"group"::VARCHAR AS group_name,
    RAW_DATA:home_team::VARCHAR   AS home_team,
    RAW_DATA:away_team::VARCHAR   AS away_team,
    RAW_DATA:score_home::INTEGER  AS score_home,
    RAW_DATA:score_away::INTEGER  AS score_away
FROM RAW_WC2026.RAW.RAW_MATCH_EVENTS-- pipeline test
