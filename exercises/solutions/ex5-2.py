#!/usr/bin/env python3
"""
###ex5-2.py
Write a file copy program
"""


def copy_file(source, destination):
    # using a context manager here as it will handle opening/closing the file gracefully
    with open(source, 'r') as infile, open(destination, 'w') as outfile:
        for line in infile.readlines():
            outfile.write(line)

    print("{0} has been copied to {1}".format(source, destination))


if __name__ == '__main__':  # 'main' function
    test_source = "./ex5-2.py"
    test_destination = "./ex5-2.copy.py"
    copy_file(test_source, test_destination)
