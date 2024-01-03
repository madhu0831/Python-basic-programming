fname=input("enter file name")
f=open(fname)
n=int(input("enter how many lines"))
for i in range(0,n+1):
    line=f.readline()
print(line)
f.close()