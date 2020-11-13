import turtle
from turtle import *
def draw(n,c):
    if(n==1):
        begin_fill()
        color(c)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        end_fill()
    elif(n==2):
        begin_fill()
        color(c)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(60)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(60)
        end_fill()
    elif(n==3):
        begin_fill()
        color(c)
        circle(100)
        end_fill()
    elif(n==4):
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
    elif(n==5):
        turtle.shape("turtle")
        color("purple")
        begin_fill()
        circle(100,extent=90,steps=2)
        end_fill()
        color("red")
        begin_fill()
        circle(100,extent=90,steps=2)
        end_fill()
        color("purple")
        begin_fill()
        circle(100,extent=90,steps=2)
        end_fill()
        color("red")
        begin_fill()
        circle(100,extent=90,steps=2)
        end_fill()
n=int(input('''Enter 1 for square ,
2 for rectangle,
3 for circle,
4 and 5 for diff patterns: '''))
c=input("Enter color: ")
if(n>0 and n<6):
    draw(n,c)
else:
    print ("Wrong choice")
    
        

    
