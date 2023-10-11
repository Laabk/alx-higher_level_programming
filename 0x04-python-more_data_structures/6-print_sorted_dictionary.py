#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_lst = sorted(a_dictionary.keys())

    for d in sort_lst:
        print("{}: {}".format(d, a_dictionary.get(d)))
