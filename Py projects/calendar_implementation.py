from calendar import day_abbr, month
from datetime import datetime, timedelta, date
import calendar
import time
import weakref

# Use for date comparism e.g  checking if April fool has passed for the current year

todayy = date.today()
afd = date(todayy.year, 4, 1)

if afd < todayy:
    print("April is passed by:", (todayy - afd).days)
    print(" Next afd", afd.replace(year=todayy.year + 1))
else:
    print(" Outstanding days before April Fool".format(afd - todayy))


# Working with Calendars
import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2022, 1, 0, 0)  # to setup any month in  year

print(str)

# create a HTML formatted calendar
c = calendar.HTMLCalendar(calendar.SUNDAY)
str = c.formatmonth(2022, 1, 0, 0)

print(str)

# Iterating over days of a Month, in case you see trailing zeros those days of the week spills into anothe Month

for i in c.itermonthdays(2022, 8):
    print(i)

# Iterating over months of the year
for month_name in calendar.month_name:
    print(month_name)

# Iterating over days of the Week
for day_name in calendar.day_name:
    print(day_name)

#Locale datetime
print(today_date.strftime("Locale date and time:%c")) # print local time
print(today_date.strftime("Locale date:%x")) # print local time
print(today_date.strftime("Localetime:%X")) # print local time


# A Minor project to calculate First Friday of every Month

print("Teams meeting will be on:")

for m in range(1,13):
    cal=calendar.monthcalendar(2022,m)
    weekone=cal[0]
    weektwo=cal[1]
    if weekone[calendar.FRIDAY] !=0:
        meetday=weekone[calendar.FRIDAY] 
    else:
        meetday=weektwo[calendar.FRIDAY]
    
    print(calendar.month_name[m],meetday)


# A minor project to calculate total dayOfweek in a month and year recursively
list1=[]
for days in calendar.day_name:
    list1.append(days)
list1

from calendar import Calendar

list2=[]
#To set firstday of the week
obj=Calendar(firstweekday=0)
for i in obj.iterweekdays():
    list2.append(i)
list2

# writing a recursive function
def total_WeekDay_month_year():
    combined_list = list(zip(list2,list1))
    for x in combined_list:
        print(x)
    int(input("Pick your year: "))
    int(input("Pick your Month: "))
    int(input("Pick your day in Integer from the list above: "))
    
    return total_WeekDay_month_year()