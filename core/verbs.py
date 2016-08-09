# NOTE: this is extraneous
# pylint: disable-msg=C0103
# NOTE: this makes code unreadable (for 1 liners)
# pylint: disable-msg=C0303

# for running shell operations
import subprocess


synonyms = {"switch":"swap",
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
            "assistance":"help",
           }

#
# DIRECTORY OPERATIONS
#

def dlist():
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

    return "%s; echo [f] Swapped %s and %s;" % (call, file1, file2)


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

# translator from string to function
verbs = {"swap":swap,
         "run":run,
         "size":size,
         "delete":delete,
         "read":read,
         "edit":edit,
         "list":dlist,
        }

def clist():
    """List all fTerm commands."""

    call = ""

    for verb in verbs:
        call += "echo %s;" % (verb), verbs[verb].__doc__

    return call

verbs["commands"] = clist

# define our help function on current getFunc
def fhelp(command):
    """Print the docstring of a command."""

    command = command.replace("'", "")
    if command == "help":
        return "echo [f] Print the docstring of a command.;"
    else:
        return "echo [f] %s;" % (verbs[command].__doc__)

verbs["help"] = fhelp
