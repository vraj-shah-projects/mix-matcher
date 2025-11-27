import requests

headers = {
    'Accept' : 'application/json'
}

def get_audio_features(id):

    audio_url = f'https://api.reccobeats.com/v1/track/{id}/audio-features'

    response = requests.get(audio_url, headers=headers)

    if response.status_code == 200:
        audio_features = response.json()
        return audio_features

    else:
        print(str(response.status_code) + f"\nError in retrieving audio features of track {id}")
        raise RuntimeError