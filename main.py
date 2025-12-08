from reccobeats_queries import get_recco_ids, get_audio_features
from spotify_queries import make_query, get_type_id_from_link, get_name_and_artists, format_track_desc

# testing value
test_link = 'https://open.spotify.com/track/4RAanjdCy7GKo8ijZlDq6O?si=84637c00d8c4409e'

if __name__ == "__main__":

    #refresh_auth_token()
    type, id = get_type_id_from_link(test_link)

    spotify_id_list = make_query(type, id)
    recco_id_list = get_recco_ids(spotify_id_list)

    for recco_id in recco_id_list:
        audio_features = get_audio_features(recco_id)
        spotify_id = get_type_id_from_link(audio_features['href'])[1]
        name, artists = get_name_and_artists(spotify_id)
        
        print(format_track_desc(name, artists))
        print(audio_features)
        print("\n")