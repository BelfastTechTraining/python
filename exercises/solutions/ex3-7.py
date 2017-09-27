#!/usr/bin/env python3
"""
###ex3-7.py
Write a function that takes two int arrays (same size) as parameters and adds the arrays together, element by element.

Print out the array as part of the function.
"""


def sum_arr_elements(arr_a, arr_b):
    if len(arr_a) != len(arr_b):  # check for equal length
        print("Arrays are of differnet length!")
        return

    for index in range(0, len(arr_a)):
        total = arr_a[index] + arr_b[index]
        print("{0} + {1} = {2}".format(arr_a[index], arr_b[index], total))


if __name__ == '__main__':  # 'main' function
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 4, 3, 2, 1]
    print("arr1:  {0}".format(arr1))
    print("arr2:  {0}".format(arr2))
    sum_arr_elements(arr1, arr2)
