#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Data: September 28, 2020
#This program changes the color of diferen region on the map

import numpy as np
import matplotlib.pyplot as plt

elevations = np.loadtxt('elevationsNYC.txt')

mapShape = elevations.shape + (3,)

floodMap = np.zeros(mapShape)

for row in range(mapShape[0]):
    for col in range(mapShape[1]):
        if elevations[row,col] <= 0:
            floodMap[row,col,2] = 1.0     

        elif elevations[row,col] <= 5:
            floodMap[row,col,0] = 1.0    

        elif elevations[row,col] <= 15:
            floodMap[row,col,0:3] = 0.5

        else:
            floodMap[row,col,1] = 1.0

plt.imsave('floodMap.png', floodMap)
