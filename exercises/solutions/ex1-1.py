#!/usr/bin/env python3
"""
###ex1-1.py
Write a program that inputs a 4 digit year and then calculates whether or not it is a leap year.
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
    test_leap_years = [1904, 1908, 1912, 1916, 1920, 1924, 1928]  # some leap years for testing
    test_regular_years = [1956, 1963, 1583, 3861, 1855, 1926]  # some other years for testing
    test_years = test_leap_years + test_regular_years

    for year in test_years:
        if (is_leap_year(year)):
            print("{0} is a leap year".format(year))
        else:
            print("{0} is NOT a leap year".format(year))
