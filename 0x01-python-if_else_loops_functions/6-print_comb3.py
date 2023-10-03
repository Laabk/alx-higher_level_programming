#!/usr/bin/python3
for digts in range(0, 90):
    if digts % 10 > digts / 10:
        if digts != 89:
            print("{:02d}, ".format(digts), end='')
        else:
            print("{:02d}".format(digts))
