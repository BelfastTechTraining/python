#!/usr/bin/env python3
"""
###ex1-1.py
Write a program that inputs a 4 digit year and then calculates whether or not it is a leap year.

###ex1-2.py
Using a variation of the above program, calculate the number of days in the inclusive date range '1st January 2000' to '31st December 2999'.
"""


def is_leap_year(year):
    """
    A year is a leap year if it is divisible by 4.
    However there is an exception to this.
    If the year is divisible by 100 it must also be divisible by 400 to be a leap year.
    """
    is_leap_year = False

    if (year % 100 != 0) and (year % 4 == 0):  # if divisible by 4 and NOT 100
        is_leap_year = True
    elif (year % 100 == 0) and (year % 400 == 0):  # if divisible by 100 AND 400
        is_leap_year = True
    else:  # anything else
        is_leap_year = False

    if (year % 4 == 0):
        if (year % 100 == 0):
            if (year % 400 == 0):
                is_leap_year = True
            else:
                is_leap_year = False

    return is_leap_year


if __name__ == '__main__':  # 'main' function
    year_min = 2000
    year_max = 3000  # note that the upper bound in range() is NOT included here!

    total_day_count = 0
    leap_year_count = 0
    for year in range(year_min, year_max):
        if (is_leap_year(year)):
            total_day_count += 366
            leap_year_count += 1
        else:
            total_day_count += 365
    print("There are {0} leap years and a total of {0} days".format(total_day_count, leap_year_count))
