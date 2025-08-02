#! /usr/bin/env python3

import sys

def calculator(num1, num2):
    print(f"num: {num1 + num2}")
    print(f"Difference: {num1 - num2}")
    print(f"Product: {num1 * num2}")
    if (num1 == 0 or num2 == 0):
        print(f"Quotient: ERROR (division by zero)\nRemainder: ERROR (modulo by zero)")
    else:
        print(f"Quotient: {num1 / num2}")
        print(f"Remainder: {num1 % num2}")

def main():
    if (len(sys.argv) < 3):
        sys.exit("Usage: pythone operations.py <num1> <num2>")
    elif (sys.argv[1].isalpha() or sys.argv[2].isalpha()):
        sys.exit("ERROR: Only integers")
    elif (len(sys.argv) > 3):
        sys.exit("ERROR: To many argumets")
    calculator(int(sys.argv[1]), int(sys.argv[2]))
if (__name__ == "__main__"):
    main()