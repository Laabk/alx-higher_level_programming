#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import sub, mul, div, add 
    import sys

    argmn = len(sys.argv) - 1
    if argmn != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    oprt = sys.argv[2]
     if oprt != '*' and oprt != '+' and op != '-' and op != '/':
        print("Unknown operator. Available operators: *, +, - and /")
        sys.exit(1)
    from calculator_1 import sub, mul, div, add
    a = int(sys.argv[1])
    b = int(sys.argv[3])
