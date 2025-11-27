import requests

max_ids = 40

def get_recco_ids(spotify_id_list):

    id_url = 'https://api.reccobeats.com/v1/track?ids='
    recco_id_list = []
    track_count = len(spotify_id_list)
    
    request_iterations = track_count // max_ids
    last_batch = track_count % max_ids

    for i in range(request_iterations):

        for id in spotify_id_list[:max_ids]:
            id_url += f'{id},'
        id_url = id_url[:-1]
    
        print(id_url)

        response = requests.get(url=id_url)
        if response.status_code == 200:
            tracks = response.json()

            track_count = len(tracks["content"])

            for j in range(track_count):
                track_id = tracks["content"][j]["id"]
                recco_id_list.append(track_id)
                print(track_id)
        else:
            print(response.status_code)
    
    print(len(recco_id_list))
    return recco_id_list