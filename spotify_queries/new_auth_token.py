import requests
from queries import client_id, client_secret

headers = {
    'Content-Type' : 'application/x-www-form-urlencoded'
}

token_url = 'https://accounts.spotify.com/api/token'
client_credentials = f'grant_type=client_credentials&client_id={client_id}&client_secret={client_secret}'

def refresh_auth_token():
    response = requests.post(url=token_url, headers=headers, data=client_credentials)

    if response.status_code == 200:
        token_details = response.json()
        print(token_details["access_token"])

    else:
        return str(response.status_code) + "\nCould not retrieve new access token."

refresh_auth_token()