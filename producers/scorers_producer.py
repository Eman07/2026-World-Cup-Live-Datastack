from kafka import KafkaProducer
import json
import requests

API_URL = "https://api.football-data.org/v4/competitions/WC/scorers"
API_KEY = "bd07e0f08a6c4c638547bd3ea6157b5b"

headers = {
    "X-Auth-Token": API_KEY
}

response = requests.get(API_URL, headers= headers)

producer = KafkaProducer(
    bootstrap_servers='127.0.0.1:29092',
    value_serializer=lambda x: json.dumps(x).encode('utf-8')
)

for scorers in response.json()['scorers']:
    message = {
    "player_id":      scorers['player']['id'],
    "player_name":    scorers['player']['name'],
    "nationality":    scorers['player']['nationality'],
    "position":       scorers['player']['position'],
    "team":           scorers['team']['shortName'],
    "played_matches": scorers['playedMatches'],
    "goals":          scorers['goals'],
    "assists":        scorers['assists'],
    "penalties":      scorers['penalties'],
    }
    
    producer.send('player-scores', value=message)

producer.flush()
print("Sent to Kafka — check localhost:8082")