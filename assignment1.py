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

"""
Script Name: assignment1.py
Description: This script calculates the number of weekend days (Saturdays and Sundays) between two given dates.

Author: [Your Name]
License: [Your Preferred License]
Academic Honesty: I declare that this is my own work and I have not copied it from any other source.
"""

import sys

def leap_year(year: int) -> bool:
    """
    Determines whether the specified year is a leap year.

    Parameters:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    # Check if the year is a multiple of 4, not a multiple of 100, unless it's also a multiple of 400
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month: int, year: int) -> int:
    """
    Returns the maximum number of days in a given month considering leap years.

    Parameters:
    month (int): The month (1-12).
    year (int): The year.

    Returns:
    int: The number of days in the month.
    """
    # Return 31 for months with 31 days
    if month in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    # Return 30 for months with 30 days
    if month in {4, 6, 9, 11}:
        return 30
    # Return 29 for February in leap years, 28 otherwise
    return 29 if leap_year(year) else 28

def day_of_week(year: int, month: int, day: int) -> str:
    """
    Determines the day of the week for a given date.
    ...
    """
    date = datetime(year, month, day)
    return date.strftime('%a').lower()

def after(date: str) -> str:
    """
    Calculates the next day's date given a date in 'YYYY-MM-DD' format.

    Parameters:
    date (str): The current date in 'YYYY-MM-DD' format.

    Returns:
    str: The next day's date in 'YYYY-MM-DD' format.
    """
    year, month, day = map(int, date.split('-'))
    day += 1  # Move to the next day
    if day > mon_max(month, year):  # Check if the next day exceeds the month's maximum days
        day = 1
        month += 1
    if month > 12:  # Check if the month exceeds December, reset to January of the next year
        month = 1
        year += 1
    return f"{year}-{month:02d}-{day:02d}"

def valid_date(date: str) -> bool:
    """
    Validates the format and existence of the given date.

    Parameters:
    date (str): The date to validate in 'YYYY-MM-DD' format.

    Returns:
    bool: True if the date is valid, False otherwise.
    """
    parts = date.split('-')
    if len(parts) != 3:
        return False

    try:
        year, month, day = map(int, parts)
        if len(parts[0]) != 4 or not (1 <= month <= 12):  # Ensure year is four digits and month is valid
            return False
        if not (1 <= day <= mon_max(month, year)):  # Validate day based on month and leap year
            return False
        return True
    except ValueError:
        return False

def day_count(start_date: str, end_date: str) -> int:
    """
    Counts the weekend days (Saturday and Sunday) between two dates.

    Parameters:
    start_date (str): The starting date in 'YYYY-MM-DD' format.
    end_date (str): The ending date in 'YYYY-MM-DD' format.

    Returns:
    int: The number of weekend days within the range.
    """
    weekend_days = 0
    current_date = start_date
    while current_date <= end_date:
        weekday = day_of_week(*map(int, current_date.split('-')))
        if weekday in ['sat', 'sun']:
            weekend_days += 1
        current_date = after(current_date)
    return weekend_days

def usage():
    """
    Prints the usage information of the script to the console.
    """
    print("Usage: python assignment1.py <start_date> <end_date>")
    print("Both dates must be in the format YYYY-MM-DD.")
    sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3 or not all(valid_date(date) for date in sys.argv[1:3]):
        usage()

    start_date, end_date = sorted(sys.argv[1:3])
    print(f"The period between {start_date} and {end_date} includes {day_count(start_date, end_date)} weekend days.")
