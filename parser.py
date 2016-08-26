"""
[fTerm] parser.py

This module parses commands, interpreting them first with a synonym check (for
any words that are synonymous with the word in question that are fTerm commands),
and secondly with a difflib.get_close_matches check (in case of typos).
"""

# NOTE: extraneous
# pylint: disable=C0103

# NOTE: for some reason, pylint doesn't recognise load.synonyms
# pylint: disable=E0611

# for string matching
from difflib import get_close_matches

# import words
from load import verbs, synonyms

def parse(word):
    """Interpret word as a fTerm word."""
    if word in synonyms.values():
        return word
    elif word in synonyms:
        return synonyms[word]
    else:
        lookup = get_close_matches(word, verbs.keys() + synonyms.keys())
        if len(lookup) == 0:
            # there aren't any reasonable matches
            raise KeyError
        else:
            if lookup[0] in synonyms:
                return synonyms[lookup[0]]
            else:
                return lookup[0]
