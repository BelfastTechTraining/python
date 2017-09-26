#!/usr/bin/env python3
"""
###ex2-2.py
Use the split() function to split a fullname such as `Julius Caesar` into two strings called firstName and lastName.
"""


def split_full_name(fullname):
    splitname = fullname.split(' ')
    return splitname[0], splitname[-1]  # note that middle names are dropped here, only 1st and last elements returned


if __name__ == '__main__':  # 'main' function
    test_names = ['Julius Caesar', 'Gaius Cassius Longinus', 'Marcus Junius Brutus']
    for name in test_names:
        firstName, LastName = split_full_name(name)
        print ("Full Name: {0}, First Name: {1}, Last Name: {2}".format(name, firstName, LastName))
