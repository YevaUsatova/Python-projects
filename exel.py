#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: October 2020
#This program get the input from user and dispalys it by pandas.

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows=5)

f=input("Enter first borough name: ")
z= input ("Enter second borough name: ")
outFile= input ("Enter output file name: ")

pop["Fraction"]= (pop[f]+pop[z])/pop['Total']

pop.plot(x="Year", y="Fraction")

fig= plt.gcf()
fig.savefig(outFile)
