from reccobeats_queries import get_recco_ids, get_recco_track_info, get_audio_features
from spotify_queries import get_type_id_from_link, get_spotify_track_id, get_spotify_track_info, get_spotify_album_ids, get_spotify_playlist_ids

# testing value
test_link = 'https://open.spotify.com/album/4SZko61aMnmgvNhfhgTuD3?si=J7yUg2JpQC-Cu6WV6whd6A'

if __name__ == "__main__":

    #refresh_auth_token()
    type, id = get_type_id_from_link(test_link)
    print(f"Retrieving audio features from your {type}...")

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

    if not spotify_id_list:
        print("No valid IDs to parse.")
        raise RuntimeError

    recco_id_list = get_recco_ids(spotify_id_list)

    for recco_id in recco_id_list:
        audio_features = get_audio_features(recco_id)
        spotify_id = get_type_id_from_link(audio_features['href'])[1]
        
        print(get_spotify_track_info(spotify_id))
        print(audio_features)
        print("\n")
