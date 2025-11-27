headers = {
    'Accept' : 'application/json'
}

def get_audio_features(id_list):

    for id in id_list:
        audio_url = f'https://api.reccobeats.com/v1/track/{id}/audio-features'