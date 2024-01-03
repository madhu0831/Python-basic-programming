s=input("enter string")
w=s.split()
print("words in even length")
for s1 in w:
    if(len(s1)%2==0):
        print(s1)
