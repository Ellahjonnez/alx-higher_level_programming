#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            number = 32
        else:
            number = 0
        print("{:c}".format(ord(str[i]) - number), end='')
    print()
