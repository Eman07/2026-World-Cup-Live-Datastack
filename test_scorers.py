import requests

playerAPI_URL = "https://api.football-data.org/v4/competitions/WC/scorers"
playerAPI_KEY = "bd07e0f08a6c4c638547bd3ea6157b5b"

headers = {
    "X-Auth-Token": playerAPI_KEY
    }

response = requests.get(playerAPI_URL, headers=headers)
scorers = response.json()['scorers']
for scorers in scorers:
     print(scorers)