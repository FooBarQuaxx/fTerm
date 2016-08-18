"""
[zapcore] zapcore.py

This module contains all Zapcore commands for fTerm.
"""

# NOTE: this is extraneous
# pylint: disable-msg=C0103

synonyms = {
            "crush":"compress",
            "expand":"decompress",
            "secure":"encrypt",
            "lock":"encrypt",
            "unlock":"decrypt",
            "decode":"decrypt",
           }

#
# ZAPCORE (github.com/lschumm/zapcore)
#

def compress(*files):
    """Compress a file."""
    return "zpaq add %s.zpaq %s -m 5 -summary;" * len(files)  % (filename, filename) * len(files)

def decompress(*files):
    """Decompress a file."""
    return "zpaq extract %s;" * len(files) % (filename) * len(files)

def encrypt(*files):
    """Encrypt a file."""
    return " openssl enc -aes-256-cbc -salt -in %s -out %s.enc;" * len(files) % (filename, filename) * len(files)

def decrypt(*files):
    """Decrypt a file."""
    return "openssl aes-256-cbc -d -salt -in %s -out %s;" * len(files) % (filename, filename[:-5]) * len(files)
