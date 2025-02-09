p=int(input("Enter principal amount:"))
r=float(input("Enter the rate of interest:"))
t=int(input("Enter the timeline:"))

print("Year\tSimple Interest")

for i in range(1,t+1):
    print(f"{i}\t{p*r*i}")

