# NOTE: this is extraneous
# pylint: disable-msg=C0103

# for running shell operations
import subprocess


synonyms = {
            "files":"list",
            "switch":"swap",
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

#
# EDITING FILES
#

def read(filename):
    """Read a file."""
    return 'cat %s;' % (filename)


def edit(filename):
    """Edit a file."""
    return 'nano %s;' % (filename)


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
