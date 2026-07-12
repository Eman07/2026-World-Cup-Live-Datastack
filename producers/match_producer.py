from kafka import KafkaProducer
import json
import requests

API_URL = "https://api.football-data.org/v4/competitions/WC/matches"
API_KEY = "bd07e0f08a6c4c638547bd3ea6157b5b"

headers = {
    "X-Auth-Token": API_KEY
}

response = requests.get(API_URL, headers=headers)

producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:29092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

for match in response.json()['matches']:
    if match['status'] != "TIMED":
        message = {
            "match_id":       match['id'],
            "status":         match['status'],
            "stage":          match['stage'],
            "group":          match['group'],
            "matchday":       match['matchday'],
            "utc_date":       match['utcDate'],
            "home_team":      match['homeTeam']['shortName'],
            "away_team":      match['awayTeam']['shortName'],
            "home_team_id":   match['homeTeam']['id'],
            "away_team_id":   match['awayTeam']['id'],
            "score_home":     match['score']['fullTime']['home'],
            "score_away":     match['score']['fullTime']['away'],
            "half_time_home": match['score']['halfTime']['home'],
            "half_time_away": match['score']['halfTime']['away'],
            "winner":         match['score']['winner'],
            "duration":       match['score']['duration'],
        }
        producer.send('match-events', value=message)

producer.flush()
print("Sent to Kafka — check localhost:8082")