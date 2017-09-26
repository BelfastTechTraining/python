#!/usr/bin/env python3
"""
###ex2-3.py
Use the range function to generate two separate tuples containing the list of integers from 10 to 19 and from 30 to 39.

Tuples are immutable, so how can you form a tuple that has all the elements of the other two tuples?

HINT: range() returns its own special type in Python 3, can you cast to another type?
"""


def generate_tuple(lowest, highest):
    range_type = range(lowest, (highest + 1))  # in python 3, range() returns it's own iterable type, but...
    tuple_type = tuple(range_type)             # ... you can cast it straight to a tuple!
    return tuple_type


if __name__ == '__main__':  # 'main' function
    tup1 = generate_tuple(10, 19)
    tup2 = generate_tuple(30, 39)
    tup3 = tup1 + tup2  # adding tuples will return a concatenated version
    print ("tuple 1: {0}".format(tup1))
    print ("tuple 2: {0}".format(tup2))
    print ("tuple 1 + tuple 2 = {0}".format(tup3))
