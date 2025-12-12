import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

path = r'clustering\data\tmp_tracks_features.pkl'

track_details = ["id", "name" , "artists"]
parameters = ["acousticness", "danceability", "energy", "instrumentalness", "loudness", "speechiness", "tempo", "valence"]

def standardise(df):
    df_scaled = df.copy()
    scaler = StandardScaler()
    df_scaled[parameters] = scaler.fit_transform(df_scaled[parameters])

    return df_scaled

def min_max_scale(df):
    df_scaled = df.copy()
    scaler = MinMaxScaler(feature_range=(0,1))
    df_scaled[parameters] = scaler.fit_transform(df_scaled[parameters])
    
    return df_scaled

def cull(df):
    return df[parameters]

def to_np_array(df):
    df = df[parameters]
    np_array = df.to_numpy()
    return np_array