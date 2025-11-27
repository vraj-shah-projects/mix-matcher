from recco_ids import get_recco_ids
from spotify_queries.playlist_query import get_spotify_ids

playlist_id = '6xlO4TC7KFTnViplLjViWV'

if __name__ == "__main__":
    spotify_id_list = get_spotify_ids(playlist_id)

    if not spotify_id_list:
        raise "No valid IDs to parse."
    
    #recco_id_list = get_recco_ids(spotify_id_list)