#number nature checker 

num=int(input("enter a number: "))

if num>0 and num%2==0:
    print("Entered number is Positive and Even")
elif num>0 and num%2!=0:
    print("Entered number is Positive and Odd")
elif num<0 and num%3==0:
    print("Entered number is Negative and divisible by 3")
else:
    print("Entered number is Zero")