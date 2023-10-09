#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_of_a = len(tuple_a)
    len_of_b = len(tuple_b)

    if len_of_a == 0:
        a_1 = 0
        a_2 = 0
    elif len_of_a == 1:
        a_1 = tuple_a[0]
        a_2 = 0
    else:
        a_1 = tuple_a[0]
        a_2 = tuple_a[1]
    if len_of_b == 0:
        b_1 = 0
        b_2 = 0
    elif len_of_b == 1:
        b_1 = tuple_b[0]
        b_2 = 0
    else:
        b_1 = tuple_b[0]
        b_2 = tuple_b[1]
    the_tuple = (a_1 + b_1, a_2 + b_2)

    return (the_tuple)
