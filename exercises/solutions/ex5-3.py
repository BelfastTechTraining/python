#!/usr/bin/env python3
"""
###ex5-3.py
Create a file call TestData.txt with test data consisting of one number per line using your favourite editor.
Your job is to read the entire file into memory so that you can compute the sum of all the numbers.

For this example im expecting that a file exists in the same folder as this example named 'ex5-3.test_data.txt':
```
    > cat ex5-3.test_data.txt
     1
     2
     3
     4
     5

```
"""


def add_numbers_in_file(filename):
    total = 0
    with open(filename, 'r') as infile:
        for line in infile.readlines():

            # casting string to int to add it to the total
            new_total = (total + int(line))

            # show my working :)  (stripping any whitespace in the line too)
            print("{0} + {1} = {2}".format(total, line.strip(), new_total))

            total = new_total

    return total


if __name__ == '__main__':  # 'main' function
    test_filename = 'ex5-3.test_data.txt'
    print("TOTAL: {0}".format(add_numbers_in_file(test_filename)))
