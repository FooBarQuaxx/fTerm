"""
fTerm 0.0.1b
"""

# NOTE: extraneous
# pylint: disable-msg=C0103

from os.path import expanduser

# for string matching
from difflib import get_close_matches

# import words
from verbs import verbs
# from nouns import nouns

# for synonym matching
meanings = {}
for item in open(expanduser("~/fTerm-dev/words/meanings.p"), "r").read().split("\n"):
    if (item != "") and (item[0] != "#"):
        parsedItem = item.split(":")
        meanings[parsedItem[0]] = parsedItem[0]
        meanings[parsedItem[1]] = parsedItem[0]


words = verbs.keys()
# words.append(nouns.keys())

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
