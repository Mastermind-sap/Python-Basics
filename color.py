import turtle
from turtle import *
radius=100
while radius>10:
    begin_fill()
    turtle.color("red")
    circle(radius)
    end_fill()
    begin_fill()
    turtle.color("purple")
    circle(radius-5)
    end_fill()
    begin_fill()
    turtle.color("blue")
    circle(radius-10)
    end_fill()
    radius-=15
