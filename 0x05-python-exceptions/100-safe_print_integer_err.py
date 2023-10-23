#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        print('{:d}'.format(value))
        return (True)
    except (TypeError, ValueError) as an errror:
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
