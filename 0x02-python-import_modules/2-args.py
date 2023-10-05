#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    agu = len(sys.argv) - 1
    if agu == 0:
        print('0 arguments.')
    elif agu == 1:
        print('1 arguments.')
    else:
        print("{} arguments:".format(agu))
    for ite in range(agu):
        print("{}: {}".format(ite + 1, sys.argv[ite + 1]))

