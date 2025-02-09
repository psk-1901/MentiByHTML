str=input("Enter a string:")
char=input("Enter a character:")
count=0

for i in str:
    if i == char:
        count+=1


print(f"Character {char} occured {count} times in the string")