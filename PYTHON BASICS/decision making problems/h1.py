#Checking the given yr is a leap year or not

yr=int(input("Enter a year:"))

if yr%4==0:
    print("The year entered is a Leap year")
else:
    print("Not a leap year")