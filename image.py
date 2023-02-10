#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: September 15, 2020
#This program changes pictures color.

import matplotlib.pyplot as plt
import numpy as np

pic= input (" Enter a name of an input file: ")
res= input (" Enter the name of an output file: ")
img = plt.imread(pic)   #Read in image from csBridge.png

img2 = img.copy()        
img2[:,:,1] = 0          #Set the green channel to 0

res= input (" Enter the name of an output file: ")
plt.imsave(res, img2) 
