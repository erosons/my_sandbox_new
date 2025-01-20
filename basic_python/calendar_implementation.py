from datetime import datetime, timedelta, date
import calendar
from calendar import Calendar
import time

obj = Calendar(firstweekday=0)


class CalenderCaller:
    def __init__(self):
        pass

    def week_day_name(self):
        list1 = []
        for days in calendar.day_name:
            list1.append(days)
        return list1

    def index_4_weekday(self):
        list2 = []
        for i in obj.iterweekdays():
            list2.append(i)
        return list2

    def total_dayweek_in_month(self, _year, _month, _day):
        firstList = self.index_4_weekday()
        secondList = self.week_day_name()
        total_day_month = 0
        combined_list = list(zip(firstList, secondList))
        for x in combined_list:
            print(x)
        #     print("Or 'exit' to quit")
        #     print("?")
        #     _year=int(input("Pick your year: "))
        #     _month=int(input("Pick your Month: "))
        #     _day=int(input("Pick your day in Integer from the list above: "))
        # Iterate over days of the month
        for day_of_week in obj.itermonthdays2(_year, _month):
            if day_of_week[1] == _day and day_of_week[0] != 0:
                total_day_month += 1
        #     print(total_day_month)
        return print("Total dayweek in a month {} :".format(total_day_month))

    def day_week_in_yr(self, _year, _day):
        total_day_month_year = 0
        firstList = self.index_4_weekday()
        secondList = self.week_day_name()
        total_day_month = 0
        combined_list = list(zip(firstList, secondList))
        # Iterate over days of the months in a year
        for days_in_yrs in obj.yeardays2calendar(_year, width=3):
            for _days in days_in_yrs:
                for i in _days:
                    for x in i:
                        if x[1] == _day and x[0] != 0:
                            total_day_month_year += 1
        return print("Total week_day in the year {}:".format(total_day_month_year))


run = True
while run:
    try:
        calendarCaller = CalenderCaller()
        _year = input("Input year value : ")
        _month = input("Input month value : ")
        _day = input("Input day value : ")

        if _year.isdigit() and _month.isdigit() and _day.isdigit():
            _year = int(_year)
            _month = int(_month)
            _day = int(_day)

            calendarCaller.total_dayweek_in_month(_year, _month, _day)
            calendarCaller.day_week_in_yr(_year, _day)

        elif _year == "exit" or _month == "exit" or _day == "exit":
            run = False

    except:
        print("Check if invalid Value has been entered")
