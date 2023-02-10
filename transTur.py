#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: September 15, 2020
#This program uses tortal for changing colors of sphere.

import turtle		        

turtle.colormode(255)		
tess = turtle.Turtle()
tess.shape("turtle")		
tess.backward(350)			 


for i in range(0,255,10):
     tess.forward(20)
     tess.pensize(i)
     tess.color(255-i,0,0+i)

