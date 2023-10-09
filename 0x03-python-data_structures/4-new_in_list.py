#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    len_of_lst = len(my_list)
    lst = my_list[:]
    if 0 <= idx < len_of_lst:
        lst[idx] = element
    return (lst)
