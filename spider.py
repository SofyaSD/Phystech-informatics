#!/usr/bin/python3

import turtle

turtle.shape('turtle')
N = 12
for i in range (12):
    turtle.forward(50)
    turtle.stamp()
    turtle.left(180)
    turtle.forward(50)
    turtle.left(180 + 360 / N)
