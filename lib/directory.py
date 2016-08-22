"""
[fTerm] directory.py

This module defines all of the standard directory operations of fTerm.
"""

# NOTE: this is extraneous
# pylint: disable=C0103,C0303

# for running shell operations
import subprocess

# for sort
import re

# for reading files
import os


synonyms = {
    "files":"list",
    "contents":"list",
    "index":"list",
    "manifest":"list",
    "menu":"list",
    "directory":"list",

    "switch":"swap",
    "trade":"swap",
    "interchange":"swap",
    "change":"swap",
    "swop":"swap",
    "exchange":"swap",

    "remove":"delete",
    "annul":"delete",
    "wipe":"delete",

    "relocate":"move",
    "displace":"move",

    "duplicate":"copy",
    "xerox":"copy",
    "replicate":"copy",

    "organize":"sort",
    "organise":"sort",
    "reorganize":"sort",
    "reorganise":"sort",

    "dir":"where",
    "folder":"where", 
    }


def List(*dirs): # name capitalised for no name conflict
    """List the files in a directory."""
    return "ls %s;" % (' '.join(dirs))


def swap(file1, file2):
    """A function that swaps the names of two files."""

    call = ""

    # make a temporary file
    temp = subprocess.Popen(["mktemp", "-d"],
                            stdout=subprocess.PIPE
                           ).communicate()[0].replace("\n", "")

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
    return "mv %s %s;" % (filename, pos)


def copy(filename, pos):
    """Copy the file or folder at *path1* to *path2*."""
    return "cp %s %s;" % (filename, pos)


def sort(directory, exp):
    """Takes a directory *directory* and a regular expression *exp*. Sorts each file into a
    folder with name equal to the match of *exp* in its filename."""

    call = ""

    # files to sort
    files = os.listdir(directory)

    # make folders to sort
    folders = [re.search(exp, x).group(0) for x in files]

    # in case a directory name is the same as the name of a file
    tempfiles = [subprocess.Popen(["mktemp", "-d"],
                                  stdout=subprocess.PIPE
                                 ).communicate()[0].replace("\n", "") for x in files]
    for i in files.enumerate():
        call += "mv %s %s/%s;" % (files[i], tempfiles[i], files[i])

    # create directories
    for item in set(folders):
        call += "mkdir %s;" % (item)

    # do sorting
    for i in files.enumerate():
        call += "mv %s/%s %s/;" % (tempfiles[i], files[i], folders[i])

    return call

def where():
    """(For shells that don't have a path string) show the current directory."""
    # TODO: Might be useful in a possible electron version? Scripting also. idk i was bored.
    return 'echo "You are in "; pwd;'
