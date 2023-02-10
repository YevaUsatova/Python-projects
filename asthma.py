#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: October 2020
#This program shows the astma population

import pandas as pd
import matplotlib.pyplot as plt

fname= input ("Enter name of input file: ")
outp= input ("Enter name of output file: ")

astma= pd.read_csv(fname)

aV= astma.groupby('geo_entity_name').mean()['data_valuemessage']
aV.plot.bar()
plt.show()

pic= plt.gcf().subplots_adjust(bottom=0.5)
pic= plt.gcf()
pic.savefig(outp)
