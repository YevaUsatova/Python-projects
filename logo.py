#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Data: September 28, 2020
#This pregram creates logo for univercity

import matplotlib.pyplot as plt
import numpy as np
logoim= np.ones((30,30,3))
logoim[:,:10,0:2]=0
logoim[:,-10:,0:2]=0
logoim[20:30,:,0:2]=0
    
plt.imsave('logo.png',logoim)
