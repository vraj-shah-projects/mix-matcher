import pandas as pd
from reccobeats_queries import get_audio_features
from spotify_queries import get_type_id_from_link, get_name_and_artists, format_track_desc
from clustering import path, track_details, parameters, standardise

def build_dataframe(recco_ids):

    # build Pandas DataFrame from dictionary
    columns = track_details + parameters
    data = {col : [] for col in columns}

    for id in recco_ids:
        audio_features = get_audio_features(id)
        spotify_id = get_type_id_from_link(audio_features['href'])[1]
        name, artists = get_name_and_artists(spotify_id)

        data["id"].append(spotify_id)
        data["name"].append(name)
        data["artists"].append(artists)

        for param in parameters:
            data[param].append(audio_features[param])

        #print(format_track_desc(name, artists))
        #print(audio_features)
        #print("\n")
    
    df = pd.DataFrame(data)
    return df
    #return df[["name", "artists", "danceability", "energy", "valence"]]

def update_dataframe(new_df):
    # Read from current dataset in track_features.pkl, and combine dataframes
    try:
        current_df = pd.read_pickle(path)
    except Exception:
        current_df = pd.DataFrame()

    df = pd.concat([current_df, new_df], ignore_index=True)
    return df
        