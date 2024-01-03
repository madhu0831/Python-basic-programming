s=input("eneter string")
def reverse(s):
    w=s.split()
    for s1 in w:
        for i in range(len(s1)-1,-1,-1):
            print(s[i],end=" ")
        print(" ",end=" ")
print(reverse(s))
