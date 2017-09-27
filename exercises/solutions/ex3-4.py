#!/usr/bin/env python3
"""
###ex3-4.py
Write a function that takes a string and capitalises the first character of the string and ensures the remaining characters are converted to lower case.

Use the following test data:

```
    UpperFirst("test1")
    UpperFirst("mIxEdCaSe")
    UpperFirst("UPPER")
    UpperFirst("lower")
    UpperFirst("oPPOSITE")
```
"""


def proper_case(raw_string):
    first_char = raw_string[0].upper()
    remaining_chars = raw_string[1:].lower()
    return first_char + remaining_chars


if __name__ == '__main__':  # 'main' function
    test_strings = ["test1", "mIxEdCaSe", "UPPER", "lower", "oPPOSITE"]
    for test_string in test_strings:
        print("{0} -> {1}".format(test_string, proper_case(test_string)))
