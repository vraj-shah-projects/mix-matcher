import requests
from .credentials import query_headers

# return as a list
def get_spotify_track_id(track_id):
    return [track_id]

def get_name_and_artists(track_id):
    track_url = f'https://api.spotify.com/v1/tracks/{track_id}'
    
    response = requests.get(url=track_url, headers=query_headers)

    if response.status_code == 200:
        track = response.json()
        name = track["name"]

        artists = []
        artist_count = len(track["artists"])

        for i in range(artist_count):
            artists.append(f"'{track["artists"][i]["name"]}'")

        return name, artists

    else:
        print(str(response.status_code) + "\nError in retrieving track from Spotify. Please enter a valid ID.")
        return None

def format_track_desc(name, artists):
    artist_count = len(artists)
    
    track_credits = ""
    
    for i in range(artist_count):
        track_credits += f"{artists[i]}, "
        
    track_credits = track_credits[:-2]

    return f"{name} by {track_credits}"