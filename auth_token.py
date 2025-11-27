import requests
import os

headers = {
    'Content-Type' : 'application/x-www-form-urlencoded'
}

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
token_url = 'https://accounts.spotify.com/api/token'
credentials = f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'

response = requests.post(url=token_url, headers=headers, data=credentials)

if response.status_code == 200:
    token = response.json()
    print(token)
else:
    print(response.status_code)