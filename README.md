# mix-matcher
**Program that generates Spotify song recommendations based on current listenings**

To generate reccomendations based on the user's preferences,
the user is able to input one of four query types (with their respective Spotify URL):

TRACK - a single song  
ARTIST - the top 10 tracks of a particular artist  
ALBUM - an artist's specific collection of tracks  
PLAYLIST - a user's personally made collection of tracks  

The program then makes call(s) to Spotify's API in order to retrieve the IDs of all the relevant tracks, 
storing the IDs in a list.

Then, the ReccoBeats API retrieves its own local unique ID for each Spotify ID, using this to retrieve audio
features for each track (i.e., energy, tempo, danceability etc.). 
These audio features and their values will be used as the basis for clustering songs with similar audio experiences.

**The parameters (audio features) selected for the clustering are:**

    acousticness (float between 0 and 1): 
    a measure of how much a song is composed of natural sounds as opposed to synthetic/electronic noise

    danceability (float between 0 and 1):
    suitability of the song for dancing and its overall rhythmic engagement

    energy (float between 0 and 1):
    liveliness and intensity of a track, ranging from calm/relaxed to upbeat/intense

    instrumentalness (float between 0 and 1):
    what portion of the track is composed of instruments as opposed to vocal noise

    loudness (float typically between -60 and 0 dB):
    loudness of a track measured in dB

    speechiness (float between 0 and 1):
    indicates what portion of the track is spoken

    tempo (float typically between 0 and 250 BPM):
    speed of the track in beats per minute

    valence (float between 0 and 1):
    measure of the emotional tone of the track, with lower values representing more mellow, melancholic songs, and higher values representing more joyful and cheery songs.

Each track is stored in a Pandas dataframe with their Spotify ID, name, artists and the aforementioned parameters.