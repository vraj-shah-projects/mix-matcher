from reccobeats_queries import get_recco_ids
from spotify_queries import make_query, get_type_id_from_link
from dataframes import build_dataframe

# testing value
test_link = 'https://open.spotify.com/album/4Uv86qWpGTxf7fU7lG5X6F?highlight=spotify:track:4mmkhcEm1Ljy1U9nwtsxUo'
if __name__ == "__main__":

    #refresh_auth_token()
    type, id = get_type_id_from_link(test_link)

    spotify_id_list = make_query(type, id)
    recco_id_list = get_recco_ids(spotify_id_list)
 
    new_df = build_dataframe(recco_id_list)
    #print(new_df)
    #update_dataframe(new_df)