import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()
load_dotenv(dotenv_path)

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")
auth_token = os.getenv("AUTH_TOKEN")

query_headers = {
    'Authorization' : f'Bearer {auth_token}'
}