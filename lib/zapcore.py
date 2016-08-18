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
            "pack":"pack",
            "unpack":"unpack",
           }

#
# ZAPCORE (github.com/lschumm/zapcore)
#

def compress(*files):
    """Compress a file."""
    return "pxz -v -5 %s;" % (' '.join(files))

def decompress(*files):
    """Decompress a file."""
    return "unxz %s;" % (' '.join(files))

def encrypt(*files):
    """Encrypt a file."""
    call = ""
    for f in files:
        call += "echo %s:; openssl enc -aes-256-cbc -salt -in %s -out %s.enc; rm %s;" % (f, f, f, f)
    return call

def decrypt(*files):
    """Decrypt a file."""
    call = ""
    for f in files:
        call += "echo %s:; openssl aes-256-cbc -d -salt -in %s -out %s; rm %s;" % (f, f, f[:-4], f)
    return call

def pack(*files):
    """Pack a file/folder into a tar archive (no compression)."""
    call = ""
    for f in files:
        return "tar cf %s.tar %s; rm -rf %s;" % (f, f, f)
    return call

def unpack(*files):
    """Unpack a tar archive into a file/folder."""
    call = ""
    for f in files:
        return "tar xf %s %s; rm %s;" % (f, f[:-4], f)
    return call
