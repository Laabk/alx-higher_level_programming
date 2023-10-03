#!/usr/bin/python3
def remove_char_at(str, n):
    t_sr = ""
    for ite in range(len(str)):
        if ite != n:
            t_sr = t_sr + str[ite]
    return (t_sr)
