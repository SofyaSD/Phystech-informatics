#!usr/bin/python3
import turtle
turtle.shape('turtle')

def draw(n):
    F = 50
    if n==1:
        turtle.penup()
        turtle.left(90)
        turtle.forward(F)
        turtle.pendown()
        turtle.right(45)
        turtle.forward(F*2**0.5)
        turtle.right(135)
        turtle.forward(2*F)
        turtle.left(90)
        turtle.penup()
        turtle.forward(F/5)
        turtle.pendown()
    if n == 2:
        turtle.penup()
        turtle.left(90)
        turtle.forward(2*F)
        turtle.pendown()
        turtle.right(90)
        turtle.forward(F)
        turtle.right(90)
        turtle.forward(F)
        turtle.right(90)
        turtle.forward(F)
        turtle.left(90)
        turtle.forward(F)
        turtle.left(90)
        turtle.forward(F)
        turtle.penup()
        turtle.forward(F/5)
        turtle.pendown()

for i in map(int, input()):
   draw(i)

