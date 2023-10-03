#!/usr/bin/python3
for lettres in range(97, 123):
    if lettres != 101 and lettres != 113:
        print("{:c}".format(lettres), end='')
