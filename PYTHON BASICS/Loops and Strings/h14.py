r=int(input("Enter no of rows:"))

for i in range(r,0,-1): 
    print(' '*(r-i) ,end='') 
    for j in range(i): 
        print('* ',end='') 
    print()