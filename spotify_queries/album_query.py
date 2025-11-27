import requests
from .credentials import query_headers

track_limit = 50

def get_album_length(album_id):

    album_url = f'https://api.spotify.com/v1/albums/{album_id}'
    
    response = requests.get(url=album_url, headers=query_headers)

    if response.status_code == 200:

        album = response.json()
        album_length = album["tracks"]["total"]
        return album_length

    else:
        raise str(response.status_code) + "\nError in retrieving album."

def get_spotify_album_ids(album_id):

    track_count = get_album_length(album_id)
    requests_needed = track_count // track_limit + 1

    spotify_id_list = []
    
    for i in range(requests_needed):
        track_offset = i*track_limit
        url = f'https://api.spotify.com/v1/albums/{album_id}/tracks?limit={track_limit}&offset={track_offset}'

        response = requests.get(url=url, headers=query_headers)

        if response.status_code == 200:
            tracks = response.json()

            upper_bound = min(track_limit, track_count - track_offset)
            for i in range(upper_bound):
                try:
                    track_id = tracks["items"][i]["id"]
                    spotify_id_list.append(track_id)
                except TypeError: # bad API call
                    pass

        else:
            raise str(response.status_code) + "\nError in retrieving album tracks."

    return spotify_id_list