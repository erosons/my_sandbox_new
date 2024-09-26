from pathlib import Path
from zipfile import ZipFile   # This allows you to perform zip operations

# how to create a zipfile
zipfilecreation = ZipFile("file.zip", "w")
for path in Path("MainDirectory").rglob("*.*"):  # To write into the zipfiles
    zipfilecreation.write(path)
 # there is an error the zip close may not be executed, Alternatively we can u try and except
zipfilecreation.close()

# Alternatively
# how to create a zipfile
with ZipFile("file.zip", "w") as zip:
    for path in Path("MainDirectory").rglob("*.*"):  # To write into the zipfiles
        zip.write(path)
 # this is does not zip close as the WITH has taken care of the zipclose()

with ZipFile("file.zip") as zip:
    print(zip.namelist())  # To read the files in the zip
# To get information about a zip fle
    fileinfo = zip.getinfo("MainDirectory/tutorial/Stacks.py")
    print(fileinfo.file_size)  # To get the size of the file
    print(fileinfo.compress_size)
    print(fileinfo.compress_type)
# how to extract a zipfile from an archive into a new directory
    zip.extractall("Extracts")
