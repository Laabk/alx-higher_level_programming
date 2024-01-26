#!/usr/bin/python3
"""getting the peak in an unsorted data list"""

def find_peak(list_of_integers):

    inte = list_of_integers
    if inte == []:
        return None
    total = len(inte)
    if total == 1:
        return inte[0]
    elif total == 2:
        return max(inte)
    middle = int(total / 2)
    peak = inte[middle]
    if peak > inte[middle - 1] and peak > inte[middle + 1]:
        return peak
    elif peak < inte[middle - 1]:
        return find_peak(inte[:middle])
    else:
        return find_peak(inte[middle + 1:])
