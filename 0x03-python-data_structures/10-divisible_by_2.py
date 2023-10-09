#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisn = []

    for d in range(len(my_list)):
        if my_list[d] % 2 == 0:
            divisn.append(True)
        else:
            divisn.append(False)

    return (divisn)
