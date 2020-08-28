from bs4 import BeautifulSoup
from wordcloud import WordCloud, STOPWORDS
from textblob import TextBlob
import warnings
warnings.simplefilter('ignore')
import requests
import textblob
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
url1 = 'https://www.idrbt.ac.in/collaborations.html'
url2 = 'https://www.idrbt.ac.in/milestones.html'
url3 = 'https://www.idrbt.ac.in/about-us.html'
url4 = 'https://www.idrbt.ac.in/idrbtahead.html'
url5 = 'https://www.idrbt.ac.in/externalprojects.html'
def text_getter(ur):
    pa = requests.get(ur, verify = False)
    Soup = BeautifulSoup(pa.content, 'lxml')
    te = Soup.find('div', attrs = {'class': 'col-md-8'})
    return te.get_text()

tex = " "
urls = [url1, url2, url3, url4, url5]
for i in urls:
    tex+=text_getter(i)
blob = TextBlob(tex)
b = blob.tags
verb = " "
noun = " "
for word, tag in b:
    if tag in ("VB", "VBD", "VBG", "VBN", "VBP", "VBZ"):
       verb = verb + ' ' + word

    if tag in ("NN", "NNS", "NNP", "NNPS"):
       noun = noun+" " + word

maskarray = np.array(Image.open('IMAG.png'))
maskarray2 = np.array(Image.open('IMge.png'))
fig, (ax1, ax2) = plt.subplots(1,2)
fig.suptitle("5 - Made of Noun's  and  G - Made of Verb's")
cloud = WordCloud(colormap = 'Dark2',background_color = 'white', max_words = 2000, max_font_size = 260, mask = maskarray,random_state = 42, stopwords = STOPWORDS)
cloud2 = WordCloud(colormap = 'Dark2',background_color = 'white', max_words = 2000, max_font_size = 260, mask = maskarray2,random_state = 42, stopwords = STOPWORDS)
cloud.generate(noun)
ax1.imshow(cloud)
ax1.axis('off')
cloud2.generate(verb)
ax2.imshow(cloud2)
ax2.axis('off')
plt.show()

