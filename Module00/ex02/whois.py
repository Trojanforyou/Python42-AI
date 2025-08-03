#! /usr/bin/env python3

import sys

if (len(sys.argv) < 2):
    sys.exit(1)
elif (len(sys.argv) > 2):
    sys.exit("ERROR: more than 2 args")
elif (sys.argv[1].isalpha()):
    sys.exit("ERROR: args is not an integer")
if (int(sys.argv[1]) == 0):
    print("I'm Zero")
elif (int(sys.argv[1]) % 2 == 0):
    print("I'm Even")
else:
    print("I'm Odd")