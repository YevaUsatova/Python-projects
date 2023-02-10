#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: September 29, 2020
#This program prints green stripes

import numpy as np
import matplotlib.pyplot as plt

size=int( input ("Enter the size: "))
file= input ("Enter output file: ")

stripe= np.ones((size,size,3))
stripe[::2,:,0]=0
stripe[::2,:,2]=0

plt.imsave(file, stripe)
