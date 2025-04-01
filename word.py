import sys
import numpy as np
from PIL import Image
import wikipedia
from wordcloud import wordCloud,STOPWORDS
#use STOPWORDS to remove common words like 'the' 'a' etc

a = str(input("Enter the name of word which you want to make word cloud = "))
title = wikipedia.search(a)[0] # it will search the title from wikipedia

page = wikipedia.page(title)
text = page.content # To extract the content of that topic

