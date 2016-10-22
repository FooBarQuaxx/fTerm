"""
[fTerm] misc.py

This module defines some miscellaneous commands for fTerm.
"""

# NOTE: this is extraneous
# pylint: disable=C0103,C0303

import subprocess
import re

synonyms = {
    "space":"size",
    
    "exec":"run",
    "execute":"run",
    "evaluate":"run",

    "end":"kill",

    "usage":"processes",
    "top":"processes",
    
    "logins":"users",
    
    "man":"rtfm",
    
    "fterm-edition":"fterm_version",
    "version":"fterm_version",
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

def kill(*procs, **keywords):
    """Kill the process with name *processname*."""
    adj_prefix = ""
    if ["force"] in keywords.values():
        adj_prefix += "-9"
    return "pkill %s %s;" * len(procs) % ((adj_prefix,)* len(procs), tuple(procs))

def processes():
    """Alias for htop."""
    return "htop;"

def users():
    """Alias for w."""
    return "w;"

def rtfm(*manpages):
    """Fun shortcut to man."""
    return "man %s;" % " ".join(manpages)

def free():
    """(MacOS doesn't have a free command) Return memory statics."""

    #
    # ALL CREDIT GOES TO drfrogsplat(http://apple.stackexchange.com/users/1587/drfrogsplat)
    #
    
    # Get process info
    ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0]
    vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0]

    # Iterate processes
    processLines = ps.split('\n')
    sep = re.compile('[\s]+')
    rssTotal = 0 # kB
    for row in range(1,len(processLines)):
        rowText = processLines[row].strip()
        rowElements = sep.split(rowText)
        try:
            rss = float(rowElements[0]) * 1024
        except:
            rss = 0 # ignore...
        rssTotal += rss

        # Process vm_stat
        vmLines = vm.split('\n')
        sep = re.compile(':[\s]+')
        vmStats = {}
        for row in range(1,len(vmLines)-2):
            rowText = vmLines[row].strip()
            rowElements = sep.split(rowText)
            vmStats[(rowElements[0])] = int(rowElements[1].strip('\.')) * 4096

    print "echo 'Wired Memory:\t\t%d MB';" % (vmStats["Pages wired down"]/1024/1024) + \
          "echo 'Active Memory:\t\t%d MB';" % (vmStats["Pages active"]/1024/1024) + \
          "echo 'Inactive Memory:\t%d MB';" % (vmStats["Pages inactive"]/1024/1024) + \
          "echo 'Free Memory:\t\t%d MB';" % (vmStats["Pages free"]/1024/1024) + \
          "echo 'Real Mem Total (ps):\t%.3f MB';" % (rssTotal/1024/1024)

def fterm_version():
    """Return the current version of fTerm."""
    return "echo {VERSION};"
