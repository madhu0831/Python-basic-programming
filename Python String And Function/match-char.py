s1= input("enter a string1")
s2= input("enter a string2")
a=set([])
for ch in s1:
    if ch in s2:
        a.add(ch)
print("number of match char=",len(a))
