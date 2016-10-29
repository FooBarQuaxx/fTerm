"""
[fTerm] macos.py

This module defines useful commands for MacOS.
"""

# NOTE: this is extraneous
# pylint: disable=C0103,C0303

synonyms = {
    "setvolume":"volume",

    "quit":"quit_application",

    "relaunch":"relaunch_application",
    }

def volume(x):
    """Set volume (0-10)."""
    return 'osascript -e "set Volume %s"' % (x)

def quit_application(appname):
    """Quit (nicely) an application."""
    return "osascript -e 'quit app \"%s\"" % (appname)

def relaunch_application(appname):
    """Relaunch an application."""
    return quit_application(appname) + "sleep 2; open -a %s" % (appname)
