from calendar import day_abbr, month
from datetime import datetime, timedelta, date
import time
import weakref

# to print todays date
todaysdate = datetime.now()
todaysdate1 = date.today()
today_date = datetime.today()
day = today_date.day
_month = today_date.month
_year = today_date.year
print(todaysdate, today_date)

# Creating a custom date or datetime
customtime = datetime(2018, 5, 2, 15, 14)
print(customtime)

# Returns the daysOfweek mon ranging from 0- Monday 6-Sunday
daysOfweek_num = today_date.weekday()
# Use Case
weekDays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
weekDays[daysOfweek_num]


# Extracting time from a datime object
t = datetime.time(datetime.now())
print(t)

# Converting date in string format from either a source file or by user input to Datetime
# - %Y/&y -> Year ,%a/%A -weekday , %b/%B -> Month , %d -> day of the Month
dtConv = datetime.strptime("2020/05/01", "%Y/%m/%d")
print(dtConv)

# Working with Hour, Minute seconds and pm/am
print(today_date.strftime("Current time: %I:%M:%S %p"))  # returns 12hr time
print(today_date.strftime("24hr time: %H:%M"))  # returns 24hr time


# Converting datetime into a string format
dateconversion1 = dtConv.strftime("%Y/%m/%d")
print(dateconversion1)

# Working with Locale's date  and Locale's time
print(today_date.strftime("Locale date and time:%c"))  # print local timestamp
print(today_date.strftime("Locale date:%x"))  # print local date
print(today_date.strftime("Localetime:%X"))  # print local time


# Coverting a TimeStamp into a Datetime object
Atimestamp = time.time()
dt1 = datetime.fromtimestamp(Atimestamp)
print(dt1)

# Creating formatted string with datetime

print(f"{dtConv.year}/{dtConv.month}")

# datetime comparism

print(todaysdate > customtime)


# working with timedelta(days,seconds difference) .This mainly has to do with datetime difference = timedelta

duration = customtime - dtConv
print("days:", duration.days)
print("seconds:", duration.seconds)
print("Total seconds:", duration.total_seconds())

# to increament dateTime with timedelta
mydate = datetime.now() + timedelta(days=1, seconds=1000)
print(mydate)


#
