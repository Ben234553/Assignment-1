#!/usr/bin/env python3

'''
OPS435 Assignment 1 - Summer 2023
Program: assignment1.py 
Author: bsundedo
The python code in this file (a1_[Student_id].py) is original work written by
"Student Name". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, day: int) -> str:
    """Based on the algorithm by Tomohiko Sakamoto to return the day of the week for a given date."""
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat']
    offset = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year -= 1
    num = (year + year // 4 - year // 100 + year // 400 + offset[month - 1] + day) % 7
    return days[num]

def mon_max(month: int, year: int) -> int:
    """Returns the maximum day for a given month. Includes leap year check."""
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if month in {4, 6, 9, 11}:
        return 30
    if month == 2:
        return 29 if leap_year(year) else 28

def leap_year(year: int) -> bool:
    """Return True if the year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def after(date: str) -> str:
    """Return the date for the next day of the given date in YYYY-MM-DD format."""
    year, month, day = map(int, date.split('-'))
    day += 1
    if day > mon_max(month, year):
        day = 1
        month += 1
    if month > 12:
        month = 1
        year += 1
    return f"{year}-{month:02d}-{day:02d}"

def valid_date(date: str) -> bool:
    """Check validity of date and return True if valid."""
    try:
        year, month, day = map(int, date.split('-'))
        return 1 <= month <= 12 and 1 <= day <= mon_max(month, year)
    except ValueError:
        return False

def day_count(start_date: str, end_date: str) -> int:
    """Loops through range of dates and returns number of weekend days."""
    weekend_days = 0
    while start_date <= end_date:
        weekday = day_of_week(*map(int, start_date.split('-')))
        if weekday in ['sat', 'sun']:
            weekend_days += 1
        start_date = after(start_date)
    return weekend_days

def usage():
    """Print a usage message to the user."""
    print("Usage: python assignment1.py <start_date> <end_date>")
    print("Dates must be in YYYY-MM-DD format.")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3 or not valid_date(sys.argv[1]) or not valid_date(sys.argv[2]):
        usage()

    start_date, end_date = sorted(sys.argv[1:3])
    print(f"The period between {start_date} and {end_date} includes {day_count(start_date, end_date)} weekend days.")
