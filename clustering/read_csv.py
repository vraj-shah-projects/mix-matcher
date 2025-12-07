import pandas as pd
path = r'clustering\data\tracks_features.csv'
# the info we want to keep in the dataframe for 
track_details = ["id", "name" , "artists"]
parameters = ["acousticness", "danceability", "energy", "instrumentalness", "loudness", "speechiness", "tempo", "valence"]

df = pd.read_csv(path)



