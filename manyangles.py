#!/usr/bin/python3
import turtle

turtle.shape('turtle')
for i in range (3,12,1):
     for _ in range(i):
        turtle.forward(5*i)
        turtle.left(360/i)
