from .track_query import get_spotify_track_id
from .artist_query import get_spotify_artist_top_tracks_ids
from .album_query import get_spotify_album_ids
from .playlist_query import get_spotify_playlist_ids

def get_type_id_from_link(link):
    segments = link.split('/')
    type = segments[-2]
    id = segments[-1].split('?')[0]
    return (type, id)

def make_query(type, id):

    match type:
        case "track":
            spotify_id_list = get_spotify_track_id(id)
            query_message = f"Retrieving audio features from the {type}...\n"

        case "artist":
            spotify_id_list = get_spotify_artist_top_tracks_ids(id)
            query_message = f"Retrieving audio features from the {type}'s top tracks...\n"

        case "album":
            spotify_id_list = get_spotify_album_ids(id)
            query_message = f"Retrieving audio features from the {type}'s tracks...\n"
            
        case "playlist":
            spotify_id_list = get_spotify_playlist_ids(id)
            query_message = f"Retrieving audio features from your {type}'s tracks...\n"

        case _:
            print("Enter a valid Spotify URL.")
            raise RuntimeError
    
    if not spotify_id_list:
        print("No valid IDs to parse.")
        raise RuntimeError
    
    print(query_message)
    return spotify_id_list