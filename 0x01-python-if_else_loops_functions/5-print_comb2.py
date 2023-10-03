#!/usr/bin/python3
for digts in range(0, 100):
    if digts != 99:
        print("{:02d}, ".format(digts), end='')
    else:
        print("{:02d}".format(digts))
