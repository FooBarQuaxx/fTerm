# NOTE: this use of eval is safe
# pylint: disable-msg=W0123

import main

verbs = {}
synonyms = {}

for item in dir(main):
    if ("__" not in item) and (item != "os"):
        package = eval("main.%s" % (item))
        for func in dir(package):
            if func == "synonyms":
                synonyms.update(eval("main.%s.%s" % (item, func)))
            elif ("__" not in func):
                verbs[func.lower()] = eval("main.%s.%s" % (item, func))

# filter out imports
for item in verbs.keys():
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
