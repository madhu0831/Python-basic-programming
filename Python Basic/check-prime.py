n=int(input("enter a number"))
flag=0
if n>1:
    for i in range(2,n):
        if(n%i)==0:
            flag=1
            break
if flag==0:
    print("number is prime")
else:
    print("number is not prime")
