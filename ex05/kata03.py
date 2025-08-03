#! /usr/bin/env python3
kata = "The right format"

def main():
    res = "-" * (42 - len(kata)) + kata
    print(res, end="")

if (__name__ == "__main__"):
    main()