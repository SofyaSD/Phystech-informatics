#!/usr/bin/python3
import sys
a = []
for line in sys.stdin:
    ... # line
    a.append(line)
a.sort(reverse = True)
for i in range(len(a)):
    print(a[i], end='')

