from pathlib import Path
import pandas as pd
import numpy as np


class Data:
    start_year = object
    stop_year = object
    start_month = object
    data = object

    def __init__(self):
        self.data = self.pathfinder()
        self.re_initialized(self.data)
        self.start_year = self.data["Start_Year"]
        self.start_month = self.data["Start_month"]
        self.stop_year = self.data["Stop_Year"]
        self.stop_month = self.data["Stop_month"]
        self.columnField =
        self.monthfields =
        self.yearfields =

    def dateConverion(self):
        ConvtdField = pd.to_datetime(
            self.columnField, format='%Y/%m/%d')  # Converting to datetime
        return ConvtdField

    def monthExtraction(self):
        ContdvFiteld = self.monthfields.apply(
            lambda x: x.month)  # Extracting a Month from date
        return ContdvFiteld

    def YearExtraction(self):
        ConvtdFiteld = self.yearfields.apply(
            lambda x: x.year)  # Extracting Year from date
        return ConvtdFiteld

    def pathfinder(self):
        CustomersDetails = Path(
            "Monthly reports/06012020_CustomerDetails.xlsx")
        if CustomersDetails.exists:
            print("Found in first directory:", CustomersDetails.exists())
         # before this can be executed use have to pip install xlrd to read in excel file
        return pd.read_excel(CustomersDetails, 0)

    def re_initialized(self, data):
        # Converting str to datetime see function above
        self.data["UTIL_ACCT_START_DT"] = Data.dateConverion(
            self.data["UTIL_ACCT_START_DT"])
        self.data["UTIL_ACCT_END_DT"] = Data.dateConverion(
            self.data["UTIL_ACCT_END_DT"])
        # print(data.info())  # This returns the colunms header and their data type

        # Extracting year and month extract from data time see function above
        self.stop_year = Data.YearExtraction(self.data["UTIL_ACCT_END_DT"])
        self.stop_month = Data.monthExtraction(self.data["UTIL_ACCT_END_DT"])

        # Extracting year and month extract from data time
        self.start_month = Data.monthExtraction(
            self.data["UTIL_ACCT_START_DT"])
        self.start_year = Data.YearExtraction(self.data["UTIL_ACCT_START_DT"])

        # Extracting year and month extract from data time
        data["Sales_Month"] = Data.monthExtraction(self.data["SALES_DATE"])
        data["Sales_Year"] = Data.YearExtraction(self.data["SALES_DATE"])

        # performed a ternary operations
        self.data["Syn_GH"] = np.where(
            self.data['SEGMENT'] == "RES", "RES", "COMM")
        # print(data.columns) # To return alL the headers in the table

        # This is modify the channel to a more synthetic Channel
        # perform an index and match like in excel
        conditions = [self.data["CHANNEL"] == "CES DIRECT SALES",
                      self.data["CHANNEL"] == "CES DIRECT SALE",
                      self.data["CHANNEL"] == "COMMERCIAL BROK",
                      self.data["CHANNEL"] == "COMMERCIAL BROKER",
                      self.data["CHANNEL"] == "CSR",
                      self.data["CHANNEL"] == "CUSTOMER SERVICE",
                      self.data["CHANNEL"] == "DOOR TO DOOR",
                      self.data["CHANNEL"] == "INTERNAL",
                      self.data["CHANNEL"] == "INTERNAL SALES",
                      self.data["CHANNEL"] == "ONLINE BROKER",
                      self.data["CHANNEL"] == "DELEGATION",
                      self.data["CHANNEL"] == "OPS",
                      self.data["CHANNEL"] == "SALESOPS",
                      self.data["CHANNEL"] == "SEAMLESS MOVE",
                      self.data["CHANNEL"] == "TELEMARKETING",
                      self.data["CHANNEL"] == "UTILITY",
                      self.data["CHANNEL"] == "Web",
                      self.data["CHANNEL"] == "",
                      self.data["CHANNEL"] == "CALL CENTER INBOUND",
                      self.data["CHANNEL"] == "CALL CENTER OUTBOUND"
                      ]
        choices = ["Direct", "Direct", "Com Broker", "Com Broker", "CSR", "CSR", "D2D", "Direct", "Direct", "Online Broker",
                   "Delegation", "Direct", "Direct", "Other", "OBTS", "Other", "Web", "Other", "CALL CENTER INBOUND", "CALL CENTER OUTBOUND"]
        self.data["GH_channel"] = np.select(conditions, choices, default='')

        # Customer Count by by utility

        # executng pivot table for Added no of Customers
        # Adds_Filter = data["LIFECYCLE_STATUS"].isin(["06 Active On Flow"]) & (
        # data["Start_Year"] == 2020.0) & (data["Start_Month"] == 5.0)
        # Adds_data = data[Adds_Filter]

        # Customer Count by by utility Channel

        """# executng pivot table for no Customers for drops Lost

        # Drops_Filter = data["LIFECYCLE_STATUS"].isin(["08 Inactive Off Flow", "09 Collections", "07 Pending Flow Stop"]) & (
        # data["Stop_Year"] == 2020.0) & (data["Stop_Month"] == 5.0)
        Drop_data = dropFilter(data["LIFECYCLE_STATUS"],
                            "08 Inactive Off Flow", "09 Collections", "07 Pending Flow Stop", 2020.0, 5.0)

        CustomersDrops = pd.pivot_table(Drop_data, values="CES_LDC_ID", index=["UTILITY"], columns=[
                                        "Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(CustomersDrops)

        # executng pivot table for no Customers for Cancel/Rejects
        # cancel_Filter = data["LIFECYCLE_STATUS"].isin(["04 Cancelled", "02 Utility Reject", "03 Ops Reject"]) & (
        #   data["Stop_Year"] == 2020.0) & (data["Stop_Month"] == 5.0)
        cancel_data = dropFilter(data["LIFECYCLE_STATUS"],
                                "04 Cancelled", "02 Utility Reject", "03 Ops Reject", 2020.0, 5.0)
        CustomersCancel = pd.pivot_table(cancel_data, values="CES_LDC_ID", index=["UTILITY"], columns=[
            "Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(CustomersCancel)

        # executng pivot table for Active
        Active_Filter = data["LIFECYCLE_STATUS"].isin(
            ["06 Active On Flow", "07 Pending Flow Stop"])
        active_data = data[Active_Filter]
        CustomersActive = pd.pivot_table(active_data, values="CES_LDC_ID", index=["UTILITY"], columns=[
            "Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(CustomersActive)

        # executng pivot table for sales by Utility
        Sales_Filter = (data["Sales_Year"] == 2020.0) & (
            data["Sales_Month"] == 5.0)
        Sales_data = data[Sales_Filter]
        Sales_by_Utility = pd.pivot_table(Sales_data, values="CES_LDC_ID", index=["UTILITY"], columns=[
            "Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(Sales_by_Utility)"""
