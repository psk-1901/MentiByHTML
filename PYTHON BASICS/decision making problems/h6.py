year=int(input("Enter year:"))
month=int(input("Enter month:"))

if month in {1,3,5,7,8,10,12}:
        print("31 days") 
elif month in {4,6,9,11}:
        print("30 days")
elif month==2:
    if (year%400==0 and year%100==0) or (year%4==0) and (year%100!=0):
         print("29 days")
    else:
         print("28 days")
else:
        print("Invalid month ")
    