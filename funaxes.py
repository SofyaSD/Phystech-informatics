#!/usr/bin/python3

def part(x,y):
    if x*y == 0:
        res = 'AXES'

    elif x > 0 and y > 0:
        res = 'I'
    elif x > 0 and y < 0:
        res = 'IV'
    elif x < 0 and y > 0:
        res = 'II'
    else:
        res = 'III'

