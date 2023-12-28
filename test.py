import matplotlib.pyplot as plt
import buildingAnalysis
import Main
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

df = pd.read_json("C:\\Users\\savan\\OneDrive\\Documents\\Codeee\\SpotifyDF.json")
#track_pop = buildingAnalysis.track_popularity(df)

colors = ['green', 'blue']
arr = df['Track Popularity']
arg = df['Artist Popularity']