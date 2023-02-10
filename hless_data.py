#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Data: October 2020
#Tis programm

import pandas as pd
import matplotlib.pyplot as plt

f=input("Enter name of input file: ")
outp= input("Enter name of output file: ")

tot= pd.read_csv(f)
tot["Fraction Single Women"] = tot['Single Adult Women in Shelter']/tot["Total Individuals in Shelter"]

tot.plot(x= 'Date of Census', y= "Fraction Single Women" )

fig=plt.gcf()
fig.savefig(outp)
