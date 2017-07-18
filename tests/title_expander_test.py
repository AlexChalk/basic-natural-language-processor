import pytest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from src.title_expander import *

df = pd.read_csv('./tests/test_csv.csv')

def test_add_tokens():
    add_tokens(df)
    assert df.TOKEN[0] == ['cushions', 'blankets']

def test_get_names():
    assert get_names(wn.synsets('world')) == ['universe',
                                              'world',
                                              'world',
                                              'Earth',
                                              'populace',
                                              'world',
                                              'worldly_concern',
                                              'world',
                                              'global']

def test_add_synonyms():
    result = [get_synonyms(keywords) for keywords in df.TOKEN]
    assert result == [['blanket', 'cushion', 'shock_absorber'], ['animal', 'artwork', 'creature']]

def test_stem_list():
    result = [stem_list(keywords) for keywords in df.TOKEN]
    assert result == [['cushion', 'blanket'], ['creatur', 'artwork']]

def test_get_synonyms_and_stem():
    result = [get_synonyms_and_stem(keywords) for keywords in df.TOKEN]
    assert result == [['blanket', 'cushion', 'shock_absorb'], ['anim', 'artwork', 'creatur']]

def test_add_keywords():
    add_keywords(df)
    assert df.KEYWORD[0] == ['blanket', 'cushion', 'shock_absorb']
