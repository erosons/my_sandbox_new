from pathlib import PurePath,Path
import os

from pathlib import PurePath,Path
import os

parent_path=Path('/home/samson/my_sandbox')
subdirectory=['a','b','c']
for folders in subdirectory:
    if parent_path.joinpath(folders).exists():
        pass
    else:
      os.mkdir(parent_path.joinpath(folders))
