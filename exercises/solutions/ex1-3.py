#!/usr/bin/env python3
"""
###ex1-3.py
Write a program that prints out the square, cubes and fourth power of the first 20 integers.
"""


def square(number):
    return pow(number, 2)


def cube(number):
    return pow(number, 3)


def forth(number):
    return pow(number, 4)


if __name__ == '__main__':  # 'main' function
    for num in range(1, 21):
        print ("{0}: squared={1} cubed={2} forth={3}".format(num,
                                                             square(num),
                                                             cube(num),
                                                             forth(num)))
