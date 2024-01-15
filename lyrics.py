# #####################
# # ignore this file  #
# #####################
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import re
# from sklearn.feature_extraction.text import CountVectorizer
# import nltk
# from nltk.tokenize import word_tokenize
# from collections import Counter
# import time
# nltk.download('stopwords')
# nltk.download('punkt')

# df = pd.read_json("C:\\Users\\savan\\OneDrive\\Documents\\Codeee\\SpotifyDF.json")

# url_list = []
# for index, row in df.iterrows():
#     x = row["Track Name"]
#     y = row["Artist Name"]
#     x = re.sub(r'[^a-zA-Z0-9]', '', x)
#     x = x.lower()
#     y = re.sub(r'[^a-zA-Z0-9]', '', y)
#     y = y.lower()
#     if y[0:3] == 'the':
#         y = y.replace('the','')
#     url = "https://www.azlyrics.com/lyrics/" + y + "/" + x + ".html"
#     url_list.append(url)


# song_lyrics_list = []
# for song in url_list:
#     print(song)
#     page = requests.get(song)

#     soup = BeautifulSoup(page.content,"html.parser")
#     ob_elements = soup.find_all('div',class_ = 'col-xs-12 col-lg-8 text-center')

#     #print(soup.prettify())

#     new_element = str(ob_elements)
#     splits = new_element.split("</div>")
#     lyrics = splits[5]
#     lyrics = lyrics.replace('<br/>','')
#     #print(lyrics[1])
#     lyricLine = lyrics.splitlines()
#     lyricList = []
#     for line in range(len(lyrics.splitlines())):
#         if line > 4:
#             lyricList.append(lyricLine[line])
#             #should I delete repeated lines??
#     song_lyrics_list.append(lyricList)
#     time.sleep(30)
# # stopwords = nltk.corpus.stopwords.words('english')
# # #print(stopwords)
# print(song_lyrics_list)
# # tokens = []
# # for x in lyricList:
# #     x = str(x).lower()
# #     word_tokens = word_tokenize(x)
# #     tokens.append(word_tokens)

# # stripped = []
# # for x in range(len(tokens)):
# #     for word in tokens[x]:
# #         if word not in stopwords:
# #             if len(word) > 2:
# #                 if "'" not in word:
# #                     stripped.append(word)

# # #print(stripped)

# # counter = Counter(stripped)

# # print(counter)
# # #remove stopwords and count frequency of words
# # #word vectors with training
# # #catagories as the playlist name??