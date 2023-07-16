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

playlist = sp.playlist("spotify:playlist:0QjKBUqAyz6PKzuEKOL8pS")

for track in sp.playlist_tracks("spotify:playlist:0QjKBUqAyz6PKzuEKOL8pS")["items"]:
    #URI
    track_id = track["track"]["uri"]
    track_id_list.append(track_id)

    trackinfo = sp.audio_features(track_id)
    trackAnalyis = sp.audio_analysis(track_id)

    danceability = trackinfo[0]['danceability']
    danceability_list.append(danceability)

    acousticness = trackinfo[0]['acousticness']
    acousticness_list.append(acousticness)

    energy = trackinfo[0]['energy']
    energy_list.append(energy)

    instrumentalness = trackinfo[0]['instrumentalness']
    instrumentalness_list.append(instrumentalness)

    liveness = trackinfo[0]['liveness']
    liveness_list.append(liveness)

    loudness = trackinfo[0]['loudness']
    loudness_list.append(loudness)

    speechiness = trackinfo[0]['speechiness']
    speechiness_list.append(speechiness)

    valence = trackinfo[0]['valence']
    valence_list.append(valence)

    tempo = trackAnalyis['track']['tempo']
    tempo_list.append(tempo)

    tempo_confidence = trackAnalyis['track']['tempo_confidence']
    tempo_confidence_list.append(tempo_confidence)

    time_sig = trackAnalyis['track']['time_signature']
    time_sig_list.append(time_sig)

    time_sig_confidence = trackAnalyis['track']['time_signature_confidence']
    time_sig_confidence_list.append(time_sig_confidence)

    key = trackAnalyis['track']['key']
    key_list.append(key)

    key_confidence = trackAnalyis['track']['key_confidence']
    key_confidence_list.append(key_confidence)

    mode = trackAnalyis['track']['mode']
    mode_list.append(mode)

    mode_confidence = trackAnalyis['track']['mode_confidence']
    mode_confidence_list.append(mode_confidence)
    
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


df = pd.DataFrame({"Track ID" : track_id_list,
                   "Track Name" : track_name_list,
                   "Artist Name":artist_name_list,
                   "Album Genre": album_genre_list,
                   "Artist Genre": artist_genre_list,
                   "Release Date": release_date_list,
                   "Track Popularity": track_pop_list,
                   "Artist Popularity": artist_pop_list,
                   "Album Label": album_label_list,
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
                   "Mode Confidence": mode_confidence_list,
                   "Tempo": tempo_list,
                   "Tempo Confidence": tempo_confidence_list,
                   "Time Signature": time_sig_list,
                   "Time Signature Confidence": time_sig_confidence_list,
                   "Key": key_list,
                   "Key Confidence": key_confidence_list})


def genre_analysis_artist(df):
    artist_genre_analysis = []
    for index, row in df.iterrows():
        for x in row["Artist Genre"]:
            artist_genre_analysis.append(x)
    genreDF = pd.DataFrame(artist_genre_analysis)
    print(genreDF.value_counts())

def release_date_analysis(df):
    release_year = []
    for index, row in df.iterrows():
        x = str(row['Release Date'])
        x = x.split('-')
        release_year.append(x[0])
    yearDF = pd.DataFrame(release_year)
    yearDF = yearDF.astype(int)
    min = yearDF.min()
    max = yearDF.max()

    #make the larger the range the less important the year is
    range = max - min

    #do a prefrence on newer or older
    mean = yearDF.mean()

    #map and look for clusters
    print(yearDF.value_counts())
release_date_analysis(df)