#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: October 2020
#This program gets the input from user and computs it by pandas.

import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv', skiprows=5)
f=input("Enter borough: ")

print ("Min: ", pop[f].min())
print ("Max: ", pop[f].max())
print ("Mean: ", pop[f].mean())
print ("Median: ",pop[f].median())
print ("Standart Deviation: ", pop[f].std())





