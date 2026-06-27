import re
import nltk
from nltk.stem import SnowballStemmer
from simplemma import lemmatize
from nltk.corpus import stopwords

#megkeresi a pageben levo szavak szamat
def find_index_number(pagecontent):
    # ebben taroljuk a szavakat, es helyet
    index = {}

    text = pagecontent['text']

    #toldalektalaniti a szavakat
    stemmer = SnowballStemmer('hungarian')

    #stop szavak szuro
    stopword = set(stopwords.words('hungarian'))
    #szetvalaszt megkeres
    for tok in [i for i in re.split(r'(\d+|\W+)', text) if i]:

        #kis nagy betu ne legyen kulonbseg
        tok = tok.lower()

        #megvalositja a toldalektalanitast
        tok = stemmer.stem(tok)

        #stop szo kiszedes az indexbol
        if tok in stopword:
            continue

        if len(tok) < 2:
            continue

        #elso talalat a szora
        if not tok in index:
            index[tok] = 1
        else:
            index[tok] = index[tok] + 1

    return index
