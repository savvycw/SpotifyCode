import streamlit as st
import Main
import pandas as pd
import buildingAnalysis
import matplotlib.pyplot as plt
import numpy as np

st.title("Test")
url = st.text_input("Paste Playlist URL")

placeholder = st.empty()

if url:
    with placeholder.container():
        loading = st.write("Loading your Playlist, This may take a moment")
    df = Main.load_playlist(url)
    placeholder.empty()
    st.write("Your Analysis is ready")

    arr = df['Track Popularity']
    fig, ax = plt.subplots()
    ax.hist(arr, bins=20, range=(0,100))

    st.pyplot(fig)