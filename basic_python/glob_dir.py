import os
import time
import datetime as d
from datetime import datetime ,date
from glob import iglob
from datetime import datetime,timedelta
import shutil


directory_path='/Users/s.eromonsei/Documents/TestFolder/'

# Define the directory path where you want to remove subdirectories

current_datetime = datetime.now()
twodaysback = current_datetime - d.timedelta(days=2)
twodaysback=twodaysback.date()

# Function to recursively remove subdirectories
def remove_old_subdirectories(directory):
    for root, subdirs, files in os.walk(directory,topdown=True):
        for subdir in subdirs:
            subdir_path = os.path.join(root, subdir)
            try:
                # Get the last modification time of the subdirectory
                modification_time = datetime.datetime.fromtimestamp(os.path.getmtime(subdir_path)).date()
                
                # Compare with today's date
                if modification_time < twodaysback:
                    print("Removing {}".format(subdir_path))
                    shutil.rmtree(subdir_path,ignore_errors=False) # Remove the subdirectory
            except Exception as e:
                print("Error while processing {}:str({})".format(subdir_path,e))

if __name__ == "__main__":
    # Call the function to start removing old subdirectories
     remove_old_subdirectories(directory_path)
