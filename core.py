"""
fTerm 0.0.1a
Liam Schumm
"""

# pylint: disable-msg=C0103

# for running shell operations
import os

import subprocess


def swap(file1, file2):
    """A function that swaps the names of two files."""

    # make a temporary file
    temp = subprocess.Popen(["mktemp"], stdout=subprocess.PIPE).communicate()[0].replace("\n", "")

    # move 1 to temp
    os.system("mv %s %s" % (file1, temp))

    # move 2 to 1
    os.system("mv %s %s" % (file2, file1))

    # move temp to 1
    os.system("mv %s %s" % (temp, file2))

    return ""

def run(filename):
    """A universal run function."""

    # filter filename to appropriate command
    command = {"py" : "python %s", "rb" : "ruby %s", "sh" : "sh %s", "pl" : "perl %s"}

    # get file extension
    ext = filename.split(".")[1]

    # run the file
    os.system(command[ext] % (filename))

    return ""

def size(filename):
    """Return the size of a file in human-readable format."""
    os.system('echo File size: $(ls -lah %s | awk -F " " {\'print $5\'})' % (filename))


# translator from string to function
getf = {"swap":swap,
        "run":run,
        "size":size,
       }

# define our help function on current getFunc
def fhelp(command):
    """Print the docstring of a command."""
    if command == "help":
        print "Print the docstring of a command."
    else:
        print getf[command].__doc__

getf["help"] = fhelp
