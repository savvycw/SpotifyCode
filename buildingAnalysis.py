import pandas as pd

df = pd.read_json("C:\\Users\\savan\\OneDrive\\Documents\\Codeee\\SpotifyDF.json")

def genre_analysis_artist(df):
    artist_genre_analysis = []
    for index, row in df.iterrows():
        for x in row['Artist Genre']:
            artist_genre_analysis.append(x)
    genreDF = pd.DataFrame(artist_genre_analysis)
    artistGenre = genreDF.value_counts()
    return artistGenre

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
    years = yearDF.value_counts()
    return range, mean, years


def track_popularity(df):
    track_popularity_mode = []
    trackPopRounded = []
    for index,row in df.iterrows():
        x = (row['Track Popularity'])
        x = x/10
        trackPopRounded.append(int(x))
    trackPopRoundedDF = pd.DataFrame(trackPopRounded)
    trackPopRoundedDF = pd.DataFrame(trackPopRoundedDF.value_counts())
    lastRow = 0
    total = len(trackPopRoundedDF)
    signifigance = (total/10)*2
    for index,row in trackPopRoundedDF.iterrows():
        if (row['count']) > signifigance:
            track_popularity_mode.append(index[0])
    
    return track_popularity_mode

def artist_popularity(df):
    artistPopRounded = []
    artist_popularity_mode = []
    for index, row in df.iterrows():
        x = (row['Artist Popularity'])
        x = x/10
        artistPopRounded.append(int(x))
    artistPopRoundedDF = pd.DataFrame(artistPopRounded)
    artistPopRoundedDF = pd.DataFrame(artistPopRoundedDF.value_counts())
    lastRow = 0
    total = len(artistPopRoundedDF)
    signifigance = (total/10)*2
    for index,row in artistPopRoundedDF.iterrows():
        if (row['count']) > signifigance:
            artist_popularity_mode.append(index[0])
    return artist_popularity_mode

def label(df):
    return (df['Album Label'].value_counts())

def track_length(df):
    songLength = []
    for index, row in df.iterrows():
        x = row['Track Duration']
        print(x)
        x = x/1000
        songLength.append(x)
    songLength.sort()
    short = ((songLength[0] + songLength[1] + songLength[2] + songLength[3] + songLength[4])/5)
    songLength.sort(reverse=True)
    long = ((songLength[0] + songLength[1] + songLength[2] + songLength[3] + songLength[4])/5)
    return short, long

def score(df, var):
    print(var)
    varList = []
    varMode = []
    for index, row in df.iterrows():
        x = row[var]
        x = x*10
        varList.append(int(x))
    print(varList)
    varRoundedDF = pd.DataFrame(varList)
    varRoundedDF = pd.DataFrame(varRoundedDF.value_counts())
    lastRow = 0
    total = len(varList)
    signifigance = (total/10)*2
    for index,row in varRoundedDF.iterrows():
        if (row['count']) > signifigance:
            varMode.append(index[0])
    return varMode

def loudnessScore(df):
    for index, row in df.iterrows():
        x = row['Loudness']
        print(x)

def tempo(df):
    tempoScore = []
    for index, row in df.iterrows():
        x = row['Tempo']
        yinput = 'Tempo' + " Confidence"
        y = row[yinput]
        if y>.4:
            tempoScore.append(x)
    tempoDF = pd.DataFrame(tempoScore)
    tempoDF = tempoDF.astype(int)
    print(tempoDF)
    min = tempoDF.min()
    max = tempoDF.max()
    mean = tempoDF.mean()
    
    
    

def withConfidenceScore(df, var):
    scoreList = []
    finalList = []
    for index, row in df.iterrows():
        x = row[var]
        yinput = var + " Confidence"
        y = row[yinput]
        if y>.5:
            scoreList.append(x)
    df2 = pd.DataFrame(scoreList)
    print(scoreList)
    values = pd.DataFrame(df2.value_counts())
    print(values)
    total = len(df2)
    denominator = len(values)
    print(total,denominator)
    signifigance = (total/denominator)
    print(signifigance)
    for index,row in values.iterrows():
        if (row['count']) > signifigance:
            finalList.append(index[0])
    print(finalList)

print(tempo(df))
#add strength to the score ones( percentage of the values) highere the percentage the more it matters