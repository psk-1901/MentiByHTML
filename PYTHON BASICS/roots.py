a=int(input("enter value of a:"))
b=int(input("enter value of b:"))
c=int(input("enter value of c:"))

d=(b**2)-4.0*a*c
r1=(-b+(d**0.5))/2*a
r2=(-b-(d**0.5))/2*a

print(f"Roots are:({r1},{r2})")