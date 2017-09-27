#!/usr/bin/env python3
"""
###ex2-4.py
Create a dictionary consisting of people's names and salaries.

Initialise the dictionary with at least 5 pairs of names and salaries. Now print the dictionary.

"""

if __name__ == '__main__':  # 'main' function
    mydict = { 'tom': 20000, 'dick': 21000, 'harry': 22000, 'foo': 23000, 'bar': 24000 }

    for i in range(1,6):
        print ("printing dict for {0}th time:".format(i))
        for item in mydict.values():
            print(item)
