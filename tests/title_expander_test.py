import pytest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from src.title_expander import *

df = pd.read_csv('./tests/test_csv.csv')
df['TOKEN'] = df.TITLE.map(lambda x: [word.lower() for word in word_tokenize(x) \
        if (word.isalpha()) & (word.lower() not in stop_words)])

def test_adds_token_column():
    assert df.TOKEN[0] == ['cushions', 'blankets']
    assert df.TOKEN[1] == ['creatures', 'artworks']

def test_synset_names_function():
    assert get_list_of_names(wn.synsets('world')) == ['universe',
            'world',
            'world',
            'Earth',
            'populace',
            'world',
            'worldly_concern',
            'world',
            'global']

def test_combine_synset_names_function():
    result = [combine_synset_names_into_list(names) for names in df.TOKEN]
    assert result == [['blanket', 'cushion', 'shock_absorber'], ['animal', 'artwork', 'creature']]
