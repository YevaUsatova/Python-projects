#Name:Yeva Usatova
#Email: yeva.usatova62@myhunter.cuny.edu
#Date: October 2020
#This program calculates score

def computeScore(answers):
    
    val=0

    val+=answers[0]

    if answers[1]>23:
        val+=1
        
    if answers[2]=="yes":
        val-=-1
    
    val+=answers[3]
        

    if answers[4]>3.5:
        val+=1
    
    sum(val)    
    return(val)   

def main():
    print("QUESTION 1")
    year=int(input("What year are you? (1,2,3,4): "))

    print("QUESTION 2")
    age=int(input("How old are you?: "))

    print("QUESTION 3")
    probation=input("Are you currently on probation? (Yes or No): ")
          
    print("QUESTION 4")
    ftime=int(input("Are you Part-time or Full-time? (0 or 1): "))
          
    print("QUESTION 5")
    gpa=float(input("What is your GPA?: "))

    val=computeScore(['year','age','probation','ftime','gpa'])
    print("Your housing score is: ", val)

if __name__ == "__main__":
     main()
