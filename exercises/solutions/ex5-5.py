#!/usr/bin/env python3
"""
###ex5-5.py
Write a program that concatenates three files into a new file.
"""


def concatenate_files(filenames, output_filename):
    with open(output_filename, 'w') as outfile:
        for infile in filenames:
            try:
                with open(infile, 'r') as source:
                    for line in source.readlines():
                        outfile.write(line)
            except FileNotFoundError:
                print("{0} could not be found, skipping...".format(infile))
                continue


if __name__ == '__main__':  # 'main' function
    test_output_filename = "./ex5-5.test_data_concatenated.txt"
    test_filenames = ["ex5-5.test_data_1.txt",
                      "ex5-5.test_data_2.txt",
                      "not.really.a.file.txt",
                      "ex5-5.test_data_3.txt"]
    concatenate_files(test_filenames, test_output_filename)
    print ("check the contents of {0}".format(test_output_filename))
