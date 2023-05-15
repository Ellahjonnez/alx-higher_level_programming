#!/usr/bin/python3
import sys

def number_of_arguments(args):
    result = 0
    for arg in args:
        result += int(arg)
    return result

if __name__ == "__main__":
    counts = sys.argv[1:]
    total = number_of_arguments(counts)
    print("{}".format(total))
