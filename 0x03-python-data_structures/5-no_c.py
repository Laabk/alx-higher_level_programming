#!/usr/bin/python3
def no_c(my_string):
    len_of_str = len(my_string)
    a = 0

    nw_str = my_string[:]
    for d in range(len_of_str):
        if (my_string[d] == 'C' or my_string[d] == 'c'):
            nw_str = nw_str[:(d - a)] + my_string[(d + 1):]
            a = a + 1
    return (nw_str)
