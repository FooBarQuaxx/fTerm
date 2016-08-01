#
# fTerm 0.0.1a
# Liam Schumm
#

# allows parsing of arguments (argv)
import sys

# import actual functions
import core

# return our results
print(core.funcs[sys.argv[1]](*sys.argv[2:]))
