from dotenv import load_dotenv
import os

import base64
import requests
import json

import openai

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

response = openai.Completion.create(
  engine="text-davinci-003",
  prompt="What dinosaurs lived in the cretaceous period?",
  max_tokens=10
)

print(response.choices[0].text.strip())


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

# returns a dictionary of genres and their frequency given a list of artist ids
def get_genres_from_artists(token, artists: list[str]) -> dict[str, int]:
    genres = {}
    
    for artist in artists:
        url = "https://api.spotify.com/v1/artists/" + artist
        headers = get_auth_header(token)
        response = requests.get(url, headers=headers)
        result = json.loads(response.content)
        result = result["genres"]
        for genre in result:
            genres[genre] = genres.get(genre, 0) + 1
        
    # return the genres sorted by frequency
    return dict(sorted(genres.items(), key=lambda x: x[1], reverse=True))
        

#returns json of playlist
def get_playlist(token, playlist_id):
    url = "https://api.spotify.com/v1/playlists/" + playlist_id + "/tracks"
    headers = get_auth_header(token)
    response = requests.get(url, headers=headers)
    result = json.dumps(json.loads(response.content))
    return result

# returns array of artists within playlist
def get_artists_from_playlist(json_playlist):
    artists = []
    playlist = json.loads(json_playlist)
    for item in playlist["items"]:
        artists.append(item["track"]["artists"][0]["id"])
    
    # returns artist ids
    return artists
    
def recommend_songs(token, genres:dict, artists:list[str], num_songs: int):
    url = "https://api.spotify.com/v1/recommendations"
    headers = get_auth_header(token)
    params = {
        "limit": num_songs,
        "seed_artists": artists,
        "seed_genres": (list(genres.keys()))[:5],
    }
    response = requests.get(url, headers=headers, params=params)
    result = json.dumps(json.loads(response.content))
    return result
    
def getValuesFromSongs(json_songs):
    tracks = json.loads(json_songs)

    track = {}
    songs = []
    for item in tracks["tracks"]:
        track["song"] =   item["name"]
        track["artist"] = item["artists"][0]["name"]
        track["album"] =  item["album"]["name"]
        track["image"] =  item["album"]["images"][0]["url"]
        songs.append(track)
        track = {}

    return songs

# token = get_token()
# map = get_playlist(token, "3gW3MRRNkjlnbrwC8LVE9H")
# genres = get_genres_from_artists(token, get_artists_from_playlist(map))
# artists = get_artists_from_playlist(map)
# print("Artists:", get_artists_from_playlist(map))
# print(" ")
# # print("Recommended Songs: " + "\n")
# songs = recommend_songs(token, genres, artists, 10)
# # print(songs)
# print(getValuesFromSongs(songs))