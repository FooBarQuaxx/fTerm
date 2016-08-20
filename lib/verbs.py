"""
[fTerm] verbs.py

This module defines all of the standard "verbs", or commands, for fTerm.
"""

# NOTE: this is extraneous
# pylint: disable-msg=C0103

# for running shell operations
import subprocess

# for sort
import re

# for reading files
import os


synonyms = {
    "files":"list",
    "switch":"swap",
    "move":"relocate",
    "organize":"sort",
    "organise":"sort",
    "exec":"run",
    "execute":"run",
    "evaluate":"run",
    "space":"size",
    "remove":"delete",
    "annul":"delete",
    "wipe":"delete",
    "display":"read",
    "write":"edit",
    "compose":"edit",
    "revise":"edit",
    "append":"addline",
    "removeline":"removeline",
    "end":"kill",
    "commands":"commands",
    "assistance":"help",
    }

#
# DIRECTORY OPERATIONS
#
 
def List(*dirs): # name capitalised for no name conflict
    """List the files in a directory."""
    return "ls %s;" % (' '.join(dirs))


def swap(file1, file2):
    """A function that swaps the names of two files."""

    call = ""

    # make a temporary file
    temp = subprocess.Popen(["mktemp", "-d"], stdout=subprocess.PIPE).communicate()[0].replace("\n", "")

    # move 1 to temp
    call += "mv %s %s/;" % (file1, temp)

    # move 2 to 1
    call += "mv %s %s;" % (file2, file1)

    # move temp to 1
    call += "mv %s/%s %s;" % (temp, file1, file2)

    return call


def delete(*files):
    """Delete a file or directory."""
    return 'rm -rf %s;' * len(files) % tuple(files)


def move(filename, pos):
    """Move the file or folder at *path1* to *path2*."""
    return "mv -r %s %s" % (filename, pos)


def sort(directory, exp):
    """Takes a directory *directory* and a regular expression *exp*. Sorts each file into a
    folder with name equal to the match of *exp* in its filename."""

    call = ""

    # files to sort
    files = os.listdir(directory)

    # make folders to sort
    folders = [re.search(exp, x).group(0) for x in files]

    # in case a directory name is the same as the name of a file
    tempfiles = [subprocess.Popen(["mktemp", "-d"], stdout=subprocess.PIPE).communicate()[0].replace("\n", "") for x in files]
    for i in range(len(files)):
        call += "mv %s %s/%s;" % (files[i], tempfiles[i], files[i])

    # create directories
    for item in set(folders):
        call += "mkdir %s;" % (item)

    # do sorting
    for i in range(len(files)):
        call += "mv %s/%s %s/;" % (tempfiles[i], files[i], folders[i])

    return call


#
# EDITING FILES
#


def read(*files):
    """Read a file."""
    return 'cat %s;' % tuple(files)

def edit(*files):
    """Edit a file."""
    return 'nano %s;' * len(files) % tuple(files)

def addline(filename, line):
    """Append *line* to *filename*."""
    return 'echo %s >> %s;' % (line, filename)

def removeline(filename, line):
    """Remove *line* from file *filename*."""

    data = open(filename.replace("\\", ""), "r").readlines()

    del data[int(line)]

    open(filename.replace("\\",""), "w").writelines(data)

    return ":;"


#
# MISCELLANEOUS
#


def size(*files):
    """Return the size of a file in human-readable format."""
    return "du -sh %s;" * len(files) % files
        
def run(*files):
    """A universal run function."""

    # filter filename to appropriate command
    command = {"py" : "python %s;", "rb" : "ruby %s;", "sh" : "sh %s;", "pl" : "perl %s;"}

    # run the files
    return ''.join(["echo %s:;" % (x) + command.setdefault(x.split(".")[1], "echo '[f-i] Filetype %s not recognized';") % (x) for x in files])

def kill(*processes):
    """Kill the process with name *processname*."""
    return "pkill %s;" * len(processes) % tuple(processes)
