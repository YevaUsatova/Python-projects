#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Data: September 28, 2020
#This program culculates change

cent= int(input("Enter the number of cents: "))
quart=cent//25
print("Quarters: ",quart)
rem=cent % 25
dime=rem//10
print ("Dimes: ",dime)
rem=rem % 10
nic= rem // 5
print ("Nickels: ", nic)
cent=rem % 5
print ("Cents: ", cent)
