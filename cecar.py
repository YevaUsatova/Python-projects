# Name: Yeva Usatova
# Email: yeva.usatova62@myhunter.cuny.edu
# Data: September 11, 2020
# This programm generates code

word= input("Enter a word: ")

codedWord=""

for i in word:

    offset = ord(i)-ord('A')+13
    wrap = offset % 26
    newch= chr(ord('A')+wrap)
    codedWord= codedWord + newch

print("Yor word in code is", codedWord.upper())
    

