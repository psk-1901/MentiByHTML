#largest of three numbers

a=int(input("Enter value of a:"))
b=int(input("Enter value of b:"))
c=int(input("Enter value of c:"))

if a>b and a>c:
    print(f"Largest:{a}")
elif b>a and b>c:
    print(f"Largest:{b}")
else:
    print(f"Largest:{c}")