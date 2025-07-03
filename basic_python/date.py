import pandas as pd
from datetime import date,timedelta,datetime

date=datetime.now()
month=date.month
day= date.day +5
if day <10:
  day=f"0{day}"
else:
   day
year=date.year


#Test DataFrame
df="df"
# converting a datetime to date
df["Pulled At"] = pd.to_datetime(df["Pulled At"]).dt.date
    #print(df)
    # if df["Pulled At"].max()==date.today() :
    #date.today()+timedelta(days=1) :
if df["Pulled At"].max()==date.today() :
        print("Okay")
else:
      raise Exception("Todays file has not been delivered to the bucket")


