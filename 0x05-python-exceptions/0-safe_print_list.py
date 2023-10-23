#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numbs = 0
    for d in range(x):
        try:
            print("{}".format(my_list[d]), end='')
            numbs = numbs + 1
        except:
            break
    print()
    return (numbs)
