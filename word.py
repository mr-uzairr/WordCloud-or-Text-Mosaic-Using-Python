import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import WordCloud, STOPWORDS

#use STOPWORDS to remove common words like 'the' 'a' etc

a = str(input("Enter the name of word which you want to make word cloud = "))
title = wikipedia.search(a)[0] # it will search the title from wikipedia


page = wikipedia.page(title)
text = page.content # To extract the content of that topic
print(text)


bg = np.array(Image.open("Image.jpeg")) #download the background image
unwated_words = set(STOPWORDS)
wordclo = WordCloud(background_color = "black", max_words = 400, mask = bg, stopwords = unwated_words)
wordclo.generate(text)
wordclo.to_file("sample.png") #Genration of the image


