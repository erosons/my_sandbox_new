import os
import time
from datetime import datetime ,date
from glob import iglob

today = float(datetime.utcnow().strftime("%d%m%y"))

root_directory = '/Users/s.eromonsei/my_sandbox/Engineering/DataEngineering/airflow-prod/logs/**'

file_list = [f for f in iglob(root_directory, recursive=True) if os.path.isfile(f)]

print(file_list)

#Assuming you want to remove all files that are not today and keep the directories for airflow to continuels  writting

[os.remove(f) for f in file_list if time.ctime(os.path.getctime(f) < today)]