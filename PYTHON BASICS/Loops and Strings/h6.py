n=int(input("Enter a number:"))
a=0
b=0

for i in range(0,n+1):
    if i%2==0:
        a+=1
    else:
        b+=1
print(f"There are {a} even numbers and {b} odd numbers between the range entered")
