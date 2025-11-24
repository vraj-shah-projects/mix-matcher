import requests

headers = {
    'Accept' : 'application/json'
}

data = 'grant_type=client_credentials&client_id=59a133469ffc487c824e4d97122954db&client_secret=579debde9a064dc3a586e213d58f23c8'

url = 'https://api.reccobeats.com/v1/track/2a716c67-b388-4250-8abb-a127d7c78856/audio-features'
track_link = ''

response = requests.get(url=url,headers=headers)
if response.status_code == 200:
    data = response.json()
    print(data)
    #print(f'{data['name']} - {data['artists'][0]['name']}')
else:
    print(response.status_code)