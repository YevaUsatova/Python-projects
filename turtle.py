#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: November 2020
#This program makes turtle randomly walk

import turtle
import random

trey = turtle.Turtle()
trey.speed(10)

for i in range(200):
  trey.forward(5)
  a = random.randrange(0,360,30)
  trey.right(a)
