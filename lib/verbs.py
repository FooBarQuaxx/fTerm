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
    "space":"size",
    "remove":"delete",
    "annul":"delete",
    "wipe":"delete",
    "display":"read",
    "write":"edit",
    "compose":"edit",
    "revise":"edit",
    "append":"addline",
    "commands":"commands", # there must be an entry
    "assistance":"help",
    }

#
# DIRECTORY OPERATIONS
#

def List(): # name capitalised for no name conflict
    """List the files in a directory."""
    return "ls;"


def swap(file1, file2):
    """A function that swaps the names of two files."""

    call = ""

    # make a temporary file
    temp = subprocess.Popen(["mktemp"], stdout=subprocess.PIPE).communicate()[0].replace("\n", "")

    # move 1 to temp
    call += "mv %s %s;" % (file1, temp)

    # move 2 to 1
    call += "mv %s %s;" % (file2, file1)

    # move temp to 1
    call += "mv %s %s;" % (temp, file2)

    return call


def delete(filename):
    """Delete a file or directory."""
    return 'rm -rf %s;' % (filename)


def move(filename, pos):
    """Move *filename* to folder *pos*."""
    return "mv -r %s %s" % (filename, pos)


def sort(directory, exp):
    """'Takes a directory and either a regular expression, or a range of numbers
    (e.g., 2:5). Sorts the directory based on '"""

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

def read(filename):
    """Read a file."""
    return 'cat %s;' % (filename)


def edit(filename):
    """Edit a file."""
    return 'nano %s;' % (filename)

def addline(filename, line):
    """Append *line* to *filename*."""
    return 'echo %s >> %s;' % (filename, line)


#
# MISCELLANEOUS
#

def size(filename):
    """Return the size of a file in human-readable format."""
    return 'echo [f] File size: $(echo %s | awk -F " " {\'print $5\'});' % (filename)

def run(filename):
    """A universal run function."""

    # filter filename to appropriate command
    command = {"py" : "python %s;", "rb" : "ruby %s;", "sh" : "sh %s;", "pl" : "perl %s;"}

    # get file extension
    ext = filename.split(".")[1]

    # run the file
    return command[ext] % (filename)

def kill(processname):
    """Kill the process with name *processname*."""
    return "pkill %s" % (processname)
