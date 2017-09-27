#!/usr/bin/env python3
"""
###ex3-3.py
Write a function to calculate Factorials.

A Factorial number is the product of all positive integers less than n, e.g.

factorial(5) = 1 x 2 x 3 x 4 x 5

Try out:

```
    factorial(1)
    factorial(10)
    factorial(40)
    factorial(100)
```
"""


def factorial(num):
    sum = 1
    for x in range(1, (num + 1)):
        sum *= x
    return sum


if __name__ == '__main__':  # 'main' function
    test_nums = [1, 10, 40, 100]
    for test_num in test_nums:
        print ("{0} factorial is {1}".format(test_num, factorial(test_num)))
