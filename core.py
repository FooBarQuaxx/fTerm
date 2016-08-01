#
# fTerm 0.0.1a
# Liam Schumm
#

# for running shell operations
import os, subprocess


def swap(file1,file2):
    """A function that swaps the names of two files."""

    # make a temporary file
    temp = subprocess.Popen(["mktemp"], stdout=subprocess.PIPE).communicate()[0].replace("\n","")

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
    nameToRunCommand = {"py" : "python %s", "rb" : "ruby %s", "sh" : "sh %s", "pl" : "perl %s"}

    # get file extension
    ext = filename.split(".")[1]

    # run the file
    os.system(nameToRunCommand[ext] % (filename))

    return ""

def size(filename):
    """Return the size of a file in human-readable format."""
    os.system('echo File size: $(ls -lah %s | awk -F " " {\'print $5\'})' % (filename))



# translator from string to function
getFunc = {"swap":swap,
           "run":run,
           "size":size,
           }
