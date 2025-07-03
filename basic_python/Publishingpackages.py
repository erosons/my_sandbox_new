#  Make a new directory mkdir <dir name>
#  type--- cd <dir name>
#  to lanuch a  new vscode on the terminal type ---code  .
# This will lancuh a new vscode with your new <dirname>

# , select your interpreter, create all folder as required
#  Create your project package and dont forget to add __init__.py
#  Create a test folder
#    -In the test folder  create a read me filename(READme.md)
#    -  ""                create a LICENSE filename(LICENSE)  go to https://choosealicense.com/ for appropriate license
#  Create a data folder
# Create your python script project into the package created above

# To publish the project into pypi.org, you need to create a user and password on that site wwww. ppypi.org
# back to you project
# Run------pip install setuptools wheel twine
# Create setupfile in the directory
# this setup below helps you to setup your own package in pipy.com for  other member of the community to use
import setuptools
from pathlib import Path

setuptools.setup(

    name="sams",
    version=1.0,
    long_description=Path("test/README.md").read_text(),
    #     if you have other directiory, then you have to exclude thenin find_packages as shown below
    packages=setuptools.find_packages(exclude=["data", "test"]))

# Run this from the terminal---- python setup.py sdist bdist_wheel
#    -----The code above help create dist files and build files
# Run this from the terminal-----twwine upload dis/*
#    --------This request for user name and password to publish your package
#
