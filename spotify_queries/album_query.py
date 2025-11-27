'''
import requests
from credentials import query_headers

album_id = '6pwuKxMUkNg673KETsXPUV'
album_url = f'https://api.spotify.com/v1/albums/{album_id}/tracks?limit=50'

response = requests.get(url=album_url, headers=query_headers)

if response.status_code == 200:
    tracks = response.json()

    track_count = tracks["total"]

    for i in range(track_count):
        try:
            track_id = tracks["items"][i]["id"]
            print(tracks["items"][i]["id"])
        except Exception:
            print(i)
else:
    print(response.status_code)
'''