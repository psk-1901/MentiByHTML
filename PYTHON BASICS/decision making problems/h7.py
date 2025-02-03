x=int(input("Enter the x coordinate:"))
y=int(input("Enter the y coordinate:"))

if x>0 and y>0:
    print("First quadrant")
elif x<0 and y>0:
    print("Second quadrant")
elif x<0 and y<0:
    print("Third quadrant")
elif x>0 and y<0:
    print("Fourth quadrant")
else:
    print("Enter the proper coordinates.")