#Name:Yeva Usatova
#Email:yeva.usatova62@myhunter.cuny.edu
#Date:October 2020
#This program runs information from csv file.

import pandas as pd

csvFile=input("Enter file name: ")
tickets= pd.read_csv(csvFile)

print("There were ",tickets.count(),"film permits.")

print(tickets.groupby('Borough').count()['ParkingHeld'])

print("The five most popular type of events were: ",tickets['EventType'].value_counts()[:5])
