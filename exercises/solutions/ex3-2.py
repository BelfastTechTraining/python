#!/usr/bin/env python3
"""
###ex3-2.py
Write a function that rotates the values of 3 variables.  For example:

```
    x = 100
    y = 200
    z = 300
    Rotate( ... )
    # x is now 200
    # y is now 300
    # z is now 100
```
"""


def rotate_vals(val_a, val_b, val_c):
    return val_b, val_c, val_a


if __name__ == '__main__':  # 'main' function
    x = 100
    y = 200
    z = 300
    print("before: x={0}, y={1}, z={2}".format(x, y, z))
    x, y, z = rotate_vals(x, y, z)
    print("after: x={0}, y={1}, z={2}".format(x, y, z))
