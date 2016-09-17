"""
[fTerm] __init__.py

This module aggregates all of the modules in lib/ to be imported by load.py.
"""

import os
for module in os.listdir(os.path.dirname(__file__)):
    if module == '__init__.py' or module[-3:] != '.py' or not os.path.exists(module):
        continue
    __import__(module[:-3], locals(), globals())
