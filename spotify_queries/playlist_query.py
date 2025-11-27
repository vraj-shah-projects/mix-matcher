import requests
import os

auth_token = os.getenv("AUTH_TOKEN")
headers = {
    'Authorization' : f'Bearer {auth_token}'
}
track_limit = 100

#def get_playlist_length(playlist_id):

def get_spotify_ids(playlist_id):

    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit={track_limit}'
    spotify_id_list = []

    response = requests.get(url=url, headers=headers)

    if response.status_code == 200:
        tracks = response.json()

        track_count = tracks["total"]

        for i in range(track_count):
            try:
                track_id = tracks["items"][i]["track"]["id"]
                spotify_id_list.append(track_id)
            except TypeError: # bad API call
                pass

    else:
        print(str(response.status_code) + "\nError in retrieving playlist tracks.")
    
    print(len(spotify_id_list))
    return spotify_id_list
