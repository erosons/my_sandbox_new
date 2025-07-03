from office365_helper import SharePoint
import re
import sys, os
from pathlib import PurePath

#1 args=SharePoint folder name . 
Folder_name=sys.argv[1]

#2 args - locate or remote folder_dest
Folder_dest=sys.argv[2]

# 3 args= SharePoint filename. This is used when only on fil is being downloaded
File_name=sys.argv[3]

#4 args= SharePoint file name pattern
file_name_pattern=sys.argv[4]



def save_file(file_n,file_obj):
    file_dir_path=PurePath(Folder_dest,file_n)
    with open(file_dir_path, 'wb') as f:
        f.write(file_obj)

def get_file_(file_n,folder):
    file_obj=SharePoint().download_file(file_n,folder)
    save_file(file_n,file_obj)

def get_files(folder):
    files_list=SharePoint._get_file_list(folder)
    for file in files_list:
        get_file_(file.name,folder)

def get_files_by_pattern(pattern,folder):
    files_list=SharePoint._get_file_list(folder)
    for file in files_list:
        if re.search(pattern,file.name):
            get_file_(file.name,folder)



if __name__ == '__main__':
    if File_name != None:
        get_file_(File_name,Folder_name)

    elif File_name != None:
        get_files_by_pattern(file_name_pattern,Folder_name)
    else:
        get_files(Folder_name)
