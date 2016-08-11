# NOTE: extraneous
# pylint: disable-msg=C0103

# for string matching
from difflib import get_close_matches

# import words
import nouns
import verbs

# for synonym matching
synonyms = verbs.synonyms.copy()
synonyms.update(nouns.synonyms)

def parse(word):
    """Interpret word as a fTerm word."""
    if word in verbs.verbs:
        return word
    elif word in verbs.synonyms:
        return verbs.synonyms[word]
    else:
        lookup = get_close_matches(word, verbs.verbs.keys())
        if len(lookup) == 0:
            # there aren't any reasonable matches
            raise KeyError
        else:
            return lookup[0]

def nounParse(word):
    """Interpret (noun) softly (i.e., see if it's defined, if not, just pass it as an argument)."""
    if word in nouns.nouns:
        return nouns.nouns[word]
    elif word in nouns.synonyms:
        return nouns.synonyms[word]
    else:
        lookup = get_close_matches(word, nouns.nouns.keys())
        if len(lookup) == 0:
            # there aren't any reasonable matches
            return word
        else:
            return lookup[0]
