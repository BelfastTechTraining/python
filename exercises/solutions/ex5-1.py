#!/usr/bin/env python3
"""
###ex5-1.py
Write a program that counts the number of lines in a file.
"""


def count_lines(filepath):
    line_count = 0
    try:
        fp = open(filepath, 'r')
        for line in fp.readlines():
            line_count += 1
    except FileNotFoundError:
        print("Could not open {0}".format(filepath))
        return
    return line_count


if __name__ == '__main__':  # 'main' function
    testfile = "./ex5-1.py"
    num_lines = count_lines(testfile)
    print("There are {0} lines in {1}".format(num_lines, testfile))
