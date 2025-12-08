from sklearn import preprocessing
import pandas as pd

path = r'clustering\data\tracks_features.csv'

# the info we want to keep in the dataframe for 
track_details = ["id", "name" , "artists"]
parameters = ["acousticness", "danceability", "energy", "instrumentalness", "loudness", "speechiness", "tempo", "valence"]

df = pd.read_csv(path)
modified_df = df[track_details + parameters]
print(modified_df.head())

#def new_dataframe(ids, names, artists, audio_features):


#def update_dataframe()