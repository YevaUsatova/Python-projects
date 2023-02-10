#Name: Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: September 15, 2020
#This program prints the list of names.

names=input("Please enter your list of names: ")
coma= names.split("; ")

for i in coma:
    s=i.split(", ")
    first=s[1]
    last=s[0]
    compl= (first[0]+". ") + last
    print(compl)

