age= int(input("Enter your age:"))

if age<=5:
    print("Free")
elif age> 5 and age<=12:
    print("INR 100")
elif age>13 and age<=59:
    print("INR 200")
else:
    print("INR 150")
