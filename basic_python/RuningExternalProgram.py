import os
from pathlib import PurePath,Path
import subprocess

# suppose we want to run external program and captures is output to execute another program which is ususally stored 
# in stdout
# all out of dir will now be available in (stdout)
try:
    filepath=Path('/home/samson/my_sandbox/myPythonprojects/MainDirectory/tutorial/data.csv')
    completed = subprocess.run(filepath, shell=True,
                               capture_output=True,
                               text=True,  # This eliminate the binary output returned and convert it to text
                               check=True)  # This check for possible error
    print("args:", completed.args)
    print("returncode:", completed.returncode)
    print("stderr:", completed.stderr)
    print("stdout:", completed.stdout)
# This catches any possible error that when returncode=1
except subprocess.CalledProcessError as checkError:
    print(checkError)
