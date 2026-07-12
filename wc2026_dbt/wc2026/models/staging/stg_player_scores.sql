SELECT
    RAW_DATA:player_id::INTEGER AS player_id,
    RAW_DATA:player_name::VARCHAR AS player_name,
    RAW_DATA:assists::INTEGER AS assists,
    RAW_DATA:goals::INTEGER AS goals,
    RAW_DATA:nationality::VARCHAR AS nationality,
    RAW_DATA:played_matches::INTEGER AS played_matches,
    RAW_DATA:team::VARCHAR AS team,
    RAW_DATA:position::VARCHAR AS position
FROM RAW_WC2026.RAW.RAW_PLAYER_SCORES

