#!/bin/bash

echo "Enter your project name"
read projectName
mkdir $projectName
cd $projectName
mkdir source
mkdir test-$projectName
touch README.md
touch requirements.txt
mkdir core
cd core touch main.py
cat ~main.py >> main.py
#/Library/Frameworks/Python.framework/Versions/3.10/bin/python3.10 -m pip install --upgrade pip
cd ..
virtualenv env$projectName
source env$projectName/bin/activate


