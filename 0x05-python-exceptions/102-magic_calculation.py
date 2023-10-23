#!/usr/bin/python3
def magic_calculation(a, b):
    thr_result = 0
    for d in range(1, 3):
        try:
            if (d > a):
                raise Exception("Too far")
            else:
                the_result = the_rresult + (a ** b) / d
        except:
            the_result = b + a
            break
    return (the_result)
