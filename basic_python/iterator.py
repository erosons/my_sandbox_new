"""
iterate using function  and sentinel
"""

with open('textFile.csv', 'r') as fp:
   #  '' in the iter is checking for  an empty and will end the iter operation
    for line in iter(fp.readline, ''):
        print(line)
