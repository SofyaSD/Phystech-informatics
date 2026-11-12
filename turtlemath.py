#!/usr/bin/python3
from math import cos, pi
import turtle
def rightpoly(r,n):
    l = (2*r*r*(1-cos(2*pi/n)))**0.5

    turtle.left(90 + 180/n)
    for _ in range(n):
        turtle.forward(l)
        turtle.left(360/n)
    turtle.right(90 + 180 / n)

r = 30
for n in range(3,12):
    turtle.penup()
    turtle.goto(r,0)
    turtle.pendown()
    rightpoly(r,n)
    r += 20
