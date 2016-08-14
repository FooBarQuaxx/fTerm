"""
[fTerm] load.py

This module parses commands, interpreting them first with a synonym check (for
any words that are synonymous with the word in question that are fTerm commands),
and secondly with a difflib.get_close_matches check (in case of typos).
"""

# NOTE: this is extraneous
# pylint: disable-msg=C0103

# NOTE: this use of eval is safe
# pylint: disable-msg=W0123

import lib

verbs = {}
synonyms = {}

for item in dir(lib):
    if ("__" not in item) and (item != "os"):
        package = eval("lib.%s" % (item))
        for func in dir(package):
            if func == "synonyms":
                synonyms.update(eval("lib.%s.%s" % (item, func)))
            elif "__" not in func:
                verbs[func.lower()] = eval("lib.%s.%s" % (item, func))

# filter out imports
for item in verbs:
    if item not in synonyms.values():
        del verbs[item]

def commands():
    """List all fTerm commands."""

    call = ""

    for verb in verbs:
        call += "echo %s : %s;" % (verb, verbs[verb].__doc__)

    return call

verbs["commands"] = commands

 # define our help function on current getFunc


def Help(command):  # name capitalised for no name conflict
    """Print the docstring of a command."""

    command = command.replace("'", "")
    if command == "help":
        return "echo [f] Print the docstring of a command.;"
    else:
        return "echo [f] %s;" % (verbs[command].__doc__)

verbs["help"] = Help
