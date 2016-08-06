"""
fTerm 0.0.1a
Liam Schumm
"""

# NOTE: this is extraneous
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

    print "[f] Swapped %s and %s" % (file1, file2)

def run(filename):
    """A universal run function."""

    # filter filename to appropriate command
    command = {"py" : "python %s", "rb" : "ruby %s", "sh" : "sh %s", "pl" : "perl %s"}

    # get file extension
    ext = filename.split(".")[1]

    # print the command we're going to run
    print "[f]", command[ext] % (filename)

    # run the file
    os.system(command[ext] % (filename))


def size(filename):
    """Return the size of a file in human-readable format."""
    os.system('echo [f] File size: $(echo %s | awk -F " " {\'print $5\'})' % (filename))


def delete(filename):
    """Delete a file or directory."""
    os.system('rm -rf %s' % (filename))


def dlist():
    """List the files in a directory."""
    print os.system("ls")


def read(filename):
    """Read a file."""
    os.system('cat %s' % (filename))


def edit(filename):
    """Edit a file."""
    os.system('nano %s' % (filename))


# translator from string to function
verbs = {"swap":swap,
         "run":run,
         "size":size,
         "delete":delete,
         "read":read,
         "edit":edit,
        }

def clist():
    """List all fTerm commands."""
    for verb in verbs:
        print verb, verbs[verb].__doc__

verbs["list"] = clist

# define our help function on current getFunc
def fhelp(command):
    """Print the docstring of a command."""
    command = command.replace("'", "")
    if command == "help":
        print "[f] Print the docstring of a command."
    else:
        print "[f] %s" % (verbs[command].__doc__)

verbs["help"] = fhelp
