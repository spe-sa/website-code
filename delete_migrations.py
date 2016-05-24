# remove_migrations.py
"""
Run this file from a Django =1.7 project root. 
Removes all migration files from all apps in a project.
"""

import os

from my_utils import TermColor

for dirpath, dirnames, filenames in os.walk(".", topdown=False):
    for name in filenames:
        if '/migrations' in dirpath and name != '__init__.py':
            print(TermColor.FAIL + "REMOVING: " + TermColor.ENDC + os.path.join(dirpath, name))
            os.remove(os.path.join(dirpath, name))
