# Name: Yeva Usatova
# Email: yeva.usatova62@myhunter.cuny.edu
# Date: September 7, 2020
# This programm draws flower

import turtle
wn = turtle.Screen()
wn.bgcolor ("hotpink")

alex= turtle.Turtle()
alex.pencolor ("red")
alex.shape ("turtle")
alex.fillcolor("yellow")
alex.speed('fast')
alex.penup()
alex.back(100)
alex.pendown()
alex.stamp()

for i in range (36):
   alex.forward(200)
   alex.left(180)
   alex.stamp()
   alex.right(10)
