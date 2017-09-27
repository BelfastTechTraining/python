#!/usr/bin/env python3
"""
###ex3-8.py
Modify the previous example to return the sum of the two input arrays instead of printing the result.
"""


def sum_arr_elements(arr_a, arr_b):
    if len(arr_a) != len(arr_b):  # check for equal length
        print("Arrays are of differnet length!")
        return
    new_arr = []
    # enumerate() will returns a tuple of (list_position, value_at_that_position)
    for index, arr_a_val in enumerate(arr_a):
        new_arr.append(arr_a_val + arr_b[index])  # 'index' used to grab value in same posiiton in arr_b
    return new_arr


if __name__ == '__main__':  # 'main' function
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [5, 4, 3, 2, 1]
    print("arr1:  {0}".format(arr1))
    print("arr2:  {0}".format(arr2))
    print("total: {0}".format(sum_arr_elements(arr1, arr2)))
