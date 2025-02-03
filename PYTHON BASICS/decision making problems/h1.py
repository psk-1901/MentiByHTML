#Checking the given yr is a leap year or not

yr=int(input("Enter a year:"))

if(yr%400==0) and (yr%100==0) :
    print("The year entered is a Leap year")
elif (yr%4==0) and (yr%100!=0):
    print("Thr year entered is a leap year")
else:
    print("Not a leap year")