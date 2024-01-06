import streamlit as st
import Main
import pandas as pd
import buildingAnalysis
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


st.title("Test")
url = st.text_input("Paste Playlist URL")


placeholder = st.empty()

if st.button('Load Playlist'):
    with placeholder.container():
        loading = st.write("Loading your Playlist, This may take a moment")
    id = (url.split("/"))[-1]
    df = Main.load_playlist(url)
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
st.plotly_chart(fig)

loaded_df1[['Release Year', 'Release Month', 'Release Day']] = (loaded_df1['Release Date'].str.split('-', expand=True))
loaded_df1["Release Year"] = pd.to_numeric(loaded_df1["Release Year"])

fig1 = ff.create_distplot([loaded_df1["Release Year"]],  ['Release Year'], bin_size=.3, histnorm = '', show_curve = False)

fig2 = ff.create_distplot([loaded_df1["Loudness"]],  ['Loudness'],histnorm = '', show_curve = False)
fig2.update_layout(xaxis_range=[-60, 0])


arg3 = loaded_df1["Album Label"].value_counts()
ylist = []
for x in arg3.index:
    ylist.append(x)
print(arg3.values)

fig3 = go.Figure(go.Bar(x = arg3.values, y=ylist,orientation='h'))

fig4 = ff.create_distplot([loaded_df1["Track Duration"]],  ['Track Duration'], bin_size= 5, histnorm = '', show_curve = False)

fig8 = ff.create_distplot([loaded_df1["Tempo"]],  ['Tempo'], bin_size= 5, histnorm = '', show_curve = False)

fig5 = px.pie(loaded_df1, names= 'Mode')

fig6 = px.pie(loaded_df1, names= 'Key')

fig7 = px.pie(loaded_df1, names = 'Time Signature')

st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)
st.plotly_chart(fig4)
st.plotly_chart(fig8)
st.plotly_chart(fig5)
st.plotly_chart(fig6)
st.plotly_chart(fig7)