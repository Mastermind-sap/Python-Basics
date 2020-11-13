import turtle
from turtle import *
turtle.shape("turtle")
radius=100
while(radius>=0):
    begin_fill()
    color ("blue")
    circle (radius)
    end_fill()
    begin_fill()
    color ("green")
    circle (radius-5)
    end_fill()
    begin_fill()
    color ("red")
    circle (radius-10)
    end_fill()
    radius-=15
radius=-100
while(radius<=0):
    begin_fill()
    color ("blue")
    circle (radius)
    end_fill()
    begin_fill()
    color ("green")
    circle (radius+5)
    end_fill()
    begin_fill()
    color ("red")
    circle (radius+10)
    end_fill()
    radius+=15
turtle.left(90)
radius=100
while(radius>=0):
    begin_fill()
    color ("blue")
    circle (radius)
    end_fill()
    begin_fill()
    color ("green")
    circle (radius-5)
    end_fill()
    begin_fill()
    color ("red")
    circle (radius-10)
    end_fill()
    radius-=15
turtle.left(180)
radius=100
while(radius>=0):
    begin_fill()
    color ("blue")
    circle (radius)
    end_fill()
    begin_fill()
    color ("green")
    circle (radius-5)
    end_fill()
    begin_fill()
    color ("red")
    circle (radius-10)
    end_fill()
    radius-=15
