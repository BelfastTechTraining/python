#!/usr/bin/env python3
"""
###ex2-1.py
Write a program that prints out the sum, difference, product and dividend of two numbers.
"""


def calc_sum(a, b):
    return a + b


def calc_difference(a, b):
    return a - b


def calc_product(a, b):
    return a * b


def calc_dividend(a, b):
    return a / b


if __name__ == '__main__':  # 'main' function
    for num in range(1, 11):  # generating some number pairings for testing
        a = num + 2
        b = num
        print ("{0} + {1} = {2}, {0} - {1} = {3}, {0} * {1} = {4}, {0} / {1} = {5}".format(a,
                                                                                           b,
                                                                                           calc_sum(a, b),
                                                                                           calc_difference(a, b),
                                                                                           calc_product(a, b),
                                                                                           calc_dividend(a, b)))
