n=int(input("enter a number"))
f=1
if n<0:
    print("factorial doesnt exist")
elif n==0:
    print("facrorial of 0 is one")
else:
    for i in range(1,n+1):
        f=f*i
    print("factorial=",f)
