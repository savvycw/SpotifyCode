import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
import dotenv
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

SPOTIPY_CLIENT_ID = os.getenv('ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SECRET')

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                           client_secret=SPOTIPY_CLIENT_SECRET))
artist_name_list = [] #Check
track_name_list = [] #Check
track_id_list = [] #Check
album_genre_list = [] #Check
artist_genre_list = [] #Check
release_date_list = [] #Check
track_pop_list = [] #Check
album_label_list = [] #Check
artist_pop_list = [] #Check
track_duration_list = [] #Check



playlist = sp.playlist("spotify:playlist:0QjKBUqAyz6PKzuEKOL8pS")
#trackids = sp.playlist_tracks("spotify:playlist:0QjKBUqAyz6PKzuEKOL8pS")["items"]

for track in sp.playlist_tracks("spotify:playlist:0QjKBUqAyz6PKzuEKOL8pS")["items"]:
    #URI
    track_id = track["track"]["uri"]
    track_id_list.append(track_id)
    
    #Track name
    track_name = track["track"]["name"]
    track_name_list.append(track_name)
    track_duration = track["track"]["duration_ms"]
    track_duration_list.append(track_duration)
    
    #Main Artist
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    
    #Name, popularity, genre
    artist_name = track["track"]["artists"][0]["name"]
    artist_name_list.append(artist_name)
    artist_pop = artist_info["popularity"]
    artist_pop_list.append(artist_pop)
    artist_genres = artist_info["genres"]
    artist_genre_list.append(artist_genres)
    
    #Album
    album_uri = track["track"]["album"]["uri"]
    album_info = sp.album(album_uri)

    album_genres = album_info["genres"]
    album_genre_list.append(album_genres)

    album_label = album_info["label"]
    album_label_list.append(album_label)
    
    #Popularity of the track
    track_pop = track["track"]["popularity"]
    track_pop_list.append(track_pop)
    release_date = track["track"]["album"]["release_date"]
    release_date_list.append(release_date)


#print(sp.audio_features(track_id_list[1]))
trackinfo = sp.track(track_id_list[1])
# artist = sp.artist(trackinfo["artists"][0]["external_urls"]["spotify"])
# print(artist["genres"])
# album = sp.album(trackinfo["album"]["external_urls"]["spotify"])
# print("album genres:", album["genres"])


df = pd.DataFrame({"track ID" : track_id_list,"Track Name" : track_name_list,"Artist Name":artist_name_list})


#id = [item['uri'] for item in playlist['items']]
#print(playlist['tracks']['href'])
# playlist = sp.user_playlists('savvythenobody')

# 4z25eUyui5hAyT6agODm7R
# results = sp.search(q='weezer', limit=20)
# for idx, track in enumerate(results['tracks']['items']):
#     print(idx, track['name'])