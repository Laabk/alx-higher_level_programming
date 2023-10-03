#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number >= 0:
    lt_va = number % 10
else:
    lt_va = number % -10

print('the last digit of {} is {}'.format(number, lt_va), end='')

if lt_va > 5:
    print(' is greater than 5')
elif lt_va == 0:
    print(' and is 0')
else:
    print(' and is less than 6 and not 0')
