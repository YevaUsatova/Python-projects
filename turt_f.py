#CSci 127 Teaching Staff
#Date:September 2020
#A template for a program that draws nested squares
#Modified by:Yeva Usatova
#Email:yeva.usatova62@myhunter.cuny.edu

import turtle
def setUp(t, dist, col):
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)
    
def squares(t,length):
    if length > 10:
        for i in range(4):
            t.forward(length)
            t.left(90)
        squares(t,length/2)       

def nestedSquares(t,length):
     if length > 10:
        for i in range(4):
            t.forward(length)
            t.left(90)
            nestedSquares(t, length/2)
     

def main():
    n = int(input('Enter length: '))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    squares(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    nestedSquares(tess, n)

if __name__ == "__main__":
     main()
