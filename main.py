from reccobeats_queries import get_recco_ids, get_recco_track_info, get_audio_features
from spotify_queries import make_query, get_type_id_from_link, get_spotify_track_info

# testing value
test_link = 'https://open.spotify.com/track/0mEdbdeRFQwBhN4xfyIeUM?si=79a99154b0b542ea'

if __name__ == "__main__":

    #refresh_auth_token()
    type, id = get_type_id_from_link(test_link)
    print(f"Retrieving audio features from your {type}...\n")

    spotify_id_list = make_query(type, id)

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
