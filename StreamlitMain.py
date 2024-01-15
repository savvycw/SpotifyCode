import streamlit as st
import Main
import pandas as pd
#import buildingAnalysis
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.dates as mdates
import plotly.figure_factory as ff
import plotly.express as px
import plotly.graph_objects as go

color_dict = {"Track Popularity": "blue",
              "Artist Popularity": "orange",
              "Danceability": "green",
              "Acousticness": "red",
              "Energy": "purple",
              "Instrumentalness": "brown",
              "Liveness": "pink",
              "Speachiness": "gray",
              "Valence": "cyan"}

st.set_page_config(layout="wide")
st.title("Spotify Playlist Analysis")
# st.markdown("<h1 style='text-align: center; color: red;'>otherTitle</h1>", unsafe_allow_html=True)
st.markdown("Paste playlist URL and press 'Load Playlist' to see stats about your playlists \n\r This is a work in progress more to come")
url = st.text_input("Paste Playlist URL")

placeholder = st.empty()
SPOTIFY_CLIENT_ID = st.secrets["SPOTIPY_CLIENT_ID"]
SECRET = st.secrets["SECRET"]

if st.button('Load Playlist'):
    with placeholder.container():
        loading = st.write("Loading your Playlist, This may take some time, especially if the playlist is long")
    id = (url.split("/"))[-1]
    df = Main.load_playlist(url, SPOTIFY_CLIENT_ID, SECRET)
    st.session_state['df'] = df
    placeholder.empty()
    st.write("Your Analysis is ready")

    chart_names = ["Track Popularity", "Artist Popularity", "Danceability", "Acousticness", "Energy", "Instrumentalness", "Liveness", "Speachiness", "Valence"]

    loaded_df = st.session_state['df']
    loaded_df1 = pd.DataFrame(loaded_df)

    chart_names = ["Track Popularity", "Artist Popularity", "Danceability", "Acousticness", "Energy", "Instrumentalness", "Liveness", "Speachiness", "Valence"]
    l1 = loaded_df1["Track Popularity"]
    l2 = loaded_df1["Artist Popularity"]
    l3 = loaded_df1["Danceability"]
    l4 = loaded_df1["Acousticness"]
    l5 = loaded_df1["Energy"]
    l6 = loaded_df1["Instrumentalness"]
    l7 = loaded_df1["Liveness"]
    l8 = loaded_df1["Speachiness"]
    l9 = loaded_df1["Valence"]


    fig = ff.create_distplot([l1,l2,l3,l4,l5,l6,l7,l8,l9], chart_names, bin_size=5)
    fig.update_layout(xaxis_range=[0, 100])

    loaded_df1[['Release Year', 'Release Month', 'Release Day']] = (loaded_df1['Release Date'].str.split('-', expand=True))
    loaded_df1["Release Year"] = pd.to_numeric(loaded_df1["Release Year"])

    fig1 = ff.create_distplot([loaded_df1["Release Year"]],  ['Release Year'], bin_size=.3, histnorm = '', show_curve = False, colors=['firebrick'])

    fig2 = ff.create_distplot([loaded_df1["Loudness"]],  ['Loudness'],histnorm = '', show_curve = False, colors=['mediumorchid'])
    fig2.update_layout(xaxis_range=[-60, 0])


    arg3 = loaded_df1["Album Label"].value_counts()
    ylist = []
    for x in arg3.index:
        ylist.append(x)

    fig3 = go.Figure(go.Bar(x = arg3.values, y=ylist,orientation='h', marker_color='gold'))

    fig4 = ff.create_distplot([loaded_df1["Track Duration"]],  ['Track Duration'], bin_size= 5, histnorm = '', show_curve = False, colors=['cyan'])

    fig8 = ff.create_distplot([loaded_df1["Tempo"]],  ['Tempo'], bin_size= 5, histnorm = '', show_curve = False, colors=['limegreen'])

    loaded_df1["Mode String"] = loaded_df1["Mode"]
    loaded_df1["Key String"] = loaded_df1["Key"]

    for x, row in loaded_df1.iterrows():
        if loaded_df1["Mode"][x] == 1:
            loaded_df1["Mode String"][x] = "Major"
        if loaded_df1["Mode"][x] == 0:
            loaded_df1["Mode String"][x] = "Minor"
        if loaded_df1["Key"][x] == 0:
            loaded_df1["Key String"][x] = "C"
        if loaded_df1["Key"][x] == 1:
            loaded_df1["Key String"][x] = "C♯/D♭"
        if loaded_df1["Key"][x] == 2:
            loaded_df1["Key String"][x] = "D"
        if loaded_df1["Key"][x] == 3:
            loaded_df1["Key String"][x] = "E♭/D♯"
        if loaded_df1["Key"][x] == 4:
            loaded_df1["Key String"][x] = "E"
        if loaded_df1["Key"][x] == 5:
            loaded_df1["Key String"][x] = "F"
        if loaded_df1["Key"][x] == 6:
            loaded_df1["Key String"][x] = "F♯/G♭"
        if loaded_df1["Key"][x] == 7:
            loaded_df1["Key String"][x] = "G"
        if loaded_df1["Key"][x] == 8:
            loaded_df1["Key String"][x] = "G♯/A♭"
        if loaded_df1["Key"][x] == 9:
            loaded_df1["Key String"][x] = "A"
        if loaded_df1["Key"][x] == 10:
            loaded_df1["Key String"][x] = "A♯/B♭"
        if loaded_df1["Key"][x] == 11:
            loaded_df1["Key String"][x] = "B"
        

    fig5 = px.pie(loaded_df1, names= 'Mode String', color_discrete_sequence=px.colors.qualitative.Set2)

    fig6 = px.pie(loaded_df1, names= 'Key String', color_discrete_sequence=px.colors.qualitative.Bold)

    fig7 = px.pie(loaded_df1, names = 'Time Signature', color_discrete_sequence=px.colors.qualitative.Safe)

    with st.container():
        st.subheader("Audio Features")
        c1, c2 = st.columns([2,1])
        c1.plotly_chart(fig)
        c2.write("Valence: 100 = Cheerful/Happy, 0 = Sad/Angry \n\r Speachiness: 100 = Spoken(talk show/audio book), 0 = Totaly Sung \n\r Liveness: 100 = Likely a Live Show, 0 = Likely Recorded \n\r Instrumentalness: 100 = No Vocal Content, 0 = Contains Vocal Content(Spoken or Sung) \n\r Energy: 100 = High Energy, 0 = Low Energy \n\r Acousticness: 100 = Likely Acoustic, 0 = Likely Not Acoustic \n\r Dancabliltiy: 100 = Very Dancable, 0 = Very Undancable \n\r Popularity: 100 = Very Popular, 0 = Very Unpopular")
        #c2.write(r"$\textsf{\scriptsize Valence: 100 = Cheerful/Happy, 0 = Sad/Angry }$")

    with st.container():
        c1, c2, c3 = st.columns([2,5,1])
        c2.subheader("Release Year")
        c2.plotly_chart(fig1)
        c2.subheader("Loudness in db")
        c2.plotly_chart(fig2)
        c2.subheader("Record Labels")
        c2.plotly_chart(fig3)
        c2.subheader("Track Duration in Seconds")
        c2.plotly_chart(fig4)
        c2.subheader("Tempo in bpm")
        c2.plotly_chart(fig8)
        c2.subheader("Mode")
        c2.plotly_chart(fig5)
        c2.subheader("Key")
        c2.plotly_chart(fig6)
        c2.subheader("Time Signature")
        c2.plotly_chart(fig7)

st.markdown("Data retrieval is thanks to Spotify API")

#****************************************************************************
#
# from here: I will work on a good way to show artists and genres in playlist
# Comparing to other playlists
# Lyrical Analysis
# Recomendations
# Commenting on data. Ex: "You like more recent songs"
#
#*****************************************************************************