# Name: Yeva Usatova
# Email: yeva.usatova62@myhunter.cuny.edu
# Data: September 8, 2020
# This program creates acronym

phrase= input ("Enter a phrase: ")

print( "Your phrase in capital letters: ", phrase.upper())

wds= phrase.split()

init=""
for i in wds:
    init= init + i[0]
print("Acronym: ",init)




