#!/usr/bin/python3

 i = 0
 while i < 10:
     print(i)
     i += 1

for i in range(10):
    if i % 2 != 0:
        continue
    if i == 8:
        break
    print(i)
