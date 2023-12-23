"""This program takes CSV file as an input, parses the content and returns the nested list as output"""

import os
import sys
import csv


def parse_csv_file(file):
    with open(file, 'r', encoding='latin-1') as f:
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            yield row


if __name__ == "__main__":
    result = []

    if len(sys.argv[1]) != 0:
        if os.path.exists(sys.argv[1]):
            for val in parse_csv_file(sys.argv[1]):
                result.append(val)
        else:
            print("The file is not present in the given location")
    else:
        print("Provide provide the file name in the parameter")

