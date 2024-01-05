import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import os
import dotenv
from dotenv import load_dotenv
from pathlib import Path
import numpy as np
import re
import buildingAnalysis
import spotipy.util as util

load_dotenv("C:\\Users\\savan\\OneDrive\\Documents\\Codeee\\NewSpotifyCode\\SpotifyCode\\env\\pyvenv.cfg")

SPOTIPY_CLIENT_ID = os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET = os.getenv('SECRET')
username = "savvythenobody"
scope = "user-read-currently-playing"
redirect_uri = "http://localhost:8888/callback/"

token = util.prompt_for_user_token(username, scope, SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, redirect_uri)

sp = spotipy.Spotify(auth=token)

results = sp.current_user_playing_track()
print(results)

# sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
#                                                            client_secret=SPOTIPY_CLIENT_SECRET))

# track = sp.current_user_playing_track()
# print(track)
#df = pd.read_json("C:\\Users\\savan\\OneDrive\\Documents\\Codeee\\SpotifyDF.json")
#track_pop = buildingAnalysis.track_popularity(df)

# colors = ['green', 'blue']
# arr = df['Track Popularity']
# arg = df['Artist Popularity']
# #print(track_pop)
# fig, ax = plt.subplots()
# ax.hist((arr,arg), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
# plt.legend(prop ={'size': 10})
# plt.show()
# color_dict = {"Track Popularity": "blue",
#               "Artist Popularity": "orange",
#               "Danceability": "green",
#               "Acousticness": "red",
#               "Energy": "purple",
#               "Instrumentalness": "brown",
#               "Liveness": "pink",
#               "Speachiness": "gray",
#               "Valence": "cyan"}
# print(color_dict["Acousticness"])