print("Sum is displayed after u enter 0")
sum=0

while True:
    n=int(input("Enter a number:"))
    if n==0:
        break
    sum+=n

print(f"Total Sum is:{sum}")
