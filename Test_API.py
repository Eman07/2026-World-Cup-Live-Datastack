import requests

FootballAPI_URL = "https://api.football-data.org/v4/competitions/WC/matches"
FootballAPI_KEY = "bd07e0f08a6c4c638547bd3ea6157b5b"

headers = {
    "X-Auth-Token": FootballAPI_KEY
    }


response = requests.get(FootballAPI_URL, headers = headers)
for match in response.json()['matches']:
    print (match)
    
import requests

API_URL = "https://api.football-data.org/v4/competitions/WC/matches"
API_KEY = "bd07e0f08a6c4c638547bd3ea6157b5b"

headers = {"X-Auth-Token": API_KEY}

response = requests.get(API_URL, headers=headers)
match = response.json()['matches'][0]
print(match.keys())
print(match)
    