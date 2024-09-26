import os
import shutil
from shutil import make_archive
from pathlib import Path
from os import path

for file in os.listdir():
    print(file)

print(shutil.disk_usage(path))

os.mkdir()
os.stat()
