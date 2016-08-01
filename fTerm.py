#
# fTerm 0.0.1a
# Liam Schumm
#

# allows parsing of arguments (argv)
import sys

# import actual functions
import core

# return our results
core.getFunc[sys.argv[1]](*sys.argv[2:])
