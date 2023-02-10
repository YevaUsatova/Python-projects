#CSci 127 Teaching Staff
#March 2018
#A template for a program that computes LIRR transit fares.
#Modified by:Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu

def computeFare(zone, ticketType):
    fare = 0
   
    if zone==1 and ticketType=="peak":
        fare=8.75
    elif zone==1 and ticketType=="off-peak":
        fare=6.25
    elif (zone==2 or zone==3) and ticketType=="peak":
        fare=10.25
    elif (zone==2 or zone==3) and ticketType=="off-peak":
        fare=7.50
    elif zone==4 and ticketType=="peak":
        fare=12.00
    elif zone==4 and ticketType=="off-peak":
        fare=8.75
    elif (zone>=5 and zone<=7) and ticketType=="peak":
        fare=13.50
    elif (zone>=5 and zone<=7) and ticketType=="off-peak":
        fare=9.75
    else:
        fare=-1      
    return(fare)

def main():
     z = int(input('Enter the number of zones: '))
     t = input('Enter the ticket type (peak/off-peak): ').lower()
     fare = computeFare(z,t)
     print('The fare is', fare)

#Allow script to be run directly:
if __name__ == "__main__":
     main()
