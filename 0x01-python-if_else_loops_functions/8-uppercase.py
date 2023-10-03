#!/usr/bin/python3
def uppercase(str):
    for items in range(len(str)):
        if ord(str[items]) >= 97 and ord(str[items]) <= 122:
            digts = 32
        else:
            digts = 0
            print("{:c}".format(ord(str[items]) - digts), end='')
        print()
