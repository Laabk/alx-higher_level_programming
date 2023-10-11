#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    the_dic = a_dictionary.copy()
    val = list(the_dic.keys())
    for d in val:
        the_dic[d] *= 2
    return (the_dic)
