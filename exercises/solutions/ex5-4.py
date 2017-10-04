#!/usr/bin/env python3
"""
###ex5-4.py
Try the previous example with other test files that may contain non integral data.
Use exception handling to filter out lines that don't contain integers.

For this example im expecting that a file exists in the same folder as this example named 'ex5-4.test_data.txt':
```
    > cat ex5-4.test_data.txt
     1
     2
     three
     4
     5

```
"""


def add_numbers_in_file(filename):
    total = 0
    with open(filename, 'r') as infile:
        for line in infile.readlines():
            try:
                new_total = (total + int(line))  # casting string to int to add it to the total
            except ValueError:  # A ValueError is thrown if int() fails
                print("{0} is not an integral value, skipping...".format(line.strip()))
                continue  # carry on with the rest of the for loop


            # show my working :)  (stripping any whitespace in the line too)
            print("{0} + {1} = {2}".format(total, line.strip(), new_total))

            total = new_total

    return total


if __name__ == '__main__':  # 'main' function
    test_filename = 'ex5-4.test_data.txt'
    print("TOTAL: {0}".format(add_numbers_in_file(test_filename)))
