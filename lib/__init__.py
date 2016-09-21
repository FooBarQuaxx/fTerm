"""
[fTerm] __init__.py

This module aggregates all of the modules in lib/ to be imported by load.py.
"""

import importlib

import sys
import os
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py':
        continue
    globals()[module[:-3]] = __import__(module[:-3], locals(), globals())

sys.path.append(os.path.expanduser("~/.fterm"))
for module in os.listdir(os.path.expanduser("~/.fterm")):
    try:
        if module[-3:] != "pyc":
            globals()[module[:-3]] = importlib.import_module(module[:-3])
    except ImportError:
        pass
