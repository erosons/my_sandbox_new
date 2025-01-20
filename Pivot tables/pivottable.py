import pandas as pd
import numpy as np
from pathlib import Path
from pivot import Pathfinder

class PivotCreator:
    dataFrame=object
    def __init__(self):
        self.dataFrame = Pathfinder()
        
    def pivot_initializer(self):
        # Converting str to datetime see function above
        self.dataFrame.data["UTIL_ACCT_START_DT"] = self.dataFrame.dateConverion("UTIL_ACCT_START_DT")
        self.dataFrame.data["UTIL_ACCT_END_DT"] = self.dataFrame.dateConverion("UTIL_ACCT_END_DT")  # This returns the colunms header and their data type
        
        # Extracting year and month extract from data time see function above
        self.dataFrame.data["Stop_Year"] = self.dataFrame.YearExtraction("UTIL_ACCT_END_DT")
        self.dataFrame.data["Stop_Month"] = self.dataFrame.monthExtraction("UTIL_ACCT_END_DT")

        # Extracting year and month extract from data time
        self.dataFrame.data["Start_Month"] =self.dataFrame.monthExtraction("UTIL_ACCT_START_DT")
        self.dataFrame.data["Start_Year"] = self.dataFrame.YearExtraction("UTIL_ACCT_START_DT")
        
        # Extracting year and month extract from data time
        self.dataFrame.data["Sales_Month"] = self.dataFrame.monthExtraction("SALES_DATE")
        self.dataFrame.data["Sales_Year"] = self.dataFrame.YearExtraction("SALES_DATE")

        # performed a ternary operations
        self.dataFrame.data["Syn_GH"] = np.where(self.dataFrame.data['SEGMENT'] == "RES", "RES", "COMM")
        # print(data.columns) # To return alL the headers in the table

        # This is modify the channel to a more synthetic Channel
        # perform an index and match like in excel
        conditions =[self.dataFrame.data["CHANNEL"] == "CES DIRECT SALES",
                    self.dataFrame.data["CHANNEL"] == "CES DIRECT SALE",
                    self.dataFrame.data["CHANNEL"] == "COMMERCIAL BROK",
                    self.dataFrame.data["CHANNEL"] == "COMMERCIAL BROKER",
                    self.dataFrame.data["CHANNEL"] == "CSR",
                    self.dataFrame.data["CHANNEL"] == "CUSTOMER SERVICE",
                    self.dataFrame.data["CHANNEL"] == "DOOR TO DOOR",
                    self.dataFrame.data["CHANNEL"] == "INTERNAL",
                    self.dataFrame.data["CHANNEL"] == "INTERNAL SALES",
                    self.dataFrame.data["CHANNEL"] == "ONLINE BROKER",
                    self.dataFrame.data["CHANNEL"] == "DELEGATION",
                    self.dataFrame.data["CHANNEL"] == "OPS",
                    self.dataFrame.data["CHANNEL"] == "SALESOPS",
                    self.dataFrame.data["CHANNEL"] == "SEAMLESS MOVE",
                    self.dataFrame.data["CHANNEL"] == "TELEMARKETING",
                    self.dataFrame.data["CHANNEL"] == "UTILITY",
                    self.dataFrame.data["CHANNEL"] == "Web",
                    self.dataFrame.data["CHANNEL"] == "",
                    self.dataFrame.data["CHANNEL"] == "CALL CENTER INBOUND",
                    self.dataFrame.data["CHANNEL"] == "CALL CENTER OUTBOUND"
                    ]
        choices = ["Direct", "Direct", "Com Broker", "Com Broker", "CSR", "CSR", "D2D", "Direct", "Direct", "Online Broker",
                "Delegation", "Direct", "Direct", "Other", "OBTS", "Other", "Web", "Other", "CALL CENTER INBOUND", "CALL CENTER OUTBOUND"]
        self.dataFrame.data["GH_channel"] = np.select(conditions, choices, default='')
        
        # Customer Count by by utility

        # executng pivot table for Added no of Customers
        # Adds_Filter = data["LIFECYCLE_STATUS"].isin(["06 Active On Flow"]) & (
        # data["Start_Year"] == 2020.0) & (data["Start_Month"] == 5.0)
        # Adds_data = data[Adds_Filter]

        # Customer Adds by Utility
        Adds_data = self.dataFrame.adds_filter("LIFECYCLE_STATUS","Start_Year","Start_Month",2020.0,5.0,"05 Pending Flow Start", "06 Active On Flow")
        
        CustomersAdd = pd.pivot_table(Adds_data, values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(f'Adds Utility:{CustomersAdd}')

        # Customer Adds by Channel
        
        CustomersAdd_by_Channel = pd.pivot_table(Adds_data, values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(f'Adds Channel:{ CustomersAdd_by_Channel}')

        #  Customers Drops by Utility
        Drop_data = self.dataFrame.drop_filter("LIFECYCLE_STATUS","Stop_Year","Stop_Month",2020.0,5.0,"08 Inactive Off Flow", "09 Collections", "07 Pending Flow Stop")
        
        CustomersDrop = pd.pivot_table(Drop_data , values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(f'Drops Utility:{CustomersDrop}')

        # Customer drops by Channel
            
        CustomersDrop_by_Channel = pd.pivot_table(Drop_data , values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(f'Drops Utility:{CustomersDrop_by_Channel}')
        
        #  Customers reject
        RejectsData = self.dataFrame.drop_filter("LIFECYCLE_STATUS","Stop_Year","Stop_Month",2020.0,5.0,"02 Utility Reject", "04 Cancelled","03 Ops Reject")
        
        CustomersReject = pd.pivot_table(RejectsData, values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(f'Adds Utility:{CustomersReject}')

        #  Customers reject by Channel
            
        CustomersReject_by_Channel = pd.pivot_table(RejectsData, values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(f'Adds Utility:{CustomersReject_by_Channel}')


        #Customers Active Counts by Utility
        Active_data = self.dataFrame.Active_filter("LIFECYCLE_STATUS","06 Active On Flow", "07 Pending Flow Stop")
    
        CustomersActive = pd.pivot_table(Active_data, values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(CustomersActive)
        #  Customers Active Counts by Channnel
        CustomersActive_by_Channel = pd.pivot_table(Active_data, values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(CustomersActive_by_Channel)

        # Sales by Utility
        sales_data= self.dataFrame.Sales_filter("Sales_Year","Sales_Month",2020.0,5.0)
        Sales_by_Utility = pd.pivot_table(sales_data, values="CES_LDC_ID", index=["UTILITY"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(Sales_by_Utility)
        
        # sales by Channel
        Sales_by_Channel = pd.pivot_table(sales_data, values="CES_LDC_ID", index=["GH_channel"], columns=["Syn_GH"], aggfunc=np.count_nonzero, margins=True, margins_name="Total")
        print(Sales_by_Channel)

    


PivotCreator().pivot_initializer()