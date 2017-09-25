#!/usr/bin/env python3
"""
###ex1-5.py
Write a program that calculates the ratio of successive pairs of the first 20 Fibonacci numbers.
Does the ratio appear to converge to a number?
"""


def fib(n):
    """
    Fibonaccii seq. is defined as each number being the sum of the previous 2 in the sequence.
    i.e f(n) = F(n-1) + f(n-2)
    """
    a = 1  # we'll use a for f(n-2) i.e. the smaller of the 2 to be added
    b = 1  # we'll use b for f(n-1) i.e. the larger of the 2 to be added
    for i in range(n-1):
        # a, b = b, a+b
        tmp = b     # keep a temp copy of f(n-1)
        b = a + b   # calculate the ith fibonacci number
        a = tmp     # set f(n-2) to f(n-1) to "step forward" one number
    return a


if __name__ == '__main__':  # 'main' function
    previous_fib = 1  #
    for num in range(2, 20):
        fibnum = fib(num)
        print ("{0} / {1} = {2}".format(fibnum, previous_fib, (fibnum / previous_fib)))
        previous_fib = fibnum
