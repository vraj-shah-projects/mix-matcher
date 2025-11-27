import requests
from credentials import client_id, client_secret

headers = {
    'Content-Type' : 'application/x-www-form-urlencoded'
}

token_url = 'https://accounts.spotify.com/api/token'
credentials = f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'

response = requests.post(url=token_url, headers=headers, data=credentials)

if response.status_code == 200:
    token = response.json()
    print(token["access_token"])
else:
    print(response.status_code)