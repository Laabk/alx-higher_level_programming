#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numb = 0
    for d in range(x):
        try:
            print("{}".format(my_list[d]), end='')
            numbs = numb + 1
        except:
            break
    print()
    return (numb)
