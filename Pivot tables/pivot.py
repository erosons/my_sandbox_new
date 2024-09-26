import pandas as pd
import numpy as np
from pathlib import Path


# my Connction to path
class Pathfinder:
    data=object
    
    def __init__(self):
        CustomersDetails = Path(
        "Monthly reports/06012020_CustomerDetails.xlsx")
         # if self.CustomersDetails.exists:
        #    print("Found in first directory:", self.CustomersDetails.exists())
        # before this can be executed use have to pip install xlrd to read in excel file
        self.data = pd.read_excel(CustomersDetails, 0)
        # else:
        # To get data Path
        # print("File folder not found in that directory:")

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

    def adds_filter(self,columnField1,columnField2,columnField3,yearreq,months,status1,status2):
        Filtered_prams = self.data[columnField1].isin([status1,status2]) & (self.data[columnField2] == yearreq) & (self.data[columnField3] == months)
        return self.data[Filtered_prams]

    def drop_filter(self,columnField1,columnField2,columnField3,yearreq,months,status1,status2,staust3):
        Filtered_prams = self.data[columnField1].isin([status1,status2]) & (self.data[columnField2] == yearreq) & (self.data[columnField3] == months)
        return self.data[Filtered_prams]
    
    def _filter(self,columnField1,columnField2,columnField3,yearreq,months,status1,status2,staust3):
        Filtered_prams = self.data[columnField1].isin([status1,status2]) & (self.data[columnField2] == yearreq) & (self.data[columnField3] == months)
        return self.data[Filtered_prams]

    def Active_filter(self,columnField1,status1,status2):
        Filtered_prams = self.data[columnField1].isin([status1,status2])
        return self.data[Filtered_prams]

    def Sales_filter(self,columnField1,columnField2,yearreq,months):
        Filtered_prams = (self.data[columnField1] == yearreq) & (self.data[columnField2] == months)
        return self.data[Filtered_prams]





"""def pivot_initializer():
    # Converting str to datetime see function above
    dataFrame.data["UTIL_ACCT_START_DT"] = dataFrame.dateConverion("UTIL_ACCT_START_DT")
    dataFrame.data["UTIL_ACCT_END_DT"] = dataFrame.dateConverion("UTIL_ACCT_END_DT")  # This returns the colunms header and their data type
    
    # Extracting year and month extract from data time see function above
    dataFrame.data["Stop_Year"] = dataFrame.YearExtraction("UTIL_ACCT_END_DT")
    dataFrame.data["Stop_Month"] = dataFrame.monthExtraction("UTIL_ACCT_END_DT")

    # Extracting year and month extract from data time
    dataFrame.data["Start_Month"] =dataFrame.monthExtraction("UTIL_ACCT_START_DT")
    dataFrame.data["Start_Year"] = dataFrame.YearExtraction("UTIL_ACCT_START_DT")
    
    # Extracting year and month extract from data time
    dataFrame.data["Sales_Month"] = dataFrame.monthExtraction("SALES_DATE")
    dataFrame.data["Sales_Year"] = dataFrame.YearExtraction("SALES_DATE")

    # performed a ternary operations
    dataFrame.data["Syn_GH"] = np.where(dataFrame.data['SEGMENT'] == "RES", "RES", "COMM")
    # print(data.columns) # To return alL the headers in the table

    # This is modify the channel to a more synthetic Channel
    # perform an index and match like in excel
    conditions = [dataFrame.data["CHANNEL"] == "CES DIRECT SALES",
                  dataFrame.data["CHANNEL"] == "CES DIRECT SALE",
                  dataFrame.data["CHANNEL"] == "COMMERCIAL BROK",
                  dataFrame.data["CHANNEL"] == "COMMERCIAL BROKER",
                  dataFrame.data["CHANNEL"] == "CSR",
                  dataFrame.data["CHANNEL"] == "CUSTOMER SERVICE",
                  dataFrame.data["CHANNEL"] == "DOOR TO DOOR",
                  dataFrame.data["CHANNEL"] == "INTERNAL",
                  dataFrame.data["CHANNEL"] == "INTERNAL SALES",
                  dataFrame.data["CHANNEL"] == "ONLINE BROKER",
                  dataFrame.data["CHANNEL"] == "DELEGATION",
                  dataFrame.data["CHANNEL"] == "OPS",
                  dataFrame.data["CHANNEL"] == "SALESOPS",
                  dataFrame.data["CHANNEL"] == "SEAMLESS MOVE",
                  dataFrame.data["CHANNEL"] == "TELEMARKETING",
                  dataFrame.data["CHANNEL"] == "UTILITY",
                  dataFrame.data["CHANNEL"] == "Web",
                  dataFrame.data["CHANNEL"] == "",
                  dataFrame.data["CHANNEL"] == "CALL CENTER INBOUND",
                  dataFrame.data["CHANNEL"] == "CALL CENTER OUTBOUND"
                  ]
    choices = ["Direct", "Direct", "Com Broker", "Com Broker", "CSR", "CSR", "D2D", "Direct", "Direct", "Online Broker",
               "Delegation", "Direct", "Direct", "Other", "OBTS", "Other", "Web", "Other", "CALL CENTER INBOUND", "CALL CENTER OUTBOUND"]
    dataFrame.data["GH_channel"] = np.select(conditions, choices, default='')
    
    # Customer Count by by utility

    # executng pivot table for Added no of Customers
    # Adds_Filter = data["LIFECYCLE_STATUS"].isin(["06 Active On Flow"]) & (
    # data["Start_Year"] == 2020.0) & (data["Start_Month"] == 5.0)
    # Adds_data = data[Adds_Filter]

    # Customer Adds by Utility
    Adds_data = dataFrame.adds_filter("LIFECYCLE_STATUS","Start_Year","Start_Month",2020.0,5.0,"05 Pending Flow Start", "06 Active On Flow")
    
    CustomersAdd = pd.pivot_table(Adds_data, values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(f'Adds Utility:{CustomersAdd}')

     # Customer Adds by Channel
    
    CustomersAdd_by_Channel = pd.pivot_table(Adds_data, values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(f'Adds Channel:{ CustomersAdd_by_Channel}')

    #  Customers Drops by Utility
    Drop_data = dataFrame.drop_filter("LIFECYCLE_STATUS","Stop_Year","Stop_Month",2020.0,5.0,"08 Inactive Off Flow", "09 Collections", "07 Pending Flow Stop")
    
    CustomersDrop = pd.pivot_table(Drop_data , values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(f'Drops Utility:{CustomersDrop}')

    # Customer drops by Channel
        
    CustomersDrop_by_Channel = pd.pivot_table(Drop_data , values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(f'Drops Utility:{CustomersDrop_by_Channel}')
    
    #  Customers reject
    RejectsData = dataFrame.drop_filter("LIFECYCLE_STATUS","Stop_Year","Stop_Month",2020.0,5.0,"02 Utility Reject", "04 Cancelled","03 Ops Reject")
    
    CustomersReject = pd.pivot_table(RejectsData, values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(f'Adds Utility:{CustomersReject}')

    #  Customers reject by Channel
        
    CustomersReject_by_Channel = pd.pivot_table(RejectsData, values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(f'Adds Utility:{CustomersReject_by_Channel}')


    #Customers Active Counts by Utility
    Active_data = dataFrame.Active_filter("LIFECYCLE_STATUS","06 Active On Flow", "07 Pending Flow Stop")
 
    CustomersActive = pd.pivot_table(Active_data, values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(CustomersActive)
    #  Customers Active Counts by Channnel
    CustomersActive_by_Channel = pd.pivot_table(Active_data, values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(CustomersActive_by_Channel)

    # Sales by Utility
    sales_data= dataFrame.Sales_filter("Sales_Year","Sales_Month",2020.0,5.0)
    Sales_by_Utility = pd.pivot_table(sales_data, values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(Sales_by_Utility)
    
    # sales by Channel
    Sales_by_Channel = pd.pivot_table(sales_data, values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
    print(Sales_by_Channel)

pivot_initializer()"""