#!/usr/bin/env python3
"""
###ex3-6.py
Write a function that takes an integer list as a parameter and doubles the value of each element of the array.
"""


def double_elements(elements):
    newarr = []
    for x in elements:
        newarr.append(x * 2)
    return newarr


if __name__ == '__main__':  # 'main' function
    test_list = [1, 2, 3, 4, 5]
    print("before: {0}".format(test_list))
    print("after:  {0}".format(double_elements(test_list)))
