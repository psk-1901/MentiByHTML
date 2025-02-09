i=0 
j=1
n=int(input("Enter a number:"))

for c in range(0,n+1):
            if(c<=1):
                    nt=c
            else:
                    nt=i+j
                    i=j
                    j=nt
            print(nt)

