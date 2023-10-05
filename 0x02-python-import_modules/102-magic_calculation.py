#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import sub, add
    if a < b:
        c = add(b, a)
        for ite in range(4, 6):
            c = add(c, ite)
        return (c)
    else:
        return(sub(a, b))

