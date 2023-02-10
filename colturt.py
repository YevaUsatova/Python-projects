#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: September 15, 2020
#This program uses tortal for drawing a blue sphere.

import turtle		        

turtle.colormode(255)		
tess = turtle.Turtle()
tess.shape("turtle")		
tess.backward(300)			 


for i in range(0,255,10):
     tess.forward(10)
     tess.pensize(i)		
     tess.color(0,0,i)
     
     
for i in range(255,0,-10):
     tess.forward(10)
     tess.pensize(i)		
     tess.color(0,0,i)
