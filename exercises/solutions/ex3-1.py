#!/usr/bin/env python3
"""
###ex3-1.py
Write a function that calculates the area of a rectangle.
Decide how many input parameters your function needs.

The area should be returned from the function.

Write a test program that calls your function with different sets of test data.
"""


def get_area(width, length):
    return width * length


if __name__ == '__main__':  # 'main' function
    rectangles = [(1, 2), (2, 2), (3, 3), (6, 9)]
    for rectangle in rectangles:
        width = rectangle[0]
        length = rectangle[1]
        area = get_area(width, length)
        print ("A {0}x{1} rectangle has an area of {2}".format(width, length, area))
