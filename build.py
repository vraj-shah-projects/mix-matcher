import pandas as pd
from reccobeats_queries import get_audio_features
from spotify_queries import get_type_id_from_link, get_name_and_artists
from clustering import parameters

def build_dataframe(recco_ids):
    for id in recco_ids:
        audio_features = get_audio_features(id)
        spotify_id = get_type_id_from_link(audio_features['href'])[1]
        name, artists = get_name_and_artists(spotify_id)