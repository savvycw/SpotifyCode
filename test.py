import matplotlib.pyplot as plt
import buildingAnalysis
import Main
import pandas as pd

df = pd.read_json("C:\\Users\\savan\\OneDrive\\Documents\\Codeee\\SpotifyDF.json")
#track_pop = buildingAnalysis.track_popularity(df)

colors = ['green', 'blue']
arr = df['Track Popularity']
arg = df['Artist Popularity']
#print(track_pop)
fig, ax = plt.subplots()
ax.hist((arr,arg), bins=20, range=(0,100), density = True, histtype ='bar', color = colors, label = colors)
plt.legend(prop ={'size': 10})
plt.show()