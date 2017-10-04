#!/usr/bin/env python3
"""
###ex5-6.py
Write a program that reads a file, reverses the order of lines in the file and then saves the changes in a new file.
"""


def write_reversed_file(input_filename, output_filename):
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        # full slicing notation is [<first element to include> : <first element to exclude> : <step>]
        for line in infile.readlines()[::-1]:
            outfile.write(line)


if __name__ == '__main__':  # 'main' function
    test_input_filename = "./ex5-6.test_data.txt"
    test_output_filename = "./ex5-6.test_output.txt"
    write_reversed_file(test_input_filename, test_output_filename)
    print("Check the contents of {0}".format(test_output_filename))
