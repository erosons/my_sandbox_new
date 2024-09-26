# Working with directories and making, renaming directories that does not exits
from pathlib import Path

# Making directories that does not exits
path = Path("MainDirectory2")
if path.exists() == False:
    path.mkdir()
    print(path.home())
else:
    pass

print(Path("MainDirectory2"))

# Removing directories that does not exits
path = Path("MainDirectory2")
if path.exists() == True:
    path.rmdir()
else:
    pass

# Renaming directories that does not exits
path = Path("MainDirectory2")
if path.exists() == True:
    path.rename("MainDirectory3")
else:
    pass

# Iterating over file in a directories that does not exits
path = Path("MainDirectory")
for paths in path.iterdir():
    print([paths])

# Instead of using these lines of codes , Use List comprehension to execute the above implementation
path = Path("MainDirectory/tutorial")
list = [paths for paths in path.iterdir() if paths.is_dir()]
# Adding a filter to a  List comprehension---(if paths)
# the iterdir() returns only a generator that can be itereate over
# Limitation of iterdir()  is that doesn't search by pattern(filetype) and recursively(repeatedly)
# solve this issue, we use the glob("*.*"") to return all files in dir or for specific files we use glob(*.py or xlsx or txt etc)
list2 = [paths for paths in path.glob("*.py")]

list3 = [paths for paths in path.rglob("*.*")]
# print the entire directories
print(list)
print(list2)
print(list3)
