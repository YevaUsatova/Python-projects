#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: October 2020
#This program prints the stars dataset.

import pandas as pd
name= input ("Enter file name: ")
col= input ("Enter the name of the column(Temperature, Luminosity, Radius or Absolute Magnitude)you would like to average: ")

st= pd.read_csv(name)

print ("The avarage ", col, "for each Star type is: ")
print(st.groupby(['Star type']).mean()[col])

