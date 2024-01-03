s= input("enter a string")
a=set([])
vowels={'a','e','i','o','u'}
for ch in s:
    if ch in vowels:
        a.add(ch)
if len(a)==5:
    print(s,"is accepted")
else:
    print(s,"is not accepted")
