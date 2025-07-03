import os
import time
from datetime import datetime ,date
from glob import iglob
import re

today = float(datetime.utcnow().strftime("%d%m%y"))

root_directory = '/Users/s.eromonsei/my_sandbox/**'

file_list = [f for f in iglob(root_directory, recursive=True) if os.path.isfile(f)]

#print(file_list)

#Assuming you want to remove all files that are not today and keep the directories for airflow to continuels  writting
# searching for a particular file pattern
searchpattern="checkpoint"
test=[os.remove(f) for f in file_list if re.search(searchpattern,f)]
print(test)