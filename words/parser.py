"""
fTerm 0.0.1a
Liam Schumm
"""

# NOTE: extraneous
# pylint: disable-msg=C0103

# for synonym matching
import pickle
meanings = pickle.load(open("/Users/lschumm/fTerm-dev/words/meanings.p", "r"))

# for string matching
from difflib import get_close_matches

# import words
from verbs import verbs
# from nouns import nouns

words = verbs.keys()
#words.append(nouns.keys())

def parse(word):
    """Interpret word as a fTerm word."""
    if word in words:
        return word
    elif meanings[word] != []:
        return meanings[word]
    else:
        lookup = get_close_matches(word, words)
        if len(lookup) == 0:
            # there aren't any reasonable matches
            raise KeyError
        else:
            return lookup[0]

def printAndParse(word):
    """Print and parse"""
    p = parse(word)
    print p,
    return p
