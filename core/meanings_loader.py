"""This module is created so that developers may set their own custom path for meanings.p (in case
they are not running it off Homebrew)"""

# for synonym matching
meanings = {}
for item in open("/usr/local/Library/Taps/lschumm/homebrew-fterm/core/meanings.p", "r").read().split("\n"):
    if (item != "") and (item[0] != "#"):
        parsedItem = item.split(":")
        meanings[parsedItem[0]] = parsedItem[0]
        meanings[parsedItem[1]] = parsedItem[0]
