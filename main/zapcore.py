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

def compress(filename):
    """Compress a file."""
    return "zpaq add %s.zpaq %s -m 5 -summary;" % (filename, filename)

def decompress(filename):
    """Decompress a file."""
    return "zpaq extract %s;" % (filename)

def encrypt(filename):
    """Encrypt a file."""
    return " openssl enc -aes-256-cbc -salt -in %s -out %s.enc;" % (filename, filename)

def decrypt(filename):
    """Decrypt a file."""
    return "openssl aes-256-cbc -d -salt -in %s -out %s;" % (filename, filename[:-5])
