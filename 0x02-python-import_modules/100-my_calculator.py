#!/usr/bin/python3
if __name__ == "__main__":
    "use in carrying some mathematical calculation"
    import sys
    agtn = len(sys.argv) - 1
    if agtn != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    oprt = sys.argv[2]
    if oprt != '+' and oprt != '-' and oprt != '*' and oprt != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
