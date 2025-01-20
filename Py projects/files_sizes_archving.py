import os
from os import path
from pathlib import Path
from shutil import make_archive
import shutil


""""
get to file size
"""


def getFilesize():
    totalFile_size = 0
    for files in os.listdir(os.getcwd()):
        if os.path.isfile(files):
            filesize = os.stat(files)
            totalFile_size += filesize.st_size
    return print("total file size {}MB".format(totalFile_size / 1000))


"""
get write out file and archive the files
"""


def file_list_archving():
    root_dir = path.realpath(os.getcwd())
    print(root_dir)
    newfile = open("list_file_path.txt", "w")
    print("-----------------------------")
    print("File List:")
    for files in os.listdir(os.getcwd()):
        if os.path.isfile(files):
            # print(f"{files}")
            print("{}\n".format(files))
            newfile.write(files)
    # root folder you want to archive
    return print("=>writing complete")


if __name__ == "__main__":
    getFilesize()
    file_list_archving()
