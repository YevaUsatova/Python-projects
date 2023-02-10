#CSci 127 Teaching Staff
#October 2017
#A program that uses functions to print out months.
#Modified by:  Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu

def monthString(monthNum):
     """
     Takes as input a number, monthNum, and
     returns the corresponding month name as a string.
     Example: monthString(1) returns "January".
     Assumes that input is an integer ranging from 1 to 12
     """
     
     monthString = ""
     
     if monthNum==1:
         monthString="January"
     elif monthNum==2:
         monthString="February"
     elif monthNum==3:
         monthString="March"
     elif monthNum==4:
         monthString="April"
     elif monthNum==5:
         monthString="May"
     elif monthNum==6:
         monthString="June"
     elif monthNum==7:
         monthString="July"
     elif monthNum==8:
         monthString="August"
     elif monthNum==9:
         monthString="September"
     elif monthNum==10:
         monthString="October"
     elif monthNum==11:
         monthString="November"
     else:
         monthString="December"
     return(monthString)



def main():
     n = int(input('Enter the number of the month: '))
     while n<1 or n>12:
         print("This is not a valid month number.")
         n=int(input("Please enter a number between 1 and 12:" ))
     mString = monthString(n)
     print('The month is', mString)



#Allow script to be run directly:
if __name__ == "__main__":
     main()






 
