#!/usr/bin/env python3
"""
###ex4-1.py
Write a program that calculates the factorial of an integer in the range 2 to 10.

Add exception handling code to prevent calculating a result where the input number is larger than 10, or any negative integer.

Make sure you can handle the case where the input is not an integer.
"""


# Addig our own custom exception
class FactorialException(Exception):
    def __init__(self, message):
        self.message = message


def factorial(num):
    if num not in range(2, 11):  # throw exception if not between 2 and 10, function will stop here
        raise FactorialException("{0} is not between 2 and 10".format(num))

    sum = 1
    for x in range(1, (num + 1)):
        sum *= x
    return sum


if __name__ == '__main__':  # 'main' function
    for x in [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 11]:  # test values
        try:
            print("{0} factorial is {1}".format(x, factorial(x)))  # try to call factorial(x)
        except FactorialException as e:  # if an exception is thrown in the try: block
            print(e.message)
