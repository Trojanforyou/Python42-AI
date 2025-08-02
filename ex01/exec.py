#! /usr/bin/env python3

import sys
if (len(sys.argv) < 2):
    sys.exit(1)
arg = sys.argv[1:]
result = []
for i in arg:
    result.append(i[::-1].swapcase())
print(" ".join(result))