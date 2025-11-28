import requests
from .credentials import query_headers

def get_spotify_artist_top_tracks_ids(artist_id):
    spotify_id_list = []
    album_url = f'https://api.spotify.com/v1/artists/{artist_id}/top-tracks'
    
    # max tracks returned is always 10, so only one request is required as this does not exceed Spotify's limit of 100
    response = requests.get(url=album_url, headers=query_headers)
    if response.status_code == 200:
        top_tracks = response.json()
        track_count = len(top_tracks["tracks"])
        
        for i in range(track_count):
            try:
                track_id = top_tracks["tracks"][i]["id"]
                spotify_id_list.append(track_id)
            except TypeError: # bad API call
                pass

    else:
        print(str(response.status_code) + "\nError in retrieving artist's top tracks from Spotify.")
        raise RuntimeError

    return spotify_id_list