import streamlit as st
import Main
import pandas as pd
import buildingAnalysis
import matplotlib.pyplot as plt
import numpy as np

st.title("Test")
url = st.text_input("Paste Playlist URL")

placeholder = st.empty()

if st.button('Load Playlist'):
    print("hello")
    with placeholder.container():
        loading = st.write("Loading your Playlist, This may take a moment")
    df = Main.load_playlist(url)
    placeholder.empty()
    st.write("Your Analysis is ready")

    # option = st.selectbox(
    # "Choose your stat",
    # ("Track Popularity", "Artist Popularity", "Danceability", "Acousticness", "Energy", "Instrumentalness", "Liveness", "Speachiness", "Valence"),
    # index=None,
    # placeholder="Choose Your Stat",
    # )

if url:
    options = st.multiselect(
    'Select Stats',
    ["Track Popularity", "Artist Popularity", "Danceability", "Acousticness", "Energy", "Instrumentalness", "Liveness", "Speachiness", "Valence"])

    if options:
        print(options)
        # arr = df[option]
        # fig, ax = plt.subplots()
        # ax.hist(arr, bins=20, range=(0,100))

        # st.pyplot(fig)