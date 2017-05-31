#!/usr/bin/python3

import calendar
from datetime import datetime

def dates(startYear, endYear, startMonth, endMonth):
    year = startYear
    month = startMonth

    while(year < endYear or (year == endYear and month < endMonth)):
        days = calendar.monthrange(year, month)[1]
        for day in range(1, days + 1):
            weekDay = datetime(year, month, day).weekday() + 1
            a = str(year)
            b = str(month)
            if len(b) == 1:
                b = '0' + b
            c = str(day)
            if len(c) == 1:
                c = '0' + c
            yield (a, b, c, str(weekDay))

        month += 1
        if month > 12:
            month = 1
            year += 1

def beforeDate(year, month, day):
    year = int(year)
    month = int(month)
    day = int(day)
    if day > 1:
        return (year, month, day - 1)
    if month > 1:
        day = calendar.monthrange(year, month - 1)[1]
        month -= 1
        return (year, month, day)
    return (year - 1, 12, 31)
