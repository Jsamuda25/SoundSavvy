from dotenv import load_dotenv
import os

import base64
import requests
import json

load_dotenv()

client_id = os.getenv('CLIENT_ID')
client_secret = os.getenv('CLIENT_SECRET')

response = requests.get('https://opentdb.com/api.php?amount=10')

print(response.status_code)
# print(getPlaylist('3gW3MRRNkjlnbrwC8LVE9H'))

def getPlaylist (playlistId): 
    response = requests.get('https://api.spotify.com/v1/playlists/' + playlistId)
    return response.json()

def get_token():
    auth_string = client_id + ':' + client_secret
    auth_bytes = auth_string.encode('utf-8')
    auth_base64 = str(base64.b64encode(auth_bytes), 'utf-8')

    url = "https://accounts.spotify.com/api/token"
    headers = {
        'Authorization': 'Basic ' + auth_base64,
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {"grant_type": "client_credentials"}

    response = requests.post(url, headers=headers, data=data)
    json_result = json.loads(response.content)
    token = json_result['access_token']
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def get_playlist_user(token, user_id):
    url = "https://api.spotify.com/v1/users/" + user_id + "/playlists"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    result = json.dumps(json.loads(response.content))
    
    return result


def get_playlist(token, playlist_id):
    url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    result = json.dumps(json.loads(response.content))
    
    return result
    

token = get_token()
print(get_playlist(token, "3gW3MRRNkjlnbrwC8LVE9H"))
