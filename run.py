"""
Python-Script executing all scripts within ./src
"""
import os
import subprocess

for path, dirs, files in os.walk(os.getcwd()):
    if 'src' in path:
        for file in files:
            subprocess.run(["python", os.path.join(path, file)])