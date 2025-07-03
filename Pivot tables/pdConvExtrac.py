
import pandas as pd
import numpy as np
from pathlib import Path


# my Connction to path
class Pathfinder:
    def __init__(self):
        self.CustomersDetails = Path(
            "Monthly reports/06012020_CustomerDetails.xlsx")
        if self.CustomersDetails.exists:
            print("Found in first directory:", self.CustomersDetails.exists())
            # before this can be executed use have to pip install xlrd to read in excel file
            self.data = pd.read_excel(self.CustomersDetails, 0)
        else:
            # To get data Path
            print("File folder not found in that directory:")

    def dateConverion(self, columnField):
        ContdFiteld = pd.to_datetime(
            self.data[columnField], format='%Y/%m/%d')  # Converting to datetime
        return ContdFiteld

    def monthExtraction(self, monthfields):
        # Extracting a Month from date
        ContdvFiteld = self.data[monthfields].apply(lambda x: x.month)
        return ContdvFiteld

    def YearExtraction(self, yearfields):
        ConvtdFiteld = self.data[yearfields].apply(
            lambda x: x.year)  # Extracting Year from date
        return ConvtdFiteld
