#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numbs = 0

    for d in range(x):
        try:
            print("{:d}".format(my_list[d]), end='')
            numbs = numbs + 1
        except ValueError:
            pass
        except TypeError:
            pass
    print()
    return (numbs)
