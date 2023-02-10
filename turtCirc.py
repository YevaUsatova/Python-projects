#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Data: September 28, 2020
#This pregram stamps turtles

st= input ("Enter number of stamps the turtle will print: ")

import turtle
wn= turtle.Screen()
anna=turtle.Turtle()
anna.shape("circle")
anna.penup()
s=20

for i in range(int(st)):
    anna.stamp()
    if int(i)%4==0:
        s=s+2
    anna.forward(s)
    anna.right(24)
