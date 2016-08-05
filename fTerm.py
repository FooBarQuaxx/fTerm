"""
fTerm 0.0.1a
Liam Schumm
"""

# pylint: disable-msg=C0103

# allows parsing of arguments (argv)
import sys

# NLP parser
import parser

# import actual functions
import core

def shellquote(s):
    print s,
    return "'" + s.replace("'", "'\\''") + "'"

def run():
    """The main function for fTerm"""

    argnum = len(sys.argv)
    if argnum == 1:
        print "[f] Please specify a command (e.g., 'f swap file1 file2')"
        return
    else:
        # retrieve the function
        try:
            print "[f]",
            f = core.verbs[parser.printAndParse(sys.argv[1])]
        except KeyError:
            print "[f] Invalid function '%s'" % (sys.argv[1])
            return

        # ensure that the correct number of arguments are being passed
        if argnum - 2 != f.func_code.co_argcount:
            print "[f] Wrong number of arguments for function %s" % (sys.argv[1])
        else:
            f(*map(shellquote,sys.argv[2:]))

run()
