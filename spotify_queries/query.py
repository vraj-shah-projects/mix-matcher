from .track_query import get_spotify_track_id
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
        case "album":
            spotify_id_list = get_spotify_album_ids(id)
        case "playlist":
            spotify_id_list = get_spotify_playlist_ids(id)
        case _:
            print("Enter a valid Spotify URL.")
            raise RuntimeError
    
    return spotify_id_list