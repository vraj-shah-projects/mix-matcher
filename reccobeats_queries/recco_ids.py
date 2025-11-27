import requests

id_limit = 40

def get_recco_ids(spotify_id_list):

    recco_id_list = []
    id_count = len(spotify_id_list)
    
    requests_needed = (id_count // id_limit) + 1

    for i in range(requests_needed):

        id_url = 'https://api.reccobeats.com/v1/track?ids='

        id_offset = i*id_limit
        upper_bound = min(id_offset + id_limit, id_count)
        ids_to_parse = spotify_id_list[id_offset:upper_bound]
        #print(id_offset, upper_bound)

        for id in ids_to_parse:
            id_url += f'{id},'
        id_url = id_url[:-1]
        #print(id_url)

        response = requests.get(url=id_url)
        if response.status_code == 200:
            tracks = response.json()

            track_count = len(tracks["content"])

            for j in range(track_count):
                try:
                    track_id = tracks["content"][j]["id"]
                    recco_id_list.append(track_id)
                except TypeError: # bad API call
                    pass
        else:
            print(response.status_code)
    
    #print(len(recco_id_list))
    #print(recco_id_list)
    return recco_id_list