#Electricity bill calculator based on the a consumed

a=int(input("Enter no of a consumed:"))
b=0
#if a<50:
  #  print(f"Bill is:{a*3}")
#elif a>50 and a<=150:
 #   print(f"Bill is:{a*8}")
#else:
#    print(f"Bill is:{a*13}")

if a<=50:
    b=a*3
    print(f"Bill is {b}")
elif a>50 and a<=150:
    b= ((a*3) + (a-50)*5)
    print(f"Bill is {b}")
else :
    b=((a*3)+(a-100)*5)

