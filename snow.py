#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Data: September 29, 2020
#This program imports image

import matplotlib.pyplot as plt
import numpy as np

file=input( "Enter file name: ")
ca= plt.imread (file)
countSnow= 0
t=0.8
for i in range(ca.shape[0]):
    for j in range(ca.shape[1]):
        if (ca[i,j,0]>t) and (ca[i,j,1]>t) and (ca[i,j,2]>t):
            countSnow= countSnow+1
print ("Snow count is", countSnow)

