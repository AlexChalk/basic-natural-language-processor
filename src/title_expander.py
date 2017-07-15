from nltk import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords
from nltk.tokenize import wordpunct_tokenize
import pandas as pd
import re

df = pd.read_csv('../openreg_dataset.csv')

stop_words = set(stopwords.words('english'))

df['TOKEN'] = df.TITLE.map(lambda x: [word.lower() for word in word_tokenize(x) \
        if (word.isalpha()) & (word.lower() not in stop_words)])

def get_list_of_names(synsets):
    return [synset.lemmas()[0].name() for synset in synsets]

def combine_synset_names_into_list(token_list):
    array = []
    for word in token_list:
        synsets = wn.synsets(word)
        list_of_names = get_list_of_names(synsets)
        array += list_of_names

    return sorted(set(array))
def stem_the_list(list):
    array = []
    for item in list:
        if re.search('[a-zA-Z]', item):
            array.append(item)
    return [stemmer.stem(t) for t in array]

def do_everything(list):
    list = combine_synset_names_into_list(list)
    return stem_the_list(list)

df['KEYWORD'] = [do_everything(names) for names in df.TOKEN]
