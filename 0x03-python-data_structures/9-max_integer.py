#!/usr/bin/python3
def max_integer(my_list=[]):
    len_of_lst = len(my_list)

    if len_of_lst == 0:
        return (None)

    lags_inte = my_list[0]

    for d in range(1, len_of_lst):
        if my_list[d] > lags_inte:
            lags_inte = my_list[d]
    return (lags_inte)
