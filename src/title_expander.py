from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
import pandas as pd
import re
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
df = pd.read_csv('../openreg_dataset.csv')
stop_words = set(stopwords.words('english'))


def add_tokens(data):
    data['TOKEN'] = data.TITLE.map(lambda x: [word.lower() for word in word_tokenize(x) \
            if (word.isalpha()) & (word.lower() not in stop_words)])
            
def get_names(synsets):
    return [synset.lemmas()[0].name() for synset in synsets]

def get_synonyms(token_list):
    array = []
    for word in token_list:
        synsets = wn.synsets(word)
        synset_names = get_names(synsets)
        array += synset_names
    return sorted(set(array))

def stem_list(list):
    array = []
    for item in list:
        if re.search('[a-zA-Z]', item):
            array.append(item)
    return [stemmer.stem(t) for t in array]

def get_synonyms_and_stem(list):
    list = get_synonyms(list)
    return stem_list(list)

def add_keywords(data):
    data['KEYWORD'] = [get_synonyms_and_stem(keywords) for keywords in data.TOKEN]
