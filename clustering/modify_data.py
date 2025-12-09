import pandas as pd
from sklearn.preprocessing import StandardScaler

path = r'clustering\data\tracks_features.pkl'

track_details = ["id", "name" , "artists"]
parameters = ["acousticness", "danceability", "energy", "instrumentalness", "loudness", "speechiness", "tempo", "valence"]

def standardise(df):
    df_scaled = df.copy()
    scaler = StandardScaler()
    df_scaled[parameters] = scaler.fit_transform(df_scaled[parameters])

    return df_scaled