# Name: Yeva Usatova
# Email: yeva.usatova62@myhunter.cuny.edu
# Data: September 28, 2020
# This programm converts time

sec= int(input ("Please enter the time in seconds: "))

sc=sec%60
s= str(sc)+"s"

hour = (sec//3600)%12
hr= str (hour)+"h: "

minute = (sec//60)%60
mt= str(minute)+"m: "    

print (hr,mt,s)
