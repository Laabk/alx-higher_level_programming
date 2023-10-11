#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list and len(my_list):
        digt = 0
        divd = 0
        for tupl in my_list:
            digt += (tupl[0] * tupl[1])
            divd += (tupl[1])
            w = digt/divd
        return w
    return 0
