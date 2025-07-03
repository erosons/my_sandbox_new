from pathlib import Path
# To do time conversion
from datetime import datetime
from time import ctime

# to copy a file and archiving from a source to a target location
import shutil

path = Path("MainDirectory/tutorial/abc.py")
print(path.stat())     # gives you the statistical details of the file
print(path.stat()[0])
print(path.stat()[1])
print(path.stat()[2])
print(path.stat()[3])
print(path.stat()[4])
print(path.stat()[5])
print("File size:", path.stat()[6])
lastTime_accesed = datetime.fromtimestamp(                # This allows you to know the last time the file was accessed and also covert to proper time.
    path.stat()[7]).strftime("%A, %B %d, %Y %I:%M:%S")
print(f"LastTime_Accesed:{lastTime_accesed}")

# Allows to know the time of creation of the file.
print("File Time of Creation:", ctime(path.stat().st_ctime))

# Allows you to open, read and close the content of the File
print(path.read_text())

# To write to a file to path in text and the second write file in bytes
print(path.write_text("...."))
print(path.write_bytes("....."))

# To perform a copy file and archive from a source to a target location
source = Path("MainDirectory/tutorial/abc.py")

target = Path("MainDirectory2")

shutil.copy(source, target)
