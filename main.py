from reccobeats_queries import get_recco_ids, get_audio_features
from spotify_queries import make_query, get_type_id_from_link, get_name_and_artists, format_track_desc
#from clustering import update_dataframe
from build import build_dataframe

# testing value
test_link = 'https://open.spotify.com/album/4SZko61aMnmgvNhfhgTuD3?highlight=spotify:track:4ZPdLEztrlZqbJkgHNw54L'

if __name__ == "__main__":

    #refresh_auth_token()
    type, id = get_type_id_from_link(test_link)

    spotify_id_list = make_query(type, id)
    recco_id_list = get_recco_ids(spotify_id_list)
 
    new_df = build_dataframe(recco_id_list)
    #update_dataframe(new_df)