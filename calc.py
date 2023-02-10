#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: November 2020
#This program culculates tax

print("Welcome to the total with tax calculator!")
print("Please enter the price of each item you would like to purchase, one at a time. ")
print("Enter a negative number when you are done.")

total=0
tax=0.0875
p=1
while (p>0):
    p=float(input("Enter the price of an item: "))
    if p>0:
        p=(p*tax)+p
        total=total+p

print("The total with tax is $",total)

    
