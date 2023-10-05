#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguco = len(sys.argv) - 1
    if arguco == 0:
        print('{} arguments'.format(arguco))
    elif arguco == 1:
        print("{} argument:".format(arguco))
