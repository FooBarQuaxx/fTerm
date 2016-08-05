"""
fTerm 0.0.1a
Liam Schumm
"""

# for synonym matching
from PyDictionary import PyDictionary
PyDictionary = PyDictionary()

# for string matching
from difflib import get_close_matches

# import words
from verbs import verbs
from nouns import nouns

words = verbs.keys()
#words.append(nouns.keys())

# build command lookup
net = {}
for word1 in words:
    for word2 in PyDictionary.synonym(word1):
        net[word2] = word1

def parse(word):
    """Interpret word as a fTerm word."""
    if word in words:
        return word;
    elif net[word] != []:
        return net[word]
    else:
        lookup = get_close_matches(word,words)
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