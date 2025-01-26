#Student grade evaluation by taking 3 sub marks as input


s1=int(input("Enter marks of sub 1:"))
s2=int(input("Enter marks of sub 2:"))
s3=int(input("Enter marks of sub 3:"))

sum= s1+s2+s3
percentage=int((sum/300)*100)

if percentage>90:
    print("A+")
elif percentage<90 and percentage>=75:
    print("A")
elif percentage<75 and percentage>=50:
    print("B")
else:
    print("Fail")

