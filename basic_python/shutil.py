from zipfile import ZipFile
from os import path
from shutil import make_archive
import os
import shutil
from pathlib import Path

# for moving file around and archiving files
# vaidate if a path exists
dirPath = Path(
    "/Users/samsoneromonsei/Documents/Playground/myPythonprojects/MainDirectory"
)
fileName = "example_2.json"


def shutil_file_movement():

    filepath = dirPath / fileName
    newfile = "example_2.json.bak"
    if filepath.exists:
        src = filepath
        dest = dirPath / newfile
        #  print(src, dest)
        shutil.copy(src, dest)
        return print("copy was succesful")
    else:
        return print("Destination not available")


"""
Renaming  a file
"""
os.rename("file.rpm", " file.txt")


"""
Creating  and puttings things into a ZIP ARCHIVE
"""


# This split file path into the parent directory and the extension
rootdir, tail_extension = path.split()

# root folder you want to archive
shutil.make_archive("archive", "zip", rootdir)


"""
Creating ZIP ARCHIVE with specific files
"""


with ZipFile("test.zip", "w") as newZipfiles:
    newZipfiles.write("test.txt")
    newZipfiles.write("test2.txt")
