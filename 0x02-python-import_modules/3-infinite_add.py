#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    # To prints the result of the addition of all arguments

    result = 0
    for i in range(len(sys.argv) - 1):
        result += int(sys.argv[i + 1])
    print("{}".format(result), end="\n")
