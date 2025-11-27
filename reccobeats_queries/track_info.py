import requests

headers = {
    'Accept' : 'application/json'
}

def get_track_info(id):
    url = f'https://api.reccobeats.com/v1/track/{id}'

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        track = response.json()

        title = track["trackTitle"]

        artists = ""
        artist_count = len(track["artists"])

        for i in range(artist_count):
            artists += f"{track["artists"][i]["name"]}, "
        artists = artists[:-2]

        return f"{title} by {artists}"

    else:
        raise str(response.status_code) + "\nError in retrieving track info from ReccoBeats."