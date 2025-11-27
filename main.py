from reccobeats_queries import get_recco_ids, get_track_info, get_audio_features
from spotify_queries import get_spotify_track_id, get_spotify_album_ids, get_spotify_playlist_ids

# testing values
playlist_id = '5s2yZcg1zP6gyX5h17AmX3'
album_id = '4SZko61aMnmgvNhfhgTuD3'
track_id = '7lmeHLHBe4nmXzuXc0HDjk'

if __name__ == "__main__":
    #spotify_id_list = get_spotify_track_id(track_id)
    #spotify_id_list = get_spotify_album_ids(album_id)
    spotify_id_list = get_spotify_playlist_ids(playlist_id)

    if not spotify_id_list:
        raise "No valid IDs to parse."
    
    recco_id_list = get_recco_ids(spotify_id_list)

    for id in recco_id_list:
        print(get_track_info(id))
        print(get_audio_features(id))
        print("\n")