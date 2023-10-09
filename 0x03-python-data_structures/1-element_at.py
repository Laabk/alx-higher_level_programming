#!/usr/bin/python3
def element_at(my_list, idx):
    if idx < 0:
        return (None)
    len_of_lst = len(my_list)
    if idx > len_of_lst - 1:
        return (None)
    return(my_list[idx])
