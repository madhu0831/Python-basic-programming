fname=input("enter file name")
f=open(fname)
n=int(input("enter how many lines"))
l=len(f.readlines())
f.close()
f=open(fname)
i=0
for s in f:
    i=i+1
    if i>l-n:
        print(s)
f.close()
