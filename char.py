# Name: Yeva Usatova
# Email: yeva.usatova62@myhunter.cuny.edu
# Date: September 8, 2020
# This program prints characters and unicode numbers

myString = input("Enter a message: ")

for c in myString:

    print (c,(ord(c)+1), chr(ord(c)+1))
