import pytest
import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from src.title_expander import *

def test_adds_token_column():
    df = pd.read_csv('./tests/test_csv.csv')
    df['TOKEN'] = df.TITLE.map(lambda x: [word.lower() for word in word_tokenize(x) \
            if (word.isalpha()) & (word.lower() not in stop_words)])
    assert df.TOKEN[0] == ['cushions', 'blankets']
    assert df.TOKEN[1] == ['creatures', 'artworks']