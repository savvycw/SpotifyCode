import streamlit as st
import Main
import pandas as pd
import buildingAnalysis
import matplotlib.pyplot as plt
import plotly.graph_objects as go
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

    fig = go.Figure()
    fig.add_trace(go.Histogram(
        x=df['Artist Popularity'],
        name='Artist Popularity', # name used in legend and hover labels
        xbins=dict( # bins used for histogram
            start=0,
            end=100,
            size=5
        ),
        marker_color='#EB89B5',
        opacity=0.75
    ))
    fig.add_trace(go.Histogram(
        x=df['Track Popularity'],
        name='Track Popularity',
        xbins=dict(
            start=0,
            end=100,
            size=5
        ),
        marker_color='#330C73',
        opacity=0.75
    ))

    fig.update_layout(
        title_text='Sampled Results', # title of plot
        xaxis_range = [0,100],
        xaxis_title_text='Value', # xaxis label
        yaxis_title_text='Count', # yaxis label
        bargap=0.2, # gap between bars of adjacent location coordinates
        bargroupgap=0.1 # gap between bars of the same location coordinates
    )

    st.plotly_chart(fig, use_container_width=True)