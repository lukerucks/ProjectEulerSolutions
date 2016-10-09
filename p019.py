"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

def isLeapYear(year):
    if year%4==0 and (year%100 !=0 or year%400==0):
        return True
    return False


def daysInMonth(year, month) :
    if month==1 or month==3 or month==5 or month ==7 or month ==8 or month ==10 or month ==12:
        return 31
    elif month ==2:
        if isLeapYear(year):
            return 29
        else:
            return 28
    else:
            return 30

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < daysInMonth(year,month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1


def nextDayofWeek(previous_day):
    week_day_list = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if previous_day not in week_day_list:
        print "Day not in week"
        return None
    else:
        len_days_in_week = len(week_day_list)
        for day in range(len_days_in_week):
            if previous_day == week_day_list[day]:
                return week_day_list[(day+1)%len_days_in_week]


def is_Sunday_on_first_of_month(day, weekday):
    if day == 1 and weekday == "Sunday":
        return True
    else:
        return False

def dateIsAfter(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is after year2-month2-day2.  Otherwise, returns False."""
    if year1 > year2:
        return True
    if year1 == year2:
        if month1 > month2:
            return True
        if month1 == month2:
            return day1 > day2
    return False

def Sundays_on_first_of_month(year1, month1, day1, year2, month2, day2, start_week_day):
    week_day = start_week_day
    days = 0
    while dateIsAfter(year2, month2, day2, year1, month1, day1):
        if day1 == 1:
            print week_day, day1, month1, year1
        if is_Sunday_on_first_of_month(day1, week_day):
            days += 1
            print "HERE #############################"
        (year1, month1, day1) = nextDay(year1, month1, day1)
        week_day = nextDayofWeek(week_day)

    return days

print Sundays_on_first_of_month(1900,12,31,2000,12,31, 'Monday')
