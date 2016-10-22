"""
[fTerm] macos.py

This module defines useful commands for MacOS.
"""

# NOTE: this is extraneous
# pylint: disable=C0103,C0303

synonyms = {
    "setvolume":"volume",

    "quit":"quit_application",
    }

def volume(x):
    """Set volume."""
    return 'osascript -e "set Volume %s"' % (x)

def quit_application(x):
    """Quit (nicely) an application."""
    return "osascript -e 'tell app \"%s\" to quit" % (x)
