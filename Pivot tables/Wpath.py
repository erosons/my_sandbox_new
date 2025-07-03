import os
from pathlib import Path
import pandas as pd
# home = os.path.expanduser('~')      # my home page
# os.path.isfile(r"C:\Users\00936124\Desktop\Book1.xlsx")
# os.path.isfile("C:/Users/00936124/Desktop/Book1.xlsx")
# location = os.path.join(home, 'Downloads') # locate a particular folder on my home page
# folder_check = os.path.isdir(location) # To check if the flde is the home page


def pathwriter(path):
    excell_writer = pd.ExcelWriter(path)
    df.to_excel(excell_writer, sheet_name="data")
    excell_writer.save()
    print(type(excell_writer))
    print("successful")


path = mypath = Path(
    r"C:\Users\00936124\Desktop\07012020_CustomerDetails.xlsx")
if path.exists == True:
    pathwriter(path)
    print("I exist")
else:
    path.mkdir()
    pathwriter(path)
