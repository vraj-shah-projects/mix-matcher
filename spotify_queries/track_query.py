import requests
from .credentials import query_headers

# return as a list
def get_spotify_track_id(track_id):
    return [track_id]


def get_spotify_track_info(track_id):
    track_url = f'https://api.spotify.com/v1/tracks/{track_id}'
    
    response = requests.get(url=track_url, headers=query_headers)

    if response.status_code == 200:
        track = response.json()
        title = track["name"]

        artists = ""
        artist_count = len(track["artists"])

        for i in range(artist_count):
            artists += f"{track["artists"][i]["name"]}, "
        artists = artists[:-2]

        return f"{title} by {artists}"

    else:
        print(str(response.status_code) + "\nError in retrieving track from Spotify. Please enter a valid ID.")
        return None