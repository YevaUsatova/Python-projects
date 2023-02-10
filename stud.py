#Name:Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Data: October 2020
#This programm uses function main

import pandas as pd
import matplotlib.pyplot as plt

in_file= input("Enter name of input file: ")
out_file= input("Enter name of output file: ")

fun=pd.read_csv(in_file)
fun["Date"]=pd.to_datetime(fun["Date"].apply(str))
 
fun["% Attending"]=(fun["Present"]/fun["Enrolled"])*100
fun.plot(x="Date", y="% Attending")

plt.show()
fig=plt.gcf()
fig.savefig(out_file)
