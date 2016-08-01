#
# fTerm 0.0.1a
# Liam Schumm
#

# for running shell operations
import os, subprocess

def swap(file1,file2):
    """A function that swaps the names of two files."""
    temp = subprocess.Popen(["mktemp"], stdout=subprocess.PIPE).communicate()[0].replace("\n","")
    os.system("mv %s %s" % (file1, temp))
    os.system("mv %s %s" % (file2, file1))
    os.system("mv %s %s" % (temp, file2))
    return ""


# translator from string to function
funcs = {"swap":swap,
         }
