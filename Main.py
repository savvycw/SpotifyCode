import spotipy
import time
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
import dotenv
from dotenv import load_dotenv
from pathlib import Path
import numpy as np
import re
#import buildingAnalysis
import datetime

load_dotenv("C:\\Users\\savan\\OneDrive\\Documents\\Codeee\\NewSpotifyCode\\SpotifyCode\\env\\pyvenv.cfg")

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SECRET')

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
danceability_list = [] #Check
acousticness_list = [] #Check
energy_list = [] #Check
instrumentalness_list = [] #Check
liveness_list = [] #Check
loudness_list = [] #Check
mode_list = [] #Check
mode_confidence_list = [] #Check
speechiness_list = [] #Check
valence_list = []#Check
tempo_list = [] #Check
tempo_confidence_list = []#Check
time_sig_list = [] #Check
time_sig_confidence_list = []#Check
key_list = [] #Check
key_confidence_list = [] #Check


def load_playlist(url):

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
    danceability_list = [] #Check
    acousticness_list = [] #Check
    energy_list = [] #Check
    instrumentalness_list = [] #Check
    liveness_list = [] #Check
    loudness_list = [] #Check
    mode_list = [] #Check
    mode_confidence_list = [] #Check
    speechiness_list = [] #Check
    valence_list = []#Check
    tempo_list = [] #Check
    time_sig_list = [] #Check
    key_list = [] #Check
    artist_id_list = []
    album_id_list = []


    for track in sp.playlist_tracks(url)["items"]:
        track_id = track["track"]["uri"]
        track_id_list.append(track_id)

        track_name = track["track"]["name"]
        track_name_list.append(track_name)

        track_pop = track["track"]["popularity"]
        track_pop_list.append(track_pop)

        release_date = track["track"]["album"]["release_date"]
        release_date_list.append(release_date)

        artist_id = track["track"]["artists"][0]["id"]
        artist_id_list.append(artist_id)

        album_uri = track["track"]["album"]["uri"]
        album_id_list.append(album_uri)
    
        artist_name = track["track"]["artists"][0]["name"]
        artist_name_list.append(artist_name)


    audio = sp.audio_features(track_id_list)
    for x in audio:
        danceability = x['danceability']
        danceability_list.append(danceability)

        acousticness = x['acousticness']
        acousticness_list.append(acousticness)

        energy = x['energy']
        energy_list.append(energy)

        instrumentalness = x['instrumentalness']
        instrumentalness_list.append(instrumentalness)

        liveness = x['liveness']
        liveness_list.append(liveness)

        loudness = x['loudness']
        loudness_list.append(loudness)

        speechiness = x['speechiness']
        speechiness_list.append(speechiness)

        valence = x['valence']
        valence_list.append(valence)

        tempo = x['tempo']
        tempo_list.append(tempo)

        time_sig = x['time_signature']
        time_sig_list.append(time_sig)

        key = x['key']
        key_list.append(key)

        mode = x['mode']
        mode_list.append(mode)
        
        track_duration = x["duration_ms"]
        track_duration_list.append(track_duration)

    # album_data = sp.albums(album_id_list)
    # for y in album_data:
    #     album_label = y["label"]
    #     album_label_list.append(album_label)

    artist_data = sp.artists(artist_id_list)
    for z in artist_data['artists']:
        artist_pop = z["popularity"]
        artist_pop_list.append(artist_pop)
        artist_genres = z["genres"]
        artist_genre_list.append(artist_genres)

    df = pd.DataFrame({"Track ID" : track_id_list,
                    "Track Name" : track_name_list,
                    "Artist Name":artist_name_list,
                    "Artist Genre": artist_genre_list,
                    "Release Date": release_date_list,
                    "Track Popularity": track_pop_list,
                    "Artist Popularity": artist_pop_list,
                    "Track Duration": track_duration_list,
                    "Danceability": danceability_list,
                    "Acousticness": acousticness_list,
                    "Energy": energy_list,
                    "Instrumentalness": instrumentalness_list,
                    "Liveness": liveness_list,
                    "Loudness": loudness_list,
                    "Speachiness": speechiness_list,
                    "Valence": valence_list,
                    "Mode": mode_list,
                    "Tempo": tempo_list,
                    "Time Signature": time_sig_list,
                    "Key": key_list})
    
    df["Danceability"] = df["Danceability"].multiply(100)
    df["Acousticness"] = df["Acousticness"].multiply(100)
    df["Energy"] = df["Energy"].multiply(100)
    df["Instrumentalness"] = df["Instrumentalness"].multiply(100)
    df["Liveness"] = df["Liveness"].multiply(100)
    df["Speachiness"] = df["Speachiness"].multiply(100)
    df["Valence"] = df["Valence"].multiply(100)
    df["Track Duration"] = df["Track Duration"].div(1000)
    
    print(df)
    return df
# # df.to_json("C:\\Users\\savan\\OneDrive\\Documents\\Codeee\\SpotifyDF.json")

# # results = sp.search(q='my playlist', type='playlist')
# # for result in results['playlists']['items']:
# #   print(result['name'])

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
#                                                            client_secret=SPOTIPY_CLIENT_SECRET))
# print(sp.playlist_tracks('0QjKBUqAyz6PKzuEKOL8pS')["track"]["uri"])