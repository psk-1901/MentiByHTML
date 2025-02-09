n=int(input("Enter a number:"))

if n<=1:
    print("Not a prime number")
else:
    for i in range(2,n):
        if n%i==0:
            print(f"{n} is not a Prime Number")
            break
    else:
        print(f"{n} is a Prime Number")        