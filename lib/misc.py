"""
[fTerm] misc.py

This module defines some miscellaneous commands for fTerm.
"""

# NOTE: this is extraneous
# pylint: disable-msg=C0103

synonyms = {
    "space":"size",
    "exec":"run",
    "execute":"run",
    "evaluate":"run",
    "end":"kill",
    }

def size(*files):
    """Return the size of a file in human-readable format."""
    return "du -sh %s;" * len(files) % files

def run(*files):
    """A universal run function."""

    # filter filename to appropriate command
    command = {"py" : "python %s;", "rb" : "ruby %s;", "sh" : "sh %s;", "pl" : "perl %s;"}

    # run the files
    return ''.join(["echo %s:;" % (x)
                    + command.setdefault(x.split(".")[1]
                                         , "echo '[f-i] Filetype %s not recognized';")
                    % (x) for x in files])

def kill(*processes):
    """Kill the process with name *processname*."""
    return "pkill %s;" * len(processes) % tuple(processes)
