#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numbs = 0
    try:
        for d in range(x):
            print("{}".format(my_list[d]), end='')
        except:
            break
        else:
            numbs = numbs + 1
    print()
    return (numbs)
