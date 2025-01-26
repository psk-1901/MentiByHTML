#movie ticket pricing based on age 

age= int(input("Enter your age:"))

if age<=5:
    print("Free")
elif age> 5 and age<=18:
    print("INR 100")
elif age>18 and age<=60:
    print("INR 200")
else:
    print("INR 50")
