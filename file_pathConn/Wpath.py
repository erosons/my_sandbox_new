# from pathlib import Path

# # Ways to access a file path in raw form(r)
# path = Path(r"C:\Users\gw\Documents\Python Scripts\tutorial\abc.py")
# print(path.name)
# print(path.is_file)
# print(path.exists)


# # Accessing path with Class Path
# path1 = Path("tutorial/abc.py")
# print(path1.name)
# print(path1.is_file)
# print(path1.stem)
# print(path1.suffix)

# # Another way of Accessing path with Class Path
# path2 = Path() / "tutorial" / "abc.py"
# print(path2.name)
# print(path2.is_file)
# print(path2.stem)
# print(path2.suffix)
# print(path2.parent)
# print(path2.absolute())  # This file does not exist in the path is
# print(path2.home())
# print(Path())

# # Creating an arbitrary file path
# path3 = path2.with_name("file.txt")
# print(path3)
# print(path3.absolute())  # This file does not exist in the path is
# print(path3.home())  # Print the main path.exit


"""
Working with os module
"""
import os
from os import path
import time
from datetime import datetime


print(os.name)
print(
    str(
        path.exists(
            "/Users/samsoneromonsei/Documents/Playground/myPythonprojects/MainDirectory/tutorial/abc.py"
        )
    )
)

# check if its a file
print(
    str(
        path.isfile(
            "/Users/samsoneromonsei/Documents/Playground/myPythonprojects/MainDirectory/tutorial/abc.py"
        )
    )
)
# check if it is directory
print(
    str(
        path.isdir(
            "/Users/samsoneromonsei/Documents/Playground/myPythonprojects/MainDirectory/tutorial/abc.py"
        )
    )
)

# Returns the real path
print(
    str(
        path.realpath(
            "/Users/samsoneromonsei/Documents/Playground/myPythonprojects/MainDirectory/tutorial/abc.py"
        )
    )
)

# This returns a tuple of the path name and the file it self
print(
    str(
        path.split(
            path.realpath(
                "/Users/samsoneromonsei/Documents/Playground/myPythonprojects/MainDirectory/tutorial/abc.py"
            )
        )
    )
)

# get The modification time of a file

t = time.ctime(
    # we have getmtime,getctime,getsize
    path.getmtime(
        "/Users/samsoneromonsei/Documents/Playground/myPythonprojects/MainDirectory/tutorial/abc.py"
    )
)
print(t)

# Make the time more readable
print(
    datetime.fromtimestamp(
        path.getmtime(
            "/Users/samsoneromonsei/Documents/Playground/myPythonprojects/MainDirectory/tutorial/abc.py"
        )
    )
)
