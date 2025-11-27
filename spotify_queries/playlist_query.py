import requests
from .credentials import query_headers

track_limit = 100

def get_playlist_length(playlist_id):

    playlist_url = f'https://api.spotify.com/v1/playlists/{playlist_id}'
    
    response = requests.get(url=playlist_url, headers=query_headers)

    if response.status_code == 200:

        playlist = response.json()
        playlist_length = playlist["tracks"]["total"]
        return playlist_length

    else:
        return str(response.status_code) + "\nError in retrieving playlist."


def get_spotify_ids(playlist_id):

    track_count = get_playlist_length(playlist_id)
    requests_needed = track_count // track_limit + 1

    spotify_id_list = []
    
    for i in range(requests_needed):
        track_offset = i*track_limit
        url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks?limit={track_limit}&offset={track_offset}'

        response = requests.get(url=url, headers=query_headers)

        if response.status_code == 200:
            tracks = response.json()

            upper_bound = min(track_limit, track_count - track_offset)
            for i in range(upper_bound):
                try:
                    track_id = tracks["items"][i]["track"]["id"]
                    spotify_id_list.append(track_id)
                except TypeError: # bad API call
                    pass

        else:
            print(str(response.status_code) + "\nError in retrieving playlist tracks.")

    print(spotify_id_list)
    print(len(spotify_id_list))
    return spotify_id_list
