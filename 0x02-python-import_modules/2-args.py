#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    agu = len(sys.argv) - 1
    if agu == 0:
        print("{} arguments:".format(agu))
    elif agu == 1:
        print("{} argument:".format(agu))
