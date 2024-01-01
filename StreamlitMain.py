import streamlit as st
import Main
import pandas as pd
import buildingAnalysis
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import matplotlib.dates as mdates

color_dict = {"Track Popularity": "blue",
              "Artist Popularity": "orange",
              "Danceability": "green",
              "Acousticness": "red",
              "Energy": "purple",
              "Instrumentalness": "brown",
              "Liveness": "pink",
              "Speachiness": "gray",
              "Valence": "cyan"}


st.title("Test")
url = st.text_input("Paste Playlist URL")


placeholder = st.empty()

if st.button('Load Playlist'):
    with placeholder.container():
        loading = st.write("Loading your Playlist, This may take a moment")
    id = (url.split("/"))[-1]
    print(id)
    df = Main.load_playlist(url)
    st.session_state['df'] = df
    placeholder.empty()
    st.write("Your Analysis is ready")

#if url:
options = st.multiselect(
'Select Stats',
["Track Popularity", "Artist Popularity", "Danceability", "Acousticness", "Energy", "Instrumentalness", "Liveness", "Speachiness", "Valence"])
if options:
    loaded_df = st.session_state['df']
    loaded_df1 = pd.DataFrame(loaded_df)

    if len(options) == 1:
        arr = loaded_df1[options[0]]
        colors = [color_dict[options[0]]]
        fig, ax = plt.subplots()
        ax.hist((arr), bins=20, range=(0,100), histtype ='bar', color = colors, label = colors)
        red_patch = mpatches.Patch(color=str(color_dict[options[0]]), label=str(options[0]))
        ax.legend(handles=[red_patch])
    if len(options) == 2:
        arr = loaded_df1[options[0]]
        arr1 = loaded_df1[options[1]]
        colors = [color_dict[options[0]], color_dict[options[1]]]
        fig, ax = plt.subplots()
        ax.hist((arr, arr1), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
    if len(options) == 3:
        arr = loaded_df1[options[0]]
        arr1 = loaded_df1[options[1]]
        arr2 = loaded_df1[options[2]]
        colors = [color_dict[options[0]], color_dict[options[1]], color_dict[options[2]]]
        fig, ax = plt.subplots()
        ax.hist((arr, arr1, arr2), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
    if len(options) == 4:
        arr = loaded_df1[options[0]]
        arr1 = loaded_df1[options[1]]
        arr2 = loaded_df1[options[2]]
        arr3 = loaded_df1[options[3]]
        colors = [color_dict[options[0]], color_dict[options[1]], color_dict[options[2]], color_dict[options[3]]]
        fig, ax = plt.subplots()
        ax.hist((arr, arr1, arr2, arr3), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
    if len(options) == 5:
        arr = loaded_df1[options[0]]
        arr1 = loaded_df1[options[1]]
        arr2 = loaded_df1[options[2]]
        arr3 = loaded_df1[options[3]]
        arr4 = loaded_df1[options[4]]
        colors = [color_dict[options[0]], color_dict[options[1]], color_dict[options[2]], color_dict[options[3]], color_dict[options[4]]]
        fig, ax = plt.subplots()
        ax.hist((arr, arr1, arr2, arr3, arr4), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
    if len(options) == 6:
        arr = loaded_df1[options[0]]
        arr1 = loaded_df1[options[1]]
        arr2 = loaded_df1[options[2]]
        arr3 = loaded_df1[options[3]]
        arr4 = loaded_df1[options[4]]
        arr5 = loaded_df1[options[5]]
        colors = [color_dict[options[0]], color_dict[options[1]], color_dict[options[2]], color_dict[options[3]], color_dict[options[4]], color_dict[options[5]]]
        fig, ax = plt.subplots()
        ax.hist((arr, arr1, arr2, arr3, arr4, arr5), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
    if len(options) == 7:
        arr = loaded_df1[options[0]]
        arr1 = loaded_df1[options[1]]
        arr2 = loaded_df1[options[2]]
        arr3 = loaded_df1[options[3]]
        arr4 = loaded_df1[options[4]]
        arr5 = loaded_df1[options[5]]
        arr6 = loaded_df1[options[6]]
        colors = [color_dict[options[0]], color_dict[options[1]], color_dict[options[2]], color_dict[options[3]], color_dict[options[4]], color_dict[options[5]], color_dict[options[6]]]
        fig, ax = plt.subplots()
        ax.hist((arr, arr1, arr2, arr3, arr4, arr5, arr6), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
    if len(options) == 8:
        arr = loaded_df1[options[0]]
        arr1 = loaded_df1[options[1]]
        arr2 = loaded_df1[options[2]]
        arr3 = loaded_df1[options[3]]
        arr4 = loaded_df1[options[4]]
        arr5 = loaded_df1[options[5]]
        arr6 = loaded_df1[options[6]]
        arr7 = loaded_df1[options[7]]
        colors = [color_dict[options[0]], color_dict[options[1]], color_dict[options[2]], color_dict[options[3]], color_dict[options[4]], color_dict[options[5]], color_dict[options[6]], color_dict[options[7]]]
        fig, ax = plt.subplots()
        ax.hist((arr, arr1, arr2, arr3, arr4, arr5, arr6, arr7), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
    if len(options) == 9:
        arr = loaded_df1[options[0]]
        arr1 = loaded_df1[options[1]]
        arr2 = loaded_df1[options[2]]
        arr3 = loaded_df1[options[3]]
        arr4 = loaded_df1[options[4]]
        arr5 = loaded_df1[options[5]]
        arr6 = loaded_df1[options[6]]
        arr7 = loaded_df1[options[7]]
        arr8 = loaded_df1[options[8]]
        colors = [color_dict[options[0]], color_dict[options[1]], color_dict[options[2]], color_dict[options[3]], color_dict[options[4]], color_dict[options[5]], color_dict[options[6]], color_dict[options[7]], color_dict[options[8]]]
        fig, ax = plt.subplots()
        ax.hist((arr, arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
    # for x in options:
        # colors = ['green', 'blue']
        # arr = df['Track Popularity']
        # arg = df['Artist Popularity']
        # #print(track_pop)
        # fig, ax = plt.subplots()
        # ax.hist((arr,arg), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
        # plt.legend(prop ={'size': 10})
    # arr = df[option]
    # fig, ax = plt.subplots()
    # ax.hist(arr, bins=20, range=(0,100))

    st.pyplot(fig)

loaded_df = st.session_state['df']
loaded_df1 = pd.DataFrame(loaded_df)
loaded_df1[['Release Year', 'Release Month', 'Release Day']] = (loaded_df1['Release Date'].str.split('-', expand=True))
loaded_df1["Release Year"] = pd.to_numeric(loaded_df1["Release Year"])
arg = loaded_df1["Release Year"]
fig1, ax = plt.subplots()
ax.hist((arg), histtype ='bar', range=((int(loaded_df1["Release Year"].min())), (int(loaded_df1["Release Year"].max()))), color = 'red', label= 'red')
red_patch = mpatches.Patch(color='red', label="Release Date")
ax.legend(handles=[red_patch])

loaded_df = st.session_state['df']
loaded_df1 = pd.DataFrame(loaded_df)
arg2 = loaded_df1["Loudness"]
fig2, ax2 = plt.subplots()
ax2.hist((arg2), histtype ='bar', range=(-60, 0), color = 'green', label= 'green')
green_patch = mpatches.Patch(color='green', label="Loudness")
ax2.legend(handles=[green_patch])
print(loaded_df1['Loudness'])

loaded_df = st.session_state['df']
loaded_df1 = pd.DataFrame(loaded_df)
arg3 = loaded_df1["Album Label"]
fig3, ax3 = plt.subplots()
ax3.hist((arg3), histtype ='bar', color = 'blue', label= 'blue')
blue_patch = mpatches.Patch(color='blue', label="Album Labels")
ax3.legend(handles=[blue_patch])

loaded_df = st.session_state['df']
loaded_df1 = pd.DataFrame(loaded_df)
arg4 = loaded_df1["Track Duration"]
fig4, ax4 = plt.subplots()
ax4.hist((arg4), histtype ='bar', color = 'yellow', label= 'yellow')
yellow_patch = mpatches.Patch(color='yellow', label="Track Duration")
ax4.legend(handles=[yellow_patch])

st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)
st.pyplot(fig4)
