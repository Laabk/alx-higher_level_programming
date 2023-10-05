#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    thesum = 0
    for argu in sys.argv:
        if argu != sys.argv[0]:
            thesum = thesum + int(argu)
    print(thesum)
