#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        last_va = number % 10
    else:
        last_va = number % -10
        last_va *= -1

    print("{:d}".format(last_va), end='')
    return (last_va)
