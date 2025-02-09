numbers=[]
for i in range(10):
    num=int(input("Enter a number:"))
    numbers.append(num)

oc=0
ec=0
for num in numbers:
    if num%2==0:
        ec+=1
    else:
        oc+=1
print(f"No of even numbers entered:{ec}")
print(f"No of odd numbers entered:{oc}")
